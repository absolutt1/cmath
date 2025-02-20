import os
import sys
import psutil
import asyncio
import json
from xml.etree import ElementTree
from urllib.parse import urlparse
import re

__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")
__scraped__ = os.path.join(__output__, "scraped")
__structured__ = os.path.join(__output__, "structured")
# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

os.makedirs(__scraped__, exist_ok=True)
os.makedirs(__structured__, exist_ok=True)

from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    print("\n=== Parallel Crawling with Browser Reuse + Memory Check ===")

    # We'll keep track of peak memory usage across all tasks
    peak_memory = 0
    process = psutil.Process(os.getpid())

    def log_memory(prefix: str = ""):
        nonlocal peak_memory
        current_mem = process.memory_info().rss  # in bytes
        if current_mem > peak_memory:
            peak_memory = current_mem
        print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")

    # Minimal browser config
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,   # corrected from 'verbos=False'
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create the crawler instance
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        # We'll chunk the URLs in batches of 'max_concurrent'
        success_count = 0
        fail_count = 0
        for i in range(0, len(urls), max_concurrent):
            batch = urls[i : i + max_concurrent]
            tasks = []

            for j, url in enumerate(batch):
                # Unique session_id per concurrent sub-task
                session_id = f"parallel_session_{i + j}"
                task = crawler.arun(url=url, config=crawl_config, session_id=session_id, magic=True)
                tasks.append(task)

            # Check memory usage prior to launching tasks
            log_memory(prefix=f"Before batch {i//max_concurrent + 1}: ")

            # Gather results
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Check memory usage after tasks complete
            log_memory(prefix=f"After batch {i//max_concurrent + 1}: ")

            # Evaluate results
            for url, result in zip(batch, results):
                if isinstance(result, Exception):
                    print(f"Error crawling {url}: {result}")
                    fail_count += 1
                elif result.success:
                    success_count += 1
                    # Save the scraped content
                    x = result.markdown.rfind("Toggle Light / Dark / Auto color theme")
                    if x == -1: x = 0
                    save_as_markdown(url, result.markdown, x)
                else:
                    fail_count += 1

        print(f"\nSummary:")
        print(f"  - Successfully crawled: {success_count}")
        print(f"  - Failed: {fail_count}")

    finally:
        print("\nClosing crawler...")
        await crawler.close()
        # Final memory log
        log_memory(prefix="Final: ")
        print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")

def get_urls():           
    sitemap_path = "otbroski.xml"
    try:
        # Read the local sitemap file
        with open(sitemap_path, 'rb') as f:
            sitemap_content = f.read()
        
        # Parse the XML
        root = ElementTree.fromstring(sitemap_content)
        
        # Extract all URLs from the sitemap
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        return urls
    except Exception as e:
        print(f"Error reading local sitemap file: {e}")
        return []
    

def save_as_markdown(url: str, content: str, x: int):
    """Save scraped content as markdown file with URL-based filename"""
    parsed_url = urlparse(url)
    # Create safe filename from URL path
    filename = parsed_url.path.strip("/").replace("/", "_") + ".md"
    filepath = os.path.join(__scraped__, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        #f.write(f"# Source URL: {url}\n\n")
        f.write(content[x + 71:])
    print(f"Saved: {filename}")

class DocumentationParser:
    """Parser for Manim documentation markdown files"""
    def __init__(self, scraped_dir: str):
        self.scraped_dir = scraped_dir
        self.parsed_data = []
        
    def parse_all(self):
        """Parse all markdown files in the scraped directory"""
        for filename in os.listdir(self.scraped_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(self.scraped_dir, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                parsed = self.parse_markdown(content)
                if parsed:
                    self.parsed_data.append(parsed)
        
        # Save structured data
        output_path = os.path.join(__structured__, "documentation.json")
        with open(output_path, "w") as f:
            json.dump(self.parsed_data, f, indent=2)
        print(f"Saved structured data to {output_path}")
    
    def parse_markdown(self, content: str) -> dict:
        """Parse individual markdown content into structured format"""
        result = {
            "class_name": "",
            "category": "",
            "description": "",
            "parameters": {},
            "examples": [],
            "methods": [],
            "attributes": [],
            "source_url": ""
        }
        
        # Extract source URL
        source_match = re.search(r"^# Source URL: (.+)$", content, re.M)
        if source_match:
            result["source_url"] = source_match.group(1)
        
        # Extract class name and category
        class_match = re.search(r"^# (\w+)\[¶\]", content)
        if class_match:
            result["class_name"] = class_match.group(1)
        
        # Extract description
        description_match = re.search(
            r"Bases:.*?\n\n(.*?)(?=\n##|\n###|\n```|\n\Z)", 
            content, 
            re.DOTALL
        )
        if description_match:
            result["description"] = description_match.group(1).strip()
        
        # Extract parameters
        param_section = re.search(r"### Parameters(.+?)(?=\n##|\n###|\n```|\n\Z)", content, re.DOTALL)
        if param_section:
            params = re.findall(r"- \*\*(\w+)\*\*: (.+)", param_section.group(1))
            result["parameters"] = {name: desc for name, desc in params}
        
        # Extract examples
        examples = re.findall(r"```python\n(.*?)\n```", content, re.DOTALL)
        result["examples"] = [ex.strip() for ex in examples if ex.strip()]
        
        # Extract methods
        method_matches = re.findall(
            r"### ([\w_]+)\n\n(.*?)(?=\n### |\n## |\n```|\n\Z)", 
            content, 
            re.DOTALL
        )
        for method_name, method_desc in method_matches:
            result["methods"].append({
                "name": method_name,
                "description": method_desc.strip()
            })
        
        return result

async def main():
    urls = get_urls()
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        await crawl_parallel(urls, max_concurrent=30)
        
        # Parse scraped data
        parser = DocumentationParser(__scraped__)
        parser.parse_all()
    else:
        print("No URLs found to crawl")

if __name__ == "__main__":
    asyncio.run(main())
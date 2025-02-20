import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://docs.manim.community/en/stable/examples.html")
        #x = result.markdown.find("Copyright ©")
        print(result.markdown[:-100])

if __name__ == "__main__":
    asyncio.run(main())
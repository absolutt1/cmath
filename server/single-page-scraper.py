import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait._original__init__")
        x = result.markdown.find("Copyright ©")
        print(result.markdown[56331:-x])
if __name__ == "__main__":
    asyncio.run(main())
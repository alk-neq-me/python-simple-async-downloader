import aiohttp
from limit_decorator import asyncio, limit
from progress import progress_bar
from download import download_file


@limit(2)
async def mock_test(n, t) -> None:
    print("start", n)
    for i in range(100+1):
        await asyncio.sleep(t)
        progress_bar(i)
    print("done", n)


async def main() -> None:
    reqs = [
        # download_file(url=""),   # url
    ]
    await asyncio.gather(*[
        asyncio.ensure_future(req)
        for req in reqs
    ])


if __name__ == "__main__":
    asyncio.run(main())

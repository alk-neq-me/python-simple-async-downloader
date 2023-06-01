import aiohttp

from progress import progress_bar
from colors import Color, Colorize
from limit_decorator import limit


colorize = Colorize()

@limit(3)
async def download_file(url: str) -> None:
    """ Download file """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                file_size = int(response.headers.get("Content-Length", 0))
                title = url.split("/")[-2]
                ext = response.headers.get("Content-Type", "None/txt").split("/")[1]
                output_file = f"{title}.{ext}"

                print("\n", colorize.colorrize("[ DOWNLOADING ]", color=Color.Purple), f"start downloading ... {output_file}", end="\n")
                
                with open(output_file, "wb") as f:
                    downloaded_bytes = 0
                    async for chunk in response.content.iter_chunked(1024):
                        f.write(chunk)
                        downloaded_bytes += len(chunk)
                        
                        progress = int(downloaded_bytes / file_size * 100)
                        progress_bar(progress)

                print("\n", colorize.colorrize("[ DONE ]", color=Color.Green), f"done downloaded ... {output_file}", end="\n")


if __name__ == "__main__":
    print("please run main.py")

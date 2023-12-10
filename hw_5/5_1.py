import aiohttp
import asyncio
import os


async def download(url, num_imgs=10, path="artifacts/5_1"):
    async with aiohttp.ClientSession() as session:
        num_zeros = len(str(num_imgs))

        await asyncio.gather(
            *[
                asyncio.create_task(
                    download_img(
                        url,
                        session,
                        path=os.path.join(path, f"{str(i)}.png"),
                    )
                )
                for i in range(num_imgs)
            ]
        )


async def download_img(url, session, path):
    async with session.get(url) as r:
        output = await r.read()
        with open(path, "wb") as f:
            f.write(output)


if __name__ == "__main__":
    path = "artifacts/5_1"
    url = "https://picsum.photos/"
    asyncio.run(download(url=url, num_imgs=10, path=path))

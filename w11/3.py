import aiohttp
import asyncio
import aiofile

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            html = re.split(r'[\n]', html)
            async with aiofile.async_open("found.txt", 'w+') as found:
                for line in lines:
                    if line.startswith("<a >"):
                        found.writer(line)


async def find_line(urls):
#    async with aiofile.async_open(urls, 'r') as urlslist:
    async for line in aiofile.LineReader(urls):
        asyncio.ensure_future(fetch(line))


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    with open('urls.txt', 'r') as urls:
        loop.run_until_complete(find_line(urls))

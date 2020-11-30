import aiohttp
import asyncio
import aiofile

async def get_response(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            print(html)

async def find_line():
    async with aiofile.AIOFile("found.txt", 'w') as found:
        async with aiofile.AIOFile("urls.txt", 'r') as urls:
            for line in urls
#what the fuck

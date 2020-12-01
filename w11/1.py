import aiohttp
import asyncio

async def get_response(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            return html



loop = asyncio.get_event_loop()
n = 100
responses = [get_response('http://127.0.0.1:8000') for _ in range(n)]
print(*loop.run_until_complete(asyncio.gather(*responses)))
loop.close()

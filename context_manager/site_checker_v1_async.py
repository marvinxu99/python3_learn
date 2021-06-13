# https://realpython.com/python-with-statement/

# site_checker_v1.py

import aiohttp
import asyncio

class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()

async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())

'''
This script works similar to its previous version, site_checker_v0.py. The main difference 
is that, in this example, you extract the logic of the original outer async with 
statement and encapsulate it in AsyncSession.

In .__aenter__(), you create an aiohttp.ClientSession(), await the .get() response, 
and finally return the response itself. In .__aexit__(), you close the session, which 
corresponds to the teardown logic in this specific case. Note that .__aenter__() and .__aexit__() must return awaitable objects. In other words, you must define them with async def, which returns a coroutine object that is awaitable by definition.

Finally, a common practice when you’re writing asynchronous context managers is to implement the four special methods:
.__aenter__()
.__aexit__()
.__enter__()
.__exit__()

This makes your context manager usable with both variations of with.
'''
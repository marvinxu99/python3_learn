# https://realpython.com/async-io-python/
# https://hynek.me/articles/waiting-in-asyncio/

import asyncio

async def f():
    print("running in f")


async def g():
    print("running in g")

async def myfunc():
    result_f = await f()
    result_g = await g()

asyncio.run(myfunc())
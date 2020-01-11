import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main(), debug=True)

# When a coroutine function is called, but not awaited (e.g. coro() instead
# of await coro()) or the coroutine is not scheduled with asyncio.create_task(),
# asyncio will emit a RuntimeWarning:


async def test():
    print("never scheduled")


async def main2():
    test()

asyncio.run(main2())

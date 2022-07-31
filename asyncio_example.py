import asyncio
import datetime


# async def main():
#     print('Hello ...')
#     await asyncio.sleep(0)
#     print('... World!')
#
#
# asyncio.run(main())
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())


# The asyncio.create_task()

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#
#     task2 = asyncio.create_task(
#         say_after(1, 'world'))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())


# async def nested():
#     return 42
#
#
# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     nested()
#
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
#
#
# asyncio.run(main())


# async def nested():
#     return 2


# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     await task
#
#
# asyncio.run(main())
#
# async def main():
#     await asyncio.sleep(1)
#     print('hello')
#
#
# asyncio.run(main())

async def display_date():
    loop = asyncio.get_running_loop()
    print(loop)
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())

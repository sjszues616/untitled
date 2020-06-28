import asyncio
import time


async def add(x,y):
    r = x+y
    return r

async def bad_call(a,b,c,d):
    a_b = await add(a,b)
    time.sleep(1)
    await asyncio.sleep(1)
    c_d = await add(c,d)
    print (a_b*c_d)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bad_call(1,2,3,4))
    print('over')

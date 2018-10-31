import asyncio
from time import time

import aiohttp
import requests

SITES = ['www.google.com', 'www.yandex.ru', 'www.lenta.ru', 'www.rbc.ru', 'rg.ru']


def get_sync():
    t0 = time()
    for site in SITES:
        r = requests.get("https://" + site)
        print(r.status_code)
    t1 = time()
    print("Sync poll took %s seconds" % (t1-t0))


async def get_async():
    t0 = time()
    responses = []
    async with aiohttp.ClientSession() as session:
        for site in SITES:
            r = session.get("https://" + site)
            responses.append(r)
        for r in await asyncio.gather(*responses):
            print(r.status)

    t1 = time()
    print("Async poll took %s seconds" % (t1 - t0))


get_sync()

loop = asyncio.get_event_loop()
loop.run_until_complete(get_async())

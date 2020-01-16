import asyncio
import concurrent.futures as cofu
from os.path import basename

import aiohttp


def download(ways):
    if not ways:
        print('ways list is empty, impossible to download')
        return
    print('downloading...')
    success_files = set()
    failure_files = set()
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            async_downloader(ways, event_loop, success_files, failure_files)
        )
    finally:
        event_loop.close()
    print('download complete!')
    print('-' * 99)


async def async_downloader(ways, loop, success_files=set(), failure_files=set()):
    async with aiohttp.ClientSession() as session:
        coroutines = [
            download_file_by_url(url, session=session)
            for url in ways
        ]
        completed, pending = await asyncio.wait(coroutines, return_when=cofu.FIRST_COMPLETED)
        while pending:
            for task in completed:
                fail, url = task.result()
                if fail:
                    failure_files.add(url)
                else:
                    success_files.add(url)
            completed, pending = await asyncio.wait(pending, return_when=cofu.FIRST_COMPLETED)
        for task in completed:
            fail, url = task.result()
            if fail:
                failure_files.add(url)
            else:
                success_files.add(url)


async def download_file_by_url(url, session=None):
    fail = True
    file_name = basename(url)
    assert session
    try:
        async with session.get(url) as response:
            if response.status == 404:
                print('\t{} from {} : Failed : {}'.format(file_name, url, '404 - Not found'))
                return fail, url
            if not response.status == 200:
                print('\t{} from {} : Failed : HTTP response {}'.format(file_name, url, response.status))
                return fail, url
            data = await response.read()
            with open(file_name, 'wb') as file:
                file.write(data)
    except asyncio.TimeoutError:
        print('\t{} from {}: Failed : {}'.format(file_name, url, 'Timeout error'))

    except aiohttp.client.ClientConnectionError:
        print('\t{} from {}: Failed : {}'.format(file_name, url, 'Client connection error'))

    else:
        print('\t{} from {} : Success'.format(file_name, url))
        fail = False

    return fail, url


def test():
    ways = ['https://www.baidu.com',
            'https://www.github.com',
            'https://www.cn.bing.com',
            'https://segmentfault.com',
            'https://www.fail-path.unknown',
            ]

    download(ways)


if __name__ == '__main__':
    test()

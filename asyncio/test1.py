import asyncio


async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")


async def main():
    await asyncio.gather(count(), count())


'''
三个 count() 依次执行，打印完 One，就休眠1秒钟，把执行权交给下一个 count()，
所以先连续打印出三个 One。等到1秒钟休眠结束，执行权重新交回第一个 count()，
开始执行 await 命令下一行的语句，所以会接着打印出三个Two。脚本总的运行时间是1秒。'''
asyncio.run(main())

'''
第一步：写一个最简单的爬虫，比如获取 B 站的弹幕或豆瓣的书评影评。
第二步：单线程爬虫扩展为多线程爬虫，了解进程、线程、锁。
第三步：对收集的数据进行清洗和分析。
第四步：将数据报告在 Web 端展示，了解 MVC 设计模式、Web 框架、数据库操作。
'''

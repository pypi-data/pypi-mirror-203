from datetime import datetime


def pytest_configure():
    print(f'{datetime.now()} pytest开始执行了')


def pytest_unconfigure():
    print(f'{datetime.now()} pytest执行结束了')

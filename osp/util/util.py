import time


def poller(interval, timeout):
    start = 0
    while (start + interval) <= timeout:
        time.sleep(interval)
        start += interval
        yield True

import time
from concurrent.futures import ProcessPoolExecutor


def handler(start=0, finish=0):
    result = 0
    for i in range(start, finish):
        result += i
    return result


def run_by(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    params = [
        [0, 2 ** 21, 2 ** 26],
        [2 ** 20, 2 ** 25, 2 ** 30]
    ]
    result = sum(executor.map(handler, *params))
    print('Result {result}. Time {executor}: {spent}'.format(
        result=result, executor=executor_class.__name__, spent=time.time() - started))


if __name__ == '__main__':
    run_by(ProcessPoolExecutor)

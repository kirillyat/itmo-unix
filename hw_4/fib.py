from threading import Thread
from multiprocessing import Process
from time import perf_counter


def fibonacci(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a



if __name__ == "__main__":
    N = 50000

    start = perf_counter()
    for i in range(10):
        fibonacci(N)
    time1 = perf_counter() - start

    start = perf_counter()
    jobs = []
    for i in range(10):
        jobs.append(Thread(target=fibonacci, args=(N,)))
        jobs[-1].start()
    for job in jobs:
        job.join()
    time2 = perf_counter() - start

    start = perf_counter()
    jobs = []
    for i in range(10):
        jobs.append(Process(target=fibonacci, args=(N,)))
        jobs[-1].start()
    for job in jobs:
        job.join()
    time3 = perf_counter() - start

    with open("artifacts/fib.txt", "w+") as f:
        f.write(f"Sync    -> {time1}\n")
        f.write(f"Thread  -> {time2}\n")
        f.write(f"Process -> {time3}\n")

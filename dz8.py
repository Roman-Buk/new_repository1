import logging
import time

logging.basicConfig(filename='HW8.log', level=logging.INFO,
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")


def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total


def speed(n):
    time.start = time.perf_counter()
    result = sum(n)
    time.end = time.perf_counter()
    total_time = time.end - time.start
    logging.info(f"'sum' for n={n}  {total_time:} sec")
    return result

if __name__ == "__main__":
    n = 10000
    total_sum = speed(n)
    print(f"Сума квадратів від 1 до {n} дорівнює {total_sum}.")












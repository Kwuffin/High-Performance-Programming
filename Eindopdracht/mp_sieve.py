import numpy as np
from mpi4py import MPI
from time import time
import math
from multiprocessing import Pool, cpu_count

comm = MPI.COMM_WORLD


def check_prime(n):
    """
    Checks whether a given integer is a prime or not
    :param n: integer
    :return: Boolean
    """
    if n == 1 or n == 2:  # 1 and 2 are not primes
        return False

    k = 2
    while k * k <= n:
        if n % k == 0:
            return False  # Return False if n can be factored
        k += 1

    # If n cannot be factored, return True
    return True


def split_list(list_length):
    """
    Splits the list up into thread_count amount of smaller lists
    :param list_length: Length of total list
    :return:
    """

    thread_count = comm.Get_size()  # Amount of threads
    # thread_count = 8  # For testing purposes
    chunk_size = math.floor(list_length / thread_count)

    chunks = []
    for i in range(thread_count):
        chunks.append(np.arange(i * chunk_size, i * chunk_size + chunk_size))

    remainder = list_length % thread_count
    last_value = chunks[-1][-1]
    for i in range(remainder):
        chunks[-1] = np.append(chunks[-1], [last_value + (i + 1)])

    return chunks


def main(lists):
    thread_id = comm.Get_rank()  # Get thread id
    if thread_id == 0:
        start = time()
    print(f"{thread_id} starting.")

    with Pool(cpu_count()) as p:
        primes = sum(p.map(check_prime, lists[thread_id]))

    primes = comm.gather(primes, root=0)

    if thread_id == 0:
        print(f"{sum(primes)} primes found.")
        print(f"Time: {time() - start}s")


if __name__ == '__main__':
    LIST_LENGTH = 1000  # TODO: Change this (1.000.000.000) does not work sadly

    split_lists = split_list(LIST_LENGTH)

    main(split_lists)

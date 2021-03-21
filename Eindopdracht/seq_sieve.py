import numpy as np
from time import time


def zeef_bools(lst):
    k = 2
    lst[0:k] = False
    while k*k <= len(lst):
        lst[k*k::k] = False
        k += np.argmax(lst[k+1:-1]) + 1
    return lst


if __name__ == '__main__':
    LIST_LENGTH = 1000000000

    start = time()
    bool_list = np.full(LIST_LENGTH, True, dtype=bool)
    print(f"Number of primes (bool): {np.count_nonzero(zeef_bools(bool_list))}")
    print(f"Time: {time() - start}s")

import numpy as np
from tqdm import tqdm
from time import time
from matplotlib import pyplot as plt


def init_lists(length, max_value, min_value):
    """
    Initializes lists that are later used for the bucket sort

    :param length: User given length of random list.
    :param max_value: Highest number to put in by the user
    :param min_value: Lowest number put in by the user
    :return random list with length n, empty 2D array with 10 rows
    """
    rand_list = np.random.randint(min_value, max_value, size=length)
    sort_list = [[], [],
                 [], [],
                 [], [],
                 [], [],
                 [], []]
    return rand_list, sort_list


def filter_negative(rand_list):
    """
    Filters negative and positive numbers and puts them in separate lists

    :param rand_list: initial random list
    :return:
    """
    neg_list = []
    pos_list = []
    for i in rand_list:
        if i < 0:
            neg_list.append(i)
        else:
            pos_list.append(i)

    return neg_list, pos_list


def distribution_pass(rand_list, sort_list, index):
    """
    Puts each value in 'rand_list' in the correct bucket in 'sort_list'

    :param rand_list: List with random integers
    :param sort_list: Empty bucket list
    :param index: Indicator of which index of the random integer to take.
    :return: A list with values sorted by the one/tenth/hundredth.../etc. number
    """

    maxi = len(str(max(rand_list)))
    mini = len(str(min(rand_list)))
    if maxi >= mini:
        max_digits = maxi
    else:
        max_digits = mini

    for i in rand_list:
        i = str(i).zfill(max_digits)

        value = int(i[-index])
        sort_list[value].append(int(i))
    return sort_list


def gathering_pass(sort_list):
    """
    Flattens the bucket list

    :param sort_list: Sorted bucket list
    :return: flattened sort_list, remove all values from sort_list
    """
    flat_sort_list = [i for lst in sort_list for i in lst]
    sort_list = [[], [],
                 [], [],
                 [], [],
                 [], [],
                 [], []]  # 10 lijsten voor het decimale stelsel. (2 voor een binair stelsel)
    return flat_sort_list, sort_list


def neg_pos(lst):
    """
    Takes a list with integer values and makes them positive/negative.

    :param lst: a list with integer values
    :return: list with all integer values made negative/positive.
    """
    for i in range(len(lst)):
        lst[i] *= -1


def analyse(elapsed_time, sorted_list):
    while True:
        print(f"Sorted list with n = {len(sorted_list)}\n"
              f"{sorted_list}")
        print(f"Finished in {elapsed_time} seconds!")

        number = False
        while not number:
            try:
                user_opt = int(input("Finished sorting!\n\n"
                                     f"1. Run again!\n"
                                     f"2. Measure time with different n values\n"
                                     f"3. Exit.\n"
                                     f"> "))

                if 1 <= user_opt <= 3:
                    number = True
                else:
                    print("Ongeldige invoer.")

            except TypeError:
                print("Voer een getal in!")

        if user_opt == 1:
            looping()

        elif user_opt == 2:
            times = []
            ns = []
            for n in tqdm(range(50000, 1000000, 50000)):
                elapsed_time, lst = main(n, -1000, 1000, False)
                times.append(elapsed_time)
                ns.append(n)

            fig, ax = plt.subplots()
            ax.plot(ns, times)

            ax.set(xlabel='n', ylabel='Time (s)', title='Tests with different n values')
            ax.grid()
            plt.show()

        elif user_opt == 3:
            exit()


def main(n=1000, min_value=0, max_value=100, userIn=True):
    if userIn:
        # User inputs for list length and number range.
        n = int(input("Give list length:\n> "))
        max_value = int(input("Give maximum value:\n> ")) + 1
        min_value = int(input("Give minimum value:\n> "))

    start = time()

    # Initializing lists with given parameters
    rand_list, bucket_list = init_lists(n, max_value, min_value)

    # Filter negative and positive numbers
    neg_list, pos_list = filter_negative(rand_list)

    # If list contains values
    if pos_list:

        # Bucket sorting
        for i in range(len(str(max_value))):
            bucketed_list = distribution_pass(pos_list, bucket_list, i)
            pos_list, bucket_list = gathering_pass(bucketed_list)

    # If list contains values
    if neg_list:

        # Make negative numbers positive
        neg_pos(neg_list)

        # Bucket sorting
        for i in range(len(str(min_value)) - 1):
            bucketed_list = distribution_pass(neg_list, bucket_list, i)
            neg_list, bucket_list = gathering_pass(bucketed_list)

        # Reverse list and make positive numbers negative again
        neg_list.reverse()
        neg_pos(neg_list)

    sorted_list = neg_list + pos_list

    end = time() - start

    return end, sorted_list


def looping():
    timestamp, lst = main()
    analyse(timestamp, lst)


if __name__ == '__main__':
    looping()

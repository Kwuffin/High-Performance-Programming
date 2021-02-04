import numpy as np


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
                 [], []]  # 10 lijsten voor het decimale stelsel. (2 voor een binair stelsel
    return flat_sort_list, sort_list


def neg_pos(lst):
    """
    Takes a list with integer values and makes them positive/negative.

    :param lst: a list with integer values
    :return: list with all integer values made negative/positive.
    """
    for i in range(len(lst)):
        lst[i] *= -1


def main():
    # User inputs for list length and number range.
    n = int(input("Give list length:\n> "))
    max_value = int(input("Give maximum value:\n> ")) + 1
    min_value = int(input("Give minimum value:\n> "))

    # Initializing lists with given parameters
    rand_list, bucket_list = init_lists(n, max_value, min_value)

    # Filter negative and positive numbers
    neg_list, pos_list = filter_negative(rand_list)

    pos = False
    neg = False

    # If list contains values
    if pos_list:
        pos = True

        # Bucket sorting
        for i in range(len(str(max_value))):
            bucketed_list = distribution_pass(pos_list, bucket_list, i + 1)
            pos_list, bucket_list = gathering_pass(bucketed_list)

    # If list contains values
    if neg_list:
        neg = True

        # Make negative numbers positive
        neg_pos(neg_list)

        # Bucket sorting
        for i in range(len(str(min_value)) - 1):
            bucketed_list = distribution_pass(neg_list, bucket_list, i + 1)
            neg_list, bucket_list = gathering_pass(bucketed_list)

        # Reverse list and make positive numbers negative again
        neg_list.reverse()
        neg_pos(neg_list)

    if pos and neg:
        print(neg_list + pos_list)

    elif pos:
        print(pos_list)

    elif neg:
        print(neg_list)


if __name__ == '__main__':
    main()

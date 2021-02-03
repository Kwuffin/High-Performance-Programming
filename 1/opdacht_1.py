import numpy as np


def init_lists(length, max_value):
    """
    Initializes lists that are later used for the bucket sort

    :param length: User given length of random list.
    :return random list with length n, empty 2D array with 10 rows
    """
    rand_list = np.random.randint(max_value, size=length)
    sort_list = [[], [],
                 [], [],
                 [], [],
                 [], [],
                 [], []]
    return rand_list, sort_list


def bucketing(rand_list, sort_list, index, max_value):
    """
    Puts each value in 'rand_list' in the correct bucket in 'sort_list'

    :param rand_list:
    :param sort_list:
    :param index:
    :param max_value:
    :return:
    """

    max_digits = len(str(max_value))

    for i in rand_list:
        i = str(i).zfill(max_digits)

        one_value = int(i[-index])
        sort_list[one_value].append(int(i))
    return sort_list


def gathering_pass(sort_list):
    """
    Flattens the nested list

    :param sort_list:
    :return:
    """
    flat_sort_list = [i for lst in sort_list for i in lst]
    sort_list = [[], [],
                 [], [],
                 [], [],
                 [], [],
                 [], []]
    return flat_sort_list, sort_list


def main():
    n = int(input("Give list length:\n> "))
    max_value = int(input("Give max value:\n> ")) + 1

    rand_list, bucket_list = init_lists(n, max_value)

    for i in range(len(str(max_value))):
        bucketed_list = bucketing(rand_list, bucket_list, i+1, max_value)
        rand_list, bucket_list = gathering_pass(bucketed_list)

    print(rand_list)


if __name__ == '__main__':
    main()

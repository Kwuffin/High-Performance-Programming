import concurrent.futures
import numpy as np


def compare_lists(list_a, list_b):
    """
    Compares all values from both given lists and merges them

    :param list_a: First sorted list
    :param list_b: Second sorted list
    :return: A sorted list that is a superset of list_a and list_b
    """
    combined_list = []
    a_cursor = b_cursor = 0

    while a_cursor < len(list_a) and b_cursor < len(list_b):

        # If element in list_a is bigger than element in list_b
        if list_a[a_cursor] > list_b[b_cursor]:
            combined_list.append(list_b[b_cursor])
            b_cursor += 1

        # If element in list_a is smaller than element in list_b
        else:
            combined_list.append(list_a[a_cursor])
            a_cursor += 1

    combined_list += list_a[a_cursor:] + list_b[b_cursor:]

    return combined_list


def merge_sort(lst):
    """
    Creates the pools and isolates elements on uneven lists.

    :param lst: Random list
    :return: Sorted list
    """

    split_elements = []
    for i in lst:
        split_elements.append([i])

    with concurrent.futures.ProcessPoolExecutor() as executor:
        while len(split_elements) != 1:

            uneven = False
            if len(split_elements) % 2 != 0:
                uneven = True
                left_over = split_elements[-1]
                split_elements.pop(-1)

            results = executor.map(compare_lists, split_elements[::2], split_elements[1::2])

            split_elements = []
            for result in results:
                split_elements.append(result)

            if uneven:
                uneven_list = compare_lists(split_elements[0], left_over)
                split_elements.pop(0)
                split_elements.append(uneven_list)
                uneven = False

        return split_elements[0]


def main():
    randlist = np.random.randint(100, size=100)
    randlist = list(randlist)
    print(f"Random list: {randlist}")
    sorted_list = merge_sort(randlist)
    print(f"Sorted list: {sorted_list}")


if __name__ == '__main__':
    main()

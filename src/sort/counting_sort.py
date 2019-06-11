# COUNTING SORT: Expected input type ---> List of positive and/or negative integers
def counting_sort(unsorted_list):
    max_val, min_val = max(unsorted_list), min(unsorted_list)
    keys = list(range(int(min_val), int(max_val) + 1))
    dictionary = dict(zip(keys, [0]*len(keys)))
    sorted_list = [0] * len(unsorted_list)

    for i in unsorted_list:
        dictionary[i] += 1

    for i in keys:
        if i != min_val:
            dictionary[i] += dictionary[i-1]

    for i in unsorted_list:
        sorted_list[dictionary[i] - 1] = i
        dictionary[i] -= 1
    return sorted_list


if __name__ == '__main__':
    from numpy.random import randint
    input_list = list(randint(-10, 600, 30))
    print(counting_sort(input_list))

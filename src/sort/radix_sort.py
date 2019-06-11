# RADIX SORT: Expected input type ---> List of positive numbers
def counting_sort(unsorted_list, place=1):
    temp_list = list(map(lambda x: int(x / place) % 10, unsorted_list))
    dictionary = dict()
    for i in range(len(temp_list)):
        if temp_list[i] in dictionary:
            dictionary[temp_list[i]].append(unsorted_list[i])
        else:
            dictionary[temp_list[i]] = [unsorted_list[i]]
    sorted_list = []
    for i in set(temp_list):        # used set to fetch the unique values in the list and sort them
        sorted_list.append(dictionary[i])
    sorted_list = [item for _list in sorted_list for item in _list]
    return sorted_list


def radix_sort(input_list):
    output_list = input_list.copy()
    max_length = len(str(max(input_list)))
    for place in range(max_length):
        output_list = counting_sort(output_list, 10 ** place)
    return output_list


if __name__ == '__main__':
    from numpy.random import randint
    input_list = list(randint(0, 600, 30))
    print(radix_sort(input_list))


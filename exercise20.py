from random import randint,choice,sample
import time

def search(search_list,search_number):
    for index, element in enumerate(search_list):
        if element == search_number:
            return index
    return -1


def search_binary(search_list, search_number):
    index = len(search_list)
    if index == 1:
        if search_list[0] == search_number:
            return 0
        else:
            return -1

    if index % 2 == 0:
        index = int(index / 2)
    else:
        index = int(index / 2) + 1

    if search_list[index] == search_number:
        return index
    elif search_list[index] < search_number:
        index_tmp = search_binary(search_list[index:], search_number)
        if index_tmp != -1:
            index = index + index_tmp
        else:
            return -1
    elif search_list[index] > search_number:
        index = search_binary(search_list[:index], search_number)
    return index

if __name__=="__main__":
    print("Welcome to the binari search!")
    search_list = range(100000000000)
    # search_list = sorted(sample(range(1, 1000), 100))
    # search_list = [10, 28, 38, 39, 47, 55, 74, 84, 97, 98, 105, 107, 132, 135, 143, 146, 152, 159, 167, 171, 172, 175, 184, 206, 212, 223, 225, 249, 251, 261, 276, 283, 286, 297, 331, 332, 336, 338, 346, 360, 388, 390, 407, 418, 434, 435, 436, 447, 474, 483, 522, 538, 543, 554, 564, 583, 590, 602, 618, 625, 642, 654, 665, 676, 678, 714, 718, 745, 747, 760, 777, 780, 781, 788, 795, 798, 821, 825, 830, 839, 841, 853, 858, 865, 869, 870, 877, 892, 894, 895, 897, 930, 963, 965, 973, 979, 983, 985, 987, 992]
    search_number = int(input('Input number:'))

    start_time = time.time()
    index = search(search_list,search_number)
    if index == -1:
        print('not found')
    else:
        print('Index: ' + str(index))
    end_time = time.time()
    print(end_time-start_time)

    start_time = time.time()
    index = search_binary(search_list,search_number)
    if index == -1:
        print('not found')
    else:
        print('Index using binary search: ' + str(index))
    end_time = time.time()
    print(end_time-start_time)
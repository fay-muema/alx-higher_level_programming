#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    num = 0

    for i in unique_numbers:
        num += i
    return (num)

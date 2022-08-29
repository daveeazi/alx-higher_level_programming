#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or len(my_list) <= idx):
        return my_list
    newList = my_list[:]
    newList[idx] = element
    return newList

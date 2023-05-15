#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if 0 <= idx < len(my_list):
        temp[idx] = element
        return(temp)
    else:
        return(my_list)

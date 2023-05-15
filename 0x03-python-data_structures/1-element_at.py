#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return ("none")
    elif 0 <= idx < len(my_list):
        return (my_list[idx])


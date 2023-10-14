#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if item == search else item for item in my_list]
    return new_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

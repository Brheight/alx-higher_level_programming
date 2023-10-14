#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()  # Create an empty set to store unique integers
    result = 0
    
    for number in my_list:
        if number not in unique_set:
            unique_set.add(number)  
            result += number 
    
    return result

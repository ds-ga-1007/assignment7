'''
@author: danielamaranto
'''
from input_functions import list_interval_assignment, single_interval_assignment
from interval_functions import mergeIntervals, mergeOverlapping, insert

def interactive():
# This function uses the above code and implements the program specified in question 5.
    main_list = list_interval_assignment()
    new_interval = 1
    while new_interval != 0:  
        new_interval = single_interval_assignment()
        main_list = insert(main_list, new_interval)
        print(main_list)

if __name__ == '__main__':
    interactive()
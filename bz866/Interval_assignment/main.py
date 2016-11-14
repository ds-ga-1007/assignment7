'''
Created on 2016年11月10日

@author: bz866
'''
import sys
from Interval_assignment.interval import *


def inputloop():
    #Input the initial list of intervals
    while True:
        try:
            initial_list=input("List of intervals?")      
            
            if initial_list.lower()=='quit':
                exit('End')
            else:
                interval_list=initial_list.split(", ")
                intervals=[]
                
            for interval_item in interval_list:
                intervals.append(interval(interval_item))
            break
        except ValueError as word:
            print(word)
            pass
        except EOFError:
            sys.exit(0)
            pass

    
    #loop for insert intervals one by one
    while True:
        try:
            next_interval=input('Interval?')
            if next_interval == 'quit':
                exit('End')
            else:
                new_interval_list=insert(intervals,interval(next_interval))
                print(str(new_interval_list)[1:-1])
        except ValueError as word:
            print(str(word))
            pass
        except EOFError:
            sys.exit(0)
            pass
        
if __name__ == '__main__':
    inputloop()
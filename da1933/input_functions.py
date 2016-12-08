'''
@author: danielamaranto
'''
from interval_class import interval

# In order to play the game to the assignment specifications,
# there are 2 types of interval input functions.

def list_interval_assignment():
    interval_list = []
    valid = False
    while valid is False:
        inputs = input('List of valid intervals? ')
        inputs = inputs.replace(' ','')
        try:
            assignments = list(inputs.split(sep=','))
            while (len(assignments) > 0):
                user_interval = assignments[:2] 
                assignments.pop(0)
                assignments.pop(0)
                if user_interval[0][0] is '[':
                    start = '['
                    lower = int(user_interval[0][1:])
                    lower_print = user_interval[0][1:]
                elif user_interval[0][0] is '(':
                    start = '('
                    lower = int(user_interval[0][1:]) + 1
                    lower_print = user_interval[0][1:]
                if user_interval[1][-1] is ']':
                    end = ']'
                    upper = int(user_interval[1][:-1])
                    upper_print = user_interval[1][:-1]
                    if upper >= lower:
                        add_interval = interval(start, lower_print, upper_print, end)
                        interval_list.append(add_interval)
                        valid = True
                    else:
                        print('Invalid Interval')
                elif user_interval[1][-1] is ')':
                    end = ')'
                    upper = int(user_interval[1][:-1]) - 1
                    upper_print = user_interval[1][:-1]
                    if upper >= lower:
                        add_interval = interval(start, lower_print, upper_print, end)
                        interval_list.append(add_interval)
                        valid = True
                    else:
                        print('Invalid Interval')
                        
# All invalid entries are handled here, except in the case of non-sensical bounds.
        except ValueError:
            print('Invalid Interval')
        except IndexError:
            print('Invalid Interval')
        except UnboundLocalError:
            print('Invalid Interval')
        except TypeError:
            print('Invalid Interval')
    
    return interval_list

def single_interval_assignment():
    single_interval_list = []
    valid = False
    while valid is False:
        inputs = input('Interval? ')
        if inputs == 'quit':
            return 0
            break
        inputs = inputs.replace(' ','')
        try:
            user_interval = inputs.split(sep=',')
            if user_interval[0][0] is '[':
                start = '['
                lower = int(user_interval[0][1:])
                lower_print = user_interval[0][1:]
            elif user_interval[0][0] is '(':
                start = '('
                lower = int(user_interval[0][1:]) + 1
                lower_print = user_interval[0][1:]
            if user_interval[1][-1] is ']':
                end = ']'
                upper = int(user_interval[1][:-1])
                upper_print = user_interval[1][:-1]
                if upper >= lower:
                    single_interval = interval(start, lower_print, upper_print, end)
                    single_interval_list.append(single_interval)
                    valid = True
                else:
                    print('Invalid Interval')
            elif user_interval[1][-1] is ')':
                end = ')'
                upper = int(user_interval[1][:-1]) - 1
                upper_print = user_interval[1][:-1]
                if upper >= lower:
                    valid = True
                    single_interval = interval(start, lower_print, upper_print, end)
                    single_interval_list.append(single_interval)
                else:
                    print('Invalid Interval')
        except ValueError:
            print('Invalid Interval')
        except IndexError:
            print('Invalid Interval')
        except UnboundLocalError:
            print('Invalid Interval')
        except TypeError:
            print('Invalid Interval')
    
    return single_interval_list
    
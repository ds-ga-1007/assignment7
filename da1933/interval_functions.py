'''
@author: danielamaranto
'''

from interval_class import interval
from defined_exceptions import mergeException

def mergeIntervals(int1, int2):
# The merge function first takes into account what the bounds of each interval are.
    if type(int1.intRange()) is int:
        max1 = int1.intRange()
        min1 = int1.intRange()
    elif type(int1.intRange()) is tuple:
        max1 = max(int1.intRange())
        min1 = min(int1.intRange())
    if type(int2.intRange()) is int:
        max2 = int2.intRange()
        min2 = int2.intRange()
    elif type(int2.intRange()) is tuple:
        max2 = max(int2.intRange())
        min2 = min(int2.intRange())

# After determining the bounds, the new interval is created.        
    if (max1 + 1) >= min2 and max1 <= max2 and min1 <= min2:
        start = int1.start
        low   = int1.lower_print
        up    = int2.upper_print
        end   = int2.end
    elif (max2 + 1) >= min1 and max2 <= max1 and min2 <= min1:
        start = int2.start
        low   = int2.lower_print
        up    = int1.upper_print
        end   = int1.end
    elif (max1 + 1) >= min2 and max1 <= max2 and min1 >= min2:
        start = int2.start
        low   = int2.lower_print
        up    = int2.upper_print
        end   = int2.end
    elif (max2 + 1) >= min1 and max2 <= max1 and min2 >= min1:
        start = int1.start
        low   = int1.lower_print
        up    = int1.upper_print
        end   = int1.end
    else:
        raise mergeException()
    
    newInterval = interval(start, low, up, end)
    return newInterval

def mergeOverlapping(intervals):
# This function makes use of mergeIntervals, and uses
# lists to consolidate severalintervals at once.
    unmerged = intervals[:]
    merged = []
    merged.append(unmerged[0])
    unmerged.pop(0)
    
    while len(unmerged) > 0:
        try:
            merged.append(mergeIntervals(merged[-1], unmerged[0]))
            merged.pop(-2)
            unmerged.pop(0)
        except mergeException:
            merged.append(unmerged[0])
            unmerged.pop(0)
        except IndexError:
            unmerged.pop(0)
    return merged

def insert(intervals, newint):
# Insert adds a new interval to the existing list and sorts it.
# The result is passed to mergeOverlapping, which then passes
# its contents to mergeIntervals.

    merged = intervals[:]
    try:
        merged.append(newint[0])
        merged.sort()
        newList = mergeOverlapping(merged)
    except TypeError:
        newList = 0
    return newList    

'''
@author: danielamaranto
'''

class mergeException(Exception):
    def __str__(self):
        return "Intervals can't be merged."
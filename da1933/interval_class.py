'''
@author: danielamaranto
'''
class interval:
    '''
    The class takes 4 inputs because each interval has 4 main charactersitics. 
    Each interval is given a print value and a numeric value because of the 
    difference between brackets and parentheses.
   '''
    
    def __init__(self, open, lower, upper, close):
        self.start = open
        self.end = close
        self.lower_print = lower
        self.upper_print = upper
        if self.start == '[':
            self.lower = int(lower)
        else:
            self.lower = int(lower) + 1
        if self.end == ']':
            self.upper = int(upper)
        else:
            self.upper = int(upper) - 1
                    
    def intRange(self):
        if self.lower == self.upper:
            self.numeric_interval = self.lower
        else:
            self.numeric_interval = tuple(range(self.lower,self.upper + 1))
        return self.numeric_interval
    
    #This sort attribute is included to allow for insertion into existing lists.
    def __lt__(self, other):
        return self.lower < other.lower        
    
    def __repr__(self):
        printable = str(self.start + self.lower_print + ',' + self.upper_print + self.end)
        return printable

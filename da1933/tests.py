'''
@author: danielamaranto
'''
import unittest
from interval_functions import mergeIntervals, mergeOverlapping, insert
from interval_class import interval

#The following tests test the Interval class and its 3 main functions.


class intervalTests(unittest.TestCase):
    
    def test_class(self):
        interval_test = interval('[','3','9',')')
        interval_result = interval('[','3','9',')')
        self.assertEqual(interval_test, interval_result)
    
    def test_merge_interval(self):
        interval1 = interval('[','1','5',')')
        interval2 = interval('[','3','9',')')
        interval_result = [interval('[','1','9',')')]
        self.assertEqual(mergeIntervals(interval1, interval2), interval_result)
    
    def test_merge_overlapping(self):
        merge_test_list = [interval('[','1','5',')'), interval('[','3','9',')')]
        merge_test_result = [interval('[','1','9',')')]
        self.assertEqual(merge_test_list, merge_test_result)
        
    def test_insert(self):
        insert_test_list = [interval('[','1','3',')'), interval('[','7','9',')')]
        insert_test_addition = [interval('[','4','6',']')]
        insert_test_results = [interval('[','1','9',')')]
        
        self.assertEqual(insert(insert_test_list,insert_test_addition),insert_test_result)
    
if __name__ == '__main__':
    unittest.main()

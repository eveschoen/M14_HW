import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        lover1 = BookLover('eve', 'es@gmail.com', 'mystery')
        lover1.add_book('Harry Potter', 5)
        
        expected = 1
        actual = len(lover1.book_list)
        self.assertEqual(actual, expected)
        
    def test_2_add_book(self):
        lover2 = BookLover('rachel', 'rg@gmail.com', 'romance')
        lover2.add_book('Redeeming Love', 5)
        lover2.add_book('Redeeming Love', 4)
        
        expected = 1
        actual = len(lover2.book_list)
        self.assertEqual(actual, expected)
    
    def test_3_has_read(self):
        lover3 = BookLover('matt', 'mm@gmail.com', 'dumb')
        lover3.add_book('Dumb and Dumber', 2)
        
        expected = True
        actual = lover3.has_read('Dumb and Dumber')
        self.assertEqual(actual, expected)
        
    def test_4_has_read(self):
        lover4 = BookLover('rob', 'rm@gmail.com', 'self-help')
        lover4.add_book('How To', 1)
        
        expected = False
        actual = lover4.has_read('Nancy Drew')
        self.assertEqual(actual, expected)
        
    def test_5_num_books_read(self):
        lover5 = BookLover('josh', 'jg@gmail.com', 'crime')
        lover5.add_book('How To', 1)
        lover5.add_book('Dumb and Dumber', 2)
        lover5.add_book('Redeeming Love', 4)
        lover5.add_book('Harry Potter', 5)
        
        expected = 4
        actual = len(lover5.book_list)
        self.assertEqual(actual, expected)
        
    def test_6_fav_books(self):
        lover6 = BookLover('neil', 'na@gmail.com', 'none')
        lover6.add_book('How To', 1)
        lover6.add_book('Dumb and Dumber', 2)
        lover6.add_book('Redeeming Love', 4)
        lover6.add_book('Harry Potter', 5)
        lover6.add_book('Glass Castle', 3)
        
        favs = lover6.fav_books()
        rates_list = list(favs['book_rating'])
        
        actual = all(x > 3 for x in rates_list)
        expected = True
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
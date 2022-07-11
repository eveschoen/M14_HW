import pandas as pd
import numpy as np

class BookLover:
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
    
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].unique():
            print('This book is already in the list')
        else:
            new_book = pd.DataFrame({'book_name': [book_name],\
                                     'book rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].unique():
            return True
        else:
            return False
    
    def num_books_read(self):
        count_books_read = len(self.book_list)
        return count_books_read
    
    def fav_books(self):
        favs = self.book_list[self.book_list['book_rating'] > 3]
        return favs
    
    
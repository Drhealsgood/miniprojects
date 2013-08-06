'''
Created on 6/08/2013

@author: luke
'''
import random
from library_catalog import *

if __name__ == '__main__':
    # First, we need to have a library
    library         = Library()
    # we'll need to have a factory to make books
    book_factory    = BookFactory()
    # we'll need a list of book names
    names   = """
    Each one of these words is sadly going to be a name
    I tried to find a csv file online, but had no luck
    it is often difficult to find data, but thank the all
    that Python has such nice string work!
    """
    
    split   = " ".join(filter(lambda word: '\n' not in word and len(word)>1,
                     names.split(' ')))
    gen_isbn= lambda size: "".join([str(random.randint(0,9)) for _ in range(size)])
    args    = [(word,gen_isbn(13),"Interesting Stu","bad") for word in split.split(" ")]
    library.add_books(book_factory.get_object(args))
    # have a look at books
    books = library.books_all
    print(books)
    # make some customers 
    customers = ["Garry","Phil","Rob"]
    # can't check same book out twice
    library.checkout(books[0], customers[0])
    print(books[0].checked_out_to)
    library.checkout(books[0], customers[1])
    print(books[0].checked_out_to)
    for book in books[1:]:
        library.checkout(book,customers[2])
    
    
    
    
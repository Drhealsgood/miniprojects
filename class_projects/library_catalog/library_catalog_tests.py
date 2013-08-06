'''
Created on 31/07/2013

@author: luke

IDoes the ISBN-13 have any meaning imbedded in the numbers?
    The five parts of an ISBN are as follows:
    1. The current ISBN-13 will be prefixed by "978"
    2. Group or country identifier which identifies a national or geographic grouping of publishers;
    3. Publisher identifier which identifies a particular publisher within a group;
    4. Title identifier which identifies a particular title or edition of a title;
    5. Check digit is the single digit at the end of the ISBN which validates the ISBN.
'''
import random
import unittest
from datetime import datetime
from datetime import date, timedelta
from library_catalog import Book, Library
from mock import Mock

class TestBook(unittest.TestCase):
    """
    A book should have a title, an ISBN, an author, a genre
    and a checked out status.
    Title, isbn, author, genre should be string and 
    checked out should be bool
    """
    _book      = Book(title="Book Tests", isbn="0000111125433",
                           author="Book Writer", genre="Educational",)
    _class_vars= vars(_book)
    
    def testInit(self):
        """
        Passing incorrect types should result in type errors
        """
        with self.assertRaises(TypeError):
            Book(title=50, isbn="0000111125433",
                           author="Book Writer", genre="Educational",)
            Book(title="Book Tests", isbn=50,
                           author="Book Writer", genre="Educational",)
            Book(title="Book Tests", isbn="0000111125433",
                           author=100, genre="Educational",)
            Book(title="Book Tests", isbn="0000111125433",
                           author="Book Writer", genre=("Educational",),)
    def testTitle(self):
        def set_title(title):
            self._book.title    = title
        """
        A book should have a title when it is created;
        the title of a book should not be able to change
        as this would imply a new book has been created
        """
        
        title       = '_title'
        # ensure book has a title
        self.assertIn(title,self._class_vars)
        self.assertNotEqual(self._class_vars[title],'','Expected legitimate title')
        # test if setting title fails
        with self.assertRaises(AttributeError):
            set_title('should_fail')
        self.assertEqual("Book Tests",self._book.title)
        
    def testISBN(self):
        def set_isbn(num):
            self._book.isbn     = num
        def bad_impl():
            Book("title","123456789","author","genre")
        """
        An ISBN number is 13 numbers long
        A book should have an ISBN when created
        the ISBN of a book should not be able to change
        """
        isbn        = '_isbn'
        isbn_num    = "0000111125433"
        self.assertIn(isbn,self._class_vars)
        self.assertEqual(self._class_vars[isbn],isbn_num)
        self.assertEqual(len(self._class_vars[isbn]),13)
        # ISBN should be 13 chars long
        with self.assertRaises(AttributeError):
            bad_impl()
            set_isbn('someNumber')
        self.assertEqual("0000111125433",self._book.isbn)
        
    def testAuthor(self):
        def set_author(author):
            self._book.author   = author
        """
        A book should have an author upon creation
        the author of a book should not be able to change
        """
        author      = '_author'
        self.assertIn(author,self._class_vars)
        self.assertNotEqual(self._class_vars[author],'')
        with self.assertRaises(AttributeError):
            set_author('fail')
        self.assertEqual("Book Writer",self._book.author)
        
    def testGenre(self):
        def set_genre(x):
            self._book.genre = x
        self.assertEqual("Educational",self._book.genre)
        with self.assertRaises(AttributeError):
            set_genre('fail')
            
    def testCheckedOut(self):
        """
        A book cshould have a property stating whether
        or not the book is checked out. This property
        should be setable. This property should always be a 
        boolean
        """
        # It's presumed a book that has just been added to the 
        # library will not be checked out
        self.assertFalse(self._book.checked_out[0],"Book should not yet be checked out")
        self._book.checked_out      = True
        # date should be noted in checked_out status
        self.assertEqual(self._book.checked_out,(True,date.today()))
        with self.assertRaises(TypeError):
            self._book.checked_out  = "True"
            
    def testCheckedOutTo(self):
        """
        A book should always be checked out to a customer
        or be back at the library(None)
        """
        lib   = Library()
        lib.add_books(self._book)
        self.assertIsNone(lib.books_all[0].checked_out_to)
        # when a book is checked out it should obtain status checked_out_to 
        # to point to a cus
        cus         = "Garry"
        lib.checkout(self._book,cus)
        self.assertEqual(cus,self._book.checked_out_to)
        
    def testOverDue(self):
        """
        A book becomes overdue after '2 weeks?'
        I don't know how to test this.
        """
        lib     = Library()
        lib.add_books(self._book)
        
        real    = Book("book_seven",'0000111125433',"author_seven","genre_seven")
        real.method = Mock(return_value=datetime().today()+datetime.timedelta(days=14))
        print(real.method(1234,"hey You!"))
        
        
class TestLibrary(unittest.TestCase):        
    """
    A library should have a listing of all books the library owns;
    the books available for hire; the books that are currently being
    hired; the ability to check in and check out books; the ability
    to add/remove books from the library permanently.
    """
    gen_isbn    = lambda size: "".join([str(random.randint(0,9)) for _ in range(size)])
    _library    = Library()
    __books     = [
                   Book("book_two",gen_isbn(13),"author_two","genre_two"),
                   Book("book_three",gen_isbn(13),"author_three","genre_three"),
                   Book("book_four",gen_isbn(13),"author_four","genre_four"),
                   Book("book_five",gen_isbn(13),"author_five","genre_five"),
                   Book("book_six",gen_isbn(13),"author_six","genre_six"),
                   Book("book_seven",gen_isbn(13),"author_seven","genre_seven"),
                   ]
    
    def setUp(self):
        self._library._clear_data()
    
    def testBooksAll(self):
        """
        Should return all books library has on hand.
        A library should start with no books on hand
        books should not be setable
        """
        self.assertEqual(self._library.books_all,[])
        with self.assertRaises(AttributeError):
            self._library.books_all = self.__books
            
    def testAddBooks(self):
        """
        should be able to add books to library catalog. Should only accept
        books, anything else should be ignored; should return True to indicate success
        """
        res     = self._library.add_books(book for book in self.__books)
        self.assertTrue(res)
        # library's books should be same len as books added now
        self.assertEqual(self._library.books_all,self.__books)
        # add extra books via unpacking
        b1      = Book("book_eight",TestLibrary.gen_isbn(13),"author_eight","genre_eight"),
        b2      = Book("book_nine",TestLibrary.gen_isbn(13),"author_nine","genre_nine")
        self._library.add_books(b1,b2)
            
    def testCheckOut(self):
        """
        testCheckout also tests books_out
        checkOut ensures book is not currently out and exists in library catalog;
        checkout then checks the book out to a customer
        Checkout should also add a date that the book was checked out to the book's
        properties to signal when it is over due.
        """
        
        # add default books to library
        self._library.add_books(book for book in self.__books) 
        book    = self._library.books_all[0]
        # checkout time = today
        today = date.today()
        self._library.checkout(book,"Garry")
        # bOOK SHOULD now be in books_out
        self.assertIn(book,self._library.books_out)
        # booksout[book] should link to person who got book out and what date
        self.assertEqual(self._library.books_out[book],("Garry",today))
        # books_out should only contain one book as only one has been withdrawn
        self.assertEqual(len(self._library.books_out),1)
        # when a book is checked out it should be removed from books_in
        self.assertEqual(len(self._library.books_in),len(self._library.books_all)-1)
        self.assertNotIn(book,self._library.books_in)
    
    def testCheckIn(self):
        """
        testCheckIn tests the returning of a book.
        check_in should ensure book is not in, ensure that it is in books_all,
        finally it should return book in by removing its checkedout status
        and reutrning it to books_in
        """
        # a book must first be checked out
        self._library.add_books(book for book in self.__books)
        book    = self._library.books_all[0]
        book_in = self._library.books_all[1]
        self._library.checkout(book,"Garry")
        self.assertIn(book,self._library.books_out)
        # try t0 return a book that is already in
        self.assertIn(book_in,self._library.books_in)
        with self.assertRaises(ValueError):
            self._library.checkin(book_in)
            # try to return a book that is not in books_all
            self._library.checkin(Book("book_nine",TestLibrary.gen_isbn(13),"author_nine","genre_nine"))
        # correctly return a book
        self._library.checkin(book)
        self.assertNotIn(book,self._library.books_out)
        self.assertIn(book,self._library.books_in)
        self.assertIsNone(book.checked_out_to)
        self.assertFalse(book.checked_out[0])
        # book was checked in today
        self.assertEqual(book.checked_out[1],date.today())
        
    def testBooksOut(self):
        # a Library with no books should return False
        self.assertFalse(self._library.books_out)
        # other testing logic taken care of in testCheckOut
        
    def testBooksIn(self):
        """
        Library should be able to return all books currently IN
        """
        # a Library with no books should not have any  in
        self.assertFalse(self._library.books_in)
        # when books are added they should all be in Books In
        self._library.add_books(book for book in self.__books)
        self.assertEqual(self._library.books_all,self._library.books_in)
        # other testing logic taken care of in testCheckOut
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
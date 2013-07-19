'''
Created on 20/07/2013

@author: luke
'''
import unittest


class TestMovie_Store(unittest.TestCase):
    """
        It is expected a store will have a database of stock and customers.
        As such, a store should be able to add new customers, and stock, to the database as well
        as  remove them; the store should be able to rent out and return rentals;  it should be able
        to check if rentals are over due and generate a summary of accounts of overdue books
        """

    def setUp(self):
        # create a new store
        self._store     = movie_store.Store()


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def testAddCustomer(self):
        f       = self._store.customers
        curr    = len(f)
        self.assertEqual(len(f)-f,1)
        for cus in f:
            self.assertIsInstance(f[f],movie_store.Customer)
    
    def testRemoveCustomer(self):
        cus_id   = 42
        curr     = self._store.customers
        self._store.addCustomer(cus_id)
        self.assertIn(42,curr)
        self._store.removeCustomer(cus_id)
        curr      = self._store.customers
        self.assertNotIn(42,curr)
        
    def testOverdue(self):
        """
        check_overdue will return all movies overdfue
        """
        self._store.add_stock_item(42)
        self._store.stock[42].overdue    = True
        self.assertIn(42,self._store.check_overdue())
        
    def testAddStock(self):
        curr        = len(self._store.stock)
        self._store.add_stock(10)
        self.assertEqual(len(self._store.stock)-curr,1) and self.assertIn(10,self._store.stock)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
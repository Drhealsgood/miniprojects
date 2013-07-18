'''
Created on 18/07/2013

@author: luke
'''
import unittest
from lookup import Lookup

class TestLookup(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCountryFromIPName(self):
        (name,code) = Lookup.countryFromIP('101.98.154.154')
        self.assertEqual(name,'New Zealand')
        self.assertEqual(code,'NZ')
        (name,code) = Lookup.countryFromName('duckduckgo.com')
        self.assertEqual(name,"Singapore")
        self.assertEqual(code,'SG')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
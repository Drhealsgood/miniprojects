'''
Created on 19/07/2013

@author: luke
'''
import unittest
import calculator


class TestCalculator(unittest.TestCase):


    def setUp(self):
        self._calc  = calculator.Calculator()


    def tearDown(self):
        pass


    def testAddition(self):
        """
        Addition should be able to take a bunch of args; a sequence; or two values
        and return the sum of them
        """
        self.assertEqual(4,self._calc.add(2,2))
        self.assertEqual(20,self.calc.add(5,4,5,6))
        self.assertEqual(sum(range(50)),self.calc.add(range(50)))
        self.assertEqual(sum(range(50))+3,self.calc.add(range(50),3))
        
    def testSubtraction(self):
        """
        Subtraction should subtract all numbers that follow the initial number
        from the initial number
        """
        self.assertEqual(0,self.calc.sub(2,2))
        self.assertEqual(0,self.calc.sub(10,5,3,2))
        self.assertEqual(0,self.calc.sub(10,[5,3,2]))
        self.assertEqual(0,self.calc.sub(10,[5,3],2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
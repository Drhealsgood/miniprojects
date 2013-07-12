'''
Created on 12/07/2013

@author: luke
'''
import unittest
import conversions


class TestConverter(unittest.TestCase):
    converter   = conversions.Converter()



    def testBinaryToDecimal(self):
        binToDec    = lambda value: self.converter.binToDec(value) 
        tests       = {'1010':10,'0010':2,'00011010':26}
        for bin,val in tests:
            self.assertEqual(binToDec(bin), val)

    def testDecimalToBinary(self):
        decToBin    = lambda value: self.converter.decToBin(value)
        tests       = {'1010':10,'0010':2,'00011010':26}
        for bin,val in tests:
            self.assertEquals(decToBin(val), bin)
            
    def testCelsiusToX(self):
        pass
    
    def testFarenheitToX(self):
        pass
    
    def testKelvinToX(self):

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
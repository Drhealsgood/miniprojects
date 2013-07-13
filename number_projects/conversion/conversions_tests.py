'''
Created on 12/07/2013

@author: luke
'''
import unittest
import conversions
import json
import urllib.request


class TestConverter(unittest.TestCase):
    converter   = conversions.Converter()

    def testBinaryToDecimal(self):
        binToDec    = lambda value: self.converter.binToDec(value) 
        tests       = {'1010':10,'0010':2,'00011010':26}
        for bin in tests:
            self.assertEqual(binToDec(bin), tests[bin])

    def testDecimalToBinary(self):
        decToBin    = lambda value: self.converter.decToBin(value)
        tests       = {'1010':10,'0010':2,'00011010':26}
        for bin in tests:
            self.assertEquals(decToBin(tests[bin]), bin)
            
    def testTemperatureConversion(self):
        conversion  = lambda msr_from, msr_to, amt: self.converter.tempConvert(msr_from, msr_to, amt)
        celToFar    = conversion('celsius','farenheit',30)
        celToKel    = conversion('celsius', 'kelvin',30)
        farToCel    = conversion('farenheit', 'celsius',100)
        farToKel    = conversion('farenheit', 'kelvin',100)
        kelToCel    = conversion('kelvin','celsius',300)
        kelToFar    = conversion('kelvin','farenheit',300)
        self.assertRaises(TypeError, conversion('asg','another',300))
        self.assertEquals(celToFar,86)
        self.assertEquals(celToKel, 303.15)
        self.assertEquals(farToCel,37.778)
        self.assertEquals(farToKel,310.928)
        self.assertEquals(kelToCel,26.85)
        self.assertEquals(kelToFar,80.33)
        
    def testCurrencyExchange(self):
        curr_exchange   = lambda c_one, c_two, amount: self.converter.currencyExchange(c_one,c_two,amount)
        exg_amt         = curr_exchange('USD','NZD',50)
        curr_page       = urllib.request.urlopen('http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
        print(json.loads(curr_page.read().decode(encoding='UTF-8')))
        curr_details    = json.loads(curr_page.read().decode(encoding='UTF-8'))
        usd,nzd         = curr_details['USD'], curr_details['NZD']
        convert_amt     = nzd/usd
        result          = convert_amt*50
        self.assertEqual(exg_amt, result) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
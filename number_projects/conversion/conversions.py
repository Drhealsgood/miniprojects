'''
Created on 12/07/2013

@author: luke
'''

class Converter():
    
    def binToDec(self, bin_no):
        """
        @param bin_no:  a string representation of a binary number
        @return:        an integer value of the binary number passed
        """
        pass
    
    def decToBin(self, dec_no):
        """
        @param dec_no:  an integer value 
        @return:        a string representation of the decimal value passed
        """
        pass
    
    def currencyExchange(self,con_from,con_to,value):
        """
        @param con_from:a string representation of the currency to convert from
        @param con_to:  a string representation of the currency to convert to
        @param value:   amount to convert
        @return:        the value of the conversion from con_from to con_to of value
        """
        pass
    
    def tempConvert(self,msr_from,msr_to,amt):
        """
        @param msr_from:a string representation of the measurement to convert from
        @param msr_to:  a string representation of the measurement to convert to
        @param amt:     the value to convert
        @return:        the converted temperature value
        """
        pass
    pass
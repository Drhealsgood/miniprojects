'''
Created on 12/07/2013

@author: luke
'''
from math import ceil

class Converter():
    
    @classmethod
    def binToDec(cls, bin_no):
        """
        @param bin_no:  a string representation of a binary number
        @return:        an integer value of the binary number passed
        """
        pass
    
    @classmethod
    def decToBin(cls, dec_no, bit_rep):
        """
        @param dec_no:  an integer value 
        @param bit_rep: bit representation amount
        @return:        a string representation of the decimal value passed
        """
        if dec_no > 0:
            return str(bin(dec_no)[2:].zfill(bit_rep))
        return '-' + str(bin(dec_no))[2:].zfill(bit_rep)
        
    
    @classmethod
    def currencyExchange(cls,con_from,con_to,value):
        """
        @param con_from:a string representation of the currency to convert from
        @param con_to:  a string representation of the currency to convert to
        @param value:   amount to convert
        @return:        the value of the conversion from con_from to con_to of value
        """
        pass
    
    @classmethod
    def tempConvert(cls,msr_from,msr_to,amt):
        """
        @param msr_from:a string representation of the measurement to convert from
        @param msr_to:  a string representation of the measurement to convert to
        @param amt:     the value to convert
        @return:        the converted temperature value
        """
        pass
    pass
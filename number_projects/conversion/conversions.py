'''
Created on 12/07/2013

@author: luke
'''
from math import ceil
import urllib.request
import json

class Converter():
    _temps   = {'cf': lambda c: c*(9/5)+32,
               'fc': lambda f: (f-32)*(5/9),
               'ck': lambda c: c+273.15,
               'kc': lambda k: k-273.15,
               'fk': lambda f: (f+459.67)*5/9,
               'kf': lambda k: k*(9/5)-459.67
        } 
    
    @classmethod
    def binToDec(cls, bin_no):
        """
        @param bin_no:  an integer or str representation of a binary number
        @return:        an integer value of the binary number passed
        """
        dec     = 0
        i       = 0
        if not isinstance(bin_no,int):
            try: bin_no = int(bin_no)
            except: raise TypeError
        while bin_no>0:
            dec     += ((bin_no%10)*(2**i))
            bin_no  //= 10
            i       += 1
        return dec
            
                        
    
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
        result          = 0
        curr_page       = urllib.request.urlopen('http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
        obj             = curr_page.read().decode(encoding='UTF-8')
        content         = json.loads(obj)
        try:
            _from       = content['rates'][con_from] 
            _to         = content['rates'][con_to]
            convert_amt = _to/_from
            result      = convert_amt*value
        except:
            raise NameError
        return result
            
        
    
    @classmethod
    def tempConvert(cls,msr_from,msr_to,amt):
        """
        @todo:    Rounding... /sigh
        @param msr_from:a string representation of the measurement to convert from
        @param msr_to:  a string representation of the measurement to convert to
        @param amt:     the value to convert
        @return:        the converted temperature value
        """
        try: return cls._temps[msr_from[0]+msr_to[0]](amt)
        except KeyError: "Cannot convert from {0} to {1}".format(msr_from,msr_to)
        
    pass
'''
Created on 18/07/2013

@author: luke
'''
import pygeoip
PYGEO_DATABASE      = '../resources/pygeo/GeoIP.dat'
GEOIP               = pygeoip.GeoIP(PYGEO_DATABASE,pygeoip.MEMORY_CACHE)

class Lookup(object):
    
    """
    Country from IP Lookup – 
    Enter an IP address and find the country that IP is registered in.
    """
    @classmethod
    def countryFromIP(cls,ip):
        return(GEOIP.country_name_by_addr(ip),GEOIP.country_code_by_addr(ip))
    
    @classmethod
    def countryFromName(cls,name):
        return(GEOIP.country_name_by_name(name),GEOIP.country_code_by_name(name))
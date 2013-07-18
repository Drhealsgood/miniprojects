'''
Created on 18/07/2013

@author: luke
'''
import pygeoip
PYGEO_DATABASE      = '../resources/pygeo/GeoIP.dat'
GEOIP               = pygeoip.GeoIP(PYGEO_DATABASE,pygeoip.MEMORY_CACHE)

class Lookup(object):
    
    @classmethod
    def countryFromIP(cls,ip):
        """
        Country from IP Lookup – 
        Enter an IP address and find the country that IP is registered in.
        """
        return(GEOIP.country_name_by_addr(ip),GEOIP.country_code_by_addr(ip))
    
    @classmethod
    def countryFromName(cls,name):
        """
        Country from site name lookup -
        Enter a site name and find the country that site is registered in.
        """
        return(GEOIP.country_name_by_name(name),GEOIP.country_code_by_name(name))
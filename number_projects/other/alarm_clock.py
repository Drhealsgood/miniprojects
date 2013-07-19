'''
Created on 18/07/2013

@author: luke
@todo: pyglet doesn't work with python 3 :(
'''
import time
from subprocess import Popen

class Alarm(object):
    '''
    classdocs
    '''
    _sound        = '/home/luke/Music/Saints Row The Third - The Soundtrack'
    
    
    def timer(self,timex):
        """
        time = time in seconds since epoch
        """
        activate    = time.time()+timex
        while time.time() < activate:
            print(time.time(),activate)
        print("out of loop")
        Popen(["vlc",self._sound])
        
    def alarm(self,timex):
        """
        Time = time in seconds since epoch to set it off
        """
        time.sleep(timex-time.time())
        print("out of loop")
        Popen(["vlc",self._sound])
        
if __name__ == "__main__":
    x       = Alarm()
    y = "Saturday 20 July 02:00:00 2013"
    print (time.mktime(y))
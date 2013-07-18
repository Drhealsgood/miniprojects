'''
Created on 18/07/2013

@author: luke
@todo: pyglet doesn't work with python 3 :(
'''
import time
import pyglet

class Alarm(object):
    '''
    classdocs
    '''
    _alarm          = pyglet.media.load('/home/luke/Music/Saints Row The Third - The Soundtrack')

    def timer(self,time):
        """
        time = time in seconds since epoch
        """
        activate    = time.time()+time
        while time.time() < activate:
            pass
        self._alarm.play()
        pyglet.app.run()
        
    def alarm(self,time):
        """
        Time = time in seconds since epoch to set it off
        """
        while time.time() < time:
            pass
        self._alarm.play()
        pyglet.app.run()
        
if __name__ == "__main__":
    x       = Alarm()
    x.timer(time.time()+10)
        
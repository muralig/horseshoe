'''
Created on Jul 26, 2011

@author: sdamaraj
'''
import urllib
import json

import kivy
#kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button

url = "http://www.reddit.com/r/fffffffuuuuuuuuuuuu/top/.json"
    
def buttonPressed(params):
    print "Pressed Button", params

def buttonReleased(params):
    print "Relased Button", params
    theJsonUrl = urllib.urlopen(url)
    jsonString = theJsonUrl.read()
    theJsonUrl.close()
    print jsonString
    

class MyClass(App):
    '''
    classdocs
    '''

    def build(self):
        self.button = Button(text='Hello World')
        self.button.bind(on_press=buttonPressed)
        self.button.bind(on_release=buttonReleased)
        return self.button
    
if __name__ == '__main__':
    MyClass().run()
    
       



'''
Created on Jul 26, 2011

@author: sdamaraj
'''

import kivy
#kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button



class MyClass(App):
    '''
    classdocs
    '''
    def build(self):
        return Button(text='Hello World')
    
if __name__ == '__main__':
    MyClass().run()
    
       



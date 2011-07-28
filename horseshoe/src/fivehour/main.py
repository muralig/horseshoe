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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.stacklayout import StackLayout

urlBase = "http://www.reddit.com/r/" #fffffffuuuuuuuuuuuu/top/.json"

class MyClass(App):
    '''
    classdocs
    '''
    
    def getJSONIterator(self, subReddit):
        theJsonUrl = urllib.urlopen(urlBase + subReddit + '/top/.json')
        jsonString = theJsonUrl.read()
        theJsonUrl.close()
        print jsonString
        parsed = json.loads(jsonString)
        print "Done"
        items = parsed["data"]["children"]
        items = [item for item in items if item["data"]["domain"] == 'imgur.com']
        
        self.items = items
        print "Got JSON with " + str(len(items)) + " items "
        for item in self.items:
            print "Returning next item: " + item["data"]["title"]
            yield item
    
    def buttonPressed(self, params):
        print "Pressed Button", params
    
        
    def buttonReleased(self, params):
        
        print "Relased Button", params
        if not hasattr(self, 'items'):
            print "Getting JSON"
            self.iterator = self.getJSONIterator('fffffffuuuuuuuuuuuu')
            
        nextItem = self.iterator.next()
        itemUrl = nextItem["data"]["url"]
        
        if (itemUrl.find('.png') == -1) and (itemUrl.find('.jpg') == -1):
            itemUrl += ".jpg"
        
        print itemUrl
    
        self.image.source = itemUrl
        
    def build(self):       
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.image = AsyncImage(size_hint=(1.0, 0.9))
        self.layout.add_widget(self.image)

        button = Button(text='Horseshoe', size_hint=(1.0, 0.1))
        button.bind(on_press=self.buttonPressed)
        button.bind(on_release=self.buttonReleased)                
        
        self.layout.add_widget(button)

        return self.layout
    
if __name__ == '__main__':
    MyClass().run()
    
       



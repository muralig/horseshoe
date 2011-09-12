import urllib
import json
import sys

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.scatter import Scatter
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget


urlBase = "http://www.reddit.com/r/" #fffffffuuuuuuuuuuuu/top/.json"

class HorseShoe(App):
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
        next = parsed["data"]["after"]
        items = parsed["data"]["children"]
        items = [item for item in items if item["data"]["domain"] == 'imgur.com' or item["data"]["domain"] == 'i.imgur.com']
        
        self.items = items
        numItems = len(items)
        print "Got JSON with " + str(numItems) + " items "
        for item in self.items:
            if item is None:
                print "Item is NOne!"
            else:
                print "Returning next item: " + item["data"]["title"]
                yield item

    
    def buttonPressed(self, params):
        print "Pressed Button", params
    
        
    def buttonReleased(self, params):
        
        print "Relased Button", params
        if not hasattr(self, 'items'):
            print "Getting JSON"
            self.iterator = self.getJSONIterator('fffffffuuuuuuuuuuuu')
        
        try:    
            nextItem = self.iterator.next() 
        except StopIteration:
            print "Ran out of iterators!"
            sys.exit(0)    
        
        itemUrl = nextItem["data"]["url"]
        
        if (itemUrl.find('.png') == -1) and (itemUrl.find('.jpg') == -1):
            itemUrl += ".jpg"
        
        print itemUrl
    
        self.image.source = itemUrl
        
        
    def build(self):       
        '''
        s = KivyImageScatter()
        col = Widget()
        col.add_widget(s)
        return col
        '''
        '''
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.image = AsyncImage(allow_stretch=True, keep_ratio=False)
        
        scatter = Scatter(do_rotation=False, auto_bring_to_front=False, size_hint=(1.0, 0.9))
        #self.image.bind(texture_size=scatter.setter('size'))
        scatter.add_widget(self.image)
        
        self.layout.add_widget(scatter)
        
        button = Button(text='Horseshoe', size_hint=(1.0, 0.1))
        button.bind(on_press=self.buttonPressed)
        button.bind(on_release=self.buttonReleased)                
        
        self.layout.add_widget(button)
        
        return self.layout
        '''
        
        self.image = AsyncImage(allow_stretch=True, keep_ratio=False, size=(480,480))
        col = Widget()
        
        #button = Button(text='Horseshoe', size_hint=(1.0, 0.1))
        self.buttonReleased(self)     
        
        scatter = Scatter(do_rotation=False, auto_bring_to_front=False, size=self.image.get_norm_image_size())
        #self.image.bind(texture_size=scatter.setter('size'))
        scatter.add_widget(self.image)

        col.add_widget(scatter)

        button = Button(text='Next', size_hint=(1.0, 0.1))
        button.bind(on_press=self.buttonPressed)
        button.bind(on_release=self.buttonReleased)                
        col.add_widget(button)
        
        return col
        
    
if __name__ == '__main__':
    HorseShoe().run()
    
       



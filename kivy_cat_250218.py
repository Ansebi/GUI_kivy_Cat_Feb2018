from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

class MyApp(App):
    
    def build(self):
        layout_1 = FloatLayout()

        background=Image(
            source="cat_background.png",
            allow_stretch = True,
            keep_ratio = False
            )        
        
        complex_button_1_relative_center_x=0.5
        complex_button_1_relative_center_y=0.5

        sound=SoundLoader.load('meow.wav')

        image_1 = Image(
            source="cat.png",                    
            allow_stretch = True,
            keep_ratio = True,
            size_hint=(0.5,0.5),
            pos_hint={'center_x': complex_button_1_relative_center_x,
                      'center_y': complex_button_1_relative_center_y}
            )
       

        label_1 = Label(
            text = "Purrress Me",
            pos_hint={'center_x': 0.5, 'center_y': 0.9,},
            font_size='40sp'
            )
        

        def my_on_press(instance):
            print("You succeded at poking a cat. Sincere congratulations!")
            sound.play()  
            image_1.source = 'cat_meow.png'
            label_1.text="Meow"
            #button_1.background_color=[0,1,1,1]            
           

        def my_on_release(instance):
            #button_1.background_color=[1,1,0,1]
            image_1.source="cat.png"
            label_1.text="Purrress Me Once Again"
            sound.stop()
            #self.source = 'off.png'
            

        button_1 = Button(            
            size_hint=image_1.size_hint,
            pos_hint=image_1.pos_hint,
            background_color = [0,0,0,0],            
            )
        button_1.bind(on_press=my_on_press)
        button_1.bind(on_release=my_on_release)

        button_2 = Button(
            size_hint = (0.1,0.1),
            pos_hint = {'center_x': 0,
                        'center_y': 0,},            
            color = (0,0,0)           
            )
        button_2.bind(on_press=my_on_press)
        button_2.bind(on_release=my_on_release)
        
        layout_1.add_widget(background)
        layout_1.add_widget(image_1)
        layout_1.add_widget(label_1)
        layout_1.add_widget(button_1)
        #layout_1.add_widget(button_2)        

        return layout_1

if __name__ == "__main__":

    MyApp().run()

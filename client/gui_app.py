from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from kivy.uix.dialog import Dialog
from methods import send,recieve
class I_Xender(App):

    def build(self):

        vlayout = BoxLayout(orientation='vertical')
        # Create a button for taking photograph
        hlayout = BoxLayout(orientation='horizontal')
        self.sendButton = Button(text="Send",
                                 font_size=30,
                                 color=(0,0,50,50),
                                 background_normal = 'send.png', 
                                 background_down ='recv.png',
                                 size_hint=(.2,.2),
                                 border=(0,0,0,0),
                                 pos_hint={'x': .1, 'y':.2},
                                 )
        # bind the button's on_press to onCameraClick
        self.sendButton.bind(on_press=self.sendFiles)
        # add send button to the hlayout

        self.recieveButton = Button(text="Recieve",
                                    font_size=30,
                                    color=(0,0,50,50),
                                    background_normal = 'recv.png', 
                                    background_down ='send.png',
                                    size_hint=(.2,.2),
                                    border=(0,0,0,0),
                                    pos_hint={'x': .6, 'y':.2}, 
                                    )
        # bind the button's on_press to onCameraClick
        self.recieveButton.bind(on_press=self.recvFiles)

        # add send button to the hlayout        
        hlayout.add_widget(self.sendButton)
        hlayout.add_widget(self.recieveButton)

        #now add hlyout to layout
        vlayout.add_widget(hlayout)
        # return the root widget
        return vlayout

 

    # Take the current frame of the video as the photo graph       

    def sendFiles(self, *args):
        #self.ask = Dialog()
        send()
        print("Hi, file sent!")
    def recvFiles(self, *args):
        print("Hi, file recieved!")
        recieve()
            
        

       

       

# Start the Camera App

if __name__ == '__main__':
    I_Xender().run()

import pytube
'''try:
    link=''
    links=[]
    count = 0
    while 1:
        link=input(f"Nhap Link Thu {count}: ")
        if link=='end':break
        links.append(link)
    for link in links:
        yt = pytube.YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"Tai Thanh Cong Video {link}")
except:
    print(f"Khong the tai video {i}")'''
from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello World')

if __name__ == '__main__':
    HelloWorldApp().run()


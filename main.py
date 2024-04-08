import vlc
import time
from tkinter import *
from PIL import ImageTk, Image

url = 'https://streaming.live365.com/a18155'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
def Play():
    player.play()

def Stop():
    player.stop()

app = Tk()
app.title('Helix Rock Radio')
app.geometry('250x350')
app.iconbitmap("cropped-logo-keep.ico")

img = ImageTk.PhotoImage(Image.open("cropped-logo-keep.png"))

logo_label = Label(app, image=img)
logo_label.grid(row=0, column=0, sticky=W)

add_btn = Button(app, text='Play', width=12, command=Play)
add_btn.grid(row=2, column=0, padx=10, pady=10)
add_btn = Button(app, text='Stop', width=12, command=Stop)
add_btn.grid(row=3, column=0, padx=10, pady=10)

#start program
app.mainloop()
#Imports
import os
import sys
import pygame

#google text to speech
from gtts import gTTS

#requests and BeautifulSoup
import requests
import bs4

#pygame audio player
from pygame import mixer

#tkinter ui
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#mp3 -> wav
from os import path
from pydub import AudioSegment


#variable declarations
x = str()
vol = float(1.0)

#Play button
def Play():
    mixer.init()
    mixer.music.load("sound.ogg")
    mixer.music.play()


#play and resume
def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def quitpy():
    sys.exit()


def volup():
    global vol
    mixer.music.set_volume(vol + 0.1)

def voldown():
    global vol
    mixer.music.set_volume(vol - 0.1)



#UI build and declarations
root = Tk()
root.title("AP Text to Speech")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

#variable declarations 2
url = StringVar()
countryvar = StringVar()
m = countryvar.get()
m = str(m)
print(m)

def check():
    m = countryvar.get()
    m = str(m)
    print(m)
    return str(m)

#webscrape function
def webscrape():
    global x
    global b
    global thing
    global countryvar
    src = "sound.mp3"
    dst = "sound.ogg"
    murl = str(url.get())
    response = requests.get(murl)
    response.raise_for_status()
    m = countryvar.get()
    m = str(m)
    print(m)
    parse = bs4.BeautifulSoup(response.text, 'html.parser')
    x = str(parse.get_text())
    print(x)
    text = gTTS(x, lang=m)
    text.save("sound.mp3")
    AudioSegment.from_mp3(src).export(dst, format='ogg')
    b.state(['!disabled'])

url_entry = ttk.Entry(mainframe, width=7, textvariable=url)
url_entry.grid(column=3, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Enter URL:").grid(column=3, row=1, sticky=S)

ttk.Button(mainframe, text="Scrape", command=webscrape).grid(column=3, row=3, sticky=S)

ttk.Button(mainframe, text="Pause", command=pause).grid(column=2, row=5, sticky=S)
b = ttk.Button(mainframe, text="Play", command=Play)
b.grid(column=3, row=4, sticky=S)
b.state(['disabled'])
ttk.Button(mainframe, text="Resume", command=unpause).grid(column=4, row=5, sticky=S)
ttk.Button(mainframe, text="Quit", command=quitpy).grid(column=3, row=5, sticky=S)

ttk.Label(mainframe, text="Set Volume:").grid(column=3, row=6, sticky=S)
ttk.Button(mainframe, text="+", command=volup).grid(column=2, row=7, sticky=S)
ttk.Button(mainframe, text="-", command=voldown).grid(column=4, row=7, sticky=S)

thing = ttk.Combobox(mainframe, textvariable=countryvar, values=["en", "fr", "es", "pt"], state='readonly', width=5).grid(column=3, row=8)
thing.current(0)
ttk.Button(mainframe, text="check", command=check).grid(column=3, row=9)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.bind('<Return>', webscrape)

root.mainloop()

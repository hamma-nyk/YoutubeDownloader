from pathlib import Path
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
import requests
import time
import shutil

# Example Link Video : https://www.youtube.com/watch?v=jhFDyDgMVUI

def selectPath():
        path = filedialog.askdirectory()
        path_field.insert(0, path)
        
def selectPPath():
        path = filedialog.askdirectory()
        path_field2.insert(0, path)
        
def downloadVHi():
    if(link_field.get()!="" and path_field.get()!=""):
        status_label.configure(text="Status : Downloading...")
        video = YouTube(link_field.get()).streams.get_highest_resolution().download()
        shutil.move(video, path_field.get())
        status_label.configure(text="Status : Download completed!")

def downloadVLow():
    if(link_field.get()!="" and path_field.get()!=""):
        status_label.configure(text="Downloading...")
        video = YouTube(link_field.get()).streams.get_lowest_resolution().download()
        shutil.move(video, path_field.get())
        status_label.configure(text="Status : Download completed!")
        
def downloadPHi():
    if(link_field2.get()!="" and path_field2.get()!=""):
        status_label2.configure(text="Status : Downloading...")
        playlist = Playlist(link_field2.get())
        for video in playlist.videos:
            vid = video.streams.get_highest_resolution().download()
            shutil.move(vid, path_field2.get())
        status_label2.configure(text="Status : Playlist Download completed!")

def downloadPLow():
    if(link_field2.get()!="" and path_field2.get()!=""):
        status_label2.configure(text="Status : Downloading...")
        playlist = Playlist(link_field2.get())
        for video in playlist.videos:
            vid = video.streams.get_lowest_resolution().download()
            shutil.move(vid, path_field2.get())
        status_label2.configure(text="Status : Playlist Download completed!")

screen = Tk()
screen.title("Youtube Downloader")
# screen.geometry("485x255")
screen.configure(background="#272727")
screen.resizable(False,False)
p = Path(__file__).with_name('icon.ico')
screen.iconbitmap(p)

# Logo
p = Path(__file__).with_name('logo.png')
logo = Image.open(p)
logo = logo.resize((160,50))
my = ImageTk.PhotoImage(logo)

# Canvas
canvas = Canvas(screen,width=485,height=450,bg="#ffffff")
canvas.pack()
canvas.create_image(242.25, 60, image=my)

# YT Link
link_label = Label(screen, text="Youtube video link", font=('arial',10), background="#ffffff", foreground="#101010")
canvas.create_window(242.25,110,window=link_label)
link_field = Entry(screen, width=55, font=('arial',10), background="#dddddd", foreground="#101010")
canvas.create_window(242.25,140,window=link_field)

# Select Path
path_label = Label(screen, text="Select path ", font=('arial',10), background="#ffffff", foreground="#101010")
canvas.create_window(85.25,170,window=path_label)
path_field = Entry(screen, width=32, font=('arial',10), background="#dddddd", foreground="#101010")
canvas.create_window(350.25,170,window=path_field,anchor="e")
path_button  = Button(screen, text="Browse",width=10, command=selectPath, background="cyan", foreground="#101010")
canvas.create_window(438.25,170,window=path_button,anchor="e")


# Status
status_label = Label(screen, text="Status : Idle", font=('arial',10), background="#ffffff",foreground="#ffffff", justify=LEFT)
canvas.create_window(47.25,200,window=status_label,anchor="w")

# Button Download
hi_button  = Button(screen, text="Download Hi-Res",width=22, command=downloadVHi, font=("arial",10,"bold"), background="green",foreground="#ffffff")
canvas.create_window(234.25,230,window=hi_button,anchor="e")
low_button = Button(screen, text="Download Low-Res",width=23, command=downloadVLow, font=("arial",10,"bold"), background="red",foreground="#ffffff")
canvas.create_window(437.25,230,window=low_button,anchor="e")

# Playlist Link : layout above + 50
link_label = Label(screen, text="Playlist video link", font=('arial',10), background="#ffffff", foreground="#101010")
canvas.create_window(242.25,280,window=link_label)
link_field2 = Entry(screen, width=55, font=('arial',10), background="#dddddd", foreground="#101010")
canvas.create_window(242.25,310,window=link_field2)

# Select Path
path_label = Label(screen, text="Select path ", font=('arial',10), background="#ffffff", foreground="#101010")
canvas.create_window(85.25,340,window=path_label)
path_field2 = Entry(screen, width=32, font=('arial',10), background="#dddddd", foreground="#101010")
canvas.create_window(350.25,340,window=path_field2,anchor="e")
path_button2  = Button(screen, text="Browse",width=10, command=selectPPath, background="cyan", foreground="#101010")
canvas.create_window(438.25,340,window=path_button2,anchor="e")


# Status
status_label2 = Label(screen, text="Status : Idle", font=('arial',10), background="#ffffff", foreground="#101010", justify=LEFT)
canvas.create_window(47.25,370, window=status_label2,anchor="w")

# Button Download
hi_button2  = Button(screen, text="Download Hi-Res",width=22, command=downloadPHi, font=("arial",10,"bold"), background="green",foreground="#ffffff")
canvas.create_window(234.25,400,window=hi_button2,anchor="e")
low_button2 = Button(screen, text="Download Low-Res",width=23, command=downloadPLow, font=("arial",10,"bold"), background="red",foreground="#ffffff")
canvas.create_window(437.25,400,window=low_button2,anchor="e")

screen.mainloop()
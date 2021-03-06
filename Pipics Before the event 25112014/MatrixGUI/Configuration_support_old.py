#! /usr/bin/env python
#
# Support module generated by PAGE version 4.3.1
# In conjunction with Tcl version 8.6
#    Nov 05, 2014 10:40:43 PM


import sys
from socket import *
import tkMessageBox
import Updating

BCAST_GRP = '192.168.0.255'
BCAST_PORT = 5007

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind(('', BCAST_PORT))

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global check
    check = IntVar()

    global spinbox
    spinbox = StringVar()

    global ISO
    ISO = StringVar()

    global Aperature
    Aperature = StringVar()

    global Speed
    Speed = StringVar()

    global Focus
    Focus = StringVar()


def allCams():
    global check
    if check.get():
        w.Spinbox1.configure(state=DISABLED)
        w.Button1.configure(state=DISABLED)
    else:
        w.Spinbox1.configure(state=NORMAL)
        w.Button1.configure(state=NORMAL)


def update():
    global check, spinbox
    updateTime = 4000
    
    if ISO.get() and Aperature.get() and Speed.get() and Focus.get():
        w.Button2.configure(state=DISABLED)
        if check.get(): #if ALL is selected
            for i in range(1,61): #writing to all files
                if i < 10:
                    outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration0"+str(i)+".txt"
                else:
                    outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration"+str(i)+".txt"
                writing(outfile)
        else:
            if int(spinbox.get())< 10:
                outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration0"+spinbox.get()+".txt"
            else:
                outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration"+spinbox.get()+".txt"
            writing(outfile)

        Updating.create_Updating(root,updateTime)
        root.after(updateTime,enableUpdate)
        sock.sendto("configure", (BCAST_GRP, BCAST_PORT))

            
    else:
        tkMessageBox.showwarning('Warning', 'Missing data.',parent=root)


def enableUpdate():
    w.Button2.configure(state=NORMAL)
    
    
def writing(outFile):
    global ISO, Aperature, Speed, Focus
    print("Wriitng on: " + outFile)
    File = open(outFile,'w') # change this directory to the PiPics & file to configure
    File.write(('%s\n%s\n%s\n%s\n')%(ISO.get(),Aperature.get(),Speed.get(),Focus.get()))
    File.close()            
        
def read():
    global spinbox, ISO, Aperature, Speed, Focus
    if int(spinbox.get()) < 61 and int(spinbox.get()) > 0:
        value = ['','','','']
        if int(spinbox.get()) < 10:
            readfile="C:\Users\Public\PiPics\ConfigFiles\Configuration0"+spinbox.get()+".txt"
        else:
            readfile="C:\Users\Public\PiPics\ConfigFiles\Configuration"+spinbox.get()+".txt"
        File = open(readfile,'r')
        for i in range(4): #read lines
            line = File.readline()
            line = line.split('\n')
            value[i] = line[0] #store data in list
        ISO.set(value[0])
        Aperature.set(value[1])
        Speed.set(value[2])
        Focus.set(value[3])

def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window ():
    # Function which closes the window_w
    global top_level
    top_level.destroy()
    top_level = None



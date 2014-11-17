#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.3.1
# In conjunction with Tcl version 8.6
#    Oct 25, 2014 10:16:24 AM
import sys

from socket import *

#_-_-__-_-_-_-_-_-Network Configuration-_-_-_-_-_-_-_-_-_-_-_-_-_

BCAST_GRP = '192.168.0.255'
BCAST_PORT = 5007

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind(('', BCAST_PORT))
#_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_--_-_-_-_-_-_-_-_-_

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

import Calibrate_support

after_id = 0

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Calibration Mode')
    root.geometry('516x355+344+122')
    root.resizable(height=FALSE,width=FALSE)
    w = Calibration_Mode (root)
    Calibrate_support.init(root, w)
    root.mainloop()

w = None
roottop = None
stopIdle = 0

def create_Calibration_Mode (root, W, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, rootTop
    rt = root
    w = Toplevel (root)
    rootTop = W
    w.title('Calibration Mode')
    w.geometry('516x355+344+122')
    w.resizable(height=FALSE,width=FALSE)
    w_win = Calibration_Mode (w)
    Calibrate_support.init(w, w_win, param)
    w.after(500,idle)
    refresh()
    w.protocol("WM_DELETE_WINDOW", destroy_Calibration_Mode)
    return w_win

def destroy_Calibration_Mode ():
    global w, rootTop
    w.destroy()
    rootTop.Calibration.configure(state=NORMAL,cursor='arrow')
    w = None

def idle():
        global stopIdle
        #root.after(1000)
        sock.sendto("idle", (BCAST_GRP, BCAST_PORT))
        print 'idle sent'
        if not stopIdle:
            w.after(1000,idle) # --MA--> The delay must be bigger the network is flooded with idle commands
            
def idleon():
        global stopIdle
        stopIdle = 0
        w.after(1000,idle) # --MA--> The delay must be bigger the network is flooded with idle commands


def refresh():
        global stopIdle
        stopIdle = 1
        w.after(1000,idleon)
        sys.stdout.flush()
        sock.sendto("calibrate", (BCAST_GRP, BCAST_PORT))
        
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "TkDefaultFont " + \
            ""
        w.configure(background="#d9d9d9")
        w.configure(highlightbackground="#d9d9d9")
        w.configure(highlightcolor="black")
        f=open('calibration.txt')
        for i in range (60):
            line = f.readline().rstrip('\n')
            line = line.split(".")
            i+=1
            name = str(i+100)
            print line
            if (int(line[1]) + int(line[2])) > 0:
                name = Label (w)
                name.configure(background="red")
                name.configure(font=font11)
                name.configure(foreground="#ffffff")
                if i<10:
                    name.configure(text='0' + str(i))
                else:
                    name.configure(text=str(i))
                name.place(height=24,width=24)
                if (i<7):
                    name.place(relx=0.04,rely=0.06+((i-1)*0.14))
                if (i>6 and i<13):
                    name.place(relx=0.136,rely=0.06+((i-7)*0.14))
                if (i>12 and i<19):
                    name.place(relx=0.233,rely=0.06+((i-13)*0.14))
                if (i>18 and i<25):
                    name.place(relx=0.330,rely=0.06+((i-19)*0.14))
                if (i>24 and i<31):
                    name.place(relx=0.426,rely=0.06+((i-25)*0.14))
                if (i>30 and i<37):
                    name.place(relx=0.523,rely=0.06+((i-31)*0.14))
                if (i>36 and i<43):
                    name.place(relx=0.620,rely=0.06+((i-37)*0.14))
                if (i>42 and i<49):
                    name.place(relx=0.716,rely=0.06+((i-43)*0.14))
                if (i>48 and i<55):
                    name.place(relx=0.813,rely=0.06+((i-49)*0.14))
                if (i>54):
                    name.place(relx=0.910,rely=0.06+((i-55)*0.14))
            else:
                name = Label (w)
                name.configure(background="green")
                name.configure(font=font11)
                name.configure(foreground="#ffffff")
                if i<10:
                    name.configure(text='0' + str(i))
                else:
                    name.configure(text=str(i))
                name.place(height=24,width=24)
                if (i<7):
                    name.place(relx=0.04,rely=0.06+((i-1)*0.14))
                if (i>6 and i<13):
                    name.place(relx=0.136,rely=0.06+((i-7)*0.14))
                if (i>12 and i<19):
                    name.place(relx=0.233,rely=0.06+((i-13)*0.14))
                if (i>18 and i<25):
                    name.place(relx=0.330,rely=0.06+((i-19)*0.14))
                if (i>24 and i<31):
                    name.place(relx=0.426,rely=0.06+((i-25)*0.14))
                if (i>30 and i<37):
                    name.place(relx=0.523,rely=0.06+((i-31)*0.14))
                if (i>36 and i<43):
                    name.place(relx=0.620,rely=0.06+((i-37)*0.14))
                if (i>42 and i<49):
                    name.place(relx=0.716,rely=0.06+((i-43)*0.14))
                if (i>48 and i<55):
                    name.place(relx=0.813,rely=0.06+((i-49)*0.14))
                if (i>54):
                    name.place(relx=0.910,rely=0.06+((i-55)*0.14))
        f.close()
        
            


class Calibration_Mode:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "TkDefaultFont " + \
            ""
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.Button1 = Button (master)
        self.Button1.place(relx=0.04,rely=0.87,height=34,width=117)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background=_bgcolor)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Refresh''')
        self.Button1.configure(command=refresh)

        self.Button3 = Button (master)
        self.Button3.place(relx=0.3,rely=0.87,height=34,width=77)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background=_bgcolor)
        self.Button3.configure(command=destroy_Calibration_Mode)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Exit''')



if __name__ == '__main__':
    vp_start_gui()




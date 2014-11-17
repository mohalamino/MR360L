### Important Notes: [1] Change the directories tp fit the new pc [2] Test the Multicast commands make sure they are common between the GUI and Listener
### [3] 
from Tkinter import *

from socket import *
import sys
import time
#import PIL

#_-_-__-_-_-_-_-_-Network Configuration-_-_-_-_-_-_-_-_-_

BCAST_GRP = '192.168.0.255'
BCAST_PORT = 5007

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#_-_-_-_-_-_-_- FUNS -_-_-_-_-_-_

def Exit():
    mainWin.destroy()
    
def capture():
    print ('capturing')
    sock.sendto("shoot", (BCAST_GRP, BCAST_PORT)) #sending command shoot
    # should send shoot via muticasting to all the cams
    
def load():
    load = Toplevel()
    load.title("Please Wait")
    
    time.sleep(2)
    load.destroy()
    
def configure(): #opens the configure window when configure button pressed
    Win = Toplevel()
    Win.title("Matrix Ring Configuration")
    configBtn = Button(mainWin, compound=LEFT, image=configImg,text="Configure", width=200, state=DISABLED)
    configBtn.grid(row = 1, column = 0,columnspan=2, padx=10, pady=10)
    
    def onClose():
        Win.destroy()
        configBtn = Button(mainWin, compound=LEFT, image=configImg,text="Configure", width=200, command=configure)
        configBtn.grid(row = 1, column = 0,columnspan=2, padx=10, pady=10)

    Win.protocol("WM_DELETE_WINDOW",onClose)
    
    def ReadfromDSLR(): 
        
        CCvarNOW="ALL"

        #ApervarNOW=ApervarNOW[0:len(ApervarNOW)-1]

        CCtxt = Entry(Win)
        CCtxt.insert(0,"ALL")
        CCtxt.grid(row = 0, column = 1,columnspan=2, padx=10, pady=10)
        
        def ReadConfig():

            global ISOvar
            global Apervar
            global Shuttvar
            global Focusvar
            iFile = CCtxt.get()
            iFile = iFile.upper()
            
            RF=0
            
            if iFile.isalpha():
                if iFile =='ALL':
                    
                    iFile = "C:\Users\Public\PiPics\ConfigFiles\Configuration.txt"
                    RF=1
                else:
                    print("Not an option")
            elif int(iFile) in range(1,60):
                
                iFile = "C:\Users\Public\PiPics\ConfigFiles\Configuration"+iFile+".txt"
                RF=1
                
            if RF == 1:
                
                ConFile=open(iFile,'r') # change this directory to the PiPics & file to configure

                ISOvarNOW=ConFile.readline()
                #ISOvarNOW=ISOvarNOW.split('\\n')
                ISOvarNOW=ISOvarNOW[0:len(ISOvarNOW)-1]
                print(ISOvarNOW)

                ApervarNOW=ConFile.readline()
                ApervarNOW=ApervarNOW[0:len(ApervarNOW)-1]
                print(ApervarNOW)

                ShuttvarNOW=ConFile.readline()
                ShuttvarNOW=ShuttvarNOW[0:len(ShuttvarNOW)-1]
                print(ShuttvarNOW)
                
                FocusvarNOW=ConFile.readline()
                FocusvarNOW=FocusvarNOW[0:len(FocusvarNOW)-1]
                print(FocusvarNOW)

                ConFile.close()
                
                ISOvar = StringVar(Win)
                #ISOvar.set("Choose a value") # initial value
                ISOvar.set(str(ISOvarNOW)) # initial value
                
                Apervar = StringVar(Win)
                #Apervar.set("Choose a value") # initial value
                Apervar.set(str(ApervarNOW)) # initial value

                Shuttvar = StringVar(Win)
                #Shuttvar.set("Choose a value") # initial value
                Shuttvar.set(str(ShuttvarNOW)) # initial value
                
                Focusvar = StringVar(Win)
                #Focusvar.set("Choose a value") # initial value
                Focusvar.set(str(FocusvarNOW)) # initial value


                ISO = [6400, 3200,1600, 800, 400, 200]  #add more depending on the camera specifications
                Aperture = [6.4, 5, 4.5, 4, 3.2, 1.7]  #add more depending on the camera specifications
                ShutterSpeed = ['0.5', '1/40', '1/100', '1/200', '1/4000']  #add more depending on the camera specifications
                FocusMode = ['One Shot', 'AI Servo', 'AI Focus']  #add more depending on the camera specifications

                CCLabel = Label(Win, text="Choose a camera: ", anchor=W, justify=LEFT)
                CCLabel.grid(row = 0, column=0, sticky=W, pady=5)
                
                ISOLabel = Label(Win, text="ISO: ", anchor=W, justify=LEFT)
                ISOLabel.grid(row = 2, column=0, sticky=W, pady=5)
                ISO = OptionMenu(Win, ISOvar,*ISO)
                ISO.grid(row = 2, column = 1, pady=5)

                ApertureLabel = Label(Win, text="Aperture: ", justify=LEFT)
                ApertureLabel.grid(row=3, column=0, sticky=W, pady=5)
                Aperture = OptionMenu(Win, Apervar,*Aperture)
                Aperture.grid(row = 3, column = 1, pady=5)

                ShutterSpeedLabel = Label(Win, text="ShutterSpeed: ", justify=LEFT)
                ShutterSpeedLabel.grid(row=4 ,column=0, sticky=W, pady=5)
                ShutterSpeed = OptionMenu(Win, Shuttvar,*ShutterSpeed)
                ShutterSpeed.grid(row = 4, column = 1, pady=5)
                
                FocusModeLabel = Label(Win, text="FocusMode: ", justify=LEFT)
                FocusModeLabel.grid(row = 5, column = 0, sticky=W, pady=5)
                FocusMode = OptionMenu(Win, Focusvar,*FocusMode)
                FocusMode.grid(row = 5, column = 1, pady=5)
            

        ReadConfig()


        
        GetCurrBtn = Button(Win, compound=LEFT, text="Get current", width=10, command=ReadConfig)
        GetCurrBtn.grid(row = 0, column = 2,columnspan=2, padx=10, pady=10)

    
        Win.geometry('{}x{}'.format(340, 260))
    
        def update():  # this function is defind inside the configure() to ease the declaration of variables (global stuff )
            #print(CCtxt.get())
            
            def writing(ofile):
                print("Wriitng on: " + ofile)
                File = open(ofile,'w') # change this directory to the PiPics & file to configure
                File.write(('%s\n%s\n%s\n%s\n')%(ISOvar.get(),Apervar.get(),Shuttvar.get(),Focusvar.get()))
                File.close()

            camera = CCtxt.get()

            print(type(camera))
            camera=camera.upper()

            flag=0
            if camera.isalpha():
                if camera == 'ALL':
                    for i in range(1,60):
                        outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration"+str(i)+".txt"
                        writing(outfile)
                        flag=1
                else:
                    print("Not an option for writing")
                    
            elif int(camera) in range (1,60):
                outfile="C:\Users\Public\PiPics\ConfigFiles\Configuration"+camera+".txt"
                writing(outfile)
                flag=1
                
            else:
                print("NO")

            if flag == 1:
                Win.destroy()  # close the configure window
                sock.sendto("configure", (BCAST_GRP, BCAST_PORT)) #Sending commad configure, Each Rpi will open the configure.py to configure the Cams
                #show call the function that reads from the file to update the cameras
                print("New file generated and Configuration command sent")
                configBtn = Button(mainWin, compound=LEFT, image=configImg,text="Configure", width=200, command=configure)
                configBtn.grid(row = 1, column = 0,columnspan=2, padx=10, pady=10)
            #load() Useless
            
            
        button = Button(Win, text="Update Parameters", command=update)
        button.grid(row = 6, column = 0,columnspan=2, pady=10)
        
    ReadfromDSLR()

def Reboot():
    print "Reboot all"
    sock.sendto("reboot", (BCAST_GRP, BCAST_PORT)) #sending command Reboot    

def USBreset():
    print "USB reset to all"
    sock.sendto("resetusb", (BCAST_GRP, BCAST_PORT)) #sending command USBReset

mainWin = Tk()
mainWin.title("Matrix Ring")
menu = Menu(mainWin)
mainWin.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=Exit)

captImg = PhotoImage(file='icon1.gif')
configImg = PhotoImage(file='icon2.gif')                          
rebootImg = PhotoImage(file='restarts.gif')
usbrstImg = PhotoImage(file='usbtras.gif')

captBtn = Button(mainWin, compound=LEFT, image=captImg, text="Capture", width=200, height= 100, command=capture)
captBtn.grid(row = 0, column = 0,columnspan=2, padx=10, pady=10)

configBtn = Button(mainWin, compound=LEFT, image=configImg,text="Configure", width=200, command=configure)
configBtn.grid(row = 1, column = 0,columnspan=2, padx=10, pady=10)

rebootBtn = Button(mainWin, compound=LEFT, image=rebootImg ,text="Reboot", width=200, command=Reboot)
rebootBtn.grid(row = 2, column = 0,columnspan=2, padx=10, pady=10)

usbrstBtn = Button(mainWin, compound=LEFT, image=usbrstImg,text="USB reset", width=200, command=USBreset)
usbrstBtn.grid(row = 3, column = 0,columnspan=2, padx=10, pady=10)

mainWin.geometry('{}x{}'.format(250, 300))  #MainWin size 130 pixels X 200 pixels
mainloop()

from Tkinter import *
import sender

def Exit():
    mainWin.destroy()
    
def capture():
    sender.sender()
    print ('captured')
    
def configure():
    w,h = 250,220
    Win = Toplevel(mainWin)
    Win.minsize(w,h)
    Win.maxsize(w,h)
    Win.title("Matrix Ring Configuration")

    ISO = [6400, 3200,1600, 800, 400, 200]  #add more depending on the camera specifications
    Aperture = [6.4, 5, 4.5, 4, 3.2, 1.7]  #add more depending on the camera specifications
    ShutterSpeed = ['0.5', '1/40', '1/100', '1/200', '1/4000']  #add more depending on the camera specifications
    FocusMode = ['One Shot', 'AI Servo', 'AI Focus']  #add more depending on the camera specifications

    def update():
        File=open("Configuration.ini",'w')
        File.write(('%s\n%s\n%s\n%s')%(ISOvar.get(),Apervar.get(),Shuttvar.get(),Focusvar.get()))
        File.close()
        Win.destroy()

    ISOvar = StringVar(Win)
    ISOvar.set("    -    ") # initial value

    Apervar = StringVar(Win)
    Apervar.set("    -    ") # initial value

    Shuttvar = StringVar(Win)
    Shuttvar.set("    -    ") # initial value

    Focusvar = StringVar(Win)
    Focusvar.set("    -    ") # initial value

    
    ISOLabel = Label(Win, text="ISO: ", anchor=W, justify=LEFT)
    ISOLabel.grid(row = 0, column=0, sticky=W, padx=10, pady=5)

    ApertureLabel = Label(Win, text="Aperture: ", justify=LEFT)
    ApertureLabel.grid(row=1, column=0, sticky=W, padx=10, pady=5)

    ShutterSpeedLabel = Label(Win, text="ShutterSpeed: ", justify=LEFT)
    ShutterSpeedLabel.grid(row=2 ,column=0, sticky=W, padx=10, pady=5)

    FocusModeLabel = Label(Win, text="FocusMode: ", justify=LEFT)
    FocusModeLabel.grid(row = 3, column = 0, sticky=W, padx=10, pady=5)
    

    ISO = OptionMenu(Win, ISOvar,*ISO)
    ISO.grid(row = 0, column = 1, padx=10, pady=5,sticky=W)

    Aperture = OptionMenu(Win, Apervar,*Aperture)
    Aperture.grid(row = 1, column = 1, padx=10, pady=5,sticky=W)
    
    ShutterSpeed = OptionMenu(Win, Shuttvar,*ShutterSpeed)
    ShutterSpeed.grid(row = 2, column = 1,padx=10, pady=5,sticky=W)

    FocusMode = OptionMenu(Win, Focusvar,*FocusMode)
    FocusMode.grid(row = 3, column = 1, padx=10, pady=5,sticky=W)
    
    
    updateButton = Button(Win, text="Update Parameters", command=update)
    updateButton.grid(pady=10, columnspan=2)

        

mainWin = Tk()

w,h = 200,170
captImg = PhotoImage(file='icon1.gif')
configImg = PhotoImage(file='icon2.gif')      

mainWin.title("Matrix Ring")
mainWin.minsize(w,h)

menu = Menu(mainWin)
mainWin.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=Exit)
                    
tab1=Frame(mainWin, height=30)
tab1.grid(row=0)

captBtn = Button(mainWin, compound=LEFT, image=captImg, text="  Capture", font=('Helvetica', '12'), width=100, command=capture)
captBtn.grid(row = 1,ipadx=3, ipady=3, padx=30)

tab2=Frame(mainWin, height=30)
tab2.grid(row=2)

configBtn = Button(mainWin, compound=LEFT, image=configImg,text="Configure", font=('Helvetica', '12'), width=100, command=configure)
configBtn.grid(row = 3, ipadx=3, ipady=3,padx=30)

tab3=Frame(mainWin, height=30)
tab3.grid(row=4)

mainloop()

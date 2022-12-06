import serial
import time
import tkinter


#################################### Buttons Functions ######################################

def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
    #varLabel.set("LED ON ")
    ser.write(bytes('H', 'UTF-8'))

def set_button2_state():
    #varLabel.set("LED OFF")
    ser.write(bytes('L', 'UTF-8'))

def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


class RpmCheck:
    pass


def RpmGenFunc():
    #if RpmCheck == 1:
        #ser.write(bytes(str(current_value.get()), 'UTF-8'))
    #else:
        #print(int(current_value.get()))
        #ser.write(bytes(str(current_value.get()), 'UTF-8'))
        if current_value.get() != 0:
            RPMinHZ = 1000 / (((current_value.get() / 60) * 120) / 1000)
            ser.write(bytes(str(RPMinHZ), 'UTF-8'))
            #print(ser.read())

def ArduConnect():
    global ser
    ser = serial.Serial(ComNum.get(), 9600)
    print("Reset Arduino")
    time.sleep(3)
    ser.write(bytes('H', 'UTF-8'))

##################################### Design ################################################

tkTop = tkinter.Tk()
tkTop.geometry('700x600')
tkTop.title("Oz the hacker")
label3 = tkinter.Label(text = 'ECU RIG Control Panel''\n Aquarius Engines',font=("Courier", 12,'bold')).pack()


ComNum = tkinter.StringVar()
ComLabel = tkinter.Label(tkTop,
                         text='Enter COM number - for example "com5"',
                         )
ComLabel.place(x=470,y=40)
ComEntr = tkinter.Entry(tkTop,
                        textvariable = ComNum
                        )
ComEntr.place(x=520,y=60)

ConnectButton = tkinter.Button(tkTop,
                               text='Connect',
                               command=ArduConnect,
                               height='3',
                               width='10',
                               bg='green'
                               )
ConnectButton.place(x=540,y=85)

"""
RpmCheck = tkinter.IntVar()
RpmActive = tkinter.Checkbutton(tkTop,
                                text='Rpm Sim Active',
                                variable=RpmCheck,
                                )
RpmActive.place(x=20,y=270)
"""





"""
tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

"""

current_value = tkinter.DoubleVar()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="ON",
    command=set_button1_state,
    height = 2,
    fg = "black",
    width = 5,
    bd = 5,
    activebackground='green'
)
#button1state.pack(side='top', ipadx=10, padx=10, pady=15)
button1state.place(x=10,y=10)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="OFF",
    command=set_button2_state,
    height = 2,
    fg = "black",
    width = 5,
    bd = 5
)
#button2state.pack(side='top', ipadx=10, padx=10, pady=15)
button2state.place(x=10,y=60)

#SlideLabel = tkinter.Label(text='RPM Slider')
#SlideLabel.place(x=160, y=250)

slider = tkinter.Scale(tkTop, from_=1, to=2700, orient='horizontal', command=slider_changed, variable=current_value)
value_label = tkinter.Label(tkTop, text=get_current_value())
slider.pack(side='left', ipadx=80, padx=10, pady=15)

SliderButton = tkinter.Button(tkTop,
    text="Set RPM",
    command=RpmGenFunc,
    height = 2,
    fg = "black",
    width = 20,
    bd = 5
)
SliderButton.place(x=50,y=350)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'red',
    bd = 5
)
#tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)
tkButtonQuit.place(x=600,y=500)

tkinter.mainloop()
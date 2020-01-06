#piano_guitar.py

#Generate a piano keyboard GUI window
#Synthesize the sound of a piano 
#Synthesize the sound of a guitar 
#Plot the output signal in real time

#Xiaohcang Pei  and  Jianfei Zhao


# Import packages

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
from matplotlib import pyplot  

BLOCKLEN   = 512        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 4000      # Frames per second
MAXVALUE = 2**15-1      # Maximum allowed output signal value (because WIDTH = 2)

#################################################################
# Parameters for piano
Ta = 2      # Decay time (seconds)

C1 = 261.63    # Frequency (Hz)
D1 = 293.67
E1 = 329.63
F1 = 349.23
G1 = 392.00
A1 = 440.00
B1 = 493.88
C2 = 523.25
D2 = 587.33
E2 = 659.26
F2 = 698.46
G2 = 783.99
A2 = 880.00
B2 = 987.77
CP1 = 277.18
DP1 = 311.13
FP1 = 369.99
GP1 = 415.30
AP1 = 466.16
CP2 = 554.37
DP2 = 622.25
FP2 = 739.99
GP2 = 830.61
AP2 = 932.33

# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1 = 2.0 * pi * float(C1)/RATE
om2 = 2.0 * pi * float(D1)/RATE
om3 = 2.0 * pi * float(E1)/RATE
om4 = 2.0 * pi * float(F1)/RATE
om5 = 2.0 * pi * float(G1)/RATE
om6 = 2.0 * pi * float(A1)/RATE
om7 = 2.0 * pi * float(B1)/RATE
om8 = 2.0 * pi * float(C2)/RATE
om9 = 2.0 * pi * float(D2)/RATE
om10 = 2.0 * pi * float(E2)/RATE
om11 = 2.0 * pi * float(F2)/RATE
om12 = 2.0 * pi * float(G2)/RATE
om13 = 2.0 * pi * float(A2)/RATE
om14 = 2.0 * pi * float(B2)/RATE
om15 = 2.0 * pi * float(CP1)/RATE
om16 = 2.0 * pi * float(DP1)/RATE
om17 = 2.0 * pi * float(FP1)/RATE
om18 = 2.0 * pi * float(GP1)/RATE
om19 = 2.0 * pi * float(AP1)/RATE
om20 = 2.0 * pi * float(CP2)/RATE
om21 = 2.0 * pi * float(DP2)/RATE
om22 = 2.0 * pi * float(FP2)/RATE
om23 = 2.0 * pi * float(GP2)/RATE
om24 = 2.0 * pi * float(AP2)/RATE


# Filter coefficients (second-order IIR)
a1 = [1, -2*r*cos(om1), r**2]
b1 = [r*sin(om1)]

a2 = [1, -2*r*cos(om2), r**2]
b2 = [r*sin(om2)]

a3 = [1, -2*r*cos(om3), r**2]
b3 = [r*sin(om3)]

a4 = [1, -2*r*cos(om4), r**2]
b4 = [r*sin(om4)]

a5 = [1, -2*r*cos(om5), r**2]
b5 = [r*sin(om5)]

a6 = [1, -2*r*cos(om6), r**2]
b6 = [r*sin(om6)]

a7 = [1, -2*r*cos(om7), r**2]
b7 = [r*sin(om7)]

a8 = [1, -2*r*cos(om8), r**2]
b8 = [r*sin(om8)]

a9 = [1, -2*r*cos(om9), r**2]
b9 = [r*sin(om9)]

a10 = [1, -2*r*cos(om10), r**2]
b10 = [r*sin(om10)]

a11 = [1, -2*r*cos(om11), r**2]
b11 = [r*sin(om11)]

a12 = [1, -2*r*cos(om12), r**2]
b12 = [r*sin(om12)]

a13 = [1, -2*r*cos(om13), r**2]
b13 = [r*sin(om13)]

a14 = [1, -2*r*cos(om14), r**2]
b14 = [r*sin(om14)]

a15 = [1, -2*r*cos(om15), r**2]
b15 = [r*sin(om15)]

a16 = [1, -2*r*cos(om16), r**2]
b16 = [r*sin(om16)]

a17 = [1, -2*r*cos(om17), r**2]
b17 = [r*sin(om17)]

a18 = [1, -2*r*cos(om18), r**2]
b18 = [r*sin(om18)]

a19 = [1, -2*r*cos(om19), r**2]
b19 = [r*sin(om19)]

a20 = [1, -2*r*cos(om20), r**2]
b20 = [r*sin(om20)]

a21 = [1, -2*r*cos(om21), r**2]
b21 = [r*sin(om21)]

a22 = [1, -2*r*cos(om22), r**2]
b22 = [r*sin(om22)]

a23 = [1, -2*r*cos(om23), r**2]
b23 = [r*sin(om23)]

a24 = [1, -2*r*cos(om24), r**2]
b24 = [r*sin(om24)]


ORDER = 2   # filter order

states1 = np.zeros(ORDER)
states2 = np.zeros(ORDER)
states3 = np.zeros(ORDER)
states4 = np.zeros(ORDER)
states5 = np.zeros(ORDER)
states6 = np.zeros(ORDER)
states7 = np.zeros(ORDER)
states8 = np.zeros(ORDER)
states9 = np.zeros(ORDER)
states10 = np.zeros(ORDER)
states11 = np.zeros(ORDER)
states12 = np.zeros(ORDER)
states13 = np.zeros(ORDER)
states14 = np.zeros(ORDER)
states15 = np.zeros(ORDER)
states16 = np.zeros(ORDER)
states17 = np.zeros(ORDER)
states18 = np.zeros(ORDER)
states19 = np.zeros(ORDER)
states20 = np.zeros(ORDER)
states21 = np.zeros(ORDER)
states22 = np.zeros(ORDER)
states23 = np.zeros(ORDER)
states24 = np.zeros(ORDER)


x1 = np.zeros(BLOCKLEN)
x2 = np.zeros(BLOCKLEN)
x3 = np.zeros(BLOCKLEN)
x4 = np.zeros(BLOCKLEN)
x5 = np.zeros(BLOCKLEN)
x6 = np.zeros(BLOCKLEN)
x7 = np.zeros(BLOCKLEN)
x8 = np.zeros(BLOCKLEN)
x9 = np.zeros(BLOCKLEN)
x10 = np.zeros(BLOCKLEN)
x11 = np.zeros(BLOCKLEN)
x12 = np.zeros(BLOCKLEN)
x13 = np.zeros(BLOCKLEN)
x14 = np.zeros(BLOCKLEN)
x15 = np.zeros(BLOCKLEN)
x16 = np.zeros(BLOCKLEN)
x17 = np.zeros(BLOCKLEN)
x18 = np.zeros(BLOCKLEN)
x19 = np.zeros(BLOCKLEN)
x20 = np.zeros(BLOCKLEN)
x21 = np.zeros(BLOCKLEN)
x22 = np.zeros(BLOCKLEN)
x23 = np.zeros(BLOCKLEN)
x24 = np.zeros(BLOCKLEN)


#################################################################
# Parameters for guitar
Xg = 32000
G = 0.996/2             # feed-forward gain

# delay in seconds
ds0 = 0.008 *2     
ds1 = 0.007 *2
ds2 = 0.0063 *2
ds3 = 0.0057 *2
ds4 = 0.005 *2
ds5 = 0.0044 *2
ds6 = 0.0038 *2      
ds7 = 0.0035 *2
ds8 = 0.0032 *2
ds9 = 0.0030 *2
ds10 = 0.0028 *2
ds11 = 0.0027 *2
ds12 = 0.0026 *2     
ds13 = 0.0024 *2
ds14 = 0.0075 *2
ds15 = 0.0066 *2
ds16 = 0.0053 *2
ds17 = 0.0046 *2
ds18 = 0.0041 *2     
ds19 = 0.0033 *2
ds20 = 0.0031 *2
ds21 = 0.00275 *2
ds22 = 0.00265 *2
ds23 = 0.0025 *2


# delay in samples
N0 = int(RATE * ds0)   
N1 = int(RATE * ds1)
N2 = int(RATE * ds2)
N3 = int(RATE * ds3)
N4 = int(RATE * ds4)
N5 = int(RATE * ds5)
N6 = int(RATE * ds6)
N7 = int(RATE * ds7)   
N8 = int(RATE * ds8)
N9 = int(RATE * ds9)
N10 = int(RATE * ds10)
N11 = int(RATE * ds11)
N12 = int(RATE * ds12)
N13 = int(RATE * ds13)   
N14 = int(RATE * ds14)
N15 = int(RATE * ds15)
N16 = int(RATE * ds16)
N17 = int(RATE * ds17)
N18 = int(RATE * ds18)
N19 = int(RATE * ds19)   
N20 = int(RATE * ds20)
N21 = int(RATE * ds21)
N22 = int(RATE * ds22)
N23 = int(RATE * ds23)


# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN0 = 2*N0              
buffer0 = BUFFER_LEN0 * [0]   
BUFFER_LEN1 = 2*N1
buffer1 = BUFFER_LEN1 * [0]
BUFFER_LEN2 = 2*N2
buffer2 = BUFFER_LEN2 * [0]
BUFFER_LEN3 = 2*N3
buffer3 = BUFFER_LEN3 * [0]
BUFFER_LEN4 = 2*N4
buffer4 = BUFFER_LEN4 * [0]
BUFFER_LEN5 = 2*N5
buffer5 = BUFFER_LEN5 * [0]
BUFFER_LEN6 = 2*N6              
buffer6 = BUFFER_LEN6 * [0]   
BUFFER_LEN7 = 2*N7
buffer7 = BUFFER_LEN7 * [0]
BUFFER_LEN8 = 2*N8
buffer8 = BUFFER_LEN8 * [0]
BUFFER_LEN9 = 2*N9
buffer9 = BUFFER_LEN9 * [0]
BUFFER_LEN10 = 2*N10
buffer10 = BUFFER_LEN10 * [0]
BUFFER_LEN11 = 2*N11
buffer11 = BUFFER_LEN11 * [0]
BUFFER_LEN12 = 2*N12              
buffer12 = BUFFER_LEN12 * [0]   
BUFFER_LEN13 = 2*N13
buffer13 = BUFFER_LEN13 * [0]
BUFFER_LEN14 = 2*N14
buffer14 = BUFFER_LEN14 * [0]
BUFFER_LEN15 = 2*N15
buffer15 = BUFFER_LEN15 * [0]
BUFFER_LEN16 = 2*N16
buffer16 = BUFFER_LEN16 * [0]
BUFFER_LEN17 = 2*N17
buffer17 = BUFFER_LEN17 * [0]
BUFFER_LEN18 = 2*N18              
buffer18 = BUFFER_LEN18 * [0]   
BUFFER_LEN19 = 2*N19
buffer19 = BUFFER_LEN19 * [0]
BUFFER_LEN20 = 2*N20
buffer20 = BUFFER_LEN20 * [0]
BUFFER_LEN21 = 2*N21
buffer21 = BUFFER_LEN21 * [0]
BUFFER_LEN22 = 2*N22
buffer22 = BUFFER_LEN22 * [0]
BUFFER_LEN23 = 2*N23
buffer23 = BUFFER_LEN23 * [0]

# Initialize buffer indices
kr0 = BUFFER_LEN0 - N0     # read index
kw0 = 0                    # write index
kr1 = BUFFER_LEN1 - N1   
kw1 = 0 
kr2 = BUFFER_LEN2 - N2   
kw2 = 0 
kr3 = BUFFER_LEN3 - N3   
kw3 = 0
kr4 = BUFFER_LEN4 - N4   
kw4 = 0
kr5 = BUFFER_LEN5 - N5   
kw5 = 0
kr6 = BUFFER_LEN6 - N6     
kw6 = 0                  
kr7 = BUFFER_LEN7 - N7   
kw7 = 0 
kr8 = BUFFER_LEN8 - N8   
kw8 = 0 
kr9 = BUFFER_LEN9 - N9   
kw9 = 0
kr10 = BUFFER_LEN10 - N10   
kw10 = 0
kr11 = BUFFER_LEN11 - N11   
kw11 = 0
kr12 = BUFFER_LEN12 - N12     
kw12 = 0                 
kr13 = BUFFER_LEN13 - N13   
kw13 = 0 
kr14 = BUFFER_LEN14 - N14   
kw14 = 0 
kr15 = BUFFER_LEN15 - N15   
kw15 = 0
kr16 = BUFFER_LEN16 - N16   
kw16 = 0
kr17 = BUFFER_LEN17 - N17   
kw17 = 0
kr18 = BUFFER_LEN18 - N18     
kw18 = 0                  
kr19 = BUFFER_LEN19 - N19   
kw19 = 0 
kr20 = BUFFER_LEN20 - N20   
kw20 = 0 
kr21 = BUFFER_LEN21 - N21   
kw21 = 0
kr22 = BUFFER_LEN22 - N22   
kw22 = 0
kr23 = BUFFER_LEN23 - N23   
kw23 = 0

xg0 = 0
xg1 = 0
xg2 = 0
xg3 = 0
xg4 = 0
xg5 = 0
xg6 = 0
xg7 = 0
xg8 = 0
xg9 = 0
xg10 = 0
xg11 = 0
xg12 = 0
xg13 = 0
xg14 = 0
xg15 = 0
xg16 = 0
xg17 = 0
xg18 = 0
xg19 = 0
xg20 = 0
xg21 = 0
xg22 = 0
xg23 = 0
xg24 = 0

outputg = [0] * BLOCKLEN

#################################################################
# Open the audio output stream for piano

p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)

# Open the audio output stream for guitar
stream2 = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)

  
# specify low frames_per_buffer to reduce latency

CONTINUE = True
KEYPRESS1 = False
KEYPRESS2 = False
KEYPRESS3 = False
KEYPRESS4 = False
KEYPRESS5 = False
KEYPRESS6 = False
KEYPRESS7 = False
KEYPRESS8 = False
KEYPRESS9 = False
KEYPRESS10 = False
KEYPRESS11 = False
KEYPRESS12 = False
KEYPRESS13 = False
KEYPRESS14 = False
KEYPRESS15 = False
KEYPRESS16 = False
KEYPRESS17 = False
KEYPRESS18 = False
KEYPRESS19 = False
KEYPRESS20 = False
KEYPRESS21 = False
KEYPRESS22 = False
KEYPRESS23 = False
KEYPRESS24 = False
Guitar = False

#################################################################

#change between guitar and piano

def guitar_on_off(event):
    global Guitar

    if v.get() == 0:
        Guitar = False
    else:
        Guitar = True



# change the image of key when it was pressed on screen
                                                                   
def label_pressed(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key_pressed.png'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key_pressed.gif'
    
    key_img = PhotoImage(file=img, master=root)
    event.widget.configure(image=key_img)
    event.widget.image = key_img


# change the image of key back  when it was released on screen

def label_released(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key.png'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key.gif'

    key_img = PhotoImage(file=img, master=root)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

#match keys and notes
    
def find_label(name, array):
    for x in range(len(array)):
        # checks against the name component in keys
        if name == array[x][1]:
            # returns the Label component in keys
            return array[x][2]


# change KEYPRESS and the image of key and  when it was pressed on keyboard

def key_pressed(event):

    global CONTINUE
    global KEYPRESS1
    global KEYPRESS2
    global KEYPRESS3
    global KEYPRESS4
    global KEYPRESS5
    global KEYPRESS6
    global KEYPRESS7
    global KEYPRESS8
    global KEYPRESS9
    global KEYPRESS10
    global KEYPRESS11
    global KEYPRESS12
    global KEYPRESS13
    global KEYPRESS14
    global KEYPRESS15
    global KEYPRESS16
    global KEYPRESS17
    global KEYPRESS18
    global KEYPRESS19
    global KEYPRESS20
    global KEYPRESS21
    global KEYPRESS22
    global KEYPRESS23
    global KEYPRESS24
    
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        if note == 'C1':
            KEYPRESS1 = True
        if note == 'D1':
            KEYPRESS2 = True
        if note == 'E1':
            KEYPRESS3 = True
        if note == 'F1':
            KEYPRESS4 = True
        if note == 'G1':
            KEYPRESS5 = True
        if note == 'A1':
            KEYPRESS6 = True
        if note == 'B1':
            KEYPRESS7 = True
        if note == 'C2':
            KEYPRESS8 = True
        if note == 'D2':
            KEYPRESS9 = True
        if note == 'E2':
            KEYPRESS10 = True
        if note == 'F2':
            KEYPRESS11 = True
        if note == 'G2':
            KEYPRESS12 = True
        if note == 'A2':
            KEYPRESS13 = True
        if note == 'B2':
            KEYPRESS14 = True
        if note == 'CP1':
            KEYPRESS15 = True
        if note == 'DP1':
            KEYPRESS16 = True
        if note == 'FP1':
            KEYPRESS17 = True
        if note == 'GP1':
            KEYPRESS18 = True
        if note == 'AP1':
            KEYPRESS19 = True
        if note == 'CP2':
            KEYPRESS20 = True
        if note == 'DP2':
            KEYPRESS21 = True
        if note == 'FP2':
            KEYPRESS22 = True
        if note == 'GP2':
            KEYPRESS23 = True
        if note == 'AP2':
            KEYPRESS24 = True
       
        print(note)   # Show the note

        if len(note) == 2:
            img = 'pictures/white_key_pressed.png'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img, master=root)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img
        guitar_on_off(event)  # Determine which sound to output

# change the image of key back  when it was released on keyboard.

def key_released(event):
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        if len(note) == 2:
            img = 'pictures/white_key.png'
        else:
            img = 'pictures/black_key.gif'
        key_img = PhotoImage(file=img, master=root)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img


# change KEYPRESS when the key was presssed on screeen
def button_pressed(event):

    global CONTINUE
    global KEYPRESS1
    global KEYPRESS2
    global KEYPRESS3
    global KEYPRESS4
    global KEYPRESS5
    global KEYPRESS6
    global KEYPRESS7
    global KEYPRESS8
    global KEYPRESS9
    global KEYPRESS10
    global KEYPRESS11
    global KEYPRESS12
    global KEYPRESS13
    global KEYPRESS14
    global KEYPRESS15
    global KEYPRESS16
    global KEYPRESS17
    global KEYPRESS18
    global KEYPRESS19
    global KEYPRESS20
    global KEYPRESS21
    global KEYPRESS22
    global KEYPRESS23
    global KEYPRESS24
    
    if event.widget.name == 'C1':
        KEYPRESS1 = True
    if event.widget.name == 'D1':
        KEYPRESS2 = True
    if event.widget.name == 'E1':
        KEYPRESS3 = True
    if event.widget.name == 'F1':
        KEYPRESS4 = True
    if event.widget.name == 'G1':
        KEYPRESS5 = True
    if event.widget.name == 'A1':
        KEYPRESS6 = True
    if event.widget.name == 'B1':
        KEYPRESS7 = True
    if event.widget.name == 'C2':
        KEYPRESS8 = True
    if event.widget.name == 'D2':
        KEYPRESS9 = True
    if event.widget.name == 'E2':
        KEYPRESS10 = True
    if event.widget.name == 'F2':
        KEYPRESS11 = True
    if event.widget.name == 'G2':
        KEYPRESS12 = True
    if event.widget.name == 'A2':
        KEYPRESS13 = True
    if event.widget.name == 'B2':
        KEYPRESS14 = True
    if event.widget.name == 'CP1':
        KEYPRESS15 = True
    if event.widget.name == 'DP1':
        KEYPRESS16 = True
    if event.widget.name == 'FP1':
        KEYPRESS17 = True
    if event.widget.name == 'GP1':
        KEYPRESS18 = True
    if event.widget.name == 'AP1':
        KEYPRESS19 = True
    if event.widget.name == 'CP2':
        KEYPRESS20 = True
    if event.widget.name == 'DP2':
        KEYPRESS21 = True
    if event.widget.name == 'FP2':
        KEYPRESS22 = True
    if event.widget.name == 'GP2':
        KEYPRESS23 = True
    if event.widget.name == 'AP2':
        KEYPRESS24 = True    

    print(event.widget.name) # Show the note
    label_pressed(event)
    guitar_on_off(event) # Determine which sound to output

# KEYS_TO_NOTES is a dictionary that ties note
# names to certain keys on the keyboard.
KEYS_TO_NOTES = {
    'z': 'C1',
    'x': 'D1',
    'c': 'E1',
    'v': 'F1',
    'b': 'G1',
    'n': 'A1',
    'm': 'B1',
    's': 'CP1',
    'd': 'DP1',
    'g': 'FP1',
    'h': 'GP1',
    'j': 'AP1',
    'Z': 'C2',
    'X': 'D2',
    'C': 'E2',
    'V': 'F2',
    'B': 'G2',
    'N': 'A2',
    'M': 'B2',
    'S': 'CP2',
    'D': 'DP2',
    'G': 'FP2',
    'H': 'GP2',
    'J': 'AP2',
}


# Description: Piano is a class that initializes the Tkinter window 

class Piano(Frame):


# Description: __init__ is a method that creates the window, colors it and calls init_user_interface.        
   
 
    def __init__(self, parent):

        # This is the initialization of the window along with the
        # coloring of the background.
        Frame.__init__(self, parent, background='white')

        # So that the parent reference does not go out of scope.
        self.parent = parent

        # A call to the init_user_interface method.
        self.init_user_interface()

    # deaign the GUI     
                       

    def init_user_interface(self):

        # The 2-dimensional array keys holds the locations, names and after the
        # for loops are executed below, the Labels that are needed
        # to create each key, both white and black.
        keys = [
            [0, 'C1'],
            [35, 'CP1'],
            [50, 'D1'],
            [85, 'DP1'],
            [100, 'E1'],
            [150, 'F1'],
            [185, 'FP1'],
            [200, 'G1'],
            [235, 'GP1'],
            [250, 'A1'],
            [285, 'AP1'],
            [300, 'B1'],
            [350, 'C2'],
            [385, 'CP2'],
            [400, 'D2'],
            [435, 'DP2'],
            [450, 'E2'],
            [500, 'F2'],
            [535, 'FP2'],
            [550, 'G2'],
            [585, 'GP2'],
            [600, 'A2'],
            [635, 'AP2'],
            [650, 'B2']
        ]

        # This for loop populates the window with the white key Labels
        # and appends a Label to each slot in keys.
        for key in keys:
            if len(key[1]) == 2:
                img = 'pictures/white_key.png'
                key.append(self.create_key(img, key))

        # This for loop populates the window with the black key Labels
        # and appends a Label to each slot in keys.
        for key in keys:
            if len(key[1]) > 2:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))

        #Radiobuttons: to change the sound between piano and guitar.
        values = [
            ("Piano",1),
            ("Guitar",2)
        ] 
        
        for val, language in enumerate(values):
            R1 = Radiobutton(root, 
                        text=language[0],
                        variable=v,
                        indicator = 0,
                        value=val).place(x=700, y=70+val*25,width=50)
        


        # This titles the window.
        self.parent.title('Piano&Guitar')

        # This group of lines centers the window on the screen
        # and specifies the size of the window.
        w = 750
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # This group of lines saves a reference to keys so that
        # it does not go out of scope and binds the presses and
        # releases of keys to their respective methods
        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)
        self.parent.bind('<KeyRelease>', key_released)


        # This line packs all elements bound to the window.
        self.pack(fill=BOTH, expand=1)

  
    # Bind images and keys

    def create_key(self, img, key):
        key_image = PhotoImage(file=img, master=root)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        label.bind('<Button-1>', button_pressed)
        label.bind('<ButtonRelease-1>', label_released)
        return label


#################################################################

root = Tk()

v = IntVar()
v.set(0)


piano = Piano(root)


pyplot.ion()           # Turn on interactive mode so plot gets updated

t = [1000.*i/RATE for i in range(BLOCKLEN)]
output = [0] * BLOCKLEN
my_fig = pyplot.figure(1)
my_plot = my_fig.add_subplot(1, 1, 1)
[my_line] = pyplot.plot(t, output)
pyplot.ylim(-30000, 30000)
pyplot.xlim(0, BLOCKLEN*1000.0/RATE)   # Time axis in milliseconds 
pyplot.xlabel('Time (milliseconds)')




while CONTINUE:
    root.update()

# Play a note using a second-order difference equation
    
    if Guitar == False:
        
        
        if KEYPRESS1:
            # key was pressed
            x1[0] = 10000.0

            
        if KEYPRESS2:

            x2[0] = 10000.0
            
        if KEYPRESS3:

            x3[0] = 10000.0
            
        if KEYPRESS4:

            x4[0] = 10000.0

        if KEYPRESS5:

            x5[0] = 10000.0

        if KEYPRESS6:

            x6[0] = 10000.0

        if KEYPRESS7:

            x7[0] = 10000.0

        if KEYPRESS8:

            x8[0] = 10000.0

        if KEYPRESS9:

            x9[0] = 10000.0
            
        if KEYPRESS10:

            x10[0] = 10000.0

        if KEYPRESS11:

            x11[0] = 10000.0

        if KEYPRESS12:

            x12[0] = 10000.0

        if KEYPRESS13:

            x13[0] = 10000.0

        if KEYPRESS14:

            x14[0] = 10000.0

        if KEYPRESS15:

            x15[0] = 10000.0

        if KEYPRESS16:

            x16[0] = 10000.0

        if KEYPRESS17:

            x17[0] = 10000.0

        if KEYPRESS18:

            x18[0] = 10000.0

        if KEYPRESS19:

            x19[0] = 10000.0

        if KEYPRESS20:

            x20[0] = 10000.0

        if KEYPRESS21:

            x21[0] = 10000.0

        if KEYPRESS22:

            x22[0] = 10000.0

        if KEYPRESS23:

            x23[0] = 10000.0

        if KEYPRESS24:

            x24[0] = 10000.0


        [y1, states1] = signal.lfilter(b1, a1, x1, zi = states1)
        [y2, states2] = signal.lfilter(b2, a2, x2, zi = states2)
        [y3, states3] = signal.lfilter(b3, a3, x3, zi = states3)
        [y4, states4] = signal.lfilter(b4, a4, x4, zi = states4)
        [y5, states5] = signal.lfilter(b5, a5, x5, zi = states5)
        [y6, states6] = signal.lfilter(b6, a6, x6, zi = states6)
        [y7, states7] = signal.lfilter(b7, a7, x7, zi = states7)
        [y8, states8] = signal.lfilter(b8, a8, x8, zi = states8)
        [y9, states9] = signal.lfilter(b9, a9, x9, zi = states9)
        [y10, states10] = signal.lfilter(b10, a10, x10, zi = states10)
        [y11, states11] = signal.lfilter(b11, a11, x11, zi = states11)
        [y12, states12] = signal.lfilter(b12, a12, x12, zi = states12)
        [y13, states13] = signal.lfilter(b13, a13, x13, zi = states13)
        [y14, states14] = signal.lfilter(b14, a14, x14, zi = states14)
        [y15, states15] = signal.lfilter(b15, a15, x15, zi = states15)
        [y16, states16] = signal.lfilter(b16, a16, x16, zi = states16)
        [y17, states17] = signal.lfilter(b17, a17, x17, zi = states17)
        [y18, states18] = signal.lfilter(b18, a18, x18, zi = states18)
        [y19, states19] = signal.lfilter(b19, a19, x19, zi = states19)
        [y20, states20] = signal.lfilter(b20, a20, x20, zi = states20)
        [y21, states21] = signal.lfilter(b21, a21, x21, zi = states21)
        [y22, states22] = signal.lfilter(b22, a22, x22, zi = states22)
        [y23, states23] = signal.lfilter(b23, a23, x23, zi = states23)
        [y24, states24] = signal.lfilter(b24, a24, x24, zi = states24)
        
        
        x1[0] = 0.0
        x2[0] = 0.0
        x3[0] = 0.0
        x4[0] = 0.0
        x5[0] = 0.0
        x6[0] = 0.0
        x7[0] = 0.0
        x8[0] = 0.0
        x9[0] = 0.0
        x10[0] = 0.0
        x11[0] = 0.0
        x12[0] = 0.0
        x13[0] = 0.0
        x14[0] = 0.0
        x15[0] = 0.0
        x16[0] = 0.0
        x17[0] = 0.0
        x18[0] = 0.0
        x19[0] = 0.0
        x20[0] = 0.0
        x21[0] = 0.0
        x22[0] = 0.0
        x23[0] = 0.0
        x24[0] = 0.0


        KEYPRESS1 = False
        KEYPRESS2 = False
        KEYPRESS3 = False
        KEYPRESS4 = False
        KEYPRESS5 = False
        KEYPRESS6 = False
        KEYPRESS7 = False
        KEYPRESS8 = False
        KEYPRESS9 = False
        KEYPRESS10 = False
        KEYPRESS11 = False
        KEYPRESS12 = False
        KEYPRESS13 = False
        KEYPRESS14 = False 
        KEYPRESS15 = False
        KEYPRESS16 = False
        KEYPRESS17 = False
        KEYPRESS18 = False
        KEYPRESS19 = False
        KEYPRESS20 = False
        KEYPRESS21 = False
        KEYPRESS22 = False
        KEYPRESS23 = False
        KEYPRESS24 = False


        y = y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24
        y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping
        
        
        binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary data
        stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

        my_line.set_ydata(y)                              #update the plot

# Real-time implementation of the Karplus-Strong (KS) algorithm 

    if Guitar:

        for i in range(0, BLOCKLEN):
            if KEYPRESS1:
                xg0 = Xg
            if KEYPRESS2:
                xg1 = Xg
            if KEYPRESS3:
                xg2 = Xg
            if KEYPRESS4:
                xg3 = Xg
            if KEYPRESS5:
                xg4 = Xg
            if KEYPRESS6:
                xg5 = Xg
            if KEYPRESS7:
                
                xg6 = Xg
            if KEYPRESS8:
                xg7 = Xg
            if KEYPRESS9:
                xg8 = Xg
            if KEYPRESS10:
                xg9 = Xg
            if KEYPRESS11:
                xg10 = Xg
            if KEYPRESS12:
                xg11 = Xg
            if KEYPRESS13:
                xg12 = Xg
            if KEYPRESS14:
                xg13 = Xg
            if KEYPRESS15:
                xg14 = Xg
            if KEYPRESS16:
                xg15 = Xg
            if KEYPRESS17:
                xg16 = Xg
            if KEYPRESS18:
                xg17 = Xg
            if KEYPRESS19:
                xg18 = Xg
            if KEYPRESS20:
                xg19 = Xg
            if KEYPRESS21:
                xg20 = Xg
            if KEYPRESS22:
                xg21 = Xg
            if KEYPRESS23:
                xg22 = Xg
            if KEYPRESS24:
                xg23 = Xg

            # Compute output value
            # y(n) = x(n) + G x(n-N) + G x(n-N-1)
            yg0 = xg0 + G * buffer0[kr0] + G * buffer0[kr0-1]
            yg1 = xg1 + G * buffer1[kr1] + G * buffer1[kr1-1]
            yg2 = xg2 + G * buffer2[kr2] + G * buffer2[kr2-1]
            yg3 = xg3 + G * buffer3[kr3] + G * buffer3[kr3-1]
            yg4 = xg4 + G * buffer4[kr4] + G * buffer4[kr4-1]
            yg5 = xg5 + G * buffer5[kr5] + G * buffer5[kr5-1]
            yg6 = xg6 + G * buffer6[kr6] + G * buffer6[kr6-1]
            yg7 = xg7 + G * buffer7[kr7] + G * buffer7[kr7-1]
            yg8 = xg8 + G * buffer8[kr8] + G * buffer8[kr8-1]
            yg9 = xg9 + G * buffer9[kr9] + G * buffer9[kr9-1]
            yg10 = xg10 + G * buffer10[kr10] + G * buffer10[kr10-1]
            yg11 = xg11 + G * buffer11[kr11] + G * buffer11[kr11-1]
            yg12 = xg12 + G * buffer12[kr12] + G * buffer12[kr12-1]
            yg13 = xg13 + G * buffer13[kr13] + G * buffer13[kr13-1]
            yg14 = xg14 + G * buffer14[kr14] + G * buffer14[kr14-1]
            yg15 = xg15 + G * buffer15[kr15] + G * buffer15[kr15-1]
            yg16 = xg16 + G * buffer16[kr16] + G * buffer16[kr16-1]
            yg17 = xg17 + G * buffer17[kr17] + G * buffer17[kr17-1]
            yg18 = xg18 + G * buffer18[kr18] + G * buffer18[kr18-1]
            yg19 = xg19 + G * buffer19[kr19] + G * buffer19[kr19-1]
            yg20 = xg20 + G * buffer20[kr20] + G * buffer20[kr20-1]
            yg21 = xg21 + G * buffer21[kr21] + G * buffer21[kr21-1]
            yg22 = xg22 + G * buffer22[kr22] + G * buffer22[kr22-1]
            yg23 = xg23 + G * buffer23[kr23] + G * buffer23[kr23-1]


            # Update buffer (pure delay)
            buffer0[kw0] = yg0
            buffer1[kw1] = yg1
            buffer2[kw2] = yg2
            buffer3[kw3] = yg3
            buffer4[kw4] = yg4
            buffer5[kw5] = yg5
            buffer6[kw6] = yg6
            buffer7[kw7] = yg7
            buffer8[kw8] = yg8
            buffer9[kw9] = yg9
            buffer10[kw10] = yg10
            buffer11[kw11] = yg11
            buffer12[kw12] = yg12
            buffer13[kw13] = yg13
            buffer14[kw14] = yg14
            buffer15[kw15] = yg15
            buffer16[kw16] = yg16
            buffer17[kw17] = yg17
            buffer18[kw18] = yg18
            buffer19[kw19] = yg19
            buffer20[kw20] = yg20
            buffer21[kw21] = yg21
            buffer22[kw22] = yg22
            buffer23[kw23] = yg23

 
            # Increment read index
            kr0 = kr0 + 1
            if kr0 == BUFFER_LEN0:
                kr0 = 0
            kr1 = kr1 + 1
            if kr1 == BUFFER_LEN1:
                kr1 = 0
            kr2 = kr2 + 1
            if kr2 == BUFFER_LEN2:
                kr2 = 0
            kr3 = kr3 + 1
            if kr3 == BUFFER_LEN3:
               kr3 = 0
            kr4 = kr4 + 1
            if kr4 == BUFFER_LEN4:
                kr4 = 0
            kr5 = kr5 + 1
            if kr5 == BUFFER_LEN5:
                kr5 = 0
            kr6 = kr6 + 1
            if kr6 == BUFFER_LEN6:
                kr6 = 0
            kr7 = kr7 + 1
            if kr7 == BUFFER_LEN7:
                kr7 = 0
            kr8 = kr8 + 1
            if kr8 == BUFFER_LEN8:
                kr8 = 0
            kr9 = kr9 + 1
            if kr9 == BUFFER_LEN9:
               kr9 = 0
            kr10 = kr10 + 1
            if kr10 == BUFFER_LEN10:
                kr10 = 0
            kr11 = kr11 + 1
            if kr11 == BUFFER_LEN11:
                kr11 = 0
            kr12 = kr12 + 1
            if kr12 == BUFFER_LEN12:
                kr12 = 0
            kr13 = kr13 + 1
            if kr13 == BUFFER_LEN13:
                kr13 = 0
            kr14 = kr14 + 1
            if kr14 == BUFFER_LEN14:
                kr14 = 0
            kr15 = kr15 + 1
            if kr15 == BUFFER_LEN15:
               kr15 = 0
            kr16 = kr16 + 1
            if kr16 == BUFFER_LEN16:
                kr16 = 0
            kr17 = kr17 + 1
            if kr17 == BUFFER_LEN17:
                kr17 = 0
            kr18 = kr18 + 1
            if kr18 == BUFFER_LEN18:
                kr18 = 0
            kr19 = kr19 + 1
            if kr19 == BUFFER_LEN19:
                kr19 = 0
            kr20 = kr20 + 1
            if kr20 == BUFFER_LEN20:
                kr20 = 0
            kr21 = kr21 + 1
            if kr21 == BUFFER_LEN21:
               kr21 = 0
            kr22 = kr22 + 1
            if kr22 == BUFFER_LEN22:
                kr22 = 0
            kr23 = kr23 + 1
            if kr23 == BUFFER_LEN23:
                kr23 = 0



            # Increment write index    
            kw0 = kw0 + 1
            if kw0 == BUFFER_LEN0:
                kw0 = 0
            kw1 = kw1 + 1
            if kw1 == BUFFER_LEN1:
                kw1 = 0
            kw2 = kw2 + 1
            if kw2 == BUFFER_LEN2:
                kw2 = 0
            kw3 = kw3 + 1
            if kw3 == BUFFER_LEN3:
                kw3 = 0
            kw4 = kw4 + 1
            if kw4 == BUFFER_LEN4:
                kw4 = 0
            kw5 = kw5 + 1
            if kw5 == BUFFER_LEN5:
                kw5 = 0
            kw6 = kw6 + 1
            if kw6 == BUFFER_LEN6:
                kw6 = 0
            kw7 = kw7 + 1
            if kw7 == BUFFER_LEN7:
                kw7 = 0
            kw8 = kw8 + 1
            if kw8 == BUFFER_LEN8:
                kw8 = 0
            kw9 = kw9 + 1
            if kw9 == BUFFER_LEN9:
                kw9 = 0
            kw10 = kw10 + 1
            if kw10 == BUFFER_LEN10:
                kw10 = 0
            kw11 = kw11 + 1
            if kw11 == BUFFER_LEN11:
                kw11 = 0
            kw12 = kw12 + 1
            if kw12 == BUFFER_LEN12:
                kw12 = 0
            kw13 = kw13 + 1
            if kw13 == BUFFER_LEN13:
                kw13 = 0
            kw14 = kw14 + 1
            if kw14 == BUFFER_LEN14:
                kw14 = 0
            kw15 = kw15 + 1
            if kw15 == BUFFER_LEN15:
                kw15 = 0
            kw16 = kw16 + 1
            if kw16 == BUFFER_LEN16:
                kw16 = 0
            kw17 = kw17 + 1
            if kw17 == BUFFER_LEN17:
                kw17 = 0
            kw18 = kw18 + 1
            if kw18 == BUFFER_LEN18:
                kw18 = 0
            kw19 = kw19 + 1
            if kw19 == BUFFER_LEN19:
                kw19 = 0
            kw20 = kw20 + 1
            if kw20 == BUFFER_LEN20:
                kw20 = 0
            kw21 = kw21 + 1
            if kw21 == BUFFER_LEN21:
               kw21 = 0
            kw22 = kw22 + 1
            if kw22 == BUFFER_LEN22:
                kw22 = 0
            kw23 = kw23 + 1
            if kw23 == BUFFER_LEN23:
                kw23 = 0

                
            yg = yg0 + yg1 + yg2 + yg3 + yg4 + yg5 +yg6+yg7+yg8+yg9+yg10+yg11+yg12+yg13+yg14+yg15+yg16+yg17+yg18+yg19+yg20+yg21+yg22+yg23

            outputg[i] = yg
        
            # Clip and convert output value to binary data
            outputg_bytes = struct.pack('h', int(np.clip(yg, -MAXVALUE, MAXVALUE-1)))

            # Write output value to audio stream
            stream2.write(outputg_bytes)
            
            xg0 = 0
            xg1 = 0
            xg2 = 0
            xg3 = 0
            xg4 = 0
            xg5 = 0
            xg6 = 0
            xg7 = 0
            xg8 = 0
            xg9 = 0
            xg10 = 0
            xg11 = 0
            xg12 = 0
            xg13 = 0
            xg14 = 0
            xg15 = 0
            xg16 = 0
            xg17 = 0
            xg18 = 0
            xg19 = 0
            xg20 = 0
            xg21 = 0
            xg22 = 0
            xg23 = 0
            xg24 = 0


            KEYPRESS1 = False
            KEYPRESS2 = False
            KEYPRESS3 = False
            KEYPRESS4 = False
            KEYPRESS5 = False
            KEYPRESS6 = False
            KEYPRESS7 = False
            KEYPRESS8 = False
            KEYPRESS9 = False
            KEYPRESS10 = False
            KEYPRESS11 = False
            KEYPRESS12 = False
            KEYPRESS13 = False
            KEYPRESS14 = False 
            KEYPRESS15 = False
            KEYPRESS16 = False
            KEYPRESS17 = False
            KEYPRESS18 = False
            KEYPRESS19 = False
            KEYPRESS20 = False
            KEYPRESS21 = False
            KEYPRESS22 = False
            KEYPRESS23 = False
            KEYPRESS24 = False
        my_line.set_ydata(outputg) #update the plot

  
pyplot.ioff()  
# Close audio stream
stream.stop_stream()
stream.close()
stream2.stop_stream()
stream2.close()
p.terminate()

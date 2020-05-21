## Toggle LEDs when the GUI buttons are pressed ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led_red=LED(14)
led_yellow=LED(15)
led_green=LED(18)

### GUI DEFINITIONS ###
win = Tk()
win.title("Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def ledToggleRed():
    if led_red.is_lit:
        led_red.off()
        ledButtonRed["text"]="Turn Red LED on" # Change only the button text property
    else:
        led_red.on()
        led_yellow.off()
        led_green.off()
        ledButtonRed["text"]="Turn Red LED off"
        ledButtonYellow["text"]="Turn Yellow LED on"
        ledButtonGreen["text"]="Turn Green LED on"
        
def ledToggleYellow():
    if led_yellow.is_lit:
        led_yellow.off()
        ledButtonYellow["text"]="Turn Yellow LED on" # Change only the button text property
    else:
        led_yellow.on()
        led_red.off()
        led_green.off()
        ledButtonYellow["text"]="Turn Yellow LED off"
        ledButtonRed["text"]="Turn Red LED on"
        ledButtonGreen["text"]="Turn Green LED on"
        
def ledToggleGreen():
    if led_green.is_lit:
        led_green.off()
        ledButtonGreen["text"]="Turn Green LED on" # Change only the button text property
    else:
        led_green.on()
        led_yellow.off()
        led_red.off()
        ledButtonGreen["text"]="Turn Green LED off"
        ledButtonYellow["text"]="Turn Yellow LED on"
        ledButtonRed["text"]="Turn Red LED on"

def close():
    RPi.GPIO.cleanup()
    win.destroy()



### WIDGETS ###

# Button, triggers the connected command when it is pressed
ledButtonRed = Button(win, text='Turn Red LED on', font=myFont, command=ledToggleRed, bg='bisque2', height=1, width=24)
ledButtonRed.grid(row=0,column=1)

ledButtonYellow = Button(win, text='Turn Yellow LED on', font=myFont, command=ledToggleYellow, bg='bisque2', height=1, width=24)
ledButtonYellow.grid(row=1,column=1)

ledButtonGreen = Button(win, text='Turn Green LED on', font=myFont, command=ledToggleGreen, bg='bisque2', height=1, width=24)
ledButtonGreen.grid(row=2,column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, height=1, width=6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever
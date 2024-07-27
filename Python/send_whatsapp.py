# -----------------------------
# From:         https://www.youtube.com/watch?v=MQQTABNMZCE
# Notes:        Error in pressing enter key. The message is not sent.
#               https://github.com/Ankit404butfound/PyWhatKit/issues/20
# -----------------------------
import pywhatkit
import pyautogui
from tkinter import *

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor
print(screen_width, screen_height) # prints your monitor's resolution

country_code = "+65"
phone_number = input("Enter the phone number: ")
if " " in phone_number:
    phone_number = phone_number.replace(" ", "")
pywhatkit.sendwhatmsg(country_code+phone_number, "Sent with Python script.", 18,57)
pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
pyautogui.click() # Clicks the bar
pyautogui.press('enter') # Sends the message





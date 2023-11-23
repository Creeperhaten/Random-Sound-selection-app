import os
import pickle
import numpy as R
from pydub import AudioSegment
from pydub.playback import play
from tkinter import *

DefaultSettings = {"Volume" : .75, "SecBetweenSounds" : 5, "StartTimeSec" : 10,
                    "AutoStopMin" : 30, "ChanceSec" : .05, "SingleFile" : True, 
                    "TrueChance" : False, "PityChanceSensitivity" : 100, "ActualRand" : False,
                    "VolumeRolette" : False, "VolumeRoletteDeviation" : .50, "System32Rolette" : False} #Default
EditSettings = {} #The Settings saved to disk
CurrentSettings = {} #Running Right Now

PlayFiles = []

files = os.listdir("./Hamburger Sounds")

def StartUp():
    S = open("settings.dat", "rb")
    EditSettings = pickle.load(S)
    S.close()
    CurrentSettings = EditSettings

def Edit():
    EditSettings = "" #PLACEHOLDER FOR GUI SETTING LIST

#Longest a sound can go is 25 minutes without playing
#VolumeRolette MinimumCap


#StartUp()
print("\n" + str(CurrentSettings) + "\n")















def Saving():
    return

def FileReload(files):
    for i in files:
        if i.endswith(".wav"):
            PlayFiles.append("./Hamburger Sounds/" + i)

















FileReload(files)

########## debug ###########
print("\n")

print(str(PlayFiles))
with open('settings.dat', "rb") as settings:
    print(settings.read())
#EditFiles = input("\nDefault the save file? y or n: ")
#if EditFiles == "y":
#    S = open("settings.dat", "wb")
#    pickle.dump(DefaultSettings, S)
#    S.close()

print("\n")
########## debug ###########

sound = AudioSegment.from_wav(PlayFiles[0])
play(sound)
print("Hamburger (Succuessful code!)(92L)")

root = Tk()

e = Entry(root, borderwidth=5)

myLabel = Label(root, text="Hello World!")
myButton = Button(root, text="Click Me!", state=DISABLED) #Command= fg="Foreground color" bg="background color"

e.pack()
myLabel.pack()
myButton.pack()
#myLabel.grid(row=0, column=0)

root.mainloop()

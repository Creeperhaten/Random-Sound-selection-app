import os
import pickle
import numpy as R
import time
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

clear = lambda: os.system("cls")

def TermLoop():
    TermVar = input("\nRaSound|> ")

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
#play(sound)
print("Hamburger (Succuessful code!)(92L)")

#Start of terminal app RaSound
print("""          _____                    _____                    _____                   _______                   _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \               /::::\    \               /::\____\                /::\____\                /::\    \        
       /::::\    \              /::::\    \              /::::\    \             /::::::\    \             /:::/    /               /::::|   |               /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \           /::::::::\    \           /:::/    /               /:::::|   |              /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/    /               /::::::|   |             /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/    /               /:::/|::|   |            /:::/  \:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \     /:::/    / \:::\    \     /:::/    /               /:::/ |::|   |           /:::/    \:::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \   /:::/____/   \:::\____\   /:::/    /      _____    /:::/  |::|   | _____    /:::/    / \:::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \ |:::|    |     |:::|    | /:::/____/      /\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/::\   \:::\   \:::\____\|:::|____|     |:::|    ||:::|    /      /::\____\/:: /    |::|   /::\____\/:::/____/     \:::|    |
\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\:::\   \:::\   \::/    / \:::\    \   /:::/    / |:::|____\     /:::/    /\::/    /|::|  /:::/    /\:::\    \     /:::|____|
 \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/   \:::\    \ /:::/    /   \:::\    \   /:::/    /  \/____/ |::| /:::/    /  \:::\    \   /:::/    / 
       |:::::::::/    /            \::::::/    /    \:::\   \:::\    \        \:::\    /:::/    /     \:::\    \ /:::/    /           |::|/:::/    /    \:::\    \ /:::/    /  
       |::|\::::/    /              \::::/    /      \:::\   \:::\____\        \:::\__/:::/    /       \:::\    /:::/    /            |::::::/    /      \:::\    /:::/    /   
       |::| \::/____/               /:::/    /        \:::\  /:::/    /         \::::::::/    /         \:::\__/:::/    /             |:::::/    /        \:::\  /:::/    /    
       |::|  ~|                    /:::/    /          \:::\/:::/    /           \::::::/    /           \::::::::/    /              |::::/    /          \:::\/:::/    /     
       |::|   |                   /:::/    /            \::::::/    /             \::::/    /             \::::::/    /               /:::/    /            \::::::/    /      
       \::|   |                  /:::/    /              \::::/    /               \::/____/               \::::/    /               /:::/    /              \::::/    /       
        \:|   |                  \::/    /                \::/    /                 ~~                      \::/____/                \::/    /                \::/____/        
         \|___|                   \/____/                  \/____/                                           ~~                       \/____/                  ~~               """)
print("\n                                                         Welcome to the terminal version of RaSound by Nicholas Watkins!\n")
TermLoop()
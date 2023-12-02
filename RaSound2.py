import os
import pickle
import numpy as R
import time
from pydub import AudioSegment
from pydub.playback import play
from tkinter import *

#Imports END
#Variables

DefaultSettings = {"Volume" : .75, "SecBetweenSounds" : 5, "StartTimeSec" : 10,
                    "AutoStopMin" : 30, "ChanceSec" : .05, "SingleFile" : True, 
                    "TrueChance" : False, "PityChanceSensitivity" : 100, "ActualRand" : False,
                    "VolumeRolette" : False, "VolumeRoletteDeviation" : .50, "System32Rolette" : False} #Default for settings to revert to

OnFile = {}

CurrentSettings = {}

#Variables END
#Program Functions

def CurrentUpdate(DeSe): #Update the current settings list from file on False
    global CurrentSettings
    global OnFile
    if DeSe:
        CurrentSettings = DefaultSettings
    else:
        with open("settings.dat", "rb") as ODS:
            File = pickle.load(ODS)
            OnFile = File
            CurrentSettings = File

def SaveToFile():
    return

#Program Functions END
#Utility Functions

def wait(sec):
    time.sleep(sec)

clear = lambda: os.system("cls")

#Utility Functions END
#Body code

CurrentUpdate(True)

clear()

print(f"\n{DefaultSettings}\n\n{OnFile}\n\n{CurrentSettings}\n")

#Body code END

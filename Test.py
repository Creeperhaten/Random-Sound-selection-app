import numpy as np
import os
import pickle
from pydub import AudioSegment
from pydub.playback import play

files = os.listdir()
TrueFiles = []

for i in files:
    if i.endswith(".wav"):
        TrueFiles.append(i)

test = open("Test.txt", "wb")
pickle.dump(TrueFiles, test)
test.close()
test = open("Test.txt", "rb")
TestFiles = pickle.load(test)

Rolette = np.random.randint(1, 10)

sound = AudioSegment.from_wav(TestFiles[0])
play(sound) 
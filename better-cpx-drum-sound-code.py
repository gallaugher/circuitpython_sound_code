# Paper 808
# Drum machine using John Park's code:
# https://learn.adafruit.com/adafruit-circuit-playground-express/playground-drum-machine

import time
 
import audioio
import board
import touchio
from digitalio import DigitalInOut, Direction
 
bpm = 120  # beats per minute, change this to suit your tempo
 
# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True
 
# make the input cap sense pads
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5,
           board.A6, board.A7)
 
touchPad = []
for i in range(7):
    touchPad.append(touchio.TouchIn(capPins[i]))
    #  Modify the line below if you find your touchpads are too sensitive
    #  You can comment out this line if touch isn't sensitive enough
    #  Or if you have continued sounds without touching, increase the #.
    #  You might also find that the sensitivity changes depending on 
    #  whether you are plugged in via USB, or you're using a battery.
    touchPad[i].threshold += 1000
 
# The seven files assigned to the touchpads
audiofiles = ["1-cymbal.wav", "2-snare.wav", "3-bass.wav",
              "4-scratch.wav", "5-zome.wav", "6-tek.wav",
              "7-cowbell.wav"]
 
a = audioio.AudioOut(board.A0)
 
def play_file(filename):
    print("playing file " + filename)
    f = open(filename, "rb")
    wave = audioio.WaveFile(f)
    a.play(wave)
    time.sleep(bpm / 960)  # sixteenthNote delay
 
 
while True: 
    for i in range(7):
        if touchPad[i].value:
            play_file(audiofiles[i])

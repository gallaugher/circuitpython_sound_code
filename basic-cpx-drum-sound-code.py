import time
from adafruit_circuitplayground.express import cpx
# Just a test
cpx.play_file("scratch.wav")
cpx.adjust_touch_threshold(400)

while True:
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.play_file("bd_tek.wav")
    if cpx.touch_A2:
        print("Touched A2!")
        cpx.play_file("elec_hi_snare.wav")
    if cpx.touch_A3:
        print("Touched A3!")
        cpx.play_file("elec_cymbal.wav")
    if cpx.touch_A4:
        print("scratch A4!")
        cpx.play_file("scratch.wav")
    if cpx.touch_A5:
        print("Touched A5!")
        cpx.play_file("bd_zome.wav")
    if cpx.touch_A6:
        print("Touched A6!")
        cpx.play_file("bass_hit_c.wav")
    if cpx.touch_A7:
        print("Touched A7!")
        cpx.play_file("drum_cowbell.wav")

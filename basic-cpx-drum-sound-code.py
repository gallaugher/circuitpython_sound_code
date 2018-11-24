# cpx drum machine
from adafruit_circuitplayground.express import cpx

# increase this number if touch is too sensitive.
# decrease if not sensitive enough.
# Note: running on battery is usually less sensitive
# than running while connected and powered by USB.
cpx.adjust_touch_threshold(600)

while True:
    if cpx.touch_A1:
        cpx.play_file("1-cymbal.wav")
    if cpx.touch_A2:
        cpx.play_file("2-snare.wav")
    if cpx.touch_A3:
        cpx.play_file("3-bass.wav")
    if cpx.touch_A4:
        cpx.play_file("4-scratch.wav")
    if cpx.touch_A5:
        cpx.play_file("5-zome.wav")
    if cpx.touch_A6:
        cpx.play_file("6-tek.wav")
    if cpx.touch_A7:
        cpx.play_file("7-cowbell.wav")

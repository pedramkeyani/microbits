# -----------------------------------------------------------------------------
# Author: Pedram Keyani
# Email: pedram@openai.com
# Date: 2024-09-10
#
# Description: 
# Honeypot server that can be used with Magic_Number_Hacking_Node
# to confuse potential attackers
# -----------------------------------------------------------------------------
from microbit import *
import radio
import random

radio.config(group=random.randint(0,100), power=7)
radio.on()

def watch_radio():
    while True:
        req = radio.receive()
        if (req):
            res = str(random.randint(0,1000))
            radio.send(res)
            print(req + ' ' + res)

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.ANGRY)
    watch_radio()

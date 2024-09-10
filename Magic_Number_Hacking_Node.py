# -----------------------------------------------------------------------------
# Author: Pedram Keyani
# Email: pedram@openai.com
# Date: 2024-09-10
#
# Description: 
# Magic Number Hacking Node. Remove comments before sharing with
# students. The variable names, initialization and logic to get the 
# number area all intended to provide fun challenges that a team has
# to overcome.
# -----------------------------------------------------------------------------

from microbit import *
import radio
import random

# Terrible variable names just simulates what it looks like
# when you reverse engineer systems and have to keep meticulous
# notes on complex state

# Make the channel and power level vary to force them to probe
# the system. They will spend a lot of time in the dark about if
# they are getting it right. 
# For an extra hard version, we could add an additional honeypot
# node that just returns random numbers
# Another idea to make it harder is to have the channel change after 
# every 5-10 requests that it handles. This will mean that an attacker
# will have to be confident about how they understand the protocol
# before engaging with the system or else they will have to hunt for
# it again
tree = random.randint(0,100)
stew = random.randint(2, 7)
# Just to confuse things. To make it harder, you could add 
# some fun logic that gets called in random ways but the output
# doesn't do anything
flag = compass.heading()

radio.config(group = tree, power = stew)
radio.on()

magic_number = random.randint(1,1000)
poison_number = random.randint(1,1000)

# low light + fun = correct number
# high light + boring = correct number + 2
# everything else gets a garbage number
def radio_wait():
    soccer = poison_number
    while True:
        light = radio.receive()
        if light:
            display.scroll(light)
            break
    if light == 'fun' and display.read_light_level() < 100: 
        soccer = magic_number
    if light == 'boring' and display.read_light_level() >= 100:
       soccer = magic_number + 2 
    radio.send(str(soccer))
    return

# Code in a 'while True:' loop repeats forever
while True:
    print(accelerometer.was_gesture('up'))
    display.scroll(magic_number)
#    sleep(200)
    display.scroll(poison_number)
    display.scroll('L')
    radio_wait()

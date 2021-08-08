def on_received_number(receivedNumber):
    global state
    compareRoShamBo(weapon_index, receivedNumber)
    state = 1
radio.on_received_number(on_received_number)

def compareRoShamBo(you: number, opponent: number):
    global result
    if you == opponent:
        result = 0
    elif you == 0 and opponent == 2 or you > opponent:
        result = 1
    else:
        result = -1

def on_button_pressed_a():
    global weapon_index
    weapon_index += -1
    if weapon_index < 0:
        weapon_index = 2
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global state
    state = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global weapon_index
    weapon_index += 1
    if weapon_index > 2:
        weapon_index = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_number(weapon_index)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

result = 0
state = 0
weapon_index = 0
radio.set_group(1000)
weapon_list = ["R", "P", "S"]
weapon_index = 0
state = 0
result = 0

def on_forever():
    if state == 0:
        basic.show_string("" + (weapon_list[weapon_index]))
    else:
        if result == 0:
            basic.show_leds("""
                . . . . .
                                . # . # .
                                . . . . .
                                # # # # #
                                . . . . .
            """)
        elif result == 1:
            basic.show_leds("""
                . . . . .
                                . # . # .
                                . . . . .
                                # . . . #
                                . # # # .
            """)
        else:
            basic.show_leds("""
                . . . . .
                                . # . # .
                                . . . . .
                                . # # # .
                                # . . . #
            """)
basic.forever(on_forever)

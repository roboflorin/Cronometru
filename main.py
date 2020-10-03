def on_button_pressed_a():
    global stop, seconds
    stop = 0
    while True:
        control.wait_micros(500000)
        seconds += 1
        basic.show_string("" + str((seconds)))
        if stop == 1:
            break
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global seconds
    seconds = 0
    basic.show_string("" + str((seconds)))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global stop
    stop = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

stop = 0
seconds = 0
seconds = 0
stop = 0
basic.show_string("" + str((seconds)))
input.onButtonPressed(Button.A, function () {
    stop = 0
    while (true) {
        control.waitMicros(500000)
        seconds += 1
        basic.showString("" + (seconds))
        if (stop == 1) {
            break;
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    seconds = 0
    basic.showString("" + (seconds))
})
input.onButtonPressed(Button.B, function () {
    stop = 1
})
let stop = 0
let seconds = 0
seconds = 0
stop = 0
basic.showString("" + (seconds))

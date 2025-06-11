from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.modules = [split]
diode_orientation = DiodeOrientation.COL2ROW

# Uncomment based on the side the board is on 
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.UART, data_pin=board.IO, data_pin2=board.IO)

if (split_side == SplitSide.LEFT) {
    keyboard.col_pins = (board.IO1, board.IO15, board.IO2, board.IO16, board.IO3, board.IO17)
    keyboard.row_pins = (board.IO11, board.IO23, board.IO10, board.IO22, board.IO9)
} else {
    keyboard.col_pins = (board.IO11, board.IO23, board.IO10, board.IO22, board.IO9, board.IO21)
    keyboard.row_pins = (board.IO1, board.IO15, board.IO2, board.IO16, board.IO3)
}

keyboard.keymap = [
    [
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
                                         KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE
    ],
]

if __name__ == '__main__':
    keyboard.go()
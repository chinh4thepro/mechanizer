from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitSide
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.IO1, board.IO38, board.IO2, board.IO39, board.IO3, board.IO40)
keyboard.row_pins = (board.IO9, board.IO13, board.IO8, board.IO12, board.IO7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
        KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,
                                         KC.ESCAPE, KC.ESCAPE, KC.ESCAPE,       KC.ESCAPE, KC.ESCAPE, KC.ESCAPE
    ],
]
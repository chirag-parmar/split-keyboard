import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from storage import getmount
name = str(getmount('/').label)

col_wiring = (
    board.GP8,
    board.A3,
    board.GP28,
    board.GP27,
    board.GP26,
    board.GP15,
    board.GP14
)

row_wiring = (
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5
)

if name.endswith('_R'):
    col_wiring = (
        board.GP9,
        board.GP28,
        board.A3,
        board.GP26,
        board.GP27,
        board.GP14,
        board.GP15,
        
    )

    row_wiring = (
        board.GP3,
        board.GP2,
        board.GP5,
        board.GP4
    )


# for the left side of the keyboard
class KMKKeyboard(_KMKKeyboard):
    row_pins = row_wiring
    col_pins = col_wiring
    data_pin = board.GP1
    data_pin2 = board.GP0
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12
    diode_orientation = DiodeOrientation.COL2ROW
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,                      33, 32, 31, 30, 29, 28,
        7,  8,  9,  10, 11, 12,                     40, 39, 38, 37, 36, 35,
        14, 15, 16, 17, 18, 19, 20,             48, 47, 46, 45, 44, 43, 42,
                    24, 25, 26, 27,             55, 54, 53, 52,
    ]


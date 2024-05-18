import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from storge import getmount
name = str(getmount('/').label)

col_pins = (
    board.A3,
    board.GP28,
    board.GP27,
    board.GP26,
    board.GP15,
    board.GP14
)

row_pins = (
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8
)

if name.endswith('L'):
    col_pins = (
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8
    )

    row_pins = (
        board.GP14,
        board.GP15,
        board.GP26,
        board.GP27,
        board.GP28,
        board.A3
    )

# for the left side of the keyboard
class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.GP14,
        board.GP15,
        board.GP26,
        board.GP27,
        board.GP28,
        board.A3
    )
    col_pins = (
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8
    )
    data_pin = board.GP1
    data_pin2 = board.GP0
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12
    diode_orientation = DiodeOrientation.COL2ROW
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,                      41, 40, 39, 38, 37, 36,
        6,  7,  8,  9, 10, 11,                      47, 46, 45, 44, 43, 42,
        12, 13, 14, 15, 16, 17,                     53, 52, 51, 50, 49, 48,
        18, 19, 20, 21, 22, 23,                     59, 58, 57, 56, 55, 54,
                26, 27,                                     63, 62,
                        24, 25,                     61, 60,
                                34, 28,     64, 70,
                                35, 29,     65, 71
    ]
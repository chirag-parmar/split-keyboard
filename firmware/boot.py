import board
from kmk.bootcfg import bootcfg
from storage import getmount

name = str(getmount('/').label)

sense_pin = board.A3
source_pin = board.GP3

if name.endswith('L'):
    sense_pin = board.GP3
    source_pin = board.GP14

applied = bootcfg(
    sense=sense_pin,  # column
    source=source_pin, # row
    storage=False,
    usb_id=('KMK Keyboards', "Custom 60% Ergo"),
)

print(applied)



import board
from kmk.bootcfg import bootcfg

from storage import getmount
name = str(getmount('/').label)

sense_pin = board.GP8
source_pin = board.GP2

if name.endswith('_R'):
    sense_pin = board.GP9
    source_pin = board.GP3

applied = bootcfg(
    sense=sense_pin,  # column
    source=source_pin, # row
    storage=False,
    usb_id=('Parmar Keyboards', "Dactyl Manuform"),
)

print(applied)
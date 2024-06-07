import board
from kmk.bootcfg import bootcfg

sense_pin = board.GP8
source_pin = board.GP2

applied = bootcfg(
    sense=sense_pin,  # column
    source=source_pin, # row
    storage=False,
    usb_id=('Parmar Keyboards', "Dactyl Manuform"),
)

print(applied)
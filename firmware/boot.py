import board

from kmk.bootcfg import bootcfg

applied = bootcfg(
    sense=board.GP3,  # column
    source=board.GP14, # row
    storage=False,
    usb_id=('KMK Keyboards', "Custom 60% Ergo"),
)

print(applied)



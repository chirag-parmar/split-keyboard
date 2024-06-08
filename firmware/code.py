from kb import KMKKeyboard
import json
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.capsword import CapsWord
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

combos = Combos()
keyboard.modules.append(combos)

caps_word = CapsWord()
keyboard.modules.append(caps_word)

tapdance = TapDance()
keyboard.modules.append(tapdance)

split = Split(
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    split_type=SplitType.UART,
    split_side=None,
    use_pio=True,
    uart_flip = True
)

keyboard.modules.append(split)

combos.combos = [
    Chord((KC.SPC, KC.LPRN), KC.MO(3)),
    Chord((KC.RPRN, KC.BSPC), KC.ENT),
    # Chord((KC.LABK, KC.LCBR), KC.LBRC),
    # Chord((KC.RABK, KC.RCBR), KC.RBRC),
    # Chord((KC.F1, KC.F2, KC.LCTL, KC.RCTL), KC.TG(3)),
    # Sequence((KC.F18, KC.F19, KC.F20), KC.MW_UP, timeout=1000),
    # Sequence((KC.F21, KC.F22, KC.F23), KC.MW_DN, timeout=1000)
]

TAPDANCE_CAPS_LEFT = KC.TD(KC.LSFT, KC.CW, tap_time=200)
TAPDANCE_CAPS_RIGHT = KC.TD(KC.RSFT, KC.CW, tap_time=200)

my_keymap = [
    [
        KC.GRV,     KC.Q,   KC.W,   KC.E,       KC.R,       KC.T,                               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.LBRC,
        KC.TAB,     KC.A,   KC.S,   KC.D,       KC.F,       KC.G,                               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LGUI,    KC.Z,   KC.X,   KC.C,       KC.V,       KC.B,       KC.LPRN,      KC.RPRN,     KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.MINS,
                                    KC.LCTL,    KC.LSFT,    KC.MO(1),   KC.SPC,     KC.BSPC,    KC.MO(2),   KC.RSFT,    KC.RALT
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                            KC.VOLU,  KC.LEFT,  KC.UP,    KC.RGHT,  KC.MNXT,  KC.MPLY,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.VOLD,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.MPRV,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                            KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                            KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS
    ]
]

# Replace KC.LSFT with TAPDANCE_CAPS_LEFT and KC.RSFT with TAPDANCE_CAPS_RIGHT
for layer in my_keymap:
    for i, key in enumerate(layer):
        if key == KC.LSFT:
            layer[i] = TAPDANCE_CAPS_LEFT
        elif key == KC.RSFT:
            layer[i] = TAPDANCE_CAPS_RIGHT

keyboard.keymap = my_keymap

if __name__ == '__main__':
    keyboard.go()
from kb import KMKKeyboard
import json
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.capsword import CapsWord
from kmk.modules.tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

combos = Combos()
keyboard.modules.append(combos)

caps_word = CapsWord()
keyboard.modules.append(caps_word)

tapdance = TapDance()
keyboard.modules.append(tapdance)

mouse_keys = MouseKeys()
keyboard.modules.append(mouse_keys)

split = Split(
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    split_type=SplitType.UART,
    split_side=None,
    use_pio=True,
    uart_flip = True
)

keyboard.modules.append(split)

TD_LSFT = KC.TD(KC.LSFT, KC.CW, tap_time=200)
TD_RSFT = KC.TD(KC.RSFT, KC.CW, tap_time=200)
TD_LBRC = KC.TD(KC.LBRC, KC.RBRC, tap_time=100)
TD_LPRN = KC.TD(KC.LPRN, KC.RPRN, tap_time=100)
TD_MO = KC.TD(KC.MO(1), KC.TG(2), tap_time=200)

combos.combos = [
    Chord((26, 54), KC.ENT, match_coord=True),
    # Chord((KC.F1, KC.F2, KC.LCTL, KC.RCTL), KC.TG(3)),
    # Sequence((KC.F18, KC.F19, KC.F20), KC.MW_UP, timeout=1000),
    # Sequence((KC.F21, KC.F22, KC.F23), KC.MW_DN, timeout=1000)
]

keyboard.keymap = [
    [
        KC.GRV,     KC.Q,   KC.W,   KC.E,       KC.R,       KC.T,                               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
        KC.TAB,     KC.A,   KC.S,   KC.D,       KC.F,       KC.G,                               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LGUI,    KC.Z,   KC.X,   KC.C,       KC.V,       KC.B,       TD_LBRC,      TD_LPRN,  KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                    KC.LCTL,    TD_LSFT,    KC.SPC,     TD_MO,     KC.BSPC,  KC.SPC,     TD_RSFT,    KC.RALT
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                            KC.VOLU,  KC.LEFT,  KC.UP,    KC.RGHT,  KC.MNXT,  KC.MPLY,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.VOLD,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.MPRV,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,                            KC.MW_UP,  KC.MS_LT, KC.MS_UP,  KC.MS_RT,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.MW_DN,  KC.MS_LT, KC.MS_DN,  KC.MS_RT,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.MB_LMB,  KC.TRNS,      KC.TRNS,  KC.MB_RMB,  KC.TRNS,  KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()
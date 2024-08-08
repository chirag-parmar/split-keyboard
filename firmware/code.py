from kb import KMKKeyboard
import json
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.capsword import CapsWord
from kmk.modules.Tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.holdTap import HoldTap
from kmk.modules.macros import Macros
from kmk.modules.macros import Tap

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

combos = Combos()
keyboard.modules.append(combos)

caps_word = CapsWord()
keyboard.modules.append(caps_word)

HT = HoldTap()
keyboard.modules.append(HT)

Tapdance = TapDance()
keyboard.modules.append(Tapdance)

mouse_keys = MouseKeys()
keyboard.modules.append(mouse_keys)

macros = Macros()
keyboard.modules.append(macros)

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
TD_MO_1 = KC.TD(KC.MO(1), KC.LM(1, KC.LSFT), tap_time=200)
TD_MO_2 = KC.TD(KC.MO(2), KC.LM(2, KC.LSFT), tap_time=200)

combos.combos = [
    # Chord((26, 54), KC.ENT, match_coord=True),
    # Chord((KC.F1, KC.F2, KC.LCTL, KC.RCTL), KC.TG(3)),
    # Sequence((KC.F18, KC.F19, KC.F20), KC.MW_UP, timeout=1000),
    # Sequence((KC.F21, KC.F22, KC.F23), KC.MW_DN, timeout=1000)
]

 
# GENERAL RULES FOR CONVENIENCE
#   do not define combos with keys from both sides, will require both hands. rather if combos are defined on one side you can one hands free
#   using the same logic, define any control keys (volume up, previous, mouse up etc.) on the same side as the layer modifier that activates them.
#   shortcuts/keys that are frequently used must not require an extra modifier. use Tapdance to enable basic modifiers over layer modifiers.
#   the above guideline applies really well for numbers, in a 40% keyboard numbers require a layer modifiers and to access special characters you will require an extra modifier(lsft). better activate Tapdance on the modifiers. check TD_MO_1
#   it also makes a lot of sense to replace basic modifiers with layer modifiers but keep the count of modifiers the same. like del usually requires fn + backspace but it can be kept as MO(1) + backspace. replacing modifiers only makes sense for modifiers that cannot be accomodated on the keyboard or modifiers that do not require to be accomodated because their frequency of usage is too less.
#   some keys just dont' make sense on a normal keyboard like capslock. enable Tapdance on the lsft key for locking caps.
#   defining combos on different sides doesn't make a lot of sense  but I would still try to maintain the split for commonly occuring shortcuts. so that if you shift back to normal key board it is easier. example:  indentation shortcut
#   lalyers more than 2 must be defined for really specific usecases and should not be momentary layer. either you activate and stay on that layer or deactivate and come back. no switching back and forth. example: gaming  
#   The best use case of a custom designed keyboard is to make it more comfortable on your fingers, move the shift key to the thumn - no more stretching pinkies.

keyboard.keymap = [
    [
        KC.ESC,     KC.Q,   KC.W,   KC.E,       KC.R,       KC.T,                               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSPC,
        KC.TAB,     KC.A,   KC.S,   KC.D,       KC.F,       KC.G,                               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LCTL,    KC.Z,   KC.X,   KC.C,       KC.V,       KC.B,       KC.MINS,      KC.EQL,   KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                    KC.TRNS,    KC.LSFT,    KC.SPC,     KC.LGUI,      TD_MO_1,  KC.ENT,     TD_MO_2,    KC.RALT
    ],
    [
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                              KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.DEL,
        KC.TRNS,  KC.TRNS,  KC.LBRC,  KC.RBRC,  KC.LPRN,  KC.RPRN,                            KC.VOLU,  KC.LEFT,  KC.UP,    KC.RGHT,  KC.MNXT,  KC.MPLY,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.LCBR,  KC.RCBR,  KC.TRNS,        KC.TRNS,  KC.VOLD,  KC.TRNS,  KC.DOWN,  KC.TRNS,  KC.MPRV,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS
    ],
    [
        KC.TRNS,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                              KC.TRNS,     KC.TRNS,   KC.TRNS,    KC.TRNS,   KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,                             KC.TRNS,     KC.MS_LT,  KC.MS_UP,   KC.MS_RT,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.F11,   KC.F12,   KC.F13,   KC.F23,   KC.F24,   KC.TRNS,        KC.TRNS,  KC.TRNS,     KC.MB_LMB, KC.MS_DN,   KC.MS_RMB, KC.TRNS,  KC.TRNS,
                                      KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,        KC.TRNS,  KC.TRNS,     KC.TRNS,   KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()

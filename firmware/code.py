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

# Example: Print the contents of the JSON file
def process_keymap(path):
    # Specify the path to the JSON file
    json_file = path
    # Read the JSON file
    with open(json_file) as file:
        data = json.load(file)
    
    keymap = [None] * len(data["layers"])
    for layer_index, layer in enumerate(data["layers"]):
        layer_map = [None] * len(layer)
        for index, key in enumerate(layer):
            if "KC" in key:
                translated_key =  key.split("_")[1]
                if translated_key == "LT":
                    translated_key = "LABK"
                elif translated_key == "GT":
                    translated_key = "RABK"
            else:
                print("unknown key: ", key)
                    
            retrieved_key = KC.get(translated_key, None)
            # check if the key exists
            if retrieved_key != None:
                layer_map[index] = retrieved_key
            else:
                print("NOT FOUND: ", translated_key)
                
        keymap[layer_index] = layer_map
            

    return keymap

combos.combos = [
    Chord((KC.UP, KC.DOWN), KC.ENT),
    Chord((KC.LEFT, KC.RGHT), KC.ENT),
]

TAPDANCE_CAPS = KC.TD(KC.LSFT, KC.CW, tap_time=1000)

my_keymap = process_keymap("keymap.json")

# Replace KC.LSFT with TAPDANCE_CAPS
for layer in my_keymap:
    for i, key in enumerate(layer):
        if key == KC.LSFT:
            layer[i] = TAPDANCE_CAPS

keyboard.keymap = my_keymap

if __name__ == '__main__':
    keyboard.go()
from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitType

# Oled start 
#import oled
# Oled end

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())

# TODO Comment one of these on each side
# Left is 0, Right is 1
#split_sidedef = SplitSide.LEFT
#split_sidedef = SplitSide.RIGHT
#split = Split(split_side=split_side)

# Using drive names (KBL, KBR) to recognize sides; use split_side arg if you're not doing it
# split = Split(split_type=SplitType.UART, use_pio=True)  PIO OPTION
split = Split()
keyboard.modules.append(split)

# # keep only split_side and split_type when wired
# split = Split(
#     split_flip=True,  # If both halves are the same, but flipped, set this True
#     #split_side=split_sidedef,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
#     split_type=SplitType.UART,  # Defaults to UART, wired 
#     #split_target_left=False,  # If you want the right to be the target, change this to false
#     #uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
#     data_pin=board.RX,  # The primary data pin to talk to the secondary device with
#     #data_pin2=None,  # Second uart pin to allow 2 way communication
#     #target_left=False,  # Assumes that left will be the one on USB. Set to folse if it will be the right
#     #uart_flip=True,  # Reverses the RX and TX pins if both are provided
# )

# encoder
# encoder_handler = EncoderHandler()
# encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

# Uncomment below if you're having RGB
# rgb_ext = RGB(
#     pixel_pin=keyboard.rgb_pixel_pin,
#     num_pixels=10,
#     animation_mode=AnimationModes.BREATHING_RAINBOW,
# )
# keyboard.extensions.append(rgb_ext)

# LAYERS
LYR_STD, LYR_LOWER, LYR_RAISE = 0, 1, 2

# KEYS
TO_STD = KC.DF(LYR_STD)
LOWER = KC.MO(LYR_LOWER)
RAISE = KC.MO(LYR_RAISE)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# RGB KEY DEFINITION
# RGB_TOG = KC.RGB_TOG
# RGB_HUI = KC.RGB_HUI
# RGB_HUD = KC.RGB_HUD
# RGB_SAI = KC.RGB_SAI
# RGB_SAD = KC.RGB_SAD
# RGB_VAI = KC.RGB_VAI
# RGB_VAD = KC.RGB_VAD

# KEYMAP
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,    KC.N1,   KC.N2,  KC.N3,  KC.N4,  KC.N5,                          KC.N6,  KC.N7,  KC.N8,      KC.N9,  KC.N0,      KC.BSPC,\
        KC.TAB,    KC.Q,    KC.W,   KC.E,   KC.R,   KC.T,                           KC.Y,   KC.U,   KC.I,       KC.O,   KC.P,       KC.BSLS,\
        KC.LCTL,   KC.A,    KC.S,   KC.D,   KC.F,   KC.G,                           KC.H,   KC.J,   KC.K,       KC.L,   KC.SCLN,    KC.QUOT,\
        KC.LSFT,   KC.Z,    KC.X,   KC.C,   KC.V,   KC.B,                           KC.N,   KC.M,   KC.COMM,    KC.DOT, KC.SLSH,    KC.RSFT,\
                   KC.LCMD, KC.LALT,KC.LCTL,LOWER,  KC.ENT, KC.MUTE,     XXXXXXX,   KC.SPC, RAISE,  KC.RCTL,    KC.RALT,    KC.RCMD,
    ],
    [  #LOWER
        KC.ESC,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                         KC.F6,   KC.F7,  KC.F8,   KC.F9,   KC.F10, KC.F11,\
        XXXXXXX,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                        KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0,  KC.F12,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                KC.LCMD, KC.LALT, KC.LCTL, LOWER,  KC.ENT, XXXXXXX,         XXXXXXX, KC.SPC,   RAISE,   KC.RCTL,  KC.RALT, KC.RCMD,
    ],
    [  #RAISE
        KC.ESC,  KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.BSPC,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSLS,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS, KC.EQL,  KC.LBRC, KC.RBRC, KC.PIPE, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                   KC.LCMD, KC.LALT,KC.LCTL,LOWER,  KC.ENT, KC.MUTE,     XXXXXXX,   KC.SPC, RAISE,  KC.RCTL,  KC.RALT,    KC.RCMD,
    ]
    #[  #ADJUST
    #    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #    RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #    XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #                                       KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    #]
]


# Rotary Encoder (1 encoder / 1 definition per layer)
# encoder_handler.map = ( ((KC.UP, KC.DOWN),(RGB_HUI, RGB_HUI),), # Standard
# encoder_handler.map = ( ((KC.UP, KC.DOWN),), # Standard
#                        ((KC.VOLD, KC.VOLU),), # Lower
#                        ((RGB_HUI, RGB_HUD),), # Raise
#                     )

# Oled Start
# Oled End

if __name__ == '__main__':
    keyboard.go()

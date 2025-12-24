import board # type: ignore
import busio # type: ignore
from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.scanners.keypad import KeysScanner, DiodeOrientation # type: ignore
from kmk.keys import KC # type: ignore
from kmk.modules.macros import Press, Release, Tap, Macros # type: ignore
from kmk.modules.encoder import EncoderHandler # type: ignore
from kmk.extensions.display import Display, TextEntry, ImageEntry # type: ignore
from kmk.extensions.display.ssd1306 import SSD1306 # type: ignore
from kmk.extensions.media_keys import MediaKeys # type: ignore
from kmk.extensions.RGB import RGB # type: ignore
from kmk.extensions.rgb import AnimationModes # type: ignore


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

macros = Macros()
keyboard.modules.append(macros)

# PIN SETUP
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# KEYMAP
keyboard.keymap = [
    [KC.A, KC.B, KC.C],
    [KC.D, KC.E, KC.F],
    [KC.G, KC.H, KC.I],
]

# ENCODER SETUP
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins((board.D6, board.D7, None, False),) #67
encoder_handler.map = [ 
    (( KC.VOLU, KC.VOLD),),
    (( KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DN),),    
]

# OLED SETUP
i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(
    i2c=i2c_bus
)
display = Display(
    display=driver,
    width=128,
    height=32,
    flip = False,
    flip_left = False,
    brightness=0.8,
    brightness_step=0.1,
    dim_time=20,
    dim_target=0.1,
    off_time=60,
    powersave_dim_time=10,
    powersave_dim_target=0.1,
    powersave_off_time=30,
)

display.entries = [
    ImageEntry(image="INSERT_67.bmp", x=0, y=0),
    # ImageEntry(image="INSERT_89.bmp", x=0, y=0, layer=1), #You can add layer-specific image
    TextEntry(text="67", x=0, y=0),
    TextEntry(text="Ryan's Macropad", x=0, y=0, x_anchor="R", y_anchor="T"), # Set origin point as top-right

]
keyboard.extensions.append(display)

# RGB SETUP
rgb = RGB(
    pixel_pin=board.D3,
    num_pixels=9,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    rgb_order=(1, 0, 2), # GRB
    val_default=100,
    hue_step=5,
    sat_step=5,
    val_step=5,
    animation_speed=1,
    breathe_center=1,  # 1.0-2.7
    knight_effect_length=3,
    animation_mode=AnimationModes.STATIC,
    reverse_animation=False,
    refresh_rate=60,
)

if __name__ == "__main__":
    keyboard.go()

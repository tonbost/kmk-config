import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.D5,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    )
    col_pins = (
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    #uart_pin = board.RX
    rgb_pixel_pin = board.TX
    data_pin = board.D1
    #data_pin2 = board.TX
    #i2c = board.I2C
    #powersave_pin = board.P0_13
    encoder_pin_0 = board.A3
    encoder_pin_1 = board.A2


    # coord_mapping = []
    # coord_mapping.extend(ic(0, x, 6) for x in range(12))
    # coord_mapping.extend(ic(1, x) for x in range(12))
    # coord_mapping.extend(ic(2, x) for x in range(12))
    # coord_mapping.extend(ic(3, x) for x in range(12))
    # # Sofle is sqare per design so encoder in on the 4 row 
    # coord_mapping.extend(ic(4, x) for x in range(0, 12))

    # coord_mapping = [
    #  0,  1,  2,  3,  4,  5,  35, 34, 33, 32, 31, 30,
    #  6,  7,  8,  9, 10, 11,  41, 40, 39, 38, 37, 36,
    # 12, 13, 14, 15, 16, 17,  47, 46, 45, 44, 43, 42,
    # 18, 19, 20, 21, 22, 23,  53, 52, 51, 50, 49, 48,
    # 24, 25, 26, 27, 28, 29,  59, 58, 57, 56, 55, 54
    # ]
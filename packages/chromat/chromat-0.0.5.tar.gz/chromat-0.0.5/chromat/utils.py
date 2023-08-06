"""
'CHROMAT.utils'
copyright (c) 2023 hex benjamin
full license available at /COPYING
"""

# > IMPORTS
from typing import Literal


# > CLASSES
class SwatchProp:
    """
    A class for storing integer and float values of a color component.
    """

    def __init__(self, i_value: int, f_value: float):
        self.integer = i_value
        self.floating = f_value
        self.i = self.integer
        self.f = self.floating

    def __repr__(self) -> str:
        return str(self.integer)


class SwatchTupleProp:
    """
    A class for storing integer and float value tuples of a color component.
    """

    def __init__(
        self,
        i_value: tuple[int, int, int],
        f_value: tuple[float, float, float],
    ):
        self.integer = i_value
        self.floating = f_value
        self.i = self.integer
        self.f = self.floating

    def __repr__(self) -> str:
        return str(self.integer)


# > FUNCTIONS
def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """
    Converts a string of hex values to RGB.

    Args:
        hex_str (str): The hex string to convert.

    Returns:
        tuple[int, int, int]: A tuple of integer RGB values.
    """
    hex_str = hex_str.strip("#").lower()

    chars = set("0123456789abcdef")
    if any((c not in chars) for c in hex_str):
        raise ValueError("Invalid hex string.")

    rgb = []
    for i in range(3):
        s = i * 2  # start index
        e = s + 2  # end index
        rgb.append(int(hex_str[s:e], 16))

    return tuple(rgb)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def hsv_down(h, s, v):
    """
    Scales integer HSV values to floats.
    """
    return (round(h / 360, 3), round(s / 100, 3), round(v / 100, 3))


def hsv_up(h, s, v):
    """
    Scales float HSV values to integers.
    """
    return (round(h * 360), round(s * 100), round(v * 100))


def rgb_down(r, g, b):
    """
    Scales integer RGB values to floats.
    """
    return (round(r / 255, 3), round(g / 255, 3), round(b / 255, 3))


def rgb_up(r, g, b):
    """
    Scales float RGB values to integers.
    """
    return (round(r * 255), round(g * 255), round(b * 255))


def validate(check: tuple[int, int, int], mode: Literal["rgb", "hsv"]) -> bool:
    """
    Verifies supplied values are within the correct range, in the given mode.

    Args:
        check (tuple[int, int, int]): Tuple of values to check.
        mode (Literal"rgb", "hsv"]): Determines which color range to use.

    Returns:
        bool: Pass/fail for the validation.
    """
    if mode == "rgb":
        if not all((0 <= x <= 255 for x in check)):
            return False
    elif mode == "hsv":
        if not 0 <= check[0] <= 360:
            return False
        if not all((0 <= x <= 100 for x in check[1:])):
            return False
    return True

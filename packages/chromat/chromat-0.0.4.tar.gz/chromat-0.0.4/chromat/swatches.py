"""
'CHROMAT.swatches'
copyright (c) 2023 hex benjamin
full license available at /COPYING
"""

# > IMPORTS
import random

from colorsys import hsv_to_rgb, rgb_to_hsv  # noqa: F401
from typing import Iterable, Literal, Optional, Union

from rich.padding import Padding
from rich.panel import Panel
from rich.style import Style
from rich.table import Table
from rich.text import Text

from .utils import (  # noqa: F401
    SwatchProp,
    SwatchTupleProp,
    hex_to_rgb,
    hsv_down,
    hsv_up,
    rgb_down,
    rgb_up,
)


# > CONSTANTS
letters = {
    "r": "red",
    "g": "green",
    "b": "blue",
    "h": "hue",
    "s": "saturation",
    "v": "value",
}


# > CLASSES
class Swatch:
    # initializes as white, to ensure property access without linting errors
    name = "Swatch"

    hex = str("#ffffff")
    rgb = SwatchTupleProp((255, 255, 255), (1.0, 1.0, 1.0))
    hsv = SwatchTupleProp((0, 0, 100), (0.0, 0.0, 1.0))

    red = SwatchProp(255, 1.0)
    green = SwatchProp(255, 1.0)
    blue = SwatchProp(255, 1.0)
    hue = SwatchProp(0, 0.0)
    saturation = SwatchProp(0, 0.0)
    value = SwatchProp(100, 1.0)

    relative_luminance = 1.0

    # dictionary which will store the SwatchProp/SwatchTupleProp objects that become properties  # noqa: E501
    components = {}

    def __init__(
        self,
        color: Union[str, tuple[int, int, int]] = "#ffffff",
        mode: Literal["hex", "rgb", "hsv"] = "hex",
        name: Optional[str] = None,
    ):
        self._mode = mode

        if self._mode == "hex" and isinstance(color, str):
            self._color = hex_to_rgb(color)
            self._mode = "rgb"
        elif isinstance(color, tuple):
            if mode == "hex":
                raise ValueError("Cannot use hex mode with tuple input.")
            self._color = color

        self.get_components()
        self.get_relative_luminance()

        if name is not None:
            self.name = name

    def get_relative_luminance(self):
        """
        Get the relative luminance of the swatch.

        Returns:
            float: Relative luminance, 0-1.
        """
        r, g, b = [
            x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
            for x in self.rgb.f
        ]
        r *= 0.2126
        g *= 0.7152
        b *= 0.0722

        self.relative_luminance = r + g + b

    def get_components(self):
        global letters

        rgb_input = True if self._mode == "rgb" else False

        in_mode = "rgb" if rgb_input else "hsv"
        out_mode = "hsv" if rgb_input else "rgb"

        in_i = self._color
        in_f = eval(f"{in_mode}_down(*in_i)")

        self.components[in_mode] = SwatchTupleProp(in_i, in_f)
        for c, i, f in zip(list(in_mode), in_i, in_f):
            self.components[letters[c]] = SwatchProp(i, f)

        out_f = tuple(
            [round(x, 3) for x in eval(f"{in_mode}_to_{out_mode}(*in_f)")],
        )
        out_i = eval(f"{out_mode}_up(*out_f)")

        self.components[out_mode] = SwatchTupleProp(out_i, out_f)
        for c, i, f in zip(list(out_mode), out_i, out_f):
            self.components[letters[c]] = SwatchProp(i, f)

        for label in self.components.keys():
            setattr(self, label, self.components[label])

        self.hex = rgb_to_hex(self.rgb.i)

    def __repr__(self):
        return f"Swatch('{self.hex}')"

    def __rich__(self):
        richrepr = Text("Swatch('")
        richrepr.append(Text(self.hex, style=f"bold {self.hex}"))
        richrepr.append(Text("')", style="not bold default"))
        return richrepr

    @property
    def r(self):
        return self.red

    @property
    def g(self):
        return self.green

    @property
    def b(self):
        return self.blue
        return self.hsv.i

    @property
    def h(self):
        return self.hue

    @property
    def s(self):
        return self.saturation

    @property
    def v(self):
        return self.value

    @property
    def rel_lum(self):
        return self.relative_luminance

    @property
    def summary_panel(self):
        return SwatchPanel(self, "summary")

    @property
    def thumb_panel(self):
        return SwatchPanel(self, "thumb")


class SwatchPanel(Panel):
    def __init__(self, swatch: Swatch, mode: Literal["summary", "thumb"]):
        self.mode = mode

        _style = make_swatch_style(swatch.hex)

        if self.mode == "summary":
            title = Text(
                swatch.name,
                style=_style + Style(bold=True),
                overflow="ellipsis",
            )
            title.truncate(13)

            args = {
                "renderable": Padding(
                    SwatchSummaryTable(swatch),
                    (2, 0, 0, 10),
                ),
                "title": title,
                "title_align": "left",
                "subtitle": Text(
                    swatch.hex.upper(),
                    style=_style + Style(italic=True),
                ),
                "subtitle_align": "left",
                "style": _style,
                "border_style": _style,
                "padding": (0, 0),
                "expand": False,
            }
        elif self.mode == "thumb":
            args = {
                "renderable": " " * 12,
                "subtitle": Text(
                    swatch.name,
                    style=_style + Style(bold=True),
                ),
                "subtitle_align": "center",
                "style": _style,
                "border_style": _style,
                "padding": (0, 1),
                "expand": False,
            }
        else:
            raise ValueError(f"Invalid mode: {self.mode}")

        super().__init__(**args)


class SwatchSummaryTable(Table):
    def __init__(self, swatch: Swatch, **kwargs):
        super().__init__(
            show_header=False,
            box=None,
            **kwargs,
        )

        self.add_column(
            "property",
            width=4,
            justify="right",
            style=make_swatch_style(swatch.hex, italic=True),
        )

        self.add_column(
            "value",
            width=4,
            justify="left",
            style=make_swatch_style(swatch.hex, bold=True, reverse=True),
        )

        props = ["r", "g", "b", "h", "s", "v"]
        for p in props:
            value = getattr(swatch, p).i
            self.add_row(f"{p}:", str(value))


# > FUNCTIONS
def get_contrast(
    color1: Swatch,
    color2: Swatch,
) -> float:
    """
    Get the contrast ratio between two Swatch objects' colors.
    Also returns a list of WCAG standards met.

    Args:
        color1 (Swatch): First Swatch to compare.
        color2 (Swatch): Second Swatch to compare.

    Returns:
        float: The contrast ratio, 0-21.
    """
    lums = [color1.rel_lum, color2.rel_lum]
    contrast = (max(lums) + 0.05) / (min(lums) + 0.05)

    return contrast


def get_wcag(contrast: float) -> dict:
    """
    Get a list of WCAG standards met by a contrast ratio.

    Args:
        contrast (float): Contrast ratio, 0-21.

    Returns:
        Optional[list[str]]: A list of WCAG standards met. If the contrast
        ratio is <4.5 , the list will have a length of 0.
    """

    standards = {
        "AA": False,
        "AA-large": False,
        "AAA": False,
        "AAA-large": False,
    }
    if contrast >= 7.0:
        standards["AAA"] = True
    if contrast >= 4.5:
        standards["AAA-large"] = True
        standards["AA"] = True
    if contrast > 3.0:
        standards["AA-large"] = True

    return standards


def generate_accents(swatch: Swatch) -> Iterable[Swatch]:
    """Creates potential accent colors for a Swatch.

    Args:
        swatch (Swatch): Input swatch to generate accents for.

    Returns:
        Iterable[Swatch]: Iterable of Swatches to contrast-test.

    Yields:
        Iterator[Iterable[Swatch]]: Swatches to contrast-test.
    """
    values = list(range(0, 100, 1))
    random.shuffle(values)

    for v in values:
        yield Swatch(
            (swatch.h.i, random.randint(0, 20), v),
            mode="hsv",
        )


def make_accent(swatch: Swatch) -> Swatch:
    """
    Selects an accent color for a given swatch.

    Args:
        swatch (Swatch): Input swatch to generate an accent for.

    Returns:
        Swatch: Accent color with a contrast ratio of 4.5 or greater.
    """
    greatest = (0, Swatch())

    for check in generate_accents(swatch):
        contrast = get_contrast(swatch, check)

        pass_fail = True if 4.5 <= contrast else False

        if pass_fail:
            return check

        if contrast > greatest[0]:
            greatest = (contrast, check)

    return greatest[1]


def make_swatch_style(swatch_hex: str, **kwargs) -> Style:
    """
    Returns a Style object for a given swatch.
    Style puts an accent color on the swatch's color as a background.
    kwargs can parse these as bools: bold, italic, reverse, strike, underline

    Args:
        swatch_hex (str): Input hexadecimal color string.

    Returns:
        Style: Style object for the swatch.
    """
    accent = make_accent(Swatch(swatch_hex))
    style = Style(
        color=accent.hex,
        bgcolor=swatch_hex,
    )

    for k, v in kwargs.items():
        if k in ["bold", "italic", "reverse", "strike", "underline"]:
            style += Style(**{k: v})

    return style


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def validate(check: tuple[int, int, int], mode: Literal["rgb", "hsv"]) -> bool:
    if mode == "rgb":
        if not all((0 <= x <= 255 for x in check)):
            return False
    elif mode == "hsv":
        if not 0 <= check[0] <= 360:
            return False
        if not all((0 <= x <= 100 for x in check[1:])):
            return False
    return True

"""
'CHROMAT.console'
copyright (c) 2023 hex benjamin
full license available at /COPYING
"""

# > IMPORTS
from typing import Union

from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install as rich_traceback_install


# > SETUP
chromat_theme = Theme(
    {
        # utility
        "c.body": "#B9B8BA",
        "c.head": "bold #EEEEEE",
        "c.title": "reverse bold #ED589B",
        "c.error1": "bold #C44040",
        "c.error2": "not bold italic #ECDCDC",
        "c.success1": "bold #3FC18D",
        "c.success2": "not bold italic #DCEAE4",
        # # swatch components
        # "cs.red": "#E06C6C",
        # "cs.green": "#7CD06D",
        # "cs.blue": "#5E7CDE",
        # "cs.hue": "#F5E07A",
        # "cs.saturation": "#7B00FF",
        # "cs.value": "#B9B8BA",
    },
    inherit=False,
)

console = Console(theme=chromat_theme, tab_size=4)

rich_traceback_install()


# > CLASSES
class ErrorPanel(Panel):
    def __init__(self, error: Union[str, Text], **kwargs):
        if isinstance(error, str):
            error = Text(error, style="c.error2")

        super().__init__(
            error,
            title="ERROR",
            title_align="right",
            border_style="c.error1",
            padding=(1, 2),
            expand=False,
            **kwargs,
        )


# > FUNCTIONS
def pass_fail_text(result: bool) -> Text:
    if result:
        return Text("PASS", style="c.success1")
    else:
        return Text("FAIL", style="c.error1")


def make_swatch_style(swatch_hex: str, accent_hex: str, **kwargs) -> Style:
    """
    Returns a Style object for a given swatch.
    The style puts an accent color on the swatch's color as a background.

    Args:
        swatch_hex (str): Main hexadecimal color string.
        accent_hex (str): Accent's hexadecimal color string.
        **kwargs: Style options. [bold, italic, reverse, strike, underline]

    Returns:
        Style: Style object for the swatch.
    """
    style = Style(
        color=accent_hex,
        bgcolor=swatch_hex,
    )

    for k, v in kwargs.items():
        if k in ["bold", "italic", "reverse", "strike", "underline"]:
            style += Style(**{k: v})

    return style

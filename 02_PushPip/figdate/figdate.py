import time
import pyfiglet

from typing import Optional


def figlet_date(fmt: Optional[str] = None, font: Optional[str] = None):
    if fmt is None:
        fmt = "%Y %d %b, %A"
    if font is None:
        font = "graceful"
    return pyfiglet.figlet_format(time.strftime(fmt), font=font)

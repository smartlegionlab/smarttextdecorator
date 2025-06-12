# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""
A library for decorating strings and displaying them beautifully in the console.

Generates and displays lines to the full width of the console with the specified text and a placeholder character.

Generates and displays a line with the specified text, decorated at the top and bottom with filler characters along the length of the line.

Use for beautiful design of console applications.

"""
from .decorators import SmartPrinter, FramedTextDecorator, CenteredTextDecorator
__version__ = '0.1.3'
__author__ = 'A.A. Suvorov'

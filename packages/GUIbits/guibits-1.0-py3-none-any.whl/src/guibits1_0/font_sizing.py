# contractor which allows the client to resize the font
#   used by a widget

# version 27 Jul 2022  10:56

# author RNB

import PyQt6.QtWidgets
from . import type_checking2_0, windowing

"""
Copyright (C) 2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed procedures
# ------------------

def set_font_size(qw,fsize):
  """
  pre:
    qw = QWidget whose font size is to be modified
    fsize = new font size for qw, in points, as a float
    
  post:
    qw's font size has been modified as specified
    
  test:
    qw = none
    qw = valid QWidget
      fsize = 20
      fsize = 20.0
  """
  type_checking2_0.check_derivative(qw,PyQt6.QtWidgets.QWidget)
  type_checking2_0.check_identical(fsize,float)
  qw.setStyleSheet("QWidget {font-size: " + str(int(fsize)) + "pt}")
  
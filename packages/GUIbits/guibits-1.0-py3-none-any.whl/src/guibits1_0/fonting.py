# contractor that allows the client to obtain a QFont 

# version 26 Jul 2022  14:45

# author RNB

from . import font_styling
from . import type_checking2_0
import PyQt6.QtGui

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

def _qfont_of(fname,fsize,fss):
  """
  pre:
    fname = font name as string
    fsize = font size in points as float
    fss = font style set as font_styling.FontStyles
    
  post:
    a QFont corresponding to the given parameters has been returned
    
  test:
    fname = None
    fname = "Courier New"
      fsize = None
      fsize = 12.0
        fss = None
        fss = empty set
    fname = "Times New Roman"
      fsize = 20.0
        fss = {BOLD,ITALIC}
  """
  type_checking2_0.check_identical(fname,str)
  type_checking2_0.check_identical(fsize,float)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  _italic = font_styling.contains(fss,font_styling.FontStyle.ITALIC)
  _qf =  PyQt6.QtGui.QFont(fname,int(fsize),italic=_italic)
  if font_styling.contains(fss,font_styling.FontStyle.BOLD):
      _qf.setBold(True)
  return _qf

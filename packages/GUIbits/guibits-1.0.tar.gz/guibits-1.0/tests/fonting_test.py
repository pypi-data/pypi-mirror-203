# Test of contractor that allows the client to obtain a QFont 

# version 26 Jul 2022  14:46

# author RNB

from guibits1_0 import font_styling
from guibits1_0 import fonting

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

# test program
# ------------

def _test():
  print("_qfont_of", end = ' ')
  fss = font_styling.new_font_styles()
  #qf = fonting._qfont_of(None,None,None)
  #qf = fonting._qfont_of("Courier New",None,None)
  #qf = fonting._qfont_of("Courier New",12.0,None)
  qf = fonting._qfont_of("Courier New",12.0,fss)
  assert qf.family() == "Courier New"
  assert qf.pointSizeF() == 12.0
  assert qf.bold() == False
  assert qf.italic() == False
  font_styling.include(fss,font_styling.FontStyle.BOLD)
  font_styling.include(fss,font_styling.FontStyle.ITALIC)
  qf = fonting._qfont_of("Times New Roman",20.0,fss)
  assert qf.family() == "Times New Roman"
  assert qf.pointSizeF() == 20.0
  assert qf.bold() == True
  assert qf.italic() == True
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

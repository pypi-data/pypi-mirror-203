# Test of contractor which allows the client to resize the font
#   used by a widget

# version 27 Jul 2022  10:57

# author RNB

import PyQt6.QtWidgets

from guibits1_0 import font_sizing, windowing

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

class TestDialog(PyQt6.QtWidgets.QDialog):
  pass


def window_closing(win):
  if win._tnum == 0:
    print("Test 0", end = ' ')
    d = TestDialog(parent = win._my_frame)
    vl = PyQt6.QtWidgets.QVBoxLayout(d)
    dirl = PyQt6.QtWidgets.QHBoxLayout()
    vl.addLayout(dirl)
    look_in = PyQt6.QtWidgets.QLabel("Look in:")
    #font_sizing.set_font_size(None,20)
    #font_sizing.set_font_size(look_in,20)
    font_sizing.set_font_size(look_in,20.0)
    dirl.addWidget(look_in)
    dirtf = PyQt6.QtWidgets.QLineEdit()
    font_sizing.set_font_size(dirtf,20.0)
    dirl.addWidget(dirtf)
    d.exec()
    print("OK")
    win._tnum += 1
    return False
  
  else:
    print("All tests OK")
    return True
    
    
def _test():
  print("Tests of set_font_size")
  win = windowing.new_window(16.0,"Test of set_font_size",800.0,500.0,1.0)
  win._tnum = 0
  windowing.show(win,None,window_closing)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

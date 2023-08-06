# contractor to check whether main window is showing.

# version 28 Jul 22  20:10

# author RNB

from guibits1_0 import show_checking, windowing

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

def window_closing(win):
  show_checking.check_showing(win,"dialog")
  print("OK")
  return True
  

def _test():
  print("check_showing", end = ' ')
  #show_checking.check_showing(None,None)
  win = windowing.new_window(10.0,"Test of check_showing",800.0,400.0,1.0)
  #show_checking.check_showing(win,None)
  #show_checking.check_showing(win,"menu")
  windowing.show(win,None,window_closing)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

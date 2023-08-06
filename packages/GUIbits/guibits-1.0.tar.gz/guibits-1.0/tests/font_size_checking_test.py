# test of contractor to check font size

# version 26 Jul 2022  14:40

# author RNB

from guibits1_0 import font_size_checking

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
  print("check_window_font_size", end=' ')
  #font_size_checking.check_window_font_size(None)
  #font_size_checking.check_window_font_size(5.9)
  #font_size_checking.check_window_font_size(24.1)
  font_size_checking.check_window_font_size(24.0)
  font_size_checking.check_window_font_size(6.0)
  print("OK")

  print("check_pane_font_size", end=' ')
  #font_size_checking.check_window_font_size(None)
  #font_size_checking.check_pane_font_size(5.9)
  #font_size_checking.check_pane_font_size(72.1)
  font_size_checking.check_pane_font_size(72.0)
  font_size_checking.check_pane_font_size(6.0)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

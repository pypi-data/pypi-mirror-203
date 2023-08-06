import coloring
import font_styling
import windowing
import writing

# author R.N.Bosworth

# version 26 Jul 2021   16:12
"""
Demo of writing.write_string.

Copyright (C) 2014,2015,2019,2020,2021  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# private members
# ---------------
_PLAIN_STYLE = font_styling.new_font_styles()
_BLACK = coloring.new_color(0.0,0.0,0.0)
_FONT_SIZE = 20.0


# test program
# ------------

def window_opening(win):
  writing.write_string(win,"hello","Times New Roman",_PLAIN_STYLE,24.0,20.0,30.0,_BLACK)

def _test():
  print("Demo of writing.write_string")
  # create a window
  win = windowing.new_window(_FONT_SIZE,"Demo window 2",600.0,450.0,1.0)
  windowing.show(win,window_opening,None)
    

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

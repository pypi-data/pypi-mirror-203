# Test of the cursor blinking thread.

# version 26 Jul 2022 14:35

# author R.N.Bosworth

from guibits1_0 import cursor_blinking

"""
Copyright (C) 2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# test program
# ------------

def cursor_changed(cursor):
  print("Start of cursor_changed")
  print("  cursor._is_colored="+str(cursor._is_colored))
  

def _test():
  print("create cursor blinker")
  cursor = cursor_blinking._Cursor()
  cb = cursor_blinking.new_cursor_blinker(cursor,cursor_changed)
  print("cb = " + str(cb))
  input("start cb (CR):  ")
  cb.start()
  input("tell cb to drop dead (CR):  ")
  cb.please_drop_dead()
  print("OK")
  

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

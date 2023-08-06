# contractor to check whether main window is showing.

# version 20 Sep 2021  11:51

# author RNB

from . import type_checking2_0, windowing

"""
Copyright (C) 2021  R.N.Bosworth

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

def check_showing(win,s):
  """
  pre:
    win = windowing.Window to be checked
    s = name of the widget client is attempting to show,
          as Python string
  
  post:
    iff win is not showing, exception message warning the client is given
    
  test:
    check_showing(None,None)
    check_showing(win,None)
    check_showing(win,"menu")
      win is showing
    check_showing(win,"dialog")
      win is not showing
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(s,str)
  if win._my_frame == None:
    m = "Attempt to display "
    m += s
    m += " before window has been shown"
    raise Exception(m)

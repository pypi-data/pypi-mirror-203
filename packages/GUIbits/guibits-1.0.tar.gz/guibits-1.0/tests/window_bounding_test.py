# Test of contractor which deals with the bounds of a window

# version 28 Jul 22  20:08

# author RNB

from guibits1_0 import windowing, window_bounding

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
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    print("get_bounds")
    wb = window_bounding.get_bounds(win)
    print("  wb._x="+str(wb._x))
    print("  wb._y="+str(wb._y))
    print("  wb._width="+str(wb._width))
    print("  wb._height="+str(wb._height))
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("set_bounds(72.0,144.0,216.0,288.0)")
    wb = window_bounding.new_bounds()
    wb._x = 72.0
    wb._y = 144.0
    wb._width  = 216.0
    wb._height = 288.0
    window_bounding.set_bounds(win,wb)
    win._tnum += 1
    return False
  elif win._tnum == 2:
    print("get_bounds")
    wb = window_bounding.get_bounds(win)
    print("  wb._x="+str(wb._x))
    print("  wb._y="+str(wb._y))
    print("  wb._width="+str(wb._width))
    print("  wb._height="+str(wb._height))
    assert wb._x == 72.0
    assert wb._y == 144.0
    assert wb._width  == 216.0
    assert wb._height == 288.0
    print("OK")
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True


def _test():
  
  print("Main thread tests")
  wb = window_bounding.WindowBounds()
  wb._x = 41.0
  wb._y = 42.0
  wb._width = 43.0
  wb._height = 44.0

  print("get_height",end=' ')
  #assert window_bounding.get_height(None) == 44.0
  assert window_bounding.get_height(wb) == 44.0
  print("OK")
  
  print("get_width",end=' ')
  #assert window_bounding.get_width(456) == 43.0
  assert window_bounding.get_width(wb) == 43.0
  print("OK")
  
  print("get_x",end=' ')
  #assert window_bounding.get_x(9.9) == 41.0
  assert window_bounding.get_x(wb) == 41.0
  print("OK")
  
  print("get_y",end=' ')
  #assert window_bounding.get_y(None) == 42.0
  assert window_bounding.get_y(wb) == 42.0
  print("OK")
  
  print("new_bounds",end=' ')
  wb = window_bounding.new_bounds()
  assert wb._x == 72.0
  assert wb._y == 72.0
  assert wb._width == windowing._MEDIUM_WIDTH
  assert wb._height == windowing._MEDIUM_HEIGHT
  print("OK")
  
  print("get_bounds")
  #wb = window_bounding.get_bounds(None)
  win = windowing.new_window(12.0,"get_bounds",720.0,360.0,1.0)
  wb = window_bounding.get_bounds(win)
  assert wb._width == 720.0
  assert wb._height == 360.0
  print("  wb._x="+str(wb._x))
  print("  wb._y="+str(wb._y))
  print("  wb._width="+str(wb._width))
  print("  wb._height="+str(wb._height))
  print("OK")
  
  
  print("set_bounds",end=' ')
  #window_bounding.set_bounds(None,None)
  win = windowing.new_window(12.0,"set_bounds",720.0,360.0,1.0) 
  #window_bounding.set_bounds(win,43)
  wb = window_bounding.new_bounds()
  wb._x = 121.0
  wb._y = 122.0
  wb._width = 123.0
  wb._height = 124.0
  window_bounding.set_bounds(win,wb)
  wb2 = window_bounding.get_bounds(win)
  assert wb2._x == 121.0
  assert wb2._y == 122.0
  assert wb2._width == 123.0
  assert wb2._height == 124.0
  print("OK")
  
  print("set_height",end=' ')
  #window_bounding.set_height(None,None)
  wb = window_bounding.new_bounds()
  #window_bounding.set_height(wb,43)
  window_bounding.set_height(wb,54.3)
  assert wb._height == 54.3
  print("OK")
   
  print("set_width",end=' ')
  #window_bounding.set_width(None,None)
  wb = window_bounding.new_bounds()
  #window_bounding.set_width(wb,43)
  window_bounding.set_width(wb,54.3)
  assert wb._width == 54.3
  print("OK")
   
  print("set_x",end=' ')
  #window_bounding.set_x(None,None)
  wb = window_bounding.new_bounds()
  #window_bounding.set_x(wb,43)
  window_bounding.set_x(wb,54.3)
  assert wb._x == 54.3
  print("OK")
   
  print("set_y",end=' ')
  #window_bounding.set_y(None,None)
  wb = window_bounding.new_bounds()
  #window_bounding.set_y(wb,43)
  window_bounding.set_y(wb,54.3)
  assert wb._y == 54.3
  print("OK")
  
  # callback thread tests
  win = windowing.new_window(12.0,"callback tests",720.0,360.0,1.0) 
  win._tnum = 0
  windowing.show(win,None,window_closing)
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

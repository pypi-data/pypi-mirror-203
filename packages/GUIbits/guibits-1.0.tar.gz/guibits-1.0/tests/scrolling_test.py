# Test of contractor for reconciling scrollbars

# version 28 Jul 22  20:11

# author RNB

import PyQt6.QtCore

from guibits1_0 import scrolling, windowing

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

_FONT_SIZE = 18.0

def _window_closing3(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Tests of _set_scrollbar")
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    print("default scrollbar")
    print("  len = 1.0, off = 0.0")
    sb = PyQt6.QtWidgets.QScrollBar()
    scrolling._set_scrollbar(sb,1.0,0.0)
    assert sb.minimum() == 0
    assert sb.maximum() == 0
    assert sb.sliderPosition() == 0
    assert sb.pageStep() == 109
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("win's horizontal scrollbar")
    sb = win._my_scroll_area.horizontalScrollBar()
    print("  len = 0.5, off = 0.25")
    scrolling._set_scrollbar(sb,0.5,0.25)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 2:
    print("win's vertical scrollbar")
    sb = win._my_scroll_area.verticalScrollBar()
    print("  len = 0.5, off = 0.5")
    scrolling._set_scrollbar(sb,0.5,0.5)
    print("OK")
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True


def _window_closing4(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Tests of _reconcile_scrollbars")
  """
  test:
    vpr = None
    vpr = (0.0,0.0,10.0,5.0)
      pr = None
      pr = (0.0,0.0,10.0,10.0)
        sa = None
        sa = PyQt6.QtWidgets.QScrollArea
      pr = (-5.0,-5.0,20.0,10.0)
  """
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    print("  vpr = None")
    vpr = None
    pr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,10.0)
    sa = win._my_scroll_area
    #scrolling._reconcile_scrollbars(vpr,pr,sa)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("  vpr = (0,0,10,5)")
    print("  pr = None")
    vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,5.0)
    pr = None
    sa = win._my_scroll_area
    #scrolling._reconcile_scrollbars(vpr,pr,sa)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 2:
    print("  vpr = (0,0,10,5)")
    print("  pr = (0,0,10,10)")
    print("  sa = None")
    vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,5.0)
    pr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,10.0)
    sa = None
    #scrolling._reconcile_scrollbars(vpr,pr,sa)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 3: 
    print("  vpr = (0,0,10,5)")
    print("  pr = (0,0,10,10)")
    print("  sa = valid QScrollArea of win")
    vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,5.0)
    pr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,10.0)
    sa = win._my_scroll_area
    scrolling._reconcile_scrollbars(vpr,pr,sa)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 4:
    print("  vpr = (0,0,10,5)")
    print("  pr = (-5,-5,20,10)")
    vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,5.0)
    pr = PyQt6.QtCore.QRectF(-5.0,-5.0,20.0,10.0)
    sa = win._my_scroll_area
    scrolling._reconcile_scrollbars(vpr,pr,sa)
    print("OK")
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True
    

def _test():
  #win = windowing.new_window(_FONT_SIZE,"Tests of scrolling._set_scrollbar",432.0,288.0,1.0)
  #win._tnum = 0
  #windowing.show(win,None,_window_closing3)
  win = windowing.new_window(_FONT_SIZE,"Tests of _reconcile_scrollbars",432.0,288.0,1.0)
  win._tnum = 0
  windowing.show(win,None,_window_closing4)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

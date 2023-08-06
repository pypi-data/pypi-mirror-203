# Test of Contractor for drawing the cursor.

# author R.N.Bosworth

# version 28 Jul 22  20:15

import PyQt6.QtCore
from guibits1_0 import coloring, cursoring, windowing

"""
Copyright (C) 2014,2015,2016,2017,2020,2021,2022  R.N.Bosworth

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

_FONT_SIZE = 18.0

def _window_closing(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Tests of drawing and wiping cursor")
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    #cursoring.draw_cursor(None,_FONT_SIZE,1.0,0.0,coloring.BLACK);
    #cursoring.draw_cursor(win,72.1,1.0,0.0,coloring.BLACK);
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 1:
    print("cursor is blue at 10,20")
    BLUE = coloring.new_color(0.0,0.0,1.0)
    cursoring.draw_cursor(win,_FONT_SIZE,10.0,20.0,BLUE)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 2: 
    #print("cursor is black at 0.99,0");
    #cursoring.draw_cursor(win,_FONT_SIZE,0.99,0.0,coloring.BLACK);
    win._tnum += 1
    print("OK")
    return False

  elif win._tnum == 3: 
    print("cursor is black at 1,0")
    cursoring.draw_cursor(win,_FONT_SIZE,1.0,0.0,coloring.BLACK)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 4: 
    #print("cursor is black at 79.01,0");
    #cursoring.draw_cursor(win,_FONT_SIZE,79.01,0.0,coloring.BLACK);
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 5: 
    print("cursor is black at 79.0,0")
    cursoring.draw_cursor(win,_FONT_SIZE,79.0,0.0,coloring.BLACK)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 6: 
    #print("cursor is black at 79.0,-0.01");
    #cursoring.draw_cursor(win,_FONT_SIZE,79.0,-0.01,coloring.BLACK);
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 7: 
    #print("cursor is black at 79.0,42.01");
    #cursoring.draw_cursor(win,_FONT_SIZE,79.0,42.01,coloring.BLACK);
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 8: 
    print("cursor is black at 79.0,42.0")
    cursoring.draw_cursor(win,_FONT_SIZE,79.0,42.0,coloring.BLACK)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 9: 
    #print("wiping cursor on None window");
    #cursoring.wipe_cursor(None);
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 10: 
    print("wiping cursor on this window");
    cursoring.wipe_cursor(win)
    print("cursor is wiped")
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 11: 
    print("wiping cursor on this window again");
    cursoring.wipe_cursor(win)
    print("cursor is wiped (no cursor)")
    print("OK")
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True
    
    
def _window_closing2(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Tests of _ensure_cursor_is_visible, _calculate_pane_location")
  print("Enlarge pane to test cursor visibility")
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    print("  draw cursor at 1,0")
    cursoring.draw_cursor(win,_FONT_SIZE,1.0,0.0,coloring.BLACK)
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("  draw cursor at 431,270")
    cursoring.draw_cursor(win,_FONT_SIZE,431.0,270.0,coloring.BLACK)
    win._tnum += 1
    return False
  elif win._tnum == 2:
    print("  draw cursor at 1,0")
    cursoring.draw_cursor(win,_FONT_SIZE,1.0,0.0,coloring.BLACK)
    win._tnum += 1
    return False
  elif win._tnum == 3:
    print("  draw cursor at 361,198")
    cursoring.draw_cursor(win,_FONT_SIZE,361.0,198.0,coloring.BLACK)
    win._tnum += 1
    return False
  elif win._tnum == 4:
    print("  draw cursor at 72,72")
    cursoring.draw_cursor(win,_FONT_SIZE,72.0,72.0,coloring.BLACK)
    win._tnum += 1
    return False
  elif win._tnum == 5:
    print("  draw cursor at 431,270")
    cursoring.draw_cursor(win,_FONT_SIZE,431.0,270.0,coloring.BLACK)
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True


def _test():
  print("Main thread tests")
  print("tests of _calculate_pane_location", end=' ')
  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(-1.0,-1.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(0.0,0.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == 0.0
  assert pl.y() == 0.0
  
  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(0.0,0.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(0.0,0.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == 0.0
  assert pl.y() == 0.0
  
  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(1.0,1.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(0.0,0.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == 1.0
  assert pl.y() == 1.0

  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(0.0,0.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(6.0,11.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == -1.0
  assert pl.y() == -1.0

  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(-1.0,-1.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(6.0,11.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == -1.0
  assert pl.y() == -1.0

  vpr = PyQt6.QtCore.QRectF(0.0,0.0,10.0,20.0)
  pr = PyQt6.QtCore.QRectF(-2.0,-2.0,11.0,21.0)
  cr = PyQt6.QtCore.QRectF(6.0,11.0,5.0,10.0)
  pl = cursoring._calculate_pane_location(vpr,pr,cr)
  assert pl.x() == -2.0
  assert pl.y() == -2.0
  
  print("OK")
  
  print("Tests of draw_cursor")
  win = windowing.new_window(_FONT_SIZE,"window with cursor",80.0,60.0,1.0)
  #cursoring.draw_cursor(win,10.0,0.0,0.0,coloring.BLACK)
  win._tnum = 0
  windowing.show(win,None,_window_closing)
  win = windowing.new_window(_FONT_SIZE,"6\" by 4\" window with extreme cursor",432.0,288.0,1.0)
  win._tnum = 0
  windowing.show(win,None,_window_closing)
  windowing.show(win,None,_window_closing2)
  print("  after show")
  
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

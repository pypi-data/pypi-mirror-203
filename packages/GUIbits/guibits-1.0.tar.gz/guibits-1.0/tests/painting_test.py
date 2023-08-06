# Test program for painting the pane.

# author R.N.Bosworth

# version 12 Jan 2023  18:39

from guibits1_0 import coloring, painting, windowing

"""
Copyright (C) 2022,2023  R.N.Bosworth

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
    
def window_closing(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown
  """
  if win._tnum == 0:
    painting.paint_rectangle(win,0.0,0.0,0.0,0.0,coloring.BLACK)
    #painting.paint_rectangle(win,10.0,20.0,90.0001,180.0,coloring.BLACK)
    #painting.paint_rectangle(win,10.0,20.0,90.0,180.0001,coloring.BLACK)
    painting.paint_rectangle(win,10.0,20.0,90.0,180.0,coloring.BLACK)
    painting.paint_rectangle(win,10.0,20.0,90.0,180.0,coloring.BLACK)
    win._tnum += 1
    print("OK")
    return False
    
  elif win._tnum == 1:
    print("More tests of clear_rectangles", end=' ')
    painting.clear_rectangles(win)
    painting.paint_rectangle(win,72.0,36.0,72.0,72.0,coloring.BLACK)
    painting.paint_rectangle(win,216.0,216.0,72.0,72.0,coloring.new_color(0.0,0.0,1.0))  # BLUE
    win._tnum += 1
    return False
  elif win._tnum == 2:
    painting.clear_rectangles(win)
    win._tnum += 1
    print("OK")
    return False
  else:
    print("All tests OK")
    return True

    
def _test():
  print("Test of clear_rectangles",end=' ')
  #painting.clear_rectangles(None)
  win = windowing.new_window(12.0,"Test of paint_rectangle, clear_rectangles",360.0,360.0,1.0 )
  painting.clear_rectangles(win)
  print("OK")
  print("Test of paint_rectangle",end=' ')
  #painting.paint_rectangle(None,None,None,None,None,None)
  #painting.paint_rectangle(win,None,None,None,None,None)
  #painting.paint_rectangle(win,-0.0001,None,None,None,None)
  #painting.paint_rectangle(win,-0.0001,-0.0001,None,None,None)
  #painting.paint_rectangle(win,-0.0001,-0.0001,0.0,None,None)
  #painting.paint_rectangle(win,-0.0001,-0.0001,0.0,0.0,None)
  #painting.paint_rectangle(win,-0.0001,-0.0001,-0.0001,0.0,coloring.BLACK)
  #painting.paint_rectangle(win,-0.0001,-0.0001,0.0,-0.0001,coloring.BLACK)
  #painting.paint_rectangle(win,-0.0001,0.0,0.0,0.0,coloring.BLACK)
  #painting.paint_rectangle(win,0.0,-0.0001,0.0,0.0,coloring.BLACK)
  #painting.paint_rectangle(win,0.0,0.0,0.0,0.0,coloring.BLACK)
  win._tnum = 0
  windowing.show(win,None,window_closing)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

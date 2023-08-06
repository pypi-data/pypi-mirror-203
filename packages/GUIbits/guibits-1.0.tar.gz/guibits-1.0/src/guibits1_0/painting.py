# Contractor for painting the pane.

# author R.N.Bosworth

# version 12 Jan 23 18:34

import PyQt6.QtGui 
from . import coloring, command_listing
from . import resolving, type_checking2_0, windowing

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

# Exposed procedures
# ------------------

def clear_rectangles(win):
  """
  pre:
    win = window whose pane is to be cleared of rectangles 
      
  post:
    a paint event has been queued for win's frame
    after this paint event is processed,
      win's pane is clear of graphics
      
  test:
    win is null
    win is non-null
      win has no frame
      win has frame
        page has several rectangles
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  if win == None:
    raise Exception("Attempt to clear_rectangles of a null window")
  with win._my_rectangle_command_list._my_lock:
    win._my_rectangle_command_list = command_listing.new_command_list()
  p = win._my_pane
  if p != None:
    p.update()  # to queue a repaint
  

def paint_rectangle(win,x,y,w,h,c):
  """
  pre:
    win = Window in whose pane rectangle is to be painted
    win must be showing on the screen
    x = horizontal offset in points of top left-hand corner of rectangle from left-hand edge of win's pane
    y = vertical offset in points of top left-hand corner of rectangle from top of win's pane
    w = width of rectangle in points
    h = height of rectangle in points
    c = Color in which rectangle is to be drawn on win's pane
    (x,y,w,h) must be such that the rectangle lies entirely within win's pane 

  post:
    a paint event has been queued for win's pane
    after the paint event has been processed,
      the rectangle has been written to win's pane as specified
      the pane of win is positioned such that the rectangle is visible
    
  test:
    invalid window
    valid window, not showing
    valid window, showing
      x not a float
      x = -0.0001
      x = 0.0
        y not a float
        y = -0.0001
        y = 0.0
          w not a float
          w = -0.0001
          w = 0.0
          x + w = pane width + 0.0001          
          x + w = pane width
            h not a float
            h = -0.0001
            h = 0.0
            y + h = pane height + 0.0001
            y + h = pane height
  """
  """
  pre:
    win._my_frame = None, iff window is not showing
    win._my_pane_width, win._my_pane_height give the pane dimensions in points
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(x,float)
  type_checking2_0.check_identical(y,float)
  type_checking2_0.check_identical(w,float)
  type_checking2_0.check_identical(h,float)
  type_checking2_0.check_derivative(c,coloring.Color)
  if w < 0.0 or h < 0.0:
    mess = "Attempt to paint rectangle with negative width or height\n" + \
           "rectangle ("+str(x)+","+str(y)+","+str(w)+","+str(h)+")"
    raise Exception(mess)
  if x <0.0 or y < 0.0 or \
     x + w > win._my_pane_width or \
     y + h > win._my_pane_height:
    mess = "Attempt to paint rectangle lying outside the pane.\n" + \
      "Pane dimensions ("+str(win._my_pane_width)+","+str(win._my_pane_height)+")\n"+ \
      "rectangle ("+str(x)+","+str(y)+","+str(w)+","+str(h)+")"
    raise Exception(mess)
  if win._my_frame == None:
    raise Exception("Attempt to paint rectangle on non-showing window")
  cmd = command_listing.new_rectangle_command(x,y,w,h,c)
  # update the rectangle command list, in a synchronized fashion
  command_listing.insert(win._my_rectangle_command_list,cmd)
  cp = win._my_pane    
  cp.update()  # to queue a repaint


  """
  pxpt = resolving.pixels_per_point(win._my_pane)
  qx = int(x*pxpt*win._my_zoom_factor)
  qy = int(y*pxpt*win._my_zoom_factor)
  qw = int(w*pxpt*win._my_zoom_factor)
  qh = int(h*pxpt*win._my_zoom_factor)
  qc = PyQt6.QtGui.QColor(int(coloring.get_red(c)*255), \
                          int(coloring.get_green(c)*255), \
                          int(coloring.get_blue(c)*255))
  painter = PyQt6.QtGui.QPainter(win._my_pane)
  painter.fillRect(qx,qy,qw,qh,qc)
  """
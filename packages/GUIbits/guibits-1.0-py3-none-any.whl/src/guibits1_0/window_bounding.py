# contractor which deals with the bounds of a window

# version 28 Jul 22  19:53

# author RNB

import PyQt6.QtCore
from . import resolving, type_checking2_0, windowing

"""
Copyright (C) 2020,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# Exposed types
# -------------

class WindowBounds:
  pass


# Exposed procedures
# ------------------

def get_bounds(win):
  """
  pre:
    win = window whose current bounds are required
    win must be showing on the screen
  
  post:
    win's current normalized window bounds have been returned, 
      as a WindowBounds variable 

  test:
    win is not a window
    win is a window
      window not yet shown
      window has been shown
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  cwb = WindowBounds()
  with win._my_lock:
    if win._my_frame == None:
      cwb._x = win._my_x
      cwb._y = win._my_y
      cwb._width = win._my_width
      cwb._height = win._my_height
    else:
      # clone the current bounds to give a snapshot
      norm_geom = win._my_frame.normalGeometry()
      pxpt = resolving.pixels_per_point(win._my_frame)
      cwb._x = norm_geom.x()/pxpt
      cwb._y = norm_geom.y()/pxpt
      cwb._width = norm_geom.width()/pxpt
      cwb._height = norm_geom.height()/pxpt
    return cwb


def get_height(wb):
  """
  pre:
    wb = WindowBounds memento variable
      
  post:
    wb's height in points has been returned, as a float
  
  test:
    wb is not a WindowBounds variable
    wb is a WindowBounds variable
  """
  type_checking2_0.check_derivative(wb,WindowBounds)  
  return wb._height
  

def get_width(wb):
  """
  pre:
    wb = WindowBounds memento variable
      
  post:
    wb's width in points has been returned, as a float
  
  test:
    wb is not a WindowBounds variable
    wb is a WindowBounds variable
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  return wb._width
  

def get_x(wb):
  """
  pre:
    wb = WindowBounds memento variable
    
  post:
    wb's x offset in points from the top left-hand corner of the screen has been returned, as a float
    
  test:
    wb is not a WindowBounds variable
    wb is a WindowBounds variable
  """
  type_checking2_0.check_derivative(wb,WindowBounds)  
  return wb._x
  

def get_y(wb):
  """
  pre:
    wb = WindowBounds memento variable
    
  post:
    wb's y offset in points from the top left-hand corner of the screen has been returned, 
      as a float 

  test:
    wb is not a WindowBounds variable
    wb is a WindowBounds variable
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  return wb._y
  

def new_bounds():
  """
  post:
    a new WindowBounds variable with default values has been returned 

  test:
    once thru
  """
  wb = WindowBounds()
  wb._x = 72.0
  wb._y = 72.0
  wb._width = float(windowing._MEDIUM_WIDTH)
  wb._height = float(windowing._MEDIUM_HEIGHT)
  return wb
  

def set_bounds(win,wb):
  """
  pre:
    win = window whose normalized bounds are to be modified
    wb = WindowBounds memento variable containing the required bounds
    
  post:
    win's normalized bounds have been updated as required

  test:
    win is not a valid Window
    win is a valid Window
      wb is not a valid WindowBounds
      wb is a valid WindowBounds
        window has not been shown
        window has been shown
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_derivative(wb,WindowBounds)
  with win._my_lock:
    win._my_x = wb._x
    win._my_y = wb._y
    win._my_width = wb._width
    win._my_height = wb._height
    if win._my_frame != None:
      pxpt = resolving.pixels_per_point(win._my_frame)
      # set geometry of associated frame
      qr = PyQt6.QtCore.QRect(int(wb._x * pxpt), \
                              int(wb._y * pxpt), \
                              int(wb._width * pxpt), \
                              int(wb._height * pxpt))
      win._my_frame.setGeometry(qr)


def set_height(wb,h):
  """
  pre:
    wb = WindowBounds memento variable
    h = required height in points, as a float 
    
  post:
    wb's height has been updated as required 

  test:
    once thru
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  type_checking2_0.check_identical(h,float)
  wb._height = h
  

def set_width(wb,w):
  """
  pre:
    wb = WindowBounds memento variable
    w = required width in points, as a float
  
  post:
    wb's width has been updated as required 

  test:
    once thru
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  type_checking2_0.check_identical(w,float)
  wb._width = w
  

def set_x(wb,x):
  """
  pre:
    wb = WindowBounds memento variable
    x = required x offset in points from top left-hand corner of screen,
          as a float

  post:
    wb's x offset has been updated as required

  test:
    once thru
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  type_checking2_0.check_identical(x,float)
  wb._x = x
  

def set_y(wb,y):
  """
  pre:
    wb = WindowBounds memento variable
    
    y = required y offset in points from top left-hand corner of screen,
          as a float
          
  post:
    wb's y offset has been updated as required

  test:
    once thru
  """
  type_checking2_0.check_derivative(wb,WindowBounds)
  type_checking2_0.check_identical(y,float)
  wb._y = y

# Contractor for drawing the cursor.

# author R.N.Bosworth

# version 28 Jul 22  19:55

import PyQt6.QtCore
from . import coloring, cursor_blinking, font_size_checking
from . import resolving, scrolling, show_checking
from . import type_checking2_0, windowing
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

# exposed procedures
# ------------------

def draw_cursor(win,fsize,x,y,c):
  """
  pre:
    win = window in whose pane cursor is to be drawn
    win must be showing on the screen
    fsize = required point size of cursor, as a float
    x = horizontal offset in points of center of cursor from left-hand edge of win's pane, as a float
    y = vertical offset in points of top of cursor from top of win's pane,
          as a float
    c = color in which cursor is to be drawn on win's pane, as coloring.Color
    (x,y) must be such that cursor lies entirely within win's pane

  post:
    the cursor has been drawn on win's pane as specified
    the pane of win is positioned such that the cursor is visible 

  test:
    win is None
    win is not showing on screen
    win is showing on screen
      win does not have a cursor
      win does have a cursor
      fsize = 72.1
      fsize = 72.0
        cursor slightly too far left
        cursor on left edge of window
        cursor slightly too far right
        cursor on right edge of window
        cursor slightly too high
        cursor on top edge of window
        cursor slightly too low
        cursor on bottom edge of window
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(fsize,float)
  type_checking2_0.check_identical(x,float)
  type_checking2_0.check_identical(y,float)
  type_checking2_0.check_derivative(c,coloring.Color)
  if win == None:
    raise Exception("specified window is None")
  show_checking.check_showing(win,"cursor")
  font_size_checking.check_pane_font_size(fsize)
      
  # check the cursor position
  _pr = PyQt6.QtCore.QRectF(0.0,0.0,win._my_pane_width,win._my_pane_height)
  if win._my_cursor == None:
    win._my_cursor = cursor_blinking._Cursor()
  # cursor is a singleton
  
  _cu = win._my_cursor
  if  not _pr.contains(PyQt6.QtCore.QRectF(x - _CURSOR_WIDTH/2.0, y, _CURSOR_WIDTH, fsize)):
    raise Exception("cursor lies outside the pane")
  # update the cursor as required
  with _cu._my_lock:
    _cu._my_font_size = fsize          # in points
    _cu._my_x = x - _CURSOR_WIDTH/2.0  # tlh corner of cursor in points
    _cu._my_y = y                      # tlh corner of cursor in points
    _cu._my_color = c                  # as coloring.Color
    _cu._is_colored = True
    _cu._my_window = win
    
    # start the blinking thread if necessary
    if _cu._my_blinker == None:
      _cu._my_blinker = cursor_blinking.new_cursor_blinker(_cu,_cursor_changed)
      _cu._my_blinker.start()
      
  # ensure cursor is visible to user
  _ensure_cursor_is_visible(win)
  win._my_pane.update()
  

def wipe_cursor(win):
  """
  pre:
    win = window in which any cursor is to be wiped
    
  post:
    a paint event has been queued for win
    when the paint event has been processed,
      the cursor does not appear in the pane of window win 

  test:
    win is None
    win is non-None
      cursor does exist
      cursor does not exist
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  if win == None:
    raise Exception("specified window is None")
    
  if win._my_cursor != None:
    with win._my_cursor._my_lock:
      # switch off blinking thread
      win._my_cursor._my_blinker.please_drop_dead()
      # make cursor invisible
      win._my_cursor = None
      
    win._my_pane.update()
    

# private members
# ---------------

_CURSOR_WIDTH = 1.0   # width in points

def _calculate_pane_location(vpr,pr,cr):
  """
  pre:
    vpr = rectangle of viewport in pixels, as QRectF
    pr = rectangle of pane relative to viewport in pixels, as QRectF
    cr = rectangle of cursor relative to pane in pixels, as QRectF
             (must intersect with pr)
             
  post:
    returns location of pane in pixels as QPointF, 
      relative to viewport which ensures that cursor rectangle 
        is visible in viewport
  
  tests:
    cursor at top left-hand corner of pane
      pane at (-1.0,-1.0)
      pane at (0.0,0.0)
      pane at (1.0,1.0)
    cursor at bottom right-hand corner of pane
      pane just off bottom and right of view
      pane just at bottom and right of view
      pane just inside bottom and right of view
  """  
  # x-axis
  px = pr.x()
  
  # find offset of left-hand edge of cursor wrt the viewport
  lhoff = cr.x() + pr.x()

  if lhoff < 0.0:
    px = pr.x()-lhoff
    
  #find offset of right-hand edge of cursor wrt the viewport
  rhoff = cr.x() + cr.width() + pr.x()

  if rhoff > vpr.width():
    px = pr.x() - (rhoff - vpr.width())
    
  # y-axis
  py = pr.y()
  # find offset of top edge of cursor wrt the viewport
  topoff = cr.y() + pr.y()

  if topoff < 0.0:
    py = pr.y()-topoff
    
  #find offset of bottom edge of cursor wrt the viewport
  botoff = cr.y() + cr.height() + pr.y()

  if botoff > vpr.height():
    py = pr.y() - (botoff - vpr.height())

  #p.set_location(px,py)
  return PyQt6.QtCore.QPointF(px,py)
  

def _cursor_changed(cursor):
  """
  pre:
    cursor = cursor whose position has changed, 
               or which has appeared
    
  post:
    a paint event has been queued for the cursor's pane
    
  test:
    once thru
  """
  #print("cursoring.cursor_changed")
  cursor._my_window._my_pane.update()
  

def _ensure_cursor_is_visible(win):
  """
  pre:
    win = window in which cursor is to be checked

  post:
      the pane of win is positioned such that the cursor is visible
      a paint event on the window has been queued so that the concrete pane will
        eventually be repositioned

  test:
    cursor is within viewport
    cursor is not within viewport
  """
  # get the viewport rectangle from the last time it was displayed
  vpr = PyQt6.QtCore.QRectF(win._my_scroll_area.viewport().geometry())

  # get the pane rectangle from the last time it was displayed   
  pr = PyQt6.QtCore.QRectF(win._my_pane.frameGeometry())

  # find cursor's rectangle in pixels
  cursor = win._my_cursor
  ppr = resolving.pixels_per_point(win._my_frame)
  with cursor._my_lock:
    cr = PyQt6.QtCore.QRectF(cursor._my_x*win._my_zoom_factor*ppr, \
                             cursor._my_y*win._my_zoom_factor*ppr, \
                             _CURSOR_WIDTH*win._my_zoom_factor*ppr, \
                             cursor._my_font_size*win._my_zoom_factor*ppr)
    # it is guaranteed that this rectangle lies inside visible pane
    
  # calculate bloated cursor rectangle (with cordon sanitaire to make visible)
  # add a cordon sanitaire of cursor height around the cursor
  cursor_x = cr.x()
  cursor_y = cr.y()
  cursor_width = cr.width()
  cursor_height = cr.height()
  bcr = PyQt6.QtCore.QRectF(cursor_x - cursor_height, cursor_y - cursor_height, \
                            cursor_width + 2.0*cursor_height, 3.0*cursor_height)

  new_location = _calculate_pane_location(vpr,pr,bcr)
  if new_location.x() != pr.x() or new_location.y() != pr.y():
    pr = PyQt6.QtCore.QRectF(new_location.x(), new_location.y(), \
                              pr.width(), pr.height())
    scrolling._reconcile_scrollbars(vpr,pr,win._my_scroll_area)

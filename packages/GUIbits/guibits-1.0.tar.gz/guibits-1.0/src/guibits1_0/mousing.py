# Contractor for mouse events.

# author R.N.Bosworth

# version 22 Sep 22  16:13

"""
This is an adapter which constructs composite mouse gestures from the atomic mouse gestures performed by the user.  The composite mouse gestures are:

 1. mouse_click
 
 2. double_click
 
 3. mouse_popup
 
 4. mouse_pressed mouse_dragged* mouse_released (mouse drag)
 
There is a client callback method for each of these gestures.  The client callbacks are contained in a mouse listener class derived from mousing.MouseListener.

The position of the mouse is returned in points relative to the top left hand
corner of the window's pane.  For convenience, the mouse_popup gesture also 
returns the position in points relative to the window's contents, 
i.e. just below the left-hand end of the title bar of the window.
"""

import PyQt6.QtCore
from enum import Enum
from . import callback_checking1_0, resolving
from . import type_checking2_0, windowing

"""
Copyright (C) 2015,2016,2017,2019,2020,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# exposed types
# -------------

class MouseListener:

  def double_clicked(self,x,y):
    """
      pre:
        the primary mouse button has been clicked (pressed and released) 
          twice in quick succession by the user
        self = MouseListener for which this mouse event occurred
        (x,y) = position in points at which the mouse pointer was 
                double-clicked, relative to the top left-hand corner of the window's pane, as floats
                
      post:
        the action required by the user has been carried out
    """
    pass


  def mouse_clicked(self,x,y):
    """
      pre:
        the primary mouse button has been clicked (pressed and released) 
          once by the user
        self = MouseListener for which this mouse event occurred
        (x,y) = position in points at which the mouse pointer was clicked, 
                relative to the top left-hand corner of the window's pane,
                as floats
                
      post:
        the action required by the user has been carried out
    """
    pass
 
 
  def mouse_dragged(self,x,y):
    """
    pre:
      the mouse has been dragged (moved with the primary mouse-button 
        pressed) at least 5 points by the user from its previous position
      self = MouseListener for which this mouse event occurred
      (x,y) = position in points to which the mouse pointer was dragged, 
              relative to the top left-hand corner of the window's pane,
              as floats              
              
    post:
      the action (if any) required by the user has been carried out
    """
    pass
    

  def mouse_popup(self,x,y,win,window_x,window_y):
    """
    pre:
      the user has gestured that a popup menu should be displayed. On some 
        platforms, this is done by clicking the right mouse button.
      self = MouseListener for which this mouse event occurred
      (x,y) = position in points at which the mouse pointer was clicked, 
              relative to the top left-hand corner of the window's pane,
              as floats
      win = windowing.Window in which the gesture was made 
      (window_x,window_y) = position in points required for popup menu,  
                            relative to the top left-hand corner of the 
                            window's contents, as floats
      
    post:
      the action (if any) required by the user has been carried out
    """
    pass
    
  
  def mouse_pressed(self,x,y):
    """
    pre:
      the user has pressed the primary mouse-button, 
        signifying the start of a mouse-drag operation
      self = MouseListener for which this mouse event occurred
      (x,y) = position in points of the mouse pointer when the mouse button 
              was pressed, relative to the top left-hand corner of the 
              window's pane, as floats
              
    post:
      the action (if any) required by the user has been carried out
    """
    pass
    

  def mouse_released(self,x,y):
    """
    pre:
      the user has released the primary mouse-button, 
        signifying the end of a mouse-drag operation
      self = MouseListener for which this mouse event occurred
      (x,y) = position in points of the mouse pointer when the mouse button 
              was released, relative to the top left-hand corner of 
              the window's pane, as floats
              
    post:
      the action (if any) required by the user has been carried out
    """
    pass


# exposed procedures
# ------------------

def attach(ml,win):
  """
  pre:
    ml = MouseListener which is to be attached to windowing.Window win
    win = Window to which ml is to be attached
    win is showing on the screen
    
  post:
    ml has been attached to win, making win's pane responsive to mouse events
  
  test:
    None mouse listener
    None window
    valid mouse listener and window
      window has not been shown
      window has been shown (check set-up values)
  """
  type_checking2_0.check_derivative(ml,MouseListener)
  type_checking2_0.check_derivative(win,windowing.Window)
  if win._my_pane == None:
    raise Exception("win has not yet been shown")
  _pane = win._my_pane
  _pane._gesture_state = Enum('_gesture_state','GESTURE_STARTED GESTURE_CONTINUED GESTURE_ENDED')
  _pane._mouse_state = _pane._gesture_state.GESTURE_ENDED
  _pane._last_mouse_press_x = 0  # mouse x position in pixel integral coordinates
  _pane._last_mouse_press_y = 0  # mouse y position in pixel integral coordinates
  _pane._last_mouse_press_button = PyQt6.QtCore.Qt.MouseButton.NoButton
  _pane._last_mouse_click_time = None # time as a QTime
  _pane._latitude_in_pixels = int(_MOUSE_LATITUDE * resolving.pixels_per_point(_pane))
  _pane._my_mouse_listener = ml
  
  
# private members
# ---------------

_DOUBLE_CLICK_INTERVAL = 500.0  # milliseconds
_MOUSE_LATITUDE = 5.0  # +- points allowed for click


def _mouseMoveEvent(self,qme):
  """
  pre:
    self = _PaneWidget on which move event occurred
    qme = QMouseEvent which has just occurred
    self._my_mouse_listener = MouseListener for this event, or None
    self._mouse_state = self._gesture_state.GESTURE_STARTED
    self._last_mouse_press_x = x-coord of last mouse press, as integer
    self._last_mouse_press_y = y-coord of last mouse press,as integer
    self._last_mouse_press_button = button pressed for last mouse press, 
                                      as PyQt6.QtCore.Qt.MouseButton
    self._latitude_in_pixels = latitude for mouse click in pixels, 
                                       as integer
    
  post:
    sends suitable event, or sequence of events, 
      to adaptee MouseListener

  test:
    None mouse listener
    valid mouse listener
      drag with press within latitude
      drag with press outside latitude
        press was on right mouse button, or equivalent on non-Windows systems
        press was on left mouse button, or equivalent on non-Windows systems
          self._my_mouse_listener.mouse_pressed has incorrect parameters
          self._my_mouse_listener.mouse_pressed has correct parameters
            self._my_mouse_listener.mouse_dragged has incorrect parameters
            self._my_mouse_listener.mouse_dragged has correct parameters
  """
  #print("mousing._mouseMoveEvent")
  if self._my_mouse_listener != None:
    if self._last_mouse_press_button == PyQt6.QtCore.Qt.MouseButton.LeftButton:
      if self._mouse_state == self._gesture_state.GESTURE_STARTED:
        if (abs(qme.pos().x() - self._last_mouse_press_x) > self._latitude_in_pixels) or \
        (abs(qme.pos().y() - self._last_mouse_press_y) > self._latitude_in_pixels):
          self._mouse_state = self._gesture_state.GESTURE_CONTINUED
          _pc = _points_in_pane_of(self._last_mouse_press_x,self._last_mouse_press_y,windowing.zoom_factor_of(self._my_window),self)
          callback_checking1_0.check_method(self._my_mouse_listener.mouse_pressed,["x","y"])
          self._my_mouse_listener.mouse_pressed(_pc.xip,_pc.yip)
          _pc = _points_in_pane_of(qme.pos().x(),qme.pos().y(),windowing.zoom_factor_of(self._my_window),self)
          callback_checking1_0.check_method(self._my_mouse_listener.mouse_dragged,["x","y"])
          self._my_mouse_listener.mouse_dragged(_pc.xip,_pc.yip)
            
      elif self._mouse_state == self._gesture_state.GESTURE_CONTINUED:
        _pc = _points_in_pane_of(qme.pos().x(),qme.pos().y(),windowing.zoom_factor_of(self._my_window),self)
        callback_checking1_0.check_method(self._my_mouse_listener.mouse_dragged,["x","y"])
        self._my_mouse_listener.mouse_dragged(_pc.xip,_pc.yip)
          
      else:
        pass # ignore for stability
      

def _mousePressEvent(self,qme):
  """
  pre:
    self = _PaneWidget on which press event occurred
    qme = QMouseEvent which has just occurred
    
  post:
    if self._my_mouse_listener != None (i.e. MouseListener has been attached)
      self._mouse_state = self._gesture_state.GESTURE_STARTED
      self._last_mouse_press_x = x-coord of this mouse press
      self._last_mouse_press_y = y-coord of this mouse press
      self._last_mouse_press_button = button pressed for this mouse press

  test:
    None mouse listener
    valid mouse listener
  """
  #print("mousing._mousePressEvent")
  if self._my_mouse_listener != None:
    self._mouse_state = self._gesture_state.GESTURE_STARTED
    self._last_mouse_press_x = qme.pos().x()
    self._last_mouse_press_y = qme.pos().y()
    self._last_mouse_press_button = qme.button()
  

def _mouseReleaseEvent(self,qme):
  """
  pre:
    self = QWidget on which release event occurred
    qme = QMouseEvent which has just occurred
    
  post:
    if mouse listener exists,
    either:
      mouse_popup
    or
      mouse_clicked
    or
      double_clicked
    or
      mouse_released
      
    has been called, depending on the context.

  test:
    None mouse listener
    valid mouse listener
      mouse left click (release within 5 points of press)
      mouse left click (release more than 5 points from press)
      mouse right click
      double click (less than 0.5.sec)
      double click (greater than 0.5.sec)
      release is end of drag
  """
  #print("mousing._mouseReleaseEvent")
  if self._my_mouse_listener != None:
      if self._mouse_state == self._gesture_state.GESTURE_STARTED:
        if (abs(qme.pos().x() - self._last_mouse_press_x) <= self._latitude_in_pixels) and \
           (abs(qme.pos().y() - self._last_mouse_press_y) <= self._latitude_in_pixels):
          # it's a click
          self._mouse_state = self._gesture_state.GESTURE_ENDED
          if self._last_mouse_press_button == PyQt6.QtCore.Qt.MouseButton.RightButton:
            _pc = _points_in_pane_of(self._last_mouse_press_x,self._last_mouse_press_y,windowing.zoom_factor_of(self._my_window),self)
            _pcw = _points_in_window_contents_of(self._last_mouse_press_x,self._last_mouse_press_y,self._my_window)
            callback_checking1_0.check_method(self._my_mouse_listener.mouse_popup,["x","y","win","window_x","window_y"])
            self._my_mouse_listener.mouse_popup(_pc.xip,_pc.yip,self._my_window,_pcw.xip,_pcw.yip)
            
          elif self._last_mouse_press_button == PyQt6.QtCore.Qt.MouseButton.LeftButton:
            if self._last_mouse_click_time != None and \
               self._last_mouse_click_time.msecsTo(PyQt6.QtCore.QTime.currentTime()) <= _DOUBLE_CLICK_INTERVAL:
              _pc = _points_in_pane_of(self._last_mouse_press_x,self._last_mouse_press_y,windowing.zoom_factor_of(self._my_window),self)
              callback_checking1_0.check_method(self._my_mouse_listener.double_clicked,["x","y"])
              self._my_mouse_listener.double_clicked(_pc.xip,_pc.yip)
            else:
              _pc = _points_in_pane_of(self._last_mouse_press_x,self._last_mouse_press_y,windowing.zoom_factor_of(self._my_window),self)
              callback_checking1_0.check_method(self._my_mouse_listener.mouse_clicked,["x","y"])
              self._my_mouse_listener.mouse_clicked(_pc.xip,_pc.yip)
            self._last_mouse_click_time = PyQt6.QtCore.QTime.currentTime()
            
        else:
          # it's a drag
          self._mouse_state = self._gesture_state.GESTURE_ENDED
          if self._last_mouse_press_button == PyQt6.QtCore.Qt.MouseButton.LeftButton:
            _pc = _points_in_pane_of(qme.pos().x(),qme.pos().y(),windowing.zoom_factor_of(self._my_window))
            callback_checking1_0.check_method(self._my_mouse_listener.mouse_released,["x","y"])
            self._my_mouse_listener.mouse_released(_pc.xip,_pc.yip)
            
          
      # it's still a drag
      elif self._mouse_state == self._gesture_state.GESTURE_CONTINUED:
        self._mouse_state = self._gesture_state.GESTURE_ENDED
        if self._last_mouse_press_button == PyQt6.QtCore.Qt.MouseButton.LeftButton:
          _pc = _points_in_pane_of(qme.pos().x(),qme.pos().y(),windowing.zoom_factor_of(self._my_window),self)
          callback_checking1_0.check_method(self._my_mouse_listener.mouse_released,["x","y"])
          self._my_mouse_listener.mouse_released(_pc.xip,_pc.yip)
          
      else:
        pass  # ignore for stability


class _PointCoordinates:
  xip = 0.0  # x coordinate in points, as float
  yip = 0.0  # y coordinate in points, as float
  

def _points_in_pane_of(x,y,zf,pw):
  """
  pre:
    x,y = coodinates in pixels of this location in the zoomed pane
    zf = zoom factor for this pane
    pw = pane, as PaneWidget 
    
  post:
    coordinates in points of this location in the unzoomed pane have been returned

  test:
    once thru with non-unity values
  """
  _pc = _PointCoordinates()
  pxpt = resolving.pixels_per_point(pw)
  _pc.xip = (x/pxpt)/zf
  _pc.yip = (y/pxpt)/zf
  return _pc
  

def _points_in_window_contents_of(x,y,win):
  """
  pre:
    x,y = coodinates in pixels of this location in the zoomed pane,
            as integers
    win = window of the pane which has this location
    
  post:
    coordinates in points of this location in win's contents have been returned, as PointCoordinates
    (The window's contents are everything below the title bar.)

  test:
    once thru with non-zero values
  """
  #print("_points_in_window_contents_of")
  _x = x
  _y = y
  #print("  _x="+str(_x))
  #print("  _y="+str(_y))
  
  _pane = win._my_pane
  # find (x,y) relative to scrollpane
  _x += _pane.x()
  _y += _pane.y()
  #print("  relative to scrollpane");
  #print("  _x="+str(_x));
  #print("  _y="+str(_y));
  
  # find (x,y) relative to _Frame's internal geometry
  _scroll_area = win._my_scroll_area
  #print("_scroll_area.x()="+str(_scroll_area.x()))
  #print("_scroll_area.y()="+str(_scroll_area.y()))
  _x += _scroll_area.x()
  _y += _scroll_area.y()
  #print("  relative to _Frame's internal geometry")
  #print("  _x="+str(_x))
  #print("  _y="+str(_y))
  
  # convert to points
  _pc = _PointCoordinates()
  pxpt = resolving.pixels_per_point(_pane)
  _pc.xip = _x/pxpt
  _pc.yip = _y/pxpt
  return _pc

# Test Contractor for mouse events.

# author R.N.Bosworth

# version 28 Jul 22  20:15

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

from guibits1_0 import mousing, windowing

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

class TestMouseListener(mousing.MouseListener):
  def double_clicked(self,x,y):
    print("TestMouseListener.double_clicked")
    print("  x=" + str(x))
    print("  y=" + str(y))
     
  def mouse_clicked(self,x,y):
    print("TestMouseListener.mouse_clicked")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_dragged(self,x,y):
    print("TestMouseListener.mouse_dragged")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_popup(self,x,y,win,window_x,window_y):
    print("TestMouseListener.mouse_popup")
    print("  x=" + str(x))
    print("  y=" + str(y))
    print("  win =" + str(win))
    print("  window_x=" + str(window_x))
    print("  window_y=" + str(window_y))
    
  def mouse_pressed(self,x,y):
    print("TestMouseListener.mouse_pressed")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_released(self,x,y):
    print("TestMouseListener.mouse_released")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
    
class TestMouseListener2(mousing.MouseListener):
  def double_clicked(self,x):
    print("TestMouseListener.double_clicked")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_clicked(self,x):
    print("TestMouseListener.mouse_clicked")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_dragged(self,x):
    print("TestMouseListener.mouse_dragged")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_popup(self,x,y,win,window_x):
    print("TestMouseListener.mouse_popup")
    print("  x=" + str(x))
    print("  y=" + str(y))
    print("  win =" + str(win))
    print("  window_x=" + str(window_x))
    print("  window_y=" + str(window_y))
    
  def mouse_pressed(self,x,y):
    print("TestMouseListener.mouse_pressed")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
  def mouse_released(self,x):
    print("TestMouseListener.mouse_released")
    print("  x=" + str(x))
    print("  y=" + str(y))
    
    
def _window_closing(win):
  #print("_window_closing")
  if win._tnum == 0:
    print("Tests of _points_in_pane_of(16,32,2.0)")
    _pc = mousing._points_in_pane_of(16,32,2.0,win._my_pane)
    print("_pc.xip="+str(_pc.xip))
    print("_pc.yip="+str(_pc.yip))
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("Tests of _points_in_window_contents_of(16,32)")
    _pc = mousing._points_in_window_contents_of(16,32,win)
    print("  _pc.xip=" + str(_pc.xip))
    print("  _pc.yip=" + str(_pc.yip))
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 2:
    print("Tests of _mousePressEvent with no attached MouseListener")
    print("  please hit the _PaneWidget! (Should have no effect)")
    print("OK")    
    win._tnum += 1
    return False
  elif win._tnum == 3:
    print("Tests of attach with live window")
    assert win._my_pane._my_mouse_listener == None
    ml = TestMouseListener()
    mousing.attach(ml,win)
    assert win._my_pane._my_mouse_listener == ml
    print("win._my_pane._mouse_state="+str(win._my_pane._mouse_state))
    print("win._my_pane._last_mouse_press_x="+str(win._my_pane._last_mouse_press_x))
    print("win._my_pane._last_mouse_press_y="+str(win._my_pane._last_mouse_press_y))
    print("win._my_pane._last_mouse_press_button="+str(win._my_pane._last_mouse_press_button))
    print("win._my_pane._last_mouse_click_time="+str(win._my_pane._last_mouse_click_time))
    print("win._my_pane._latitude_in_pixels="+str(win._my_pane._latitude_in_pixels))
    print("OK")    
    win._tnum += 1
    return False
  elif win._tnum == 4:
    print("Tests of _mousePressEvent")
    print("  please hit the _PaneWidget!")
    win._tnum += 1
    return False  
  elif win._tnum == 5:
    print("Tests of _mousePressEvent with bad callbacks")
    #ml = TestMouseListener2()
    #mousing.attach(ml,win)
    print("  please hit the _PaneWidget!")
    win._tnum += 1
    return False  
  else:
    print("All tests OK")
    return True
    
  
def _test():
  win = windowing.new_window(18.0,"mousing tests",800.0,400.0,1.0)
 
  print("Tests of attach with window not shown")
  ml = TestMouseListener()
  #mousing.attach (None,None)
  #mousing.attach (ml,None)
  #mousing.attach(ml,win)
  print("OK")
  
  print("Tests with live window")
  win._tnum = 0
  windowing.show(win,None,_window_closing)
  print("return from windowing.show")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

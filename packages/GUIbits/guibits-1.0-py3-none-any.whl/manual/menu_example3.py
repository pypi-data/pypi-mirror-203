from guibits1_0 import menuing,mousing,type_checking2_0,windowing

# author R.N.Bosworth

# version 24 Sep 22  16:01

"""
Example of a drop-down menu from a right mouse-click.

Copyright (C) 2019,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

font_size = 20.0

class MyMouseListener(mousing.MouseListener):
  def double_clicked(self,x,y):
    """
    pre:
      the primary mouse button has been clicked (pressed and released) twice in quick
        succession (< 0.5 sec) by the user
      self = pane for this mouse event
      (x,y) = position in points at which the mouse pointer was double-clicked,
        relative to the top left-hand corner of the window's pane 
        
    post:
        the action required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    pass
    
  
  def mouse_clicked(self,x,y):
    """
    pre:
      the primary mouse button has been clicked (pressed and released) once by the user
      self = pane for this mouse event
      (x,y) = position in points at which the mouse pointer was clicked, relative to the top left-hand corner of the window's pane 
    post:
      the action required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    pass
    
  
  def mouse_dragged(self,x,y):
    """
    pre:
      the mouse has been dragged (moved with the primary mouse-button pressed) at least 5 points by the user  
        from its previous position
      self = pane for this mouse event
      (x,y) = position in points to which the mouse pointer was dragged, relative to the top left-hand corner of the window's pane
      
    post:
      the action (if any) required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    pass
    
  
  def mouse_popup(self,x,y,win,window_x,window_y):
    """
    pre:
      the user has gestured that a popup menu should be displayed. On some platforms, this is done by clicking 
        the right mouse button.
      self = pane for this mouse event
      (x,y) = position in points at which the mouse pointer was clicked, relative to the top left-hand corner 
        of the window's pane
      win = window in which the gesture was made
      (window_x,window_y) = position in points required for popup menu, relative to the top left-hand corner 
        of the window's contents
        
    post:
      the action (if any) required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    type_checking2_0.check_derivative(win,windowing.Window)
    type_checking2_0.check_identical(window_x,float)
    type_checking2_0.check_identical(window_y,float)
    print("mouse_popup hit")
    print("window_x=" + str(window_x))
    print("window_y=" + str(window_y))
    _m = menuing.new_menu(win)
    menuing.add_menu_item(_m,12.0,"Action 1",None)
    menuing.add_menu_item(_m,12.0,"Action 2",None)
    menuing.display(_m,win,window_x,window_y)
    
  
  def mouse_pressed(self,x,y):
    """
    pre:
      the user has pressed the primary mouse-button, signifying the start of a mouse-drag operation
      self = pane for this mouse event
      (x,y) = position in points of the mouse pointer when the mouse button was pressed, relative to the top 
        left-hand corner of the window's pane
        
    post:
      the action (if any) required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    pass
    
  
  def mouse_released(self,x,y):
    """
    pre:
      the user has released the primary mouse-button, signifying the end of a mouse-drag operation
      self = pane for this mouse event
      (x,y) = position in points of the mouse pointer when the mouse button was released, relative to the top 
        left-hand corner of the window's pane
        
    post:
      the action (if any) required by the user has been carried out
    """
    type_checking2_0.check_identical(x,float)
    type_checking2_0.check_identical(y,float)
    pass
    
    

def window_opening(win):
  """
  pre:
    the Window has just appeared on the screen
    win = Window on which the opening event occurred 
    
  post:
    client's initiation has been carried out 
  """
  print("menu_example3.window_opening")
  mousing.attach(MyMouseListener(),win)
  
  
# test program
# ------------

def _test():
  win = windowing.new_window(font_size,"Menu Example 3",800.0,600.0,1.0)
  windowing.show(win,window_opening,None)
  print("OK")
  


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

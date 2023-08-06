# Test program windowing contractor.

# author R.N.Bosworth

# version 21 Sep 22  11:24

from guibits1_0 import coloring,cursoring,font_styling
from guibits1_0 import painting,windowing,writing
"""
Copyright (C) 2020,2021,2022  R.N.Bosworth

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

def window_closing():
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("window_closing")
  return True


def window_closing2(self):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    self = WindowClosingListener on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("window_closing2")
  return True


def window_closing3(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("window_closing3")
  return 0


def window_closing4(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("window_closing4")
  if windowing.zoom_factor_of(win) == 2.0:
    print("All tests OK")
    return True
  print("Callback thread tests")
  print("set_font_size(win,6.0)")
  windowing.set_font_size(win,6.0)
  print('set_title(win,"New Title")')
  windowing.set_title(win,"New Title")
  print('set_zoom_factor(win,2.0)')
  windowing.set_zoom_factor(win,2.0)
  print("OK")
  return False
  
  
def window_closing5(win):
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
    print("Callback thread tests")
    print("set_font_size(win,6.0)")
    windowing.set_font_size(win,6.0)
    print('set_title(win,"New Title")')
    windowing.set_title(win,"New Title")
    print('set_zoom_factor(win,2.0)')
    windowing.set_zoom_factor(win,2.0)
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("attributes of _Frame once window shown")
    print("  win._my_frame.pos()="+str(win._my_frame.pos()))
    print("  win._my_frame.x()="+str(win._my_frame.x()))
    print("  win._my_frame.y()="+str(win._my_frame.y()))
    print("  win._my_frame.rect()="+str(win._my_frame.rect()))
    print("  win._my_frame.size()="+str(win._my_frame.size()))
    print("  win._my_frame.width()="+str(win._my_frame.width()))
    print("  win._my_frame.height()="+str(win._my_frame.height()))
    print("  win._my_frame.frameGeometry()="+str(win._my_frame.frameGeometry()))
    print("  win._my_frame.geometry()="+str(win._my_frame.geometry()))
    cm = win._my_frame.contentsMargins()
    top = cm.top()
    bottom = cm.bottom()
    left = cm.left()
    right = cm.right()
    print("  win._my_frame.contentsMargins()="+ \
      "top:"+str(top)+",bottom:"+str(bottom)+",left:"+str(left)+",right:"+str(right))    
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 2:
    print("Test of clear")
    fss = font_styling.new_font_styles()
    print("Text and thin cursor")
    writing.write_string(win,"This is a test string","Times New Roman",fss,12.0,36.0,72.0,coloring.BLACK)
    cursoring.draw_cursor(win,12.0,36.0,72.0,coloring.BLACK)
    input("Please enter NL:")
    windowing.clear(win)
    print("Page should be clear")
    input("Please enter NL:")
    print("Text and fat cursor")
    writing.write_string(win,"This is another test string","Times New Roman",fss,12.0,36.0,72.0,coloring.BLACK)
    painting.paint_rectangle(win,36.0,72.0,24.0,12.0,coloring.BLACK)
    input("Please enter NL:")
    windowing.clear(win)
    print("Page should be clear")
    input("Please enter NL:")
    print("OK")
    win._tnum += 1
    return False
    
  else:
    print("All tests OK")
    return True


def window_opening(self,win):
  """
  pre:
      the window has just appeared on the screen
      win = Window on which the opening event occured 
      
  post:
      client's initiation has been carried out 
  """
  print("window_opening")

def window_opening2(win):
  """
  pre:
      the window has just appeared on the screen
      win = Window on which the opening event occured 
      
  post:
      client's initiation has been carried out 
  """
  print("window_opening2")


def fred():
  pass

def fred2(a):
  pass

def fred3(b,c):
  pass

def fred4(a,c):
  pass

def fred5(a,b):
  pass

def _test():

  print("Test of _focussed_color_of",end=' ')
  c = coloring.new_color(0.1,0.2,0.3)
  fc = windowing._focussed_color_of(c,True)
  assert coloring.get_red(fc) == 0.1
  assert coloring.get_green(fc) == 0.2
  assert coloring.get_blue(fc) == 0.3
  fc = windowing._focussed_color_of(c,False)
  assert coloring.get_red(fc) == 0.55
  assert coloring.get_green(fc) == 0.6
  assert coloring.get_blue(fc) == 0.65
  print("OK")  
 
  print("Test of new_window", end=' ')
  #win = windowing.new_window(5.9,"Test Window 1",9.9,1000.1)
  #win = windowing.new_window(72.1,"Test Window 1",9.9,1000.1)
  #win = windowing.new_window(6.0,"Test Window 1",9.9,9.9)
  #win = windowing.new_window(72.0,"Test Window 1",10.0,9.9)
  #win = windowing.new_window(72.0,"Test Window 1",1000.1,9.9)
  #win = windowing.new_window(72.0,"Test Window 1",1000.0,9.9)
  #win = windowing.new_window(72.0,"Test Window 1",1000.0,1000.1)
  #win = windowing.new_window(6.0,"Test Window 1",10.0,1000.0,None)
  #win = windowing.new_window(6.0,"Test Window 1",10.0,1000.0,0.09)
  #win = windowing.new_window(6.0,"Test Window 1",10.0,1000.0,10.1)
  #win = windowing.new_window(6.0,"Test Window 1",10.0,1000.0,10.0)
  #win = windowing.new_window(6.0,"Test Window 1",10.0,1000.0,0.1)
  win = windowing.new_window(12.0,"Test Window 2",720.0,360.0,1.0)
  assert win._my_font_size == 12
  assert win._my_title == "Test Window 2"
  assert win._my_pane_width == 720.0
  assert win._my_pane_height == 360.0
  assert win._my_zoom_factor == 1.0
  assert win._my_frame == None
  print("OK")
  
  print("Test of clear", end= ' ')
  #windowing.clear(None)
  win = windowing.new_window(12.0,"Clear window",500.0,250.0,1.0)
  windowing.clear(win)
  print("OK")
    
  print("Test of set_font_size", end= ' ')
  win = windowing.new_window(12.0,"Set font size",500.0,250.0,1.0)
  #windowing.set_font_size(win,5.9)
  #windowing.set_font_size(win,73.0)
  #windowing.set_font_size(win,6.0)
  #windowing.show(win,None)
  #windowing.set_font_size(win,72.0)
  #windowing.show(win,None)
  #windowing.set_font_size(win,10.0)
  #windowing.show(win,None)
  #windowing.set_font_size(win,20.0)
  #windowing.show(win,None)
  print("OK")
  
  print("Test of set_title", end= ' ')
  #set_title(None,None)
  win = windowing.new_window(12.0,"Original title",500.0,250.0,1.0)
  #set_title(win,None)
  #set_title(win,"")
  #windowing.show(win,None)
  #set_title(win,"New title")
  #windowing.show(win,None)
  print("OK")
  
  print("Test of set_zoom_factor, zoom_factor_of", end= ' ')
  #windowing.set_zoom_factor(None,0.09)
  #assert windowing.zoom_factor_of(None) == 0.09
  win = windowing.new_window(12.0,"set_zoom_factor",500.0,250.0,1.0)
  #windowing.set_zoom_factor(win,0.09)
  #assert windowing.zoom_factor_of(win) == 0.09
  #windowing.set_zoom_factor(win,10.01)
  #assert windowing.zoom_factor_of(win) == 10.01
  windowing.set_zoom_factor(win,0.1)
  assert windowing.zoom_factor_of(win) == 0.1
  windowing.set_zoom_factor(win,10.0)
  assert windowing.zoom_factor_of(win) == 10.0
  windowing.set_zoom_factor(win,1.0)
  assert windowing.zoom_factor_of(win) == 1.0
  print("OK")
  
  print("Test of show")
  #windowing.show(None,23,43)
  #win = windowing.new_window(18.0,"show window",720.0,360.0,1.0)
  #windowing.show(win,23,43)
  win = windowing.new_window(18.0,"show window",720.0,360.0,1.0)
  #windowing.show(win,None,43)
  #windowing.show(win,None,None)
  #windowing.show(win,window_opening,window_closing)
  #windowing.show(win,window_opening2,window_closing)
  #windowing.show(win,window_opening2,window_closing2)
  #windowing.show(win,window_opening2,window_closing3)
  #windowing.show(win,window_opening2,window_closing4)
  win._tnum = 0
  windowing.show(win,window_opening2,window_closing5)
  print("OK")

  
if __name__ == "__main__":
  print("Main thread tests")
  import sys
  _test()
  print("All tests OK")

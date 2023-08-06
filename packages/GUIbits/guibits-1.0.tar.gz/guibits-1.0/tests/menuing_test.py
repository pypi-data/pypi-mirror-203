# tests of menu contractor

# version 28 Jul 22  20:14

# author RNB

import PyQt6.QtWidgets
import PyQt6.QtCore

from guibits1_0 import menuing, qapp_creating, windowing

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

# test program
# ------------

def _menu_item_hit(win,x,y,l):
  print("_menu_item_hit for horace")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)

def _menu_item_hit2(won,x,y,l):
  pass

def _menu_item_hit3(win,x,y,l):
  print("_menu_item_hit for ermintrude")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit4(win,y,x,l):
  print("_menu_item_hit for ermintrude")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit5(win,x,z,l):
  print("_menu_item_hit for ermintrude")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit6(win,x,y,l):
  print("_menu_item_hit for My Menu")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  #menuing.add_menu_item(None,20.0,"Item 1",_menu_item_hit7)
  #menuing.add_menu_item(m,5.9,"Item 1",_menu_item_hit7)
  #menuing.add_menu_item(m,10.0,None,_menu_item_hit7)
  #menuing.add_menu_item(m,10.0,"",_menu_item_hit7)
  #menuing.add_menu_item(m,10.0,"Item 1",None)
  #menuing.add_menu_item(m,10.0,"Item 1",_menu_item_hit2) # (won,x,y)
  #menuing.add_menu_item(m,10.0,"Item 1",_menu_item_hit4)  # (win,y,x)
  #menuing.add_menu_item(m,10.0,"Item 1",_menu_item_hit5)  # (win,x,z)
  #menuing.add_menu_item(m,10.0,"Item 1",None)
  #menuing.add_menu_item(m,20.0,"Item 2Item 2",None)
  menuing.add_menu_item(m,10.0,"Item 1",_menu_item_hit7)
  menuing.add_menu_item(m,20.0,"Item 2Item 2",_menu_item_hit8)
  menuing.display(m,win,x,y)
  
def _menu_item_hit7(win,x,y,l):
  print("_menu_item_hit for Item 1")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit8(win,x,y,l):
  print("_menu_item_hit for Item 2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit9(win,x,y,l):
  print("_menu_item_hit for My Menu2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,10.0,"Item 1",None)
  #menuing.add_separator(None)
  menuing.add_separator(m)
  menuing.add_menu_item(m,20.0,"Item 2Item 2",_menu_item_hit8)
  menuing.display(m,win,x,y)
  
def _menu_item_hit10(win,x,y,l):
  print("_menu_item_hit10")
  print("_menu_item_hit for Menu Level 1")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  print("  made new menu")
  menuing.add_menu_item(m,12.0,"Level 1, Item 1",None)
  menuing.add_menu_item(m,12.0,"Level 1, Item 2",_menu_item_hit11)
  print("  items added")
  r = menuing.display(m,win,x,y)
  print("  return from menu display")
  print("  r="+str(r))
  print("OK")
  
def _menu_item_hit11(win,x,y,l):
  print("_menu_item_hit for Level 1, Item 2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,12.0,"Level 2, Item 1",None)
  menuing.add_menu_item(m,12.0,"Level 2, Item 2",_menu_item_hit12)
  r = menuing.display(m,win,x,y)
  print("  return from menu display")
  print("  r="+str(r))
  print("OK")
  
  
def _menu_item_hit12(win,x,y,l):
  print("_menu_item_hit for Level 2, Item 2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,12.0,"Level 3, Item 1",None)
  menuing.add_menu_item(m,12.0,"Level 3, Item 2",_menu_item_hit13)
  r = menuing.display(m,win,x,y)
  print("  return from menu display")
  print("  r="+str(r))
  print("OK")
  
def _menu_item_hit13(win,x,y,l):
  print("_menu_item_hit for Level 3, Item 2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  
def _menu_item_hit14(win,x,y,l):
  print("_menu_item_hit for Menu 2 Level 1")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,12.0,"Menu 2 Level 2, Item 1",None)
  menuing.add_menu_item(m,12.0,"Menu 2 Level 2, Item 2",_menu_item_hit15)
  r = menuing.display(m,win,x,y)
  print("  return from menu display")
  print("  r="+str(r))
  print("OK")
  
def _menu_item_hit15(win,x,y,l):
  print("_menu_item_hit for Menu 2 Level 2, Item 2")
  print("  x="+str(x))
  print("  y="+str(y))
  print("  l="+l)
  print("OK")
  
def window_closing(win):
  print("window_closing")
  print("  win._tnum= "+str(win._tnum))
  if win._tnum == 0:
    menuing._clear_menus(win)
    assert menuing._has_active(win) == False
    print("  Test 0 OK")
    win._tnum += 1
    return False
  if win._tnum == 1:
    win._tnum += 1
    m = menuing.new_menu(win)
    r = menuing.display(m,win,72.0,72.0)
    assert menuing._has_active(win) == False
    assert menuing._am_active(win,m) == False
    print("  r="+str(r))
    if r == menuing.MenuReply.ABORT:
      return True
    assert r == menuing.MenuReply.NORMAL
    print("  just before creating m2")
    m2 = menuing.new_menu(win)
    print("  just before displaying m2")
    r = menuing.display(m2,win,144.0,144.0)
    print("  r="+str(r))
    if r == menuing.MenuReply.ABORT:
      return True
    assert r == menuing.MenuReply.NORMAL
    assert menuing._has_active(win) == False
    assert menuing._am_active(win,m) == False
    assert menuing._am_active(win,m2) == False
    menuing._clear_menus(win)
    assert menuing._has_active(win) == False
    print("  Test 1 OK")
    return False
  else:
    print("All tests OK")
    return True
    
def window_closing2(win):
  if win._tnum == 0:
    m = menuing.new_menu(win)
    #menuing.display(m,None,0,0)
    #menuing.display(m,win,0,0)
    #menuing.display(m,win,0.0,0)
    menuing.add_menu_item(m,12.0,"Test menu",None)
    r = menuing.display(m,win,0.0,0.0)
    print("  r="+str(r))
    win._tnum += 1
    if r == menuing.MenuReply.ABORT:
      return True
    else:
      return False
  else:
    print("All tests OK")
    return True
    
def window_closing3(win):
  if win._tnum ==0:
    menu = menuing.new_menu(win)
    print("  menu="+str(menu))
    print("  menu._my_qmenu.windowModality()="+str(menu._my_qmenu.windowModality()))
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True
    

def window_closing4(win):
  print("All tests OK")
  return True
    

def window_closing5(win):
  assert menuing._has_active(win) == False
  m = menuing.new_menu(win)
  assert menuing._am_active(win,m) == False
  menuing._set_active(win,m)
  assert menuing._has_active(win) == True
  assert menuing._am_active(win,m) == True
  #menuing._set_active(win,m)
  m2 = menuing.new_menu(win)
  menuing._set_active(win,m2)
  assert menuing._has_active(win) == True
  assert menuing._am_active(win,m) == False
  assert menuing._am_active(win,m2) == True
  menuing._set_inactive(win)
  assert menuing._has_active(win) == True
  assert menuing._am_active(win,m) == True
  menuing._set_inactive(win)
  assert menuing._has_active(win) == False
  print("OK")
  return True
    

def window_closing6(win):
  if win._tnum == 0:
    menuing.set_menu_bar_font_size(win,24.0)
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True
    
    
class TestLayout1223(PyQt6.QtWidgets.QLayout):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(12,23)


class TestSpacerItem3445(PyQt6.QtWidgets.QSpacerItem):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(34,45)


class TestWidget3344(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(33,44)


def _test():
  """
  print("Test of _am_active,_has_active, _set_active, _set_inactive", end=' ')
  win = windowing.new_window(12.0,"Test of active menus",720.0,360.0,1.0)
  windowing.show(win,None,window_closing5)
  
  print("Test of _clear_menus")
  win = windowing.new_window(18.0,"show window",720.0,360.0,1.0)
  win._tnum = 0
  windowing.show(win,None,window_closing)
  
  print("Test of instantiating a QWidget",end=' ')
  _qapp = qapp_creating._get_qapp()
  qw = PyQt6.QtWidgets.QWidget()
  assert qw.layout() == None
  print("OK")

  print("Test of add_menu_bar_item")
  win = windowing.new_window(18.0,"Test of menu bar",800.0,600.0,1.0)
  #windowing.show(win,None,None)
  #menuing.add_menu_bar_item(None,20.0,"horace",_menu_item_hit)
  #menuing.add_menu_bar_item(win,5.9,"horace",_menu_item_hit)
  #menuing.add_menu_bar_item(win,10.0,None,_menu_item_hit)
  #menuing.add_menu_bar_item(win,10.0,"",_menu_item_hit)
  #menuing.add_menu_bar_item(win,10.0,"horace",None)
  #menuing.add_menu_bar_item(win,10.0,"horace",_menu_item_hit2)  # (won,x,y)
  #menuing.add_menu_bar_item(win,10.0,"horace",_menu_item_hit4)  # (win,y,x)
  #menuing.add_menu_bar_item(win,10.0,"horace",_menu_item_hit5)  # (win,x,z)
  menuing.add_menu_bar_item(win,10.0,"horace",_menu_item_hit)
  menuing.add_menu_bar_item(win,20.0,"ermintrude",_menu_item_hit3)
  windowing.show(win,None,None)

  print("Test of set_menu_bar_font_size")
  win = windowing.new_window(18.0,"Test of set_menu_bar_font_size",800.0,600.0,1.0)
  #menuing.set_menu_bar_font_size(None,None)
  #menuing.set_menu_bar_font_size(win,None)
  #menuing.set_menu_bar_font_size(win,5.0)
  #menuing.set_menu_bar_font_size(win,25.0)
  menuing.add_menu_bar_item(win,10.0,"horace",_menu_item_hit)
  menuing.add_menu_bar_item(win,20.0,"ermintrude",_menu_item_hit3)
  menuing.set_menu_bar_font_size(win,6.0)
  win._tnum = 0
  windowing.show(win,None,window_closing6)
  
  print("Test of new_menu")
  #menu = menuing.new_menu(None)
  win = windowing.new_window(18.0,"Test of new_menu",800.0,600.0,1.0)
  #menu = menuing.new_menu(win)
  win._tnum = 0
  windowing.show(win,None,window_closing3)

  print("Test of add_menu_item")
  win = windowing.new_window(18.0,"Test of add_menu_item",800.0,600.0,1.0)
  menuing.add_menu_bar_item(win,12.0,"My Menu",_menu_item_hit6)
  win._tnum = 0
  windowing.show(win,None,window_closing4)

  print("Test of add_separator")
  win = windowing.new_window(18.0,"Test of add_separator",800.0,600.0,1.0)
  menuing.add_menu_bar_item(win,12.0,"My Menu2",_menu_item_hit9)
  windowing.show(win,None,window_closing4)
  
  print("Test of display")
  #menuing.display(None,None,0,0)
  win = windowing.new_window(18.0,"Test of display",800.0,600.0,1.0)
  #m = menuing.new_menu(win)
  win._tnum = 0
  windowing.show(win,None,window_closing2)  
  """
  print("Test of menu tree")
  win = windowing.new_window(18.0,"Test of menu tree",800.0,600.0,1.0)
  menuing.add_menu_bar_item(win,12.0,"Menu Level 1",_menu_item_hit10)
  menuing.add_menu_bar_item(win,12.0,"Menu 2 Level 1",_menu_item_hit14)
  windowing.show(win,None,window_closing4)


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

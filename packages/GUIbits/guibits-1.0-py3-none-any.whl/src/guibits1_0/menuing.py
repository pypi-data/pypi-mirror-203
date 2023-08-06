"""
Note: this version uses a list of menus attached to the window to determine the currently active menu.  This mechanism does not work 100%, probably because the list becomes out-of-kilter with the actual situation, resulting in non-responsive menu-bar buttons.
"""

# contractor for menus

# version 29 Jul 22  15:17

# author RNB

import PyQt6.QtCore
import PyQt6.QtWidgets
from enum import Enum
from . import callback_checking1_0, font_size_checking
from . import laying_out, qapp_creating, resolving, show_checking
import threading
from . import type_checking2_0, windowing

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
# -----------------

MenuReply = Enum('MenuReply','NORMAL ABORT')

class Menu:
  _my_qmenu = None
  _my_window = None


# Exposed callback procedures
# ---------------------------

def menu_item_hit(win,x,y,l):
  """
  pre:
    menu item associated with this callback procedure has been hit by user
    win = windowing.Window where mouse-hit occurred
    x,y = x and y offsets of mouse hit from top left-hand corner of window's contents, in points as float 
    l = label of menu item hit by the user 

  post:
    action required by user has been carried out
  """
  pass


# Exposed procedures
# ------------------

def add_menu_bar_item(win,fsize,l,menu_item_hit):
  """
  pre:
    win = window to which menu bar item is to be added
    fsize = font size in points for label of menu bar item, in range 6.0..24.0, as float
    l = label of menu bar item, as Python string of at least one character
    menu_item_hit = callback procedure for this menu bar item 
    
  post:
    if win has no menu bar, one has been created
    the specified menu bar item has been appended to the menu bar of win 

  test:
    win is None
    win is valid
      menu bar with no items
      fsize = 5.9
              6.0
              10.0
        l = None
        l is empty
        l is valid
          menu_item_hit = None
          menu_item_hit(won,x,y,l)
          menu_item_hit(win,y,x,l)
          menu_item_hit(win,x,z,l)
          menu_item_hit(win,x,y,m)
          menu_item_hit(win,x,y,l)
            adding two menu bar items
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_derivative(l,str)
  if len(l) == 0:
    raise Exception("attempt to add menu bar item with empty label")
  callback_checking1_0.check_function(menu_item_hit,["win","x","y","l"])

  with win._my_lock:
    _menu = _MenuBarItem(' '+l+' ',parent=win._my_menu_bar)
    _set_font_size(_menu,fsize)
    _width = _menu.sizeHint().width()
    _menu._my_window = win
    _menu._my_callback = menu_item_hit
    win._my_menu_bar.setSizePolicy(PyQt6.QtWidgets.QSizePolicy(PyQt6.QtWidgets.QSizePolicy.Policy.Preferred, PyQt6.QtWidgets.QSizePolicy.Policy.Fixed))
    if win._my_menu_bar.layout() == None:
      win._my_menu_bar.setLayout(laying_out.LineLayout())
    win._my_menu_bar.layout().addWidget(_menu)
    

def add_menu_item(m,fsize,l,menu_item_hit):
  """
  pre:
    m = menuing.Menu to which menu item is to be added
    fsize = font size in points of menu item to be added to m, in range 6.0..24.0, as float
    l = label of menu item to be added to m, as Python string
    menu_item_hit = callback procedure for menu item to be added to m, 
                      or None if none 

  post:
    specified menu item has been appended to m
    if menu_item_hit was None, the menu item has been disabled, 
    otherwise, the user hitting the menu item will result in the callback procedure being activated
    
  test:
    m is None
    m is valid
      menu with no items
      fsize = 5.9
              6.0
              10.0
        l = None
        l is empty
        l is valid
          menu_item_hit = None
            adding two menu items
          menu_item_hit(won,x,y,l)
          menu_item_hit(win,y,x,l)
          menu_item_hit(win,x,x,l)
          menu_item_hit(win,x,y,m)
          menu_item_hit(win,x,y,l)
            adding two menu items
    
  """
  type_checking2_0.check_derivative(m,Menu)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_derivative(l,str)
  if len(l) == 0:
    raise Exception("attempt to add menu item with empty label")  
  _item =  _MenuItem(' '+l+' ',parent=m._my_qmenu)
  _set_font_size(_item,fsize)
  if menu_item_hit == None:
    _item.setDisabled(True)
    _item._my_callback = None
  else:
    callback_checking1_0.check_function(menu_item_hit,["win","x","y","l"])
    # add an enabled item with this callback 
    _item.setStyleSheet("color: black; font-weight: normal")     
    _item._my_callback = menu_item_hit
  _qwa =  PyQt6.QtWidgets.QWidgetAction(m._my_qmenu)
  _item._my_qwa = _qwa
  _qwa.setDefaultWidget(_item)
  m._my_qmenu.addAction(_qwa)
  

def add_separator(m):
  """
  pre:
    m = menuing.Menu to which separator is to be added 
  
  post:
    a horizontal separator bar has been appended to m
    
  test:
    m is not a Menu
    m is a Menu
  """
  type_checking2_0.check_derivative(m,Menu)
  qm = m._my_qmenu
  qm.addSeparator()
  
  
def display(m,win,x,y):
  """
  pre:
    m = menuing.Menu to be displayed
    win = windowing.Window within which menu is to be displayed
    win is showing on screen
    (x,y) = position in points in win at which m is to be displayed, 
              relative to the top left-hand corner of win's contents, as floats 

  post:
    m has been displayed at (x,y) relative to the top left-hand corner of win's contents
    m has been set active
    the user has responded and any callbacks requested by the user have been executed
    m has been hidden
    m has been set inactive
    if the user aborted the menu (e.g. by pressing the window close button)
      MenuReply.ABORT has been returned
    else 
      MenuReply.NORMAL has been returned
      
  note: the ABORT signal is only relevant if the display is executed from the
          window-closing callback

  test:
    m is not a Menu
    m is  a Menu
      win is not a windowing.Window
      win is a windowing.Window
        x is not a float
        x is a float
          y is not a float
          y is a float
            user presses an option
            user presses window closing
  """
  """
  pre:
    m._my_qmenu = QMenu associated with m
    
  post:
    m._my_qmenu._my_window = win
    m._my_qmenu._my_menu = m
  """
  type_checking2_0.check_derivative(m,Menu)
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(x,float)
  type_checking2_0.check_identical(y,float)
  m._my_qmenu._my_window = win
  f = win._my_frame
  pxpt = resolving.pixels_per_point(f)
  xpix = int(x * pxpt)
  ypix = int(y * pxpt)
  m._my_qmenu.setParent(f)
  _set_active(win,m)
  m._my_qmenu._my_menu = m
  win._menu_waiting = True
  qac = m._my_qmenu.exec(PyQt6.QtCore.QPoint(xpix,ypix))
  # display synchronously (will not return until menu hidden)
  # Note: there is an apparent error in PyQt6 such that the window closing button
  #       is not disabled while the menu is being shown.
  #       Hitting the window closing button hangs the system.
  _set_inactive(win)
  if win._menu_waiting:  # user has aborted
    return MenuReply.ABORT
  else:
    return MenuReply.NORMAL
  

def new_menu(win):
  """
  pre:
    win = windowing.Window for which this menu is being created
    win has been created and shown on screen

  post:
    a new menuing.Menu has been returned
    
  test:
    win = None
    win = valid window, not shown
    win = valid window, showing
  """
  """
  post:
    new_menu()._my_qmenu = a valid QMenu with autofilled background
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  show_checking.check_showing(win,"menu")
  _menu = Menu()
  _menu._my_qmenu =  PyQt6.QtWidgets.QMenu()
  _menu._my_qmenu.setAutoFillBackground(True)
  _menu._my_qmenu.setWindowModality(PyQt6.QtCore.Qt.WindowModality.ApplicationModal)

  # set up the close button
  _item =  _MenuItem("x",parent=_menu._my_qmenu)
  _item.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignRight|PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter)
  _set_font_size(_item,_DEFAULT_FONT_SIZE)
  _item._my_callback = None
  _qwa =  PyQt6.QtWidgets.QWidgetAction(_menu._my_qmenu)
  _item._my_qwa = _qwa
  _qwa.setDefaultWidget(_item)
  _menu._my_qmenu.addAction(_qwa)
  # set up a separator
  _menu._my_qmenu.addSeparator()
  return _menu
  
  
def set_menu_bar_font_size(win,fsize):
  """
  pre:
    win = windowing.Window whose menu bar's font size is to be set
    fsize = new font size in points for win's menu bar, in range 6.0..24.0, as float 

  post:
    the font size of all win's menu bar's items has been set to fsize points 

  tests:
    win = None
    win = valid window
      fsize = None
      fsize = 5.0
      fsize = 73.0
      fsize = 6.0
        menu bar with no items
        menu bar with two items of font size 10.0,20.0
      fsize = 72.0
        menu bar with two items of font size 10.0,20.0  
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  with win._my_lock:
    _layout = win._my_menu_bar.layout()
    if _layout != None:
      i = 0
      _item = _layout.itemAt(i)
      while _item != None:
        if isinstance(_item,PyQt6.QtWidgets.QWidgetItem): # only widgets need apply
          _item = _item.widget()
          _set_font_size(_item,fsize)
        i += 1
        _item = _layout.itemAt(i)


# private members
# ---------------

# private constants
# -----------------
_DEFAULT_FONT_SIZE = 18


# private procedures
# ------------------

def _am_active(win,m):
  """
  pre:
    win = windowing.Window which is to be tested
    win._menus = list of current menus, the last one being active
    m = menuing.Menu to be tested for activeness
    
  post:
    has returned True iff m was active
    
  note:
    This procedure is thread-safe
    
  test:
    no menus in list
    two menus in list
      m is first in list
      m is last in list
  """
  with win._my_lock:
    l = len(win._menus)
    if l == 0:
      return False
    else:
      return win._menus[l-1] == m
        
  
def _clear_menus(win):
  """
  pre:
    win = windowing.Window whose menus are to be cleared
    win._menus = list of current menus, the last one being active
    
  post:
    win._menus has been cleared
    the menus on the list have all been hidden
    
  note:
    This procedure is thread-safe
    
  test:
    empty menu list
    two menus in list
  """
  with win._my_lock:
    i = len(win._menus) - 1
    while i >= 0:
      win._menus[i]._my_qmenu.hide()
      del win._menus[i]
      i -= 1


def _has_active(win):
  """
  pre:
    win = windowing.Window to be tested for active menus
    win._menus = list of current menus, the last one being active
    
  post:
    has returned True iff win has active menus
    
  note:
    This procedure is thread-safe
    
  test:
    no menus
    one menu
  """
  with win._my_lock:
    ac = len(win._menus) > 0
  return ac
  
   
def _set_active(win,m):
  """
  pre:
    win = windowing.Window to be tested for active menus
    win._menus = list of current menus, the last one being active
    m = menuing.Menu to be set active
    m is not already on the list
    
  post:
    m is active (i.e. has been appended to the list)
    
  note:
    This procedure is thread-safe
    
  test:
    add menu m
      add menu m again
  """
  with win._my_lock:
    for mm in win._menus:
      if mm == m:
        raise Exception("Attempt to add duplicate entry on active menu list: m="+str(m))
    win._menus.append(m)
  
  
def _set_font_size(qw,fsize):
  """
  pre:
    qw = Qwidget whose font size is to be modified
    fsize = new font size for qw, in points, as a float
    
  post:
    qw's font size has been modified as specified
    
  test:
    once thru  
  """
  _font = qw.font()
  _font.setPointSize(int(fsize))
  qw.setFont(_font)


def _set_inactive(win):
  """
  pre:
    win = windowing.Window with active menus list
    win._menus = list of current menus, the last one being active
    
  post:
    the last menu on the list, if it exists, has been set inactive 
      (i.e. has been removed from to the list)
    
  note:
    This procedure is thread-safe
    
  test:
    once thru
  """
  with win._my_lock:
    i = len(win._menus) - 1
    if i >= 0:
      del win._menus[i]
  

# private classes
# ---------------

class _MenuBar(PyQt6.QtWidgets.QWidget):

  def set_window(self,w):
    """
    pre:
     self = this menu bar
      w = Window to be associated with this menu bar
      
    post:
      w has been associated with this menu bar
      
    test:
      once thru
    """
    self.my_window = w
  
  
class _MenuBarItem(PyQt6.QtWidgets.QLabel):

  def enterEvent(self,qme):
    """
    pre:
      self = menu on which this mouse event occurred
      qme = QMouseEvent which has just occurred
      
    post:
      if the window does not have an active menu,
        the menu's background has been modified to show that the mouse is hovering
      
    test:
      window has an active menu
      window does not have an active menu
    """
    win = self._my_window
    if not _has_active(win):
      self.setStyleSheet("background-color: lightBlue; color: black")
      
      
  def leaveEvent(self,qme):
    """
    pre:
      self = menu on which this mouse event occurred
      qme = QMouseEvent which has just occurred
      
    post:
      the menu's background has been restored to the default
      
    test:
      once thru
    """
    # restore default background
    self.setStyleSheet("color: black")


  def mousePressEvent(self,qme):
    """
    pre:
      self = _MenuBarItem on which this mouse event occurred
      qme = QMouseEvent which has just occurred
      self._my_window = windowing.Window on which this mouse press occurred
      self._my_callback = callback procedure associated with this menu
      self.parent() = _MenuBar of this _MenuBarItem
      _has_active(self._my_window) = True, iff window has an active menu
      
    post:
      if _has_active(self._my_window) = False,
        if the mouse event was a left-click,
          this _MenuItem's callback has been activated, and has returned
          _has_active(self._my_window) = False
          
      else
        _has_active(self._my_window) = True, iff this window already has an active menu
                                 
    test:
      only one menu bar item active at any one time
        right mouse hit
        left mouse hit
          multi level menu
    """
    win = self._my_window
    if not _has_active(win):
      if qme.button() == PyQt6.QtCore.Qt.MouseButton.LeftButton:
        x = qme.pos().x() + self.x() + self.parent().x()  
        # x offset relative to tlh corner of menu bar
        y = qme.pos().y() + self.parent().y()  
        # y offset relative to tlh corner of menu bar
        pxpt = resolving.pixels_per_point(self)
        xpoints = x / pxpt
        ypoints = y / pxpt
        self._my_callback(self._my_window,xpoints,ypoints,self.text()[1:-1])
        # Note: self.text() has an extra space fore and aft


class _MenuItem(PyQt6.QtWidgets.QLabel):

  def enterEvent(self,qme):
    """
    pre:
      self = _MenuItem on which this mouse event occurred
      qme = mouse event which has just occurred
      self.parent() = QMenu containing this _MenuItem
      self.parent()._my_window = windowing.Window containing this QMenu
      self.parent()._my_menu = menuing.Menu corresponding to this QMenu
      
    post:
      if the item is enabled and this menu is active,
        the menu item's background has been modified to show that the mouse is hovering
      
    test:
      self has no callback
      self has callback
        self is in active menu
        self is in inactive menu
    """
    if self.isEnabled():
      win = self.parent()._my_window
      m = self.parent()._my_menu
      if _am_active(win,m):
        self.setStyleSheet("background-color: lightBlue; color: black; font-weight: normal")


  def leaveEvent(self,qme):
    """
    pre:
      self = _MenuItem on which this mouse event occurred
      qme = mouse event which has just occurred
      
    post:
      if the item is enabled,
        the menu item's background has been restored to the default
      
    test:
      self has no callback
      self has callback
    """
    # restore default background
    if self.isEnabled():
      self.setStyleSheet("")


  def mousePressEvent(self,qme):
    """
    pre:
      self = _MenuItem on which this mouse event occurred
      qme = mouse event which has just occurred
      self.parent() = QMenu containing this _MenuItem
      self.parent()._my_window = windowing.Window containing this QMenu
      self.parent()._my_menu = menuing.Menu corresponding to this QMenu
      self._my_callback = callback procedure associated with this _MenuItem,
                            or None

    post:
      if the mouse event was a left-click,
        if this menu is the active menu
          this _MenuItem's callback has been activated, and has returned
          win._menu_waiting = False
    """
    qme.accept()  # to avoid propagation up the containment hierarchy
    if qme.button() == PyQt6.QtCore.Qt.MouseButton.LeftButton:
      win = self.parent()._my_window
      m = self.parent()._my_menu
      if _am_active(win,m):
        x = qme.pos().x() + self.parent().x()  # x offset relative to tlh corner of menu bar
        y = qme.pos().y() + self.y() + self.parent().y()  # y offset relative to tlh corner of menu bar
        pxpt = resolving.pixels_per_point(self)
        xpoints = x / pxpt
        ypoints = y / pxpt
        if self._my_callback != None:
          self._my_callback(self.parent()._my_window,xpoints,ypoints,self.text()[1:-1])
        # Note: self.text() has an extra space fore and aft
        self.parent().hide()  # to close the menu
        win._menu_waiting = False

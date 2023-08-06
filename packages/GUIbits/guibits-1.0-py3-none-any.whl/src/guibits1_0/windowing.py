"""
Note: this version uses a list of menus attached to the window to determine the currently active menu.  This mechanism does not work 100%, probably because the list becomes out-of-kilter with the actual situation, resulting in non-responsive menu-bar buttons.
"""

# Contractor for dealing with windows.

# author R.N.Bosworth

# version 31 Dec 22  13:32

import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.QtWidgets
from . import callback_checking1_0, coloring, command_listing
from . import cursoring, fonting
from . import font_size_checking, font_sizing, font_styling
from . import keyboarding, menuing, mousing
from . import qapp_creating, resolving, scrolling
import sys
import threading
import time
from . import type_checking2_0
from . import writing

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

# exposed types
# -------------

class Window:
  pass
  

def window_closing(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener
    win = Window on which the close event occured
    
  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown
  """
  pass    
    

def  window_opening(win):
  """
  pre:
      the window has just appeared on the screen
      win = Window on which the opening event occured 
      
  post:
      client's initiation has been carried out 
  """
  pass
    
    
# exposed procedures
# ------------------

def clear(win):
  """
  pre:
    win = window whose pane is to be cleared 
      
  post:
    a paint event has been queued for win's frame
    after this paint event is processed,
      win's pane is clear of text and graphics 
      
  test:
    win is null
    win is non-null
      win has no frame
      win has frame
        page has text
          page has thin cursor
          page has fat cursor
  """
  type_checking2_0.check_derivative(win,Window)
  if win == None:
    raise Exception("Attempt to clear a null window")
  with win._my_text_command_list._my_lock:
    win._my_text_command_list = command_listing.new_command_list()
  with win._my_rectangle_command_list._my_lock:
    win._my_rectangle_command_list = command_listing.new_command_list()
  _f = win._my_frame
  if _f != None:
    cursoring.wipe_cursor(win)
    _f.update()
  

def new_window(fsize,t,w,h,zf):
  """
  pre:
    fsize = point size of font used by this window,
              in range 6.0..24.0, as a float
    t = title for this window as Python str (may be empty)
    w = width of this window's pane in points,
          in range 10.0..1000.0, as a float
    h = height of this window's pane in points,
          in range 10.0..1000.0, as a float
    zf = zoom factor of this window's pane in points,
           as a float (0.10 ≤ zf ≤ 10.0)
    
  post:
    returns new Window with specified font size, title, pane size and zoom factor
    
  test:
    fsize = 6
    fsize = 5.9
    fsize = 72.1
    fsize = 72.0
    fsize = 6.0
    fsize = 12.0
      t = 43
      t = valid string
        w = None
        w = 9.9
        w = 1000.1
        w = 1000.0
        w = 10.0
          h = 9.9
          h = 1000.1
          h = 1000.0
          h = 10.0
        w = 144.0
          h = 288.0
            zf = 0.0 
            zf = 10.1 
            zf = 10.0 
            zf = 0.1    
            zf = 1.0
              window has been created by this app            
              window has not been created by this app            
  """
  """
  post:
    _my_menu_bar = a new _MenuBar (empty)
    _window_opening_called = False
    _active = False
    _active_menu = False  
    _menus is an empty list
    _menu_waiting is False
    _my_text_command_list = empty command list
    _my_rectangle_command_list = empty command list
    _my_lock = lock to access dimensions
    dimensions set up for midimized window
    the active menu mechanism has been set up
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  type_checking2_0.check_identical(w,float)
  if w < 10.0 or w > 1000.0:
    raise Exception("Window's width is not in range 10.0..1000.0. w="+str(w))
  type_checking2_0.check_identical(h,float)
  if h < 10.0 or h > 1000.0:
    raise Exception("Window's height is not in range 10.0..1000.0. h="+str(h))
  type_checking2_0.check_identical(zf,float)
  if (zf < 0.1 or zf > 10.0):
    raise Exception("Window's zoom factor is not in range 0.1..10.0. zf="+str(zf))
  
  _window = Window()
  
  # set up the app (needed before any PyQt classes can be used)
  #_window._my_app = PyQt6.QtWidgets.QApplication([])
  _window._my_app = qapp_creating._get_qapp()
  
  # set attributes of GUIbits Window
  _window._my_font_size = fsize
  _window._my_title = t
  _window._my_pane_width = w
  _window._my_pane_height = h
  _window._my_zoom_factor = zf
  _window._my_frame = None
  
  # set up the command lists (needed before rendering can be done)
  _window._my_text_command_list = command_listing.new_command_list()
  _window._my_rectangle_command_list = command_listing.new_command_list()
  
  _window._my_plus_button = None
  _window._my_equals_button = None
  _window._my_minus_button = None
  _window._my_pane = None
  _window._my_cursor = None
  
  # set up the lock (needed to access dimensions safely)
  _window._my_lock = threading.Lock()
  
  _window._my_x = _MEDIUM_X
  _window._my_y = _MEDIUM_Y
  _window._my_width = _MEDIUM_WIDTH
  _window._my_height = _MEDIUM_HEIGHT
  _window._window_opening_called = False
  
  # set up the menu bar (it will not show until items are added)
  _window._my_menu_bar = menuing._MenuBar()
  _window._my_menu_bar.set_window(_window)
  
  # set up the active menu mechanism
  _window._active = False
  _window._active_menu = False
  _window._menus = []
  _window._menu_waiting = False
  return _window
  
  
def set_font_size(win,fsize):
  """
  pre:
    win = window whose font size is to be set
    fsize = new point size of font used by this window,
              in range 6.0..24.0, as a float
    
  post:
    win's font size is fsize points
    if present, win's buttons have been set to the new font size

  test:
    win = None
          valid window
      fsize = 5.9
              6.0
             25.0
             24.0
             10.0
             20.0
  """
  type_checking2_0.check_derivative(win,Window)
  type_checking2_0.check_derivative(fsize,float)
  font_size_checking.check_window_font_size(fsize)  
  win._my_font_size = fsize
  if win._my_plus_button != None:
    _set_buttons_font_size(win)


def set_title(win,t):
  """
  pre:
    win = window whose title is to be set
    t = title for this window as Python str (may be empty)
    
  post:
    win's title is t
    
  test:
    win is None
    win is valid window
      t is None
      t is empty string
      t is non-empty string
        win's frame not present on screen
        win's frame is present on screen
  """
  type_checking2_0.check_derivative(win,Window)
  type_checking2_0.check_identical(t,str)
  win._my_title = t
  if win._my_frame != None:
    _set_frame_title(win)


def set_zoom_factor(win,d):
  """
  pre:
    win = window whose zoom factor is to be set
    d = zoom factor for win (0.10 ≤ d ≤ 10.0), as a float
    
  post:
    win's zoom factor is d
    if win's frame is visible
      a paint event has been queued on win's pane

  test:
    win is null
    win is non-null
      d = 0.09
      d = 10.01
      d = 0.1
      d = 10.0
      d = 1.0
        win's frame not present on screen
        win's frame is present on screen
  """
  type_checking2_0.check_derivative(win,Window)
  type_checking2_0.check_identical(d,float)
  if d < 0.10 or d > 10.0:
    raise Exception(" attempt to set zoom factor out of range 0.1..10.0")
  win._my_zoom_factor = d
  if win._my_pane != None:
    win._my_pane.update()
  

def show(win,wo,wc):
  """
  pre:
    win = window to be displayed on the screen
    wo = window opening callback procedure for win (may be None)
    wc = window closing callback procedure for win (may be None)
    
  post:
      Window win has been displayed maximized on the screen, 
        any window_opening procedure has been executed, 
          the user has interacted with the window, 
            the user has pressed the close button, 
              and any window_closing procedure has been executed
      The application has been terminated
      This method does not return to the client code 

  test:
    win is not valid Window
    win is valid Window
      wo is not valid window_opening procedure
      wo is None
      wo is valid window_opening procedure
        wcl is not valid window_closing procedure
        wcl is None
        wcl is valid window_closing procedure
  """
  type_checking2_0.check_identical(win,Window)
  if wo != None:
    callback_checking1_0.check_function(wo,['win'])
  win._my_wo = wo
  if wc != None:
    callback_checking1_0.check_function(wc,['win'])
  win._my_wc = wc
  # set up the Qt frame
  win._my_frame = _Frame()
  _set_frame_title(win)
  
  #print attributes of _Frame
  #print("  win._my_frame.pos()="+str(win._my_frame.pos()))
  #print("  win._my_frame.x()="+str(win._my_frame.x()))
  #print("  win._my_frame.y()="+str(win._my_frame.y()))
  #print("  win._my_frame.rect()="+str(win._my_frame.rect()))
  #print("  win._my_frame.size()="+str(win._my_frame.size()))
  #print("  win._my_frame.width()="+str(win._my_frame.width()))
  #print("  win._my_frame.height()="+str(win._my_frame.height()))
  #print("  win._my_frame.frameGeometry()="+str(win._my_frame.frameGeometry()))
  #print("  win._my_frame.geometry()="+str(win._my_frame.geometry()))
  #print("  win._my_frame.getContentsMargins()="+str(win._my_frame.getContentsMargins()))
  
  # link the frame back to the window
  win._my_frame._my_window = win
  
  # resize the frame to normalized screen size
  _pxpt = resolving.pixels_per_point(win._my_frame)
  win._my_frame.resize(int(win._my_width*_pxpt),int(win._my_height*_pxpt))
  #win._my_frame.resize(resolving.pixels_of(win._my_width,_pxpt),resolving.pixels_of(win._my_height,_pxpt))
  
  # set up the scroll area
  win._my_scroll_area = PyQt6.QtWidgets.QScrollArea(parent = win._my_frame)
  _scroll_bar_always_on = PyQt6.QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn
  win._my_scroll_area.setHorizontalScrollBarPolicy(_scroll_bar_always_on)
  win._my_scroll_area.setVerticalScrollBarPolicy(_scroll_bar_always_on)
  win._my_scroll_area.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
  
  # set up the pane widget
  win._my_pane = _PaneWidget(parent = win._my_scroll_area)
  win._my_pane.setBackgroundRole(PyQt6.QtGui.QPalette.ColorRole.Base)
  win._my_pane.setFocusPolicy(PyQt6.QtCore.Qt.FocusPolicy.StrongFocus)
  
  # link the pane widget to the Window
  win._my_pane.set_window(win)

  # make pane widget a child of the scroll area  
  win._my_scroll_area.setWidget(win._my_pane)
  
  # set up the button panel
  _button_layout = PyQt6.QtWidgets.QVBoxLayout()
  win._my_plus_button = _PlusButton("+",win._my_frame)
  win._my_equals_button = _EqualsButton("=",win._my_frame)
  win._my_minus_button = _MinusButton("-",win._my_frame)
  
  # connect buttons' clicked signal to the _clicked callback
  win._my_plus_button.clicked.connect(win._my_plus_button._clicked)
  win._my_equals_button.clicked.connect(win._my_equals_button._clicked)
  win._my_minus_button.clicked.connect(win._my_minus_button._clicked)
  
  # link the buttons to this window
  win._my_plus_button._my_window = win
  win._my_equals_button._my_window = win
  win._my_minus_button._my_window = win
  
  # make the buttons stretch vertically, not horizontally
  _size_policy = win._my_plus_button.sizePolicy()
  _size_policy.transpose()
  win._my_plus_button.setSizePolicy(_size_policy)
  win._my_equals_button.setSizePolicy(_size_policy)
  win._my_minus_button.setSizePolicy(_size_policy)
  
  # set the font size of the buttons
  _set_buttons_font_size(win)
  
  # add buttons to _button_layout
  _button_layout.addWidget(win._my_plus_button)
  _button_layout.addWidget(win._my_equals_button)
  _button_layout.addWidget(win._my_minus_button)
  
  # set up the viewer
  _viewer_layout = PyQt6.QtWidgets.QHBoxLayout()
  _viewer_layout.addLayout(_button_layout)
  _viewer_layout.addWidget(win._my_scroll_area)
  
  # set up the frame layout
  _frame_layout = PyQt6.QtWidgets.QVBoxLayout()
  _frame_layout.addWidget(win._my_menu_bar)
  _frame_layout.addLayout(_viewer_layout)
  win._my_frame.setLayout(_frame_layout)
  
  # show the frame
  win._my_frame.showMaximized()
  sys.exit(win._my_app.exec())
    

def zoom_factor_of(win):
  """
  pre:
    win = window whose current zoom factor is required
      
  post:
    win's current zoom factor has been returned (1.0 = no zoom), as a float

  test:
    win is null
    win is non-null
  """
  type_checking2_0.check_derivative(win,Window)    
  return win._my_zoom_factor


# private members
# ---------------

# private constants
# -----------------

_MEDIUM_WIDTH = 720.0
_MEDIUM_HEIGHT = 360.0
_MEDIUM_X = 72.0
_MEDIUM_Y = 72.0
_BLOCK_INCREMENT_POINTS = 100.0
_UNIT_INCREMENT_POINTS = 10.0
_ZOOM_IN = 1.1
_ZOOM_OUT = 0.909
_HALF_OPAQUE = 85   # alpha value for half-opaque


# private procedures
# ------------------

def _focussed_color_of(c,is_f):
  """
  pre:
    c = coloring.Color to be used for focussed pane
    is_f = True, iff pane is focussed
    
  post:
    returns coloring.Color required for current state of pane
    
  test:
    is_f = True
    is_f = False
  """
  if is_f:
    return c
  else:
    return coloring.new_color(0.5 + 0.5*coloring.get_red(c), \
                              0.5 + 0.5*coloring.get_green(c), \
                              0.5 + 0.5*coloring.get_blue(c))


def _newoff(oldoff,zf,vdim):
  """
  pre:
    oldoff = original offset of pane wrt viewport
    zf = zoom factor ratio for one button-press
    vdim = dimension of the viewport

  post:
    new offset of pane wrt viewport has been returned, 
      with the centre of the viewable pane in the centre of the viewport
      
  test:
    once thru
  """
  return int((1.0 - zf)*vdim/2 + zf*oldoff)


def _qcolor_of(c):
  """
  pre:
    c = coloring.Color to be converted
    
  post:
    a QColor corresponding to c has been returned
    
  test:
    once thru with non-black color
  """
  qcolor =  PyQt6.QtGui.QColor()
  qcolor.setRed(int(coloring.get_red(c)*255.0))  
  qcolor.setGreen(int(coloring.get_green(c)*255.0))
  qcolor.setBlue(int(coloring.get_blue(c)*255.0))
  return qcolor

  
def _resize_pane_widget(pw,zf,vp,sa):
  """
  pre:
    pw = _PaneWidget to be resized according to the zoom_factor
           of its associated window
    zoom factor of pw's window has been set as required
    zf = zoom factor ratio for one button press of + = or - buttons,
           as float
    vp = viewport through which pw is to be viewed
    sa = QScrollArea for the viewport
    
  post:
    pw has been resized and repositioned 
      according to the zoom factor of pw's window
    a paint event has been queued for pw
    
  test:
    once thru
  """
  _size = pw.sizeHint()
  _w = _size.width()
  _h = _size.height()
  _xoff = _newoff(pw.x(),zf,vp.width())
  _yoff = _newoff(pw.y(),zf,vp.height())
  pw.resize(_w,_h)
  pw.move(_xoff,_yoff)
  vpr = PyQt6.QtCore.QRectF(vp.geometry())
  pr = PyQt6.QtCore.QRectF(pw.geometry())
  scrolling._reconcile_scrollbars(vpr,pr,sa)
  

def _set_buttons_font_size(win):
  """
  pre:
    win = window whose buttons' font size is to be modified
    win._my_plus_button = plus button for win
    win._my_equals_button = equals button for win
    win._my_minus_button = minus button for win
    win._my_font_size = new font size for buttons
    
  post:
    buttons' labels and size have been set according to win._my_font_size
    
  test:
    once thru
  """
  # set the font size of the buttons
  font_sizing.set_font_size(win._my_plus_button,win._my_font_size)
  font_sizing.set_font_size(win._my_equals_button,win._my_font_size)
  font_sizing.set_font_size(win._my_minus_button,win._my_font_size)
  
  # set the minimum and maximum width of the button to 1.5 the font size
  _b_width = int(1.5 * int(win._my_font_size*resolving.pixels_per_point(win._my_frame)))
  win._my_plus_button.setMinimumWidth(_b_width)
  win._my_plus_button.setMaximumWidth(_b_width)
  win._my_equals_button.setMinimumWidth(_b_width)
  win._my_equals_button.setMaximumWidth(_b_width)
  win._my_minus_button.setMinimumWidth(_b_width)
  win._my_minus_button.setMaximumWidth(_b_width)


def _set_frame_title(win):
  """
  pre:
    win = window whose frame title is to be set
    win._my_frame = frame for this window
    win._my_title = title for this window as Python string (may be empty)
  
  post:
    frame has title win._my_title
    
  test:
    win._my_title is empty string
    win._my_title is non-empty string
  """
  if len(win._my_title) == 0:
    win._my_frame.setWindowTitle(" ")
  else:
    win._my_frame.setWindowTitle(win._my_title)
  
  
# private classes
# ---------------

class _EqualsButton(PyQt6.QtWidgets.QPushButton):
  def _clicked(self,b):
    """
    pre:
      self = this button
      b = true iff this button is checked
      the window associated with this button has been set
      
    post:
      the zoom factor of the associated pane has been set to 1.0,
        and a resize has been requested for the pane
    """
    win = self._my_window
    old_zf = win._my_zoom_factor
    win._my_zoom_factor = 1.0
    pw = win._my_pane
    sa = win._my_scroll_area
    vp = sa.viewport()
    _resize_pane_widget(pw,1.0/old_zf,vp,sa)
    
  
class _Frame(PyQt6.QtWidgets.QWidget):
  def changeEvent(self,ce):
    """
    pre:
      self = _Frame on which this change event has happened
      ce = QEvent which has just occurred
      self._my_window = Window associated with this _Frame
      
    post:
      
    """
    if isinstance(ce,PyQt6.QtGui.QWindowStateChangeEvent):
      if self.isMinimized():
        menuing._clear_menus(self._my_window)
        # to avoid PyQt making a mess of the menus

  def closeEvent(self,ce):
    """
    pre:
      self = _Frame on which this close event has happened
      ce = QCloseEvent which has just occurred
      self._my_window = Window associated with this _Frame
      
    post:
      if the client has specified a window closing procedure,
        the client's window_closing procedure has been called
        if window_closing returned True,
          the app has been terminated
        else
          the app continues
      else
        the cursor has been wiped
        the app has been terminated
    
    test:
      no window closing listener
      valid window closing listener
        window_closing returns true
        window_closing returns false
    """
    _window = self._my_window
    _wc = _window._my_wc
    if _wc != None:
      _result = _wc(_window)
      if type(_result) != bool:
        raise Exception("Return type of window_closing procedure is not bool")
      if _result:
        cursoring.wipe_cursor(_window)
        menuing._clear_menus(self._my_window)  # clear any menus that are showing
        ce.accept()  # i.e. terminate the app
      else:
        ce.ignore()  # i.e. do not terminate the app
    
    
  def showEvent(self,se):
    """
    pre:
      self = _Frame on which this show event has happened
      se = QShowEvent which has just occurred
      self._my_window = Window associated with this _Frame
      
    post:
      if the client has specified a window_opening procedure,
        the client's window_opening procedure has been called
      (note: the window_opening procedure will be called only once)
    
    test:
      no window_opening listener
      valid window_opening listener
    """
    _window = self._my_window
    if not _window._window_opening_called:
      _wo = _window._my_wo
      if _wo != None:
        _wo(_window)
      _window._window_opening_called = True
    

class _MinusButton(PyQt6.QtWidgets.QPushButton):
  def _clicked(self,b):
    """
    pre:
      self = this button
      b = true iff this button is checked
      the window associated with this button has been set
      
    post:
      the zoom factor of the associated pane has been reduced by _ZOOM_OUT,
        and a resize has been requested for the pane
    """
    win = self._my_window
    win._my_zoom_factor *= _ZOOM_OUT
    pw = win._my_pane
    sa = win._my_scroll_area
    vp = sa.viewport()
    _resize_pane_widget(pw,_ZOOM_OUT,vp,sa)
  

class _PaneWidget(PyQt6.QtWidgets.QWidget):
  """ The QWidget peer of the GUIbits pane"""
  def enterEvent(self,ee):
    pass


  def event(self,e):
    return PyQt6.QtWidgets.QWidget.event(self,e)
  
  
  def focusInEvent(self,e):
    """
    pre:
      self = _PaneWidget which has obtained the keyboard focus
    
    post:
       a repaint has been queued on this _PaneWidget,
         so that the pane can be re-rendered with the correct greying-out
           for the current focus-state of the pane
    
    test:
      once thru
    """
    self.update()


  def focusOutEvent(self,e):
    """
    pre:
      self = _PaneWidget which has lost the keyboard focus
    
    post:
       a repaint has been queued on this _PaneWidget,
         so that the pane can be re-rendered with the correct greying-out
           for the current focus-state of the pane
    
    test:
      once thru
    """
    self.update()


  def keyPressEvent(self,qke):
    keyboarding._keyPressEvent(self,qke)
  
    
  def mouseMoveEvent(self,qme):
    """
    pre:
      self = _paneWidget on which this mouse move event occurred
      qme = mouse move event which has just occurred
    post:
      mousing._mouseMoveEvent has been executed
      
    note:
      this is a shell method for the mousing._mouseMoveEvent procedure    
    """
    mousing._mouseMoveEvent(self,qme)


  def mousePressEvent(self,qme):
    """
    pre:
      self = _paneWidget on which this mouse press event occurred
      qme = mouse press event which has just occurred
    post:
      mousing._mousePressEvent has been executed
      
    note:
      this is a shell method for the mousing._mousePressEvent procedure    
    """
    mousing._mousePressEvent(self,qme)


  def mouseReleaseEvent(self,qme):
    """
    pre:
      self = _paneWidget on which this mouse release event occurred
      qme = mouse release event which has just occurred
    post:
      mousing._mouseReleaseEvent has been executed
      
    note:
      this is a shell method for the mousing._mouseReleaseEvent procedure    
    """
    mousing._mouseReleaseEvent(self,qme)


  def moveEvent(self,pe):
    pass


  def paintEvent(self,pe):
    """
    pre:
      self = current instance of the _PaneWidget class
      self._my_window._my_rectangle_command_list = 
        list of rectangle paint commands to be painted
      self._my_window._my_text_command_list = list of text paint commands to be painted
      self._my_window._my_zoom_factor = zoom factor to be used to paint
      self._my_window._my_cursor = cursor to be painted, or None
      pe = QPaintEvent for this callback
      
    post:
      this _PaneWidget has been painted according to the contents
        of self._my_window._my_rectangle_command_list, 
          self._my_window._my_text_command_list and self._my_window.my_cursor 
            at a zoom of self._my_window._my_zoom_factor
      
    test:
      empty rectangle command list
        empty text command list
          no cursor
      rectangle command list of at least two commands
        text command list of at least two commands
          valid cursor
    """
    start_time = time.time()
    painter = PyQt6.QtGui.QPainter(self)
    win = self._my_window
    cl = win._my_rectangle_command_list
    with cl._my_lock:
      command_listing.to_start_of_list(cl)
      pc = command_listing.next_command(cl)
      while pc != None:
        x = command_listing.x_offset_of(pc)
        y = command_listing.y_offset_of(pc)
        w = command_listing.width_of(pc)
        h = command_listing.height_of(pc)
        pxpt = resolving.pixels_per_point(self)
        qx = int(x*pxpt*win._my_zoom_factor)
        qy = int(y*pxpt*win._my_zoom_factor)
        qw = int(w*pxpt*win._my_zoom_factor)
        qh = int(h*pxpt*win._my_zoom_factor)
        col = command_listing.text_color_of(pc)
        qc = _qcolor_of(col)
        painter.fillRect(qx,qy,qw,qh,qc)
        pc = command_listing.next_command(cl)
    cl = win._my_text_command_list
    with cl._my_lock:
      command_listing.to_start_of_list(cl)
      pc = command_listing.next_command(cl)
      while pc != None:
        col = _focussed_color_of(command_listing.text_color_of(pc),self.hasFocus())
        qc = _qcolor_of(col)
        painter.setPen(qc)
        self._paint_text_scaled(pc,win._my_zoom_factor,painter)
        pc = command_listing.next_command(cl)
    cu = win._my_cursor
    if cu != None:
      with cu._my_lock:
        self._paint_cursor_scaled(cu,win._my_zoom_factor,painter)
    painter.end()
    end_time = time.time()
    #print("  pt="+str(end_time - start_time))
    
    
  def _paint_cursor_scaled(self,cursor,zf,painter):
    """
    pre:
      self = current instance of the _PaneWidget class
      cursor = _Cursor to be painted
      cursor is locked
      zf = zoom factor to be applied, as float
      painter = QPainter object to paint the text
      
    post:
      cursor has been painted scaled as specified,
        in position scaled as specified,
        on pane scaled as specified
      
    test:
      unity zoom factor
      non-unity zoom factor
        scaled width >= 0 
        scaled width < 0 
    """
    ppr = resolving.pixels_per_point(self)
    _scaled_x_offset = cursor._my_x * ppr * zf
    _scaled_y_offset = cursor._my_y * ppr * zf
    _scaled_width = cursoring._CURSOR_WIDTH * ppr * zf
    _scaled_height = cursor._my_font_size * ppr * zf
    if _scaled_width > 0:
      if cursor._is_colored:
        col = _focussed_color_of(cursor._my_color,self.hasFocus())
        qc = _qcolor_of(col)
      else:
        qc = _qcolor_of(coloring.WHITE)
      qr = PyQt6.QtCore.QRectF(_scaled_x_offset, _scaled_y_offset, _scaled_width, _scaled_height)
      painter.fillRect(qr,qc)


  def _paint_text_scaled(self,pc,zf,painter):
    """
    pre:
      self = current instance of the _PaneWidget class
      pc = PaintCommand to be painted
      zf = zoom factor to be applied, as float
      painter = QPainter object to paint the text
      painter's scale factor = 1.0
      
    post:
      text has been painted zoomed as specified,
        in position zoomed as specified,
        on pane zoomed as specified
      painter's scale factor = 1.0
      
    test:
      unity zoom factor
      non-unity zoom factor
        scaled point size > 0.0
        scaled point size <= 0.0
    """    
    point_size = command_listing.font_size_of(pc)
    baseline_y = command_listing.y_offset_of(pc) + point_size  
    # because QPainter paints on baseline

    x_zoomed = command_listing.x_offset_of(pc) * zf
    y_zoomed = baseline_y * zf
    point_size_zoomed = point_size * zf
    
    qf = fonting._qfont_of(command_listing.font_name_of(pc), \
                           writing._STANDARD_FONT_SIZE, \
                           command_listing.font_styles_of(pc))
    actual_point_size = qf.pointSize()
    
    scaling_factor = point_size_zoomed/actual_point_size
    x_scaled = x_zoomed/scaling_factor  # to compensate
    y_scaled = y_zoomed/scaling_factor  # to compensate

    if point_size_zoomed >= 1.0:
      painter.setFont(qf)
      painter.scale(scaling_factor,scaling_factor)
      # scale everything in both x and y directions
      
      pxppt = resolving.pixels_per_point(self)
      x_pix = x_scaled * pxppt
      y_pix = y_scaled * pxppt
      
      qp = PyQt6.QtCore.QPointF(x_pix,y_pix)
      painter.drawText(qp,command_listing.text_string_of(pc))
      # draw standard-size text, scaled exactly
      
      painter.resetTransform()  # return scaling factor to 1.0


  def set_window(self,w):
    """
    pre:
      self = _PaneWidget which is to be linked to w
      w = window to which self is to be linked
      
    post:
      self has been linked to w
    """
    self._my_window = w
    
    
  def sizeHint(self):
    """
    pre:
      self._my_window._my_pane_width = width of this pane in points as float
      self._my_window._my_pane_height = height of this pane in points as float
      self._my_window._my_zoom_factor = zoom factor of this pane in points as float
    post:
      size hint for this pane has been returned as a QSize in integer pixels
    test:
      Once thru with non-unity zoom factor
    """
    _my_pane_width = self._my_window._my_pane_width
    _my_pane_height = self._my_window._my_pane_height
    _my_zoom_factor = self._my_window._my_zoom_factor
    _size = PyQt6.QtCore.QSize()  
    _size.setWidth(int(resolving.pixels_per_point(self) * _my_pane_width * _my_zoom_factor))
    _size.setHeight(int(resolving.pixels_per_point(self) * _my_pane_height * _my_zoom_factor))
    return _size
    
  _my_mouse_listener = None
  _my_keyboard_callback = None
  _my_control_callback = None


class _PlusButton(PyQt6.QtWidgets.QPushButton):
  def _clicked(self,b):
    """
    pre:
      self = this button
      b = true iff this button is checked
      the window associated with this button has been set
      
    post:
      the zoom factor of the associated pane has been increased by _ZOOM_IN,
        and a resize has been requested for the pane
    """
    win = self._my_window
    win._my_zoom_factor *= _ZOOM_IN
    pw = win._my_pane
    sa = win._my_scroll_area
    vp = sa.viewport()
    _resize_pane_widget(pw,_ZOOM_IN,vp,sa)

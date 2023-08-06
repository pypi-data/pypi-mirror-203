# contractor which allows the client to write text onto the pane of the window

# version 12 Jan 23  18:48

# author RNB

import PyQt6.QtCore
import PyQt6.QtGui

from . import coloring, command_listing, fonting
from . import font_size_checking, font_styling, resolving
from . import type_checking2_0, windowing

"""
Copyright (C) 2013,2014,2015,2016,2017,2018,2020,2021,2022,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed procedures
# ------------------

def clear_text(win):
  """
  pre:
    win = window whose pane is to be cleared of text
      
  post:
    a paint event has been queued for win's frame
    after this paint event is processed,
      win's pane is clear of text
      
  test:
    win is null
    win is non-null
      win has no frame
      win has frame
        page has text
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  if win == None:
    raise Exception("Attempt to clear text from a null window")
  with win._my_text_command_list._my_lock:
    win._my_text_command_list = command_listing.new_command_list()
  p = win._my_pane
  if p != None:
    p.update()


def width_in_points_of(win,s,fname,fss,fsize):
  """
  pre:
    win = window on which s is to be written
    win must be present on the screen
    s = string to be measured, as a str
    fname = name of font for s, as a str
    fss = set of FontStyles for s (empty set implies the string should be measured plain)
    fsize = point size of font for s, in range 6.0..72.0, as a float
    
  post:
    the width of s in points, for the given window, font name, font styles and font size, has been returned as a float 

  test:
    None window
    valid window
      None text string
      valid text string
        None font name
        valid font name
          None font style
          valid font style
            None font size
            5.9 font size
            72.1 font size
            72.0 font size
              text "hello"
            6.0 font size
              text "goodbye"
            18.0 font size
              text "Thankyou"
              text "ThankyouThankyou" (should be double)
                fss is plain
                fss is bold
                fss is italic
                fss is (bold,italic)
  """
  #print("Start of width_in_points_of")
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(s,str)
  type_checking2_0.check_identical(fname,str)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_pane_font_size(fsize)
  if win._my_frame == None:
    raise Exception("attempt to find length of string for non-showing window")
  else:
    _qf = fonting._qfont_of(fname,_STANDARD_FONT_SIZE,fss)
    #_italic = font_styling.contains(fss,font_styling.FontStyle.ITALIC)
    #_qf =  PyQt6.QtGui.QFont(fname,int(fsize),italic=_italic)
    #if font_styling.contains(fss,font_styling.FontStyle.BOLD):
    #  _qf.setBold(True)
    #_qfm = PyQt6.QtGui.QFontMetrics(_qf)
    #_width = _qfm.horizontalAdvance(s)
    #print("  _width="+str(_width))
    _qfmf = PyQt6.QtGui.QFontMetricsF(_qf)
    _widthf = _qfmf.horizontalAdvance(s)
    #print("  _widthf="+str(_widthf))
    # this is the width of the standard font in pixels
    
    brf = _qfmf.boundingRect(PyQt6.QtCore.QRectF(),0,s)
    #print("  brf="+str(brf))

    _pxpt = resolving.pixels_per_point(win._my_frame)
    return (_widthf/_pxpt) * fsize/_STANDARD_FONT_SIZE
    # scale width up from standard font size


def write_string(win,s,fname,fss,fsize,x,y,c):
  """
  pre:
    win = window in which Unicode string s is to be written
    win must be present on the screen
    s = string to be written on win's pane, as a str
    fname = font name of required font for string s, as a str
    fss = set of FontStyles required for string s 
            (empty set implies the string should be rendered plain)
    fsize = required point size of font for string s, as a float
    x = horizontal offset in points of left-hand edge of s from left-hand edge of 
          win's pane, as a float
    y = vertical offset in points of top of s from top of win's pane, as a float
    c = color in which s is to be written on win's pane, 
          as a coloring.Color value
    
  post:
    the horizontal offset in points of the right-hand edge of the written string from the left-hand edge of win's pane has been returned as a float
    a paint event has been queued for win's pane
    after the paint event has been processed,
      the string s has been written to win's pane as specified

  test:
    invalid window
    valid window
      invalid text string
      valid text string
        invalid font name
        valid font name
          invalid font style
          valid font style
            invalid font size
            zero font size
            1.0 font size
              invalid x
              negative x
              zero x
                invalid y
                negative y
                zero y
                  invalid color
                    black color
            positive font size
              positive x
                positive y
                  blue color
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_derivative(s,str)
  type_checking2_0.check_derivative(fname,str)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_pane_font_size(fsize)
  type_checking2_0.check_identical(x,float)
  if x < 0.0:
    raise Exception("specified x-offset is negative")
  type_checking2_0.check_identical(y,float)
  if y < 0.0:
    raise Exception("specified y-offset is negative")
  type_checking2_0.check_derivative(c,coloring.Color)
    
  _len = width_in_points_of(win,s,fname,fss,fsize)
  _cmd = command_listing.new_text_command(s,fname,fss,fsize,x,y,_len,c)
  # update the text command list, in a synchronized fashion
  command_listing.insert(win._my_text_command_list,_cmd)
  win._my_pane.update()  # to queue a paint event
  return x + _len

# private constants
# -----------------

_STANDARD_FONT_SIZE = 24.0

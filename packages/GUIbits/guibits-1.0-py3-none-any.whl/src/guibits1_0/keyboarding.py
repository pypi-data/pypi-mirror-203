# Contractor for keyboard input.

# author R.N.Bosworth

# version 5 Aug 22  22:01

import PyQt6.QtWidgets
from . import callback_checking1_0, controlling
from . import type_checking2_0, windowing

"""
Copyright (C) 2012,2015,2016,2017,2019,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# exposed callback procedure specification
# ----------------------------------------

def character_key_hit(cp):
  """
  pre:
    cp = Unicode code point of key (combination) hit by user, as int
    
  post:
    action required by this key-hit has been carried out
  """
  pass
    

# exposed procedures
# ------------------

def attach(win,ckh):
  """
  pre:
    win = windowing.Window to which ckh is to be attached
    ckh = character_key_hit callback which is to be attached to win
    
  post:
    ckh has been attached to win, making win responsive to keyboard input
    
  test:
    win has not been shown
    win has been shown
      ckh = None
      ckh has no parameter
      ckh is valid
        check _my_keyboard_callback
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  callback_checking1_0.check_function(ckh,['cp'])
  if win._my_pane == None:
    raise Exception("Attempt to attach callback to non-showing window")
  win._my_pane._my_keyboard_callback = ckh
  

# private members
# ---------------

def _keyPressEvent(self,qke):
  """
  pre:
    self = PaneWidget on which this key press event has occurred
    qke = QKeyEvent which has occurred
    
  post:
    key press event has been passed on to 
      keyboarding callback
    or
      controlling callback
    or
      base class keyPressEvent
      
  test:
    all keys on the keyboard
      no callbacks attached
      keyboarding callback attached
      controlling callback attached
      both callbacks attached
       lowercase printable
       uppercase printable
       BACKSPACE
       DELETE
       ENTER
       UP_ARROW
       DOWN_ARROW
       LEFT_ARROW
       RIGHT_ARROW
       CTRL_S
       CTRL_Z
       CTRL_C
       CTRL_V
       other crazy combinations, such as Windows-key, Esc, F1 etc.
  """
  key_code = qke.keyCombination().toCombined()
  if 0x20 <= key_code <= 0x7E or \
     0x80 <= key_code <= 0x10FFFF:  # lower case character
    self._my_keyboard_callback(ord(qke.text()[0]))
  elif 0x02000020 <= key_code <= 0x0200007E or \
       0x02000080 <= key_code <= 0x0210FFFF:  # upper case character
    self._my_keyboard_callback(ord(qke.text()[0]))
  elif self._my_control_callback != None:
    if key_code == 0x01000003:
      self._my_control_callback(controlling.ActionCode.BACKSPACE)
    elif key_code == 0x01000007:
      self._my_control_callback(controlling.ActionCode.DELETE)
    elif key_code == 0x01000004:
      self._my_control_callback(controlling.ActionCode.ENTER)
    elif key_code == 0x01000013:  # PyQt6.Qt.Key.Key_Up
        self._my_control_callback(controlling.ActionCode.UP_ARROW)
    elif key_code == 0x01000015:  # PyQt6.Qt.Key.Key_Down
        self._my_control_callback(controlling.ActionCode.DOWN_ARROW)
    elif key_code == 0x01000012:  # PyQt6.Qt.Key.Key_Left
        self._my_control_callback(controlling.ActionCode.LEFT_ARROW)
    elif key_code == 0x01000014:  # PyQt6.Qt.Key.Key_Right
        self._my_control_callback(controlling.ActionCode.RIGHT_ARROW)
    elif key_code == 0x04000053:
         self._my_control_callback(controlling.ActionCode.CTRL_S)
    elif key_code == 0x0400005a:
         self._my_control_callback(controlling.ActionCode.CTRL_Z)
    elif key_code == 0x04000058:
         self._my_control_callback(controlling.ActionCode.CTRL_X)
    elif key_code == 0x04000043:
         self._my_control_callback(controlling.ActionCode.CTRL_C)
    elif key_code == 0x04000056:
         self._my_control_callback(controlling.ActionCode.CTRL_V)
    else:
      PyQt6.QtWidgets.QWidget.keyPressEvent(self,qke)
  else:
    PyQt6.QtWidgets.QWidget.keyPressEvent(self,qke)

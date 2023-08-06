# Contractor for GUI dialogs.

# author R.N.Bosworth

# version 30 Jul 22  18:18

import PyQt6.QtCore
import PyQt6.QtWidgets

from enum import Enum
from . import font_size_checking, font_sizing, font_styling
from . import qapp_creating, show_checking, type_checking2_0

"""
Copyright (C) 2010,2012,2015,2016,2017,2019,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# Confirm dialog
# --------------

def show_confirm_dialog(fsize,t,m):
  """
  pre:
    fsize = point size of text for dialog message, as float in range 6.0..24
    t = title of this dialog, as Python string
    m = message to be displayed inside dialog, as Python string
      
  post:
    dialog has been displayed at centre of screen, 
      and user has pressed either the Yes button, the No button, the Close button, or the Esc key
    returns True iff the user pressed the Yes button, 
      otherwise returns False.  

  test:
    fsize = None
    fsize = 24.1
    fsize = 24
      t = None
    fsize = 10
      t = ""
      t = "x"
        m = None
      t = "grenoble"
        m = ""
        m = "y"
        m = "<p>"
        m = "a very long long long string with a long long word: antidisestablishmentarianism"
          user says yes
          user says no
          user closes dialog
          user presses Esc key
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("attempt to show confirm dialog with empty title string")
  type_checking2_0.check_identical(m,str)
  if len(m) == 0:
    raise Exception("attempt to show confirm dialog with empty message string")

  # ensure QApplication object exists
  qapp = qapp_creating._get_qapp()
  
  # make a QMessageBox
  qmb = PyQt6.QtWidgets.QMessageBox()
  
  # set the font size
  font_sizing.set_font_size(qmb,fsize)
  
  # set the title 
  qmb.setWindowTitle(t)
  
  # set the text message
  qmb.setText("<center>"+escaped(m)+"</center>")
  
  yes_button = qmb.addButton("Yes",PyQt6.QtWidgets.QMessageBox.ButtonRole.YesRole)
  qmb.addButton("No",PyQt6.QtWidgets.QMessageBox.ButtonRole.NoRole)
  
  # display modally and wait
  qmb.exec()
  return (qmb.clickedButton() == yes_button)


# Input dialog
# ------------

def show_input_dialog(fsize,t,up):
  """
  pre:
    fsize = point size of text for dialog message, 
              as float in range 6.0..24.0
    t = title of this dialog, as Python string
    up = user prompt to be displayed inside dialog, as Python string
    
  post:
    dialog has been displayed at centre of screen, 
      and user has entered a text to their satisfaction, 
        and then pressed the OK button or the Close button, 
          or hit the Esc key
    Returns text (possibly empty) as Python string, 
      or None if user closed the dialog or hit the Esc key 

  tests:
    fsize = 5.9
    fsize = 6.0
      t = None
    fsize = 24.1
    fsize = 24.0
      t = ""
    fsize = 10
      t = "x"
        up = None
      t = "florestan"
        up = ""
        up = "Please enter your name:"
          user closes dialog
          user hits Esc key
          user enters nothing
          use enters valid name
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("attempt to show input dialog with empty title string")
  type_checking2_0.check_identical(up,str)
  if len(up) == 0:
    raise Exception("attempt to show input dialog with empty user prompt")
    
  # ensure QApplication object exists
  qapp = qapp_creating._get_qapp()
  
  # make a QInputDialog
  qid = PyQt6.QtWidgets.QInputDialog \
        (None, PyQt6.QtCore.Qt.WindowType.WindowSystemMenuHint | \
               PyQt6.QtCore.Qt.WindowType.WindowTitleHint | \
               PyQt6.QtCore.Qt.WindowType.WindowCloseButtonHint)
  
  # set the font size
  font_sizing.set_font_size(qid,fsize)
  
  # set the title 
  qid.setWindowTitle(t)
  
  # set the input mode to text
  qid.setInputMode(PyQt6.QtWidgets.QInputDialog.InputMode.TextInput)
  
  # set the label text (user prompt)
  qid.setLabelText(up)
  
  # display modally and wait
  result = qid.exec()
  if result == PyQt6.QtWidgets.QDialog.DialogCode.Accepted:
    return qid.textValue()
  else:
    return None
    

# Message dialog
# --------------

def show_message_dialog(fsize,t,m):
  """
  pre:
    fsize = point size of text for dialog message, as float
              in range 6.0..72.0
    t = title of this dialog, as Python string
    m = message to be displayed inside dialog, as Python string
      
  post:
    dialog has been displayed at centre of screen, 
      and acknowledged by the user   

  test:
    fsize = 5
    fsize = 5.0
    fsize = 25.0
    fsize = 6.0
      t = None
    fsize = 10
      t = ""
      t = "x"
        m = None
      t = "grenoble"
        m = ""
        m = "y"
        m = "<p>"
        m = "a very long long long string with a long long word: antidisestablishmentarianism"
          user says OK
          user closes dialog
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("attempt to show message dialog with empty title string")
  type_checking2_0.check_identical(m,str)
  if len(m) == 0:
    raise Exception("attempt to show message dialog with empty message string")
    
  # ensure QApplication object exists
  qapp = qapp_creating._get_qapp()
  
  # make a QMessageBox
  qmb = PyQt6.QtWidgets.QMessageBox()
  
  # set the font size
  font_sizing.set_font_size(qmb,fsize)
  
  # set the title 
  qmb.setWindowTitle(t)
  
  # set the text message
  qmb.setText("<center>"+escaped(m)+"</center>")
  
  # display modally and wait
  qmb.exec()


# private procedures
# ------------------

def escaped(s):
  """
  pre:
    s = str which is to be escaped
    
  post:
    an escaped version of the string has been returned, 
      using the HTML escaping conventions:
      
        <  ->  &lt;
        >  ->  &gt;
        &  ->  &amp;
      
  test:
    s = ""
    s= "the <p> tag indicates a paragraph & the <b> tag bold"
  """
  s2 = ""
  for ch in s:
    if ch =='<':
      s2 += "&lt;"
    elif ch == '>':
      s2 += "&gt;"
    elif ch == '&':
      s2 += "&amp;"
    else:
      s2 += ch
  return s2

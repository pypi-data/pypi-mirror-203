# Contractor for control key input.

# author R.N.Bosworth

# version 2 Aug 2022  14:39

from enum import Enum
from . import callback_checking1_0, type_checking2_0, windowing

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

# exposed constants
# -----------------

ActionCode = Enum('ActionCode','BACKSPACE DELETE ENTER UP_ARROW DOWN_ARROW LEFT_ARROW RIGHT_ARROW CTRL_S CTRL_X CTRL_C CTRL_V CTRL_Z')

# exposed callback procedure specification
# ----------------------------------------

def action_key_hit(ac):
  """
  pre:
    ac = action code of key (combination) hit by user
    
  post:
    action required by this key-hit has been carried out      
  """
  pass
    
  
# exposed procedures
# ------------------

def attach(win,akh):
  """
  pre:
    win = windowing.Window to which action_key_hit callback is to be attached
    akh = action_key_hit callback which is to be attached to win
    
  post:
    akh has been attached to win, making win responsive to control key input

  test:
    win has not been shown
    win has been shown
      akh = None
      akh has no parameter
      akh is valid
        check _my_keyboard_callback
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  callback_checking1_0.check_function(akh,['ac'])  
  if win._my_pane == None:
    raise Exception("Attempt to attach callback to non-showing window")
  win._my_pane._my_control_callback = akh

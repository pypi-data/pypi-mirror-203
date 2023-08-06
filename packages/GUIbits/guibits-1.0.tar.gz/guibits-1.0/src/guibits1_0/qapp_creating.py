# contractor for creating a singleton QApplication

# version 26 Jul 2022  17:44

# author RNB

import PyQt6.QtWidgets

"""
Copyright (C) 2020,2022  R.N.Bosworth

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

def _get_qapp():
  """
  pre:
    none
    
  post:
    returns the singleton instantiation of QApplication

  test:
    twice thru (check QApplication instance is the same)
  """
  """
  pre:
    global _qapp holds the singleton QApplication instance, or None
  """
  global _qapp
  if _qapp == None:
    _qapp = PyQt6.QtWidgets.QApplication([])  
  return _qapp
  
  
# private variables
# -----------------
_qapp = None

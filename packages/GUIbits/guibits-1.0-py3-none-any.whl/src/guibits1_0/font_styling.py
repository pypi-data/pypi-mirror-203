# Contractor which allows the client to describe font styles.

# author R.N.Bosworth

# version 13 Sep 2021  15:17

from . import type_checking2_0
from enum import Enum

"""
Copyright (C) 2013,2014,2015,2016,2017,2018,2020,2021  R.N.Bosworth

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

FontStyle = Enum('FontStyle','BOLD ITALIC')

class FontStyles:
  pass
  

# exposed procedures
# ------------------

def contains(fss,fs):
  """
  pre:
    fss = font style set to be tested
    fs = font style to be tested for membership of fss
    
  post:
    returns true iff fss contains fs 

  test:
    fss has no styles
      fs = BOLD
      fs = ITALIC
    fss has {BOLD}
      fs = BOLD
      fs = ITALIC
    fss has {ITALIC}
      fs = BOLD
      fs = ITALIC
    fss has {BOLD,ITALIC}
      fs = BOLD
      fs = ITALIC
  """
  type_checking2_0.check_derivative(fss,FontStyles)
  type_checking2_0.check_derivative(fs,FontStyle)
  return fs in fss._my_styles
  

def exclude(fss,fs):
  """
  pre:
    fss = font style set from which fs is to be excluded
    
  post:
    fss does not contain fs 

  test:
    fss has no styles
      exclude BOLD
      exclude ITALIC
    fss has {BOLD,ITALIC}
      exclude BOLD
      exclude ITALIC
      exclude BOLD
      exclude ITALIC
  """
  type_checking2_0.check_derivative(fss,FontStyles)
  type_checking2_0.check_derivative(fs,FontStyle)
  fss._my_styles = fss._my_styles.difference({fs})



def include(fss,fs):
  """
  pre:
    fss = font style set in which fs is to be included
    
  post:
    fss contains fs

  test:
    fss with no styles
      include BOLD
      include ITALIC
      include BOLD
      include ITALIC
  """
  type_checking2_0.check_derivative(fss,FontStyles)
  type_checking2_0.check_derivative(fs,FontStyle)
  fss._my_styles = fss._my_styles.union({fs}) 
  

def new_font_styles():
  """
  pre:
    none
    
  post:
    a new empty FontStyles set has been returned
    
  test:
    once thru
  """
  _fss = FontStyles()
  _fss._my_styles = set()
  return _fss
  
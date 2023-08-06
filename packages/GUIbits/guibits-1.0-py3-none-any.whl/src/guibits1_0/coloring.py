# contractor for colors.

"""
Colors are represented as a triple (red,green,blue) where each color coordinate is a float between 0.0 and 1.0. This format is consistent with the Python standard. The standard library module colorsys.py defines bidirectional conversions of color values between colors expressed in the RGB (Red Green Blue) color space and other coordinate systems.
"""

# version 25 Sep 2021  10:39

# author RNB

from . import type_checking2_0

"""
Copyright (C) 2020,2021  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed types
# -------------

class Color:
  pass


# exposed procedures
# ------------------

def get_blue(c):
  """
  pre:
    c = Color value whose blue coordinate is to be found
    
  post:
    blue coordinate value has been returned as a float in the range 0.0 to 1.0
    
  test:
    c is invalid Color
    c is valid Color
  """
  type_checking2_0.check_derivative(c,Color)
  return c._b


def get_green(c):
  """
  pre:
    c = Color value whose green coordinate is to be found
    
  post:
    green coordinate value has been returned as a float in the range 0.0 to 1.0
    
  test:
    c is invalid Color
    c is valid Color
  """
  type_checking2_0.check_derivative(c,Color)
  return c._g


def get_red(c):
  """
  pre:
    c = Color value whose red coordinate is to be found
    
  post:
    red coordinate value has been returned as a float in the range 0.0 to 1.0
    
  test:
    c is invalid Color
    c is valid Color
  """
  type_checking2_0.check_derivative(c,Color)
  return c._r


def new_color(r,g,b):
  """
  pre:
    r = red coordinate of color, as a float between 0.0 and 1.0
    g = green coordinate of color, as a float between 0.0 and 1.0
    b = blue coordinate of color, as a float between 0.0 and 1.0
    
  post:
    new Color value has been returned
    
  test:
    (43,44,45)
    (-0.1,44,45)
    (-0.1,-0.1,45)
    (-0.1,-0.1,-0.1)
    (1.1,-0.1,-0.1)
    (1.0,-0.1,-0.1)
    (1.0,1.1,-0.1)
    (1.0,1.0,-0.1)
    (1.0,1.0,1.1)
    (1.0,1.0,1.0)
    (0.0,0.0,0.0)
    (0.1,0.2,0.3)
  """
  type_checking2_0.check_identical(r,float)
  type_checking2_0.check_identical(g,float)
  type_checking2_0.check_identical(b,float)
  if r < 0.0 or r > 1.0:
    raise Exception("red color value is out of range: r="+str(r))
  if g < 0.0 or g > 1.0:
    raise Exception("green color value is out of range: g="+str(g))
  if b < 0.0 or b > 1.0:
    raise Exception("blue color value is out of range: b="+str(b))
  _c = Color()
  _c._r = r
  _c._g = g
  _c._b = b
  return _c


# exposed constants
# -----------------

BLACK = new_color(0.0,0.0,0.0)
WHITE = new_color(1.0,1.0,1.0)

# test of contractor for colors.

# version 27 Jul 2022  11:02

# author RNB

from guibits1_0 import coloring

"""
Copyright (C) 2021,2022  R.N.Bosworth

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

def _test():
  print("new_color", end = ' ')
  #c = coloring.new_color(43,44,45)
  #c = coloring.new_color(-0.1,44,45)
  #c = coloring.new_color(-0.1,-0.1,45)
  #c = coloring.new_color(-0.1,-0.1,-0.1)
  #c = coloring.new_color(1.1,-0.1,-0.1)
  #c = coloring.new_color(1.0,-0.1,-0.1)
  #c = coloring.new_color(1.0,1.1,-0.1)
  #c = coloring.new_color(1.0,1.0,-0.1)
  #c = coloring.new_color(1.0,1.0,1.1)
  c = coloring.new_color(1.0,1.0,1.0)
  assert c._r == 1.0
  assert c._g == 1.0
  assert c._b == 1.0
  c = coloring.new_color(0.0,0.0,0.0)
  assert c._r == 0.0
  assert c._g == 0.0
  assert c._b == 0.0
  c = coloring.new_color(0.1,0.2,0.3)
  assert c._r == 0.1
  assert c._g == 0.2
  assert c._b == 0.3
  print("OK")

  print("get_red", end= ' ')
  #coloring.get_red(None)
  c = coloring.new_color(0.5,0.6,0.7)
  assert coloring.get_red(c) == 0.5
  print("OK")

  print("get_green", end= ' ')
  #coloring.get_green(None)
  c = coloring.new_color(0.5,0.6,0.7)
  assert coloring.get_green(c) == 0.6
  print("OK")


  print("get_blue", end= ' ')
  #coloring.get_blue(None)
  c = coloring.new_color(0.5,0.6,0.7)
  assert coloring.get_blue(c) == 0.7
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

#test of contractor for checking the type of a variable

# version 26 Jul 2022  14:32

# author RNB

from guibits1_0 import type_checking2_0

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

# test program
# ------------

def _test():

  import io
  
  print("check_identical",end=' ')
  t = str
  #type_checking2_0.check_identical(None,t)
  type_checking2_0.check_identical("hello",t)
  print("OK")
  
  print("check_derivative",end=' ')
  t = io.TextIOBase
  #type_checking2_0.check_derivative(None,t)
  #type_checking2_0.check_derivative("hello",t)
  f = open("../guibits1_0/type_checking2_0.py")  # bound to exist!
  type_checking2_0.check_derivative(f,t)
  print("OK")

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

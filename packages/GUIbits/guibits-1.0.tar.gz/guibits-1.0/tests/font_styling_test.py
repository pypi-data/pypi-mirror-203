# test of font_styling contractor

# author R.N.Bosworth

# version 26 Jul 2022  14:42

from guibits1_0 import font_styling

"""
Contractor which allows the client to describe font styles.

Copyright (C) 2021,2022  R.N.Bosworth

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License (lgpl.txt) for more details.
"""

# test program
# ------------

def _test():
  print("Tests of include", end=' ')
  #font_styling.include(None,None)
  _fss = font_styling.new_font_styles()
  assert len(_fss._my_styles) == 0
  #font_styling.include(_fss,None)
  font_styling.include(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  font_styling.include(_fss,font_styling.FontStyle.ITALIC)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  font_styling.include(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  print("OK")
  
  print("Tests of exclude", end=' ')
  #font_styling.exclude(None,None)
  _fss = font_styling.new_font_styles()
  #font_styling.exclude(_fss,None)
  font_styling.exclude(_fss,font_styling.FontStyle.BOLD)
  assert len(_fss._my_styles) == 0
  font_styling.exclude(_fss,font_styling.FontStyle.ITALIC)
  assert len(_fss._my_styles) == 0
  font_styling.include(_fss,font_styling.FontStyle.BOLD)
  font_styling.include(_fss,font_styling.FontStyle.ITALIC)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  font_styling.exclude(_fss,font_styling.FontStyle.BOLD)
  assert not font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  font_styling.exclude(_fss,font_styling.FontStyle.ITALIC)
  assert not font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert not font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  print("OK")
  
  print("Tests of contains", end=' ')
  #font_styling.contains(None,None)
  _fss = font_styling.new_font_styles()
  #font_styling.contains(_fss,None)
  assert  not font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert  not font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  _fss = font_styling.new_font_styles()
  font_styling.include(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert  not font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  _fss = font_styling.new_font_styles()
  font_styling.include(_fss,font_styling.FontStyle.ITALIC)
  assert  not font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  _fss = font_styling.new_font_styles()
  font_styling.include(_fss,font_styling.FontStyle.BOLD)
  font_styling.include(_fss,font_styling.FontStyle.ITALIC)
  assert font_styling.contains(_fss,font_styling.FontStyle.BOLD)
  assert font_styling.contains(_fss,font_styling.FontStyle.ITALIC)
  print("OK")
  

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

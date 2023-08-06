# contractor to check font size

# version 13 Sep 2021  12:50

# author RNB

from . import type_checking2_0

"""
Copyright (C) 2021  R.N.Bosworth

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

def check_window_font_size(wfs):
  """
  pre:
    wfs = font size to be checked, in points as a float
    
  post:
    iff wfs was out of the range 6.0..24.00 
      an exception has been raised
  test:
    wfs = None
    wfs = 5.9
    wfs = 24.1
    wfs = 24.0
    wfs = 6.0
  """
  type_checking2_0.check_identical(wfs,float)
  if wfs < 6.0 or wfs > 24.0:
    raise Exception ("Point size of font is not in range 6.0..24.0. wfs="+str(wfs))


def check_pane_font_size(pfs):
  """
  pre:
    pfs = font size to be checked, in points as a float
    
  post:
    iff pfs was out of the range 6.0..72.00 
      an exception has been raised
  test:
    pfs = None
    pfs = 5.9
    pfs = 72.1
    pfs = 72.0
    pfs = 6.0
  """
  type_checking2_0.check_identical(pfs,float)
  if pfs < 6.0 or pfs > 72.0:
    raise Exception ("Point size of font is not in range 6.0..72.0. pfs="+str(pfs))

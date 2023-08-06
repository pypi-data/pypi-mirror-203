# test of Contractor for dealing with the resolution of pixelated devices.

import PyQt6.QtGui
import PyQt6.QtPrintSupport
import PyQt6.QtWidgets
from guibits1_0 import resolving

# author R.N.Bosworth

# version 27 Jul 2022  11:08

"""
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

  print("Tests of pixels_per_point")
  app = PyQt6.QtWidgets.QApplication(sys.argv)
  #resolving.pixels_per_point(None)
  qi = PyQt6.QtGui.QImage()
  #ppp = resolving.pixels_per_point(qi)
  qpd = PyQt6.QtPrintSupport.QPrinter()
  print("pixels_per_point(qpd)=" + str(resolving.pixels_per_point(qpd)))
  qw = PyQt6.QtWidgets.QWidget()
  print("pixels_per_point(qw)=" + str(resolving.pixels_per_point(qw)))
  print("OK")
  """
  print("Tests of pixels_of, points_of", end=' ')
  #resolving.pixels_of(True,None)
  #resolving.pixels_of(123,2)
  #resolving.pixels_of(123.0,2)
  assert resolving.pixels_of(123.0,2.0) == 246
  #resolving.points_of(True,None)
  #resolving.points_of(45.0,3)
  #resolving.points_of(45,3)
  assert resolving.points_of(45,3.0) == 15.0
  assert resolving.points_of(resolving.pixels_of(234.5,2.0),2.0) == 234.5
  print("OK")
  """
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

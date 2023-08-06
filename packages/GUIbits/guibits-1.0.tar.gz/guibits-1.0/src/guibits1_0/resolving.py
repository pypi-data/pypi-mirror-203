# Contractor for dealing with the resolution of pixelated devices.

# author R.N.Bosworth

# version 27 Jul 2022  11:06

import PyQt6.QtGui
import PyQt6.QtPrintSupport
import PyQt6.QtWidgets
from guibits1_0 import type_checking2_0
import sys

"""
Copyright (C) 2015,2016,2017,2018,2019,2021,2022  R.N.Bosworth

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

POINTS_PER_INCH = 72.0


# exposed procedures
# ------------------
  
def pixels_per_point(qpd):
  """
  pre:
    qpd = QPaintDevice whose resolution in pixels per point is to be measured
    
  post:
    pixels per point of qpd has been returned, as a float
    
  test:
    qpd = None
    qpd = PyQt6.QtGui.QImage
    qpd = PyQt6.QtGui.QPrinter
    qpd = PyQt6.QWidgets.QWidget
  """
  type_checking2_0.check_derivative(qpd,PyQt6.QtGui.QPaintDevice)
  if isinstance(qpd,PyQt6.QtWidgets.QWidget):
    dpi = qpd.screen().logicalDotsPerInch()
  elif isinstance(qpd,PyQt6.QtPrintSupport.QPrinter):
    dpi = qpd.resolution()
  else:
    raise Exception("Attempt to find resolution of object that is not a QWidget or a QPrinter")
  return dpi/POINTS_PER_INCH

# Contractor which prints documents.

# author R.N.Bosworth

# version 16 Mar 23  14:36

import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.QtPrintSupport
from . import fonting, font_size_checking, font_styling
from . import qapp_creating, resolving, type_checking2_0

"""
Copyright (C) 2016,2017,2019,2021,2022,2023  R.N.Bosworth

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

class PrintJob:
  _is_active = False

  
# internal globals
# ----------------
  
_pj = PrintJob()  # to ensure that set_page_dimensions is not called twice


# exposed procedures
# ------------------

def end_printing(p):
  """
  pre:
    p = PrintJob which is to be ended 

  post:
    the printer will be released for the use of other apps when this app's current print job has finished 

  test:
    p = None
    p = valid PrintJob
      PrintJob is active
      PrintJob is not active
  """
  type_checking2_0.check_derivative(p,PrintJob)
  if not p._is_active:
    raise Exception("Attempt to end a non-active PrintJob")
  p._painter.end()
  p._is_active = False


def print_string(p,s,fn,fss,fsize,x,y):
  """
  pre:
    p = PrintJob object for which s is to be printed
    s = text which is to be printed, as Python string
    fn = name of font to be used to print s, as Python string
    fss = set of fontstyles to be used to print s (empty set implies that s should be printed plain)
    fsize = size of font used to print s, in the range 6.0 to 72.0 points, as a float
    x = x-offset in points, from the specified page x-indent, of the top left-hand corner of rectangle in which s is to be printed, as a float
    y = y-offset in points, from the specified page y-indent, of the top left-hand corner of rectangle in which s is to be printed, as a float 

  post:
    either:
      s has or will be been printed as required
    or:
      s cannot be printed for some reason, and an Exception has been thrown 

  test:
    p = None
    p = valid PrintJob
      s = None
          ""
          "X"
        fn = None
             ""
             "a"
          fss = None
                empty list
            fsize = 5.9
                    6.0
              x = -0.1
                  0.0
            fsize = 72.1
            fsize = 72.0
                y = -0.1
        fn = "Courier New"
          fss = {}
            fsize = 72.0
              x = 0.0
                y = 0.0
                  p is inactive                
                  p is active                
      s = "Helloy"
        fn = "Courier New"
          fss = {BOLD}
            fsize = 18.0
              x = 72.0
                y = 144.0
  """
  type_checking2_0.check_derivative(p,PrintJob)
  type_checking2_0.check_identical(s,str)
  type_checking2_0.check_identical(fn,str)
  if len(fn) == 0:
    raise Exception("Attempt to print a string using an empty font name")
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_pane_font_size(fsize)
  type_checking2_0.check_identical(x,float)
  if x < 0.0:
    raise Exception("Specified x-offset is negative")
  type_checking2_0.check_identical(y,float)
  if y < 0.0:
    raise Exception("Specified y-offset is negative")
    
  # check the PrintJob is active
  if not p._is_active:
    raise Exception("Attempt to print string on inactive PrintJob")  
  # set the font
  qf = fonting._qfont_of(fn,fsize,fss)
  p._painter.setFont(qf)
  
  # draw the string
  qfm = p._painter.fontMetrics()

  pxpt = resolving.pixels_per_point(p._printer)
  x_in_dots = int(x * pxpt)
  y_in_dots = int(y * pxpt)
  baseline_y = y_in_dots + qfm.ascent()
  p._painter.drawText(x_in_dots,baseline_y,s)
  
  
def set_page_dimensions(w,h,ind):
  """
  pre:
    w = required width in points of printed page (50 ≤ w ≤ 1000), as a float
    h = required height in points of printed page (50 ≤ h ≤ 1000), as a float
    ind = required indent in points at top, bottom, lhs and rhs of printed page (10 ≤ ind ≤ 200), as a float 
  
  post:
    either:
      the required page dimensions have been set up and the print job 
        has been started
      a PrintJob object has been returned 
    or:
      the actual printer page is not large enough to accept the 
        specified page
      None has been returned
    or:
      the print job could not be started
      None has been returned      

  test:
    w = None
    w = 49.9
    w = 50.0
      h = None
      h = 49.9
      h = 50.0
        ind = None
        ind = 9.9
        ind = 10.0
          check returned PrintJob
    w = 1000.1
    w = 1000.0
      h = 1000.1
      h = 1000.0
        ind = 200.1
        ind = 200.0
    w = 595.1
    w = 595.0
      h = 842.1
      h = 842.0
        ind = 72.0
          printer is inactive
            check returned PrintJob
          printer is active
            check returned PrintJob
    calling set_page_dimensions twice in succession
  """
  type_checking2_0.check_identical(w,float)
  if w < 50.0 or w > 1000.0:
    raise Exception("specified page width not in range 50..1000 points. w = " + str(w))
  type_checking2_0.check_identical(h,float)
  if h < 50.0 or h > 1000.0:
    raise Exception("specified page height not in range 50..1000 points. h = " + str(h))
  type_checking2_0.check_identical(ind,float)
  if ind < 10.0 or ind > 200.0:
    raise Exception("specified page indent not in range 10..200 points. ind = " + str(ind))
    
  global _pj 
  # to ensure that failure by the client to preserve the PrintJob
  # does not give a Qt error
  if _pj._is_active:
    raise Exception("Attempt to start print job when one is already active")
    _pj._painter.end()
    _pj._is_active = False
    return None
  _pj = PrintJob()
  _pj._page_width = w
  _pj._page_height = h
  _pj._page_indent = ind
  
  qapp = qapp_creating._get_qapp()
  _pj._printer = PyQt6.QtPrintSupport.QPrinter()
  page_layout = _pj._printer.pageLayout()
  p_size = page_layout.pageSize()
  rect_points = p_size.rectPoints()
  if _pj._page_width > float(rect_points.width()) or \
     _pj._page_height > float(rect_points.height()):  
   _pj._is_active = False
   return None
  else:
    # set the page size
    point_size = PyQt6.QtCore.QSizeF(w,h)
    new_page_size = PyQt6.QtGui.QPageSize(point_size,PyQt6.QtGui.QPageSize.Unit.Point)
    page_size_set = _pj._printer.setPageSize(new_page_size)
    
    # set the margins
    qtm = PyQt6.QtCore.QMarginsF(ind,ind,ind,ind)
    margins_ok = _pj._printer.setPageMargins(qtm,units=PyQt6.QtGui.QPageLayout.Unit.Point)
    if not margins_ok:
      _pj._is_active = False
      return None
    page_layout = _pj._printer.pageLayout()
    margins = page_layout.marginsPoints()
    
    # start the print job, grabbing the printer
    _pj._painter = PyQt6.QtGui.QPainter()
    _pj._is_active = _pj._painter.begin(_pj._printer)
    if not _pj._is_active:
     _pj._painter.end()
     return None
    else:
      return _pj
  

def throw_page(p):
  """
  pre:
    p = PrintJob object whose current page is to be thrown 

  post:
    The current page has been or will be thrown from p

  test
    p = None
    p is valid PrintJob
      p is inactive
      p is active
        page throw succeeds
        page throw fails
  """
  type_checking2_0.check_derivative(p,PrintJob)
  if not p._is_active:
    raise Exception("Attempt to throw page on a non-active PrintJob")
  success = p._printer.newPage()
  if not success:
    raise Exception("Attempt to throw page was unsuccessful")

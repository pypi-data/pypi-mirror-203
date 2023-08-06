# contractor for reconciling scrollbars

# version 28 Jul 22  19:52

# author RNB

import PyQt6.QtCore
import PyQt6.QtWidgets
from . import type_checking2_0, windowing

"""
Copyright (C) 2020, 2021  R.N.Bosworth

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

def _reconcile_scrollbars(vpr,pr,sa):
  """
  pre:
    vpr = viewport rectangle for scroll area whose scrollbars are to be modified,
            as QRectF
    pr = pane rectangle whose dimensions and position are to be used to modify scrollbars,
           as QRectF
    sa = scroll area whose scrollbars are to be reconciled with pr
            
  post:
    sa's scrollbars have been reconciled with the dimensions and position 
      of its pane
      
  test:
    vpr = None
    vpr = (0.0,0.0,10.0,5.0)
      pr = None
      pr = (0.0,0.0,10.0,10.0)
        sa = None
        sa = PyQt6.QtWidgets.QScrollArea
      pr = (-5.0,-5.0,20.0,10.0)
  """
  type_checking2_0.check_derivative(vpr,PyQt6.QtCore.QRectF)
  type_checking2_0.check_derivative(pr,PyQt6.QtCore.QRectF)
  type_checking2_0.check_derivative(sa,PyQt6.QtWidgets.QScrollArea)
  # find required length and offset of horizontal scrollbar
  hslen = vpr.width()/pr.width()
  hsoff = -pr.x()/pr.width()
  
  # find required length and position of vertical scrollbar
  vslen = vpr.height()/pr.height()
  vsoff = -pr.y()/pr.height()
  
  # set the horizontal scrollbar
  _set_scrollbar(sa.horizontalScrollBar(),hslen,hsoff)
    
  # set the vertical scrollbar
  _set_scrollbar(sa.verticalScrollBar(),vslen,vsoff)
  
  
# private members
# ---------------

def _set_scrollbar(sb,len,off):
  """     
  pre:
    sb = PyQt6.QtWidgets.QScrollBar to be updated
    len = length of slider as proportion of scrollbar (0.0..1.0), as float
    off = offset of slider as proportion of scrollbar (0.0..1.0) as float
     
  post:
    sb's slider has been set to the required length and offset
  
  test:
    len = 0.5
      off = 0.25
  """    
  # find scrollbar length, and size and position of slider
  scrollbar_length = float(sb.maximum() + sb.pageStep())
  slider_length = float(sb.pageStep())
  slider_position = float(sb.sliderPosition())
  
  # keep scrollbar length the same, and modify slider length and position
  new_slider_length = len * scrollbar_length
  new_slider_position = off * scrollbar_length
  sb.setPageStep(int(new_slider_length + 0.5))
  sb.setMaximum(int(scrollbar_length) - int(new_slider_length + 0.5))
  sb.setSliderPosition(int(new_slider_position + 0.5))

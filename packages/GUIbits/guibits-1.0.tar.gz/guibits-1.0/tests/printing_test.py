# Test of contractor which prints documents.

# author R.N.Bosworth

# version 16 Mar 23  14:42

from guibits1_0 import printing, font_styling
"""
Copyright (C) 2021,2022,2023  R.N.Bosworth

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

  print("Tests of set_page_dimensions")
  #printing.set_page_dimensions(None,49.9,9.9)
  #printing.set_page_dimensions(49.9,49.9,9.9)
  #printing.set_page_dimensions(50.0,None,9.9)
  #printing.set_page_dimensions(50.0,49.9,9.9)
  #printing.set_page_dimensions(50.0,50.0,None)
  #printing.set_page_dimensions(50.0,50.0,9.9)
  #pj = printing.set_page_dimensions(50.0,50.0,10.0)
  #assert pj._page_width == 50.0
  #assert pj._page_height == 50.0
  #assert pj._page_indent == 10.0
  #printing.set_page_dimensions(1000.1,1000.1,200.1)
  #printing.set_page_dimensions(1000.0,1000.1,200.1)
  #printing.set_page_dimensions(1000.0,1000.0,200.1)
  #printing.set_page_dimensions(1000.0,1000.0,200.0)
  #printing.end_printing()
  pj = printing.set_page_dimensions(1000.0,1000.0,200.0)
  assert pj == None
  pj = printing.set_page_dimensions(595.1,842.1,72.0)
  assert pj == None
  pj = printing.set_page_dimensions(595.0,842.1,72.0)
  assert pj == None
  pj = printing.set_page_dimensions(595.1,842.0,72.0)
  assert pj == None
  pj = printing.set_page_dimensions(595.0,842.0,72.0)
  assert pj._page_width == 595.0
  assert pj._page_height == 842.0
  assert pj._page_indent == 72.0
  assert pj._printer != None
  assert pj._painter != None
  assert pj._is_active
  assert pj._printer.pageLayout().pageSize().sizePoints().width() == 595
  assert pj._printer.pageLayout().pageSize().sizePoints().height() == 842
  assert pj._printer.pageLayout().marginsPoints().top() == 72
  printing.end_printing(pj)
  input("Please set the printer inactive and press Enter")
  pj = printing.set_page_dimensions(595.0,842.0,72.0)  # should give unable to start job
  assert pj == None
  input ("Please set printer active again")
  pj = printing.set_page_dimensions(595.0,842.0,72.0)
  #print("attempting to set page dimensions twice")
  #pj = printing.set_page_dimensions(595.0,842.0,72.0)  # should give print job already active
  printing.end_printing(pj)
  print("OK")

  print("Tests of end_printing", end=' ')
  #printing.end_printing(None)
  p = printing.set_page_dimensions(50.0,50.0,10.0)
  printing.end_printing(p)
  #printing.end_printing(p)
  print("OK")

  print("Tests of print_string", end=' ')
  fss0 = font_styling.new_font_styles()
  fss1 = font_styling.new_font_styles()
  font_styling.include(fss1,font_styling.FontStyle.BOLD)
  pj = printing.set_page_dimensions(595.0,842.0,72.0)
  if pj == None:
    raise Exception("print job could not be started")
  #printing.print_string(None,None,None,None,None,None,None)
  #printing.print_string(pj,None,None,None,None,None,None)
  #printing.print_string(pj,"",None,None,0.0,-0.1,-0.1)
  #printing.print_string(pj,"X",None,None,0.0,-0.1,-0.1)
  #printing.print_string(pj,"X","",None,0.0,-0.1,-0.1)
  #printing.print_string(pj,"X","a",None,0.0,-0.1,-0.1)
  #printing.print_string(pj,"X","a",fss0,0.0,-0.1,-0.1)
  #printing.print_string(pj,"X","a",fss0,5.9,-0.1,-0.1)
  #printing.print_string(pj,"X","a",fss0,6.0,-0.1,-0.1)
  #printing.print_string(pj,"X","a",fss0,72.1,-0.1,-0.1)
  #printing.print_string(pj,"X","a",fss0,72.0,0.0,-0.1)
  printing.print_string(pj,"Xy","Courier New",fss0,72.0,0.0,0.0)
  printing.end_printing(pj)
  #printing.print_string(pj,"Z","Courier New",fss0,72.0,0.0,0.0)
  pj = printing.set_page_dimensions(595.0,842.0,72.0)
  if pj == None:
    raise Exception("  print job could not be started")
  printing.print_string(pj,"Helloy","Courier New",fss1,18.0,72.0,144.0)
  printing.end_printing(pj)
  print("OK")

  print("Tests of throw_page", end=' ')
  #printing.throw_page(None)
  pj = printing.set_page_dimensions(595.0,842.0,72.0)
  if pj == None:
    raise Exception("print job could not be started")
  fss0 = font_styling.new_font_styles()
  printing.print_string(pj,"Page 1","Courier New",fss0,72.0,0.0,0.0)
  printing.throw_page(pj)
  printing.print_string(pj,"Page 2","Courier New",fss0,72.0,0.0,0.0)
  printing.throw_page(pj)
  printing.print_string(pj,"Page 3","Courier New",fss0,72.0,0.0,0.0)
  printing.end_printing(pj)  
  #printing.throw_page(pj)
  print("OK")
  

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

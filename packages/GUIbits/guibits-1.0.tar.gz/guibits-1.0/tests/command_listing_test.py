"""
Test of Contractor for listing paint commands.
"""

# author R.N.Bosworth

# version 25 Aug 2022  10:02

from guibits1_0 import coloring, command_listing, font_styling
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
  print("Tests of new_text_command, projection functions", end=' ')
  _fss = font_styling.new_font_styles()
  #_pc = command_listing.new_text_command(None,None,None,None,None,None,None,None)
  #_pc = command_listing.new_text_command("test command",None,None,None,None,None,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",None,None,None,None,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,None,None,None,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,None,None,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,123.0,None,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,123.0,456.0,None,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,123.0,456.0,789.0,None)
  #_pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,123.0,456.0,789.0,coloring.new_color(0.0,0.0,43.0))
  _pc = command_listing.new_text_command("test command","Times New Roman",_fss,24.0,123.0,456.0,789.0,coloring.new_color(0.0,0.0,0.0))
  assert command_listing.text_string_of(_pc) == "test command"
  assert command_listing.font_name_of(_pc) == "Times New Roman"
  assert command_listing.font_styles_of(_pc) == _fss
  assert command_listing.font_size_of(_pc) == 24.0
  assert command_listing.x_offset_of(_pc) == 123.0
  assert command_listing.y_offset_of(_pc) == 456.0
  c = command_listing.text_color_of(_pc)
  assert coloring.get_red(c) == 0.0
  assert coloring.get_green(c) == 0.0
  assert coloring.get_blue(c) == 0.0
  print("OK")
  
  print("Tests of new_rectangle_command, projection functions", end=' ')
  #_pc = command_listing.new_rectangle_command(None,None,None,None,None)
  #_pc = command_listing.new_rectangle_command(1.0,None,None,None,None)
  #_pc = command_listing.new_rectangle_command(1.0,2.0,None,None,None)
  #_pc = command_listing.new_rectangle_command(1.0,2.0,3.0,None,None)
  #_pc = command_listing.new_rectangle_command(1.0,2.0,3.0,4.0,None)
  _pc = command_listing.new_rectangle_command(1.0,2.0,3.0,4.0,coloring.BLACK)
  assert command_listing.width_of(_pc) == 3.0
  assert command_listing.height_of(_pc) == 4.0
  assert command_listing.x_offset_of(_pc) == 1.0
  assert command_listing.y_offset_of(_pc) == 2.0
  c = command_listing.rectangle_color_of(_pc)
  assert coloring.get_red(c) == 0.0
  assert coloring.get_green(c) == 0.0
  assert coloring.get_blue(c) == 0.0
  #assert command_listing.text_string_of(_pc) == "test command"
  print("OK")
  
  print("Tests of new_command_list, next_command", end=' ')
  _cl = command_listing.new_command_list()
  assert command_listing.next_command(_cl) == None
  print("OK")
    
  print("Tests of _is_overpainted_by", end=' ')
  pc1 = command_listing.PaintCommand()
  pc1._text_string = "pc1"
  pc1._x_offset = 1.0
  pc1._y_offset = 2.0
  pc1._width = 3.0
  pc1._height = 4.0
  pc2 = command_listing.PaintCommand()
  pc2._text_string = "pc2"
  pc2._x_offset = 1.0
  pc2._y_offset = 2.0
  pc2._width = 3.0
  pc2._height = 4.0
  assert command_listing._is_overpainted_by(pc1,pc2) == True
  #pc2._x_offset = 2.0
  #pc2._y_offset = 2.0
  #pc2._width = 2.0
  #pc2._height = 4.0
  #assert command_listing._is_overpainted_by(pc1,pc2) == False
  pc2._x_offset = 1.0
  pc2._y_offset = 3.0
  pc2._width = 3.0
  pc2._height = 3.0
  assert command_listing._is_overpainted_by(pc1,pc2) == True
  #pc2._x_offset = 1.0
  #pc2._y_offset = 2.0
  #pc2._width = 2.0
  #pc2._height = 4.0
  #assert command_listing._is_overpainted_by(pc1,pc2) == False
  pc2._x_offset = 1.0
  pc2._y_offset = 2.0
  pc2._width = 3.0
  pc2._height = 3.0
  assert command_listing._is_overpainted_by(pc1,pc2) == True
  pc2._x_offset = 0.0
  pc2._y_offset = 1.0
  pc2._width = 5.0
  pc2._height = 6.0
  assert command_listing._is_overpainted_by(pc1,pc2) == True
  print("OK")
  
  print("Tests of _lt", end=' ')
  assert not command_listing._lt(123.0,122.8) 
  assert not command_listing._lt(123.0,122.9) 
  assert not command_listing._lt(123.0,123.0) 
  assert not command_listing._lt(123.0,123.1) 
  assert command_listing._lt(123.0,123.2) 
  print("OK")
  
  print("Tests of insert", end=' ')
  _fss = font_styling.new_font_styles()
  # insertion into empty list
  _pc1 = command_listing.new_text_command("_pc1","Times New Roman",_fss,12.0,1.0,12.0,10.0,coloring.new_color(1.0,1.0,1.0))
  cl = command_listing.new_command_list()  
  assert cl._first == None
  assert cl._last == None
  assert cl._current == None
  command_listing.insert(cl,_pc1)
  assert cl._first == _pc1
  assert cl._last == _pc1
  assert cl._current == _pc1
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s =="_pc1"
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc1
  assert cl._last == _pc1
  assert cl._current == None
  command_listing.to_start_of_list(cl)
  assert cl._first == _pc1
  assert cl._last == _pc1
  assert cl._current == _pc1
  # overpaint only item
  _pc2 = command_listing.new_text_command("_pc2","Times New Roman",_fss,12.0,1.0,12.0,10.0,coloring.new_color(1.0,1.0,1.0))
  command_listing.insert(cl,_pc2)
  assert cl._first == _pc2
  assert cl._last == _pc2
  assert cl._current == _pc2
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s =="_pc2"
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc2
  assert cl._last == _pc2
  assert cl._current == None
  # insertion before _first
  _pc0 = command_listing.new_text_command("_pc0","Times New Roman",_fss,12.0,1.0,0.0,10.0,coloring.new_color(1.0,1.0,1.0))
  command_listing.insert(cl,_pc0)
  assert cl._first == _pc0
  #print("  cl._last._text_string="+str(cl._last._text_string))
  assert cl._last == _pc2
  assert cl._current == _pc0
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc0"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc2"
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc0
  assert cl._last == _pc2
  assert cl._current == None
  _pc = cl._last
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc2"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc0"
  _pc = _pc._previous_command
  assert _pc == None
  # insertion after end
  _pc3 = command_listing.new_text_command("_pc3","Times New Roman",_fss,12.0,1.0,24.0,10.0,coloring.new_color(0.0,0.0,0.0))
  command_listing.insert(cl,_pc3)
  assert cl._first == _pc0
  assert cl._last == _pc3
  assert cl._current == _pc0
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc0"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc2"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc3"
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc0
  assert cl._last == _pc3
  assert cl._current == None
  _pc = cl._last
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc3"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc2"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc0"
  _pc = _pc._previous_command
  assert _pc == None
  # insert in middle of list
  _pc1 = command_listing.new_text_command("_pc1","Times New Roman",_fss,12.0,1.0,12.0,10.0,coloring.new_color(1.0,1.0,1.0))
  command_listing.insert(cl,_pc1)
  assert cl._first == _pc0
  assert cl._last == _pc3
  assert cl._current == _pc0
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s =="_pc0"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc1"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc3"
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc0
  assert cl._last == _pc3
  assert cl._current == None
  _pc = cl._last
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc3"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc1"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc0"
  _pc = _pc._previous_command
  assert _pc == None
  # pc overpaints two items in the middle of the list
  _pc4 = command_listing.new_text_command("_pc4","Times New Roman",_fss,36.0,1.0,12.0,10.0,coloring.new_color(1.0,1.0,1.0))
  command_listing.insert(cl,_pc4)
  assert cl._first == _pc0
  #print("  cl._last._text_string="+cl._last._text_string)
  assert cl._last == _pc4
  assert cl._current == _pc0
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc0"
  _pca = command_listing.next_command(cl)
  _s = command_listing.text_string_of(_pca)
  assert _s == "_pc4"
  _pca = command_listing.next_command(cl)
  _pca = command_listing.next_command(cl)
  assert _pca == None
  assert cl._first == _pc0
  assert cl._last == _pc4
  assert cl._current == None
  _pc = cl._last
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc4"
  _pc = _pc._previous_command
  _s = command_listing.text_string_of(_pc)
  assert _s == "_pc0"
  _pc = _pc._previous_command
  assert _pc == None
  print("OK")

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

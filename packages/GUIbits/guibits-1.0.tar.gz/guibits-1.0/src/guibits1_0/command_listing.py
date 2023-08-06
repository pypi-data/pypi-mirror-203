"""
Contractor for listing paint commands.

Note that this contractor is thread-safe. A reentrant lock (RLock) is used to allow the client to lock a whole sequence of procedure calls.
"""

# author R.N.Bosworth

# version 25 Aug 2022  09:57

from . import coloring, font_styling, type_checking2_0
import threading
"""
Copyright (C) 2014,2105,2016,2017,2020,2021,2022  R.N.Bosworth

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

class CommandList:
  """ a list of zero or more PaintCommands in order of increasing y-offset """
  pass
  

class PaintCommand:
  pass
  

# exposed procedures
# ------------------

# PaintCommand
# ------------

def new_rectangle_command(x,y,w,h,c):
  """
  pre:
    x = x-offset in points from left-hand edge of pane of top 
          left-hand corner of rectangle which is to be painted, as float
    y = y-offset in points from top of pane of top left-hand corner of 
          rectangle which is to be painted, as float
    w = width in points of rectangle which is to be painted, as float
    h = height in points of rectangle which is to be painted, as float
    c = color in which rectangle is to be painted, as a coloring.Color value
    
  post:
    a new rectangle PaintCommand has been returned, as specified
    
  test:
    x is invalid float
    x is valid float
      y is invalid float
      y is valid float
        w is invalid float
        w is valid float
          h is invalid float
          h is valid float
            c is invalid Color
            c is valid Color
  """
  type_checking2_0.check_identical(x,float)
  type_checking2_0.check_identical(y,float)
  type_checking2_0.check_identical(w,float)
  type_checking2_0.check_identical(h,float)
  type_checking2_0.check_derivative(c,coloring.Color)
  pc = PaintCommand()
  pc._x_offset = x
  pc._y_offset = y
  pc._width = w
  pc._height = h
  pc._color = c
  pc._next_command = None
  pc._previous_command = None
  return pc
  

def new_text_command(s,fn,fss,fsize,x,y,w,c):
  """
  pre:
    s = string which is to be painted, as Python str
    fn = font name to be used to paint s, as str
    fss = font-style set to be used to paint s
    fsize = font size in points to be used for painting s, as float
         (note. this is the height of the rectangle in which s is to be painted)
    x = x-offset in points from left-hand edge of pane of top 
          left-hand corner of rectangle where s is to be painted, as float
    y = y-offset in points from top of pane of top left-hand corner of 
          rectangle where s is to be painted, as float
    w = width in points of rectangle where s is to be painted, as float 
    c = color in which s is to be painted, as a coloring.Color value
    
  post:
    a new text PaintCommand has been returned, as specified
    
  test:
    s is invalid Python str
    s is valid Python str
      fn is invalid string
      fn is valid string
        fss is invalid font style set
        fss is valid font style set
          fsize is invalid float
          fsize is valid float
            x is invalid float
            x is valid float
              y is invalid float
              y is valid float
                c is not a triple  
                c is invalid color
                c is valid color
  """
  type_checking2_0.check_derivative(s,str)
  type_checking2_0.check_derivative(fn,str)
  type_checking2_0.check_identical(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  type_checking2_0.check_identical(x,float)
  type_checking2_0.check_identical(y,float)
  type_checking2_0.check_identical(w,float)
  type_checking2_0.check_derivative(c,coloring.Color)
  pc = PaintCommand()
  pc._text_string = s
  # clone of s
  pc._font_name = fn
  pc._font_styles = fss
  pc._height = fsize
  pc._x_offset = x
  pc._y_offset = y
  pc._width = w
  pc._color = c
  pc._next_command = None
  pc._previous_command = None
  return pc
  

def font_name_of(pc):
  """
  pre:
    pc = text PaintCommand whose font name is to be found
    
  post:
    font name of pc has been returned, as str
  
  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._font_name
  

def font_size_of(pc):
  """
  pre:
    pc = text PaintCommand whose font size is to be found
    
  post:
    font size of pc in points has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._height
  

def font_styles_of(pc):
  """
  pre:
    pc = text PaintCommand whose font styles are to be found
    
  post:
    font style set of pc has been returned, as font_styling.FontStyles

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._font_styles
  

def height_of(pc):
  """
  pre:
    pc = rectangle PaintCommand whose height is to be found
    
  post:
    height of pc in points has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._height
  

def rectangle_color_of(pc):
  """
  pre:
    pc = rectangle PaintCommand whose rectangle color is to be found
    
  post:
    rectangle color of pc has been returned, as a coloring.Color value


  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._color
  

def text_color_of(pc):
  """
  pre:
    pc = text PaintCommand whose text color is to be found
    
  post:
    text color of pc has been returned, as a coloring.Color value


  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._color
  

def text_string_of(pc):
  """
  pre:
    pc = text PaintCommand whose text string is to be found
    
  post:
    text string of pc has been returned, as str

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)  
  return pc._text_string
  

def width_of(pc):
  """
  pre:
    pc = PaintCommand whose width is to be found
    
  post:
    width of pc in points has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._width
  

def x_offset_of(pc):
  """
  pre:
    pc = PaintCommand whose x-offset is to be found
  post:
    x-offset of pc in points from origin of text has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._x_offset
  

def y_offset_of(pc):
  """
  pre:
    pc = PaintCommand whose y-offset is to be found
    
  post:
    y-offset of pc in points from origin of text has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(pc,PaintCommand)
  return pc._y_offset
  

# CommandList
# -----------

def insert(cs,pc):
  """
  pre:
    cs = CommandList into which pc is to be inserted
    pc = PaintCommand to be inserted in cs

  post:
    pc has been inserted into cs, retaining the increasing ordering of y-offsets.
    Any PaintCommands in pc which are overpainted by pc have been deleted from cs.
    cs has been initialized to the first command (if any) in the list

  test:
    another thread trying to access cs while an insert is being done (put stop inside insert)  THIS NEEDS TESTING.
    cs is empty
    insert at start of list (y-offset less than any command in list)
    insert at end of list (y-offset greater than any command in list)
    insert in middle of list
    pc overpaints only item in list
    pc overpaints several items in the middle of the list
  """
  type_checking2_0.check_derivative(cs,CommandList)
  type_checking2_0.check_derivative(pc,PaintCommand)  
  with cs._my_lock:
    # start inserting at end of list
    cs._current = cs._last
    #while y-offset of _current command is >= pc's y-offset,
    while cs._current != None and cs._current._y_offset >= pc._y_offset:
      if _is_overpainted_by(cs._current,pc):
        # delete cs._current from the list
        if cs._current._previous_command != None:
          cs._current._previous_command._next_command = cs._current._next_command
        else:
          cs._first = cs._current._next_command
        if cs._current._next_command != None:
          cs._current._next_command._previous_command = cs._current._previous_command
        else:
          cs._last = cs._current._previous_command
      cs._current = cs._current._previous_command
      
    # found a command whose y-offset is < pc._y_offset, or got to start of list
    # cs._current == null || cs._current._y_offset < pc._y_offset
    if cs._current == None:
      # insert pc as _first member of command list
      pc._previous_command = None
      pc._next_command = cs._first
      if cs._first != None:
        cs._first._previous_command = pc       
      cs._first = pc
      cs._current = pc
      if cs._last == None:
        # the list was empty
        cs._last = pc
    # cs._current not null
    else:
      # insert pc immediately after _current member of command list
      pc._previous_command = cs._current
      pc._next_command = cs._current._next_command
      if cs._current._next_command != None:
        # pc is not _last member of list
        cs._current._next_command._previous_command = pc
      # pc is _last member of list
      else:
        cs._last = pc
      cs._current._next_command = pc
      cs._current = cs._first
  return 
  

def new_command_list():
  """
  post:
    a new empty CommandList has been returned

  test:
    once thru
  """
  _cs = CommandList()
  _cs._first = None
  _cs._current = None
  _cs._last = None
  _cs._my_lock = threading.RLock()
  return _cs
  

def next_command(cs):
  """
  pre:
    cs = CommandList whose next PaintCommand is to be returned

  post:
    next PaintCommand of cs has been returned, or None if none

  test:
    valid command
    end of list
  """
  with cs._my_lock:
    pc = cs._current
    if pc != None:
      cs._current = pc._next_command
    return pc
    
  
def to_start_of_list(cs):
  """
  pre:
    cs = CommandList which is to be initialized

  post:
    cs has been initialized to the _first command (if any) in the list

  test:
    list of two or more entries
    list of one entry
    empty list
  """
  type_checking2_0.check_derivative(cs,CommandList)
  with cs._my_lock:
    cs._current = cs._first
    
  
# private members
# ---------------

def _lt(y1,y2):
  """
  pre:
    y1, y2 = paint values to be compared
    
  post:
    returns true iff y1 is less than y2
  
  note:
    this procedure has a tolerance of 0.1 points
  
  test:
    y1 = 123.0
      y2 = 122.8
      y2 = 122.9
      y2 = 123.0
      y2 = 123.1
      y2 = 123.2
  """
  return y1 < y2 - 0.1
  

def _is_overpainted_by(pc1,pc2):
  """
  pre:
    pc1, pc2 = PaintCommands which are to be compared

  post:
    returns true iff pc2 overpaints pc1

  test:
    pc2 == pc1 in area painted
    pc2's y-offset  = pc1's y-offset + 1
    pc2's end y-offset  = pc1's y-offset - 1
    pc2's area is 1 point longer than pc1
  """
  if pc2._y_offset >= pc1._y_offset + pc1._height:
    return False
  if pc2._y_offset + pc2._height <= pc1._y_offset:
    return False    
  return True

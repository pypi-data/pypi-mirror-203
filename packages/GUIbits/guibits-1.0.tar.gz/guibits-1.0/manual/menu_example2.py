from guibits1_0 import menuing, windowing

# author R.N.Bosworth

# version 24 Sep 22  15:49
"""
Example of nested menus.

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

font_name = ""

font_size = 20.0

def tag_of(b):
  """
  pre:
    b = true, if bullet point is to be returned
        else blank string is returned

  post:
    appropriate string has been returned

  test:
    b = True
    b = False
  """
  tag = ""
  if b:
    tag += '\u2022'  # unicode bullet point
    tag += ' '
  else:
    tag += "  "
  return tag
  
  
def tagged_label_of(l,sv):
  """
  pre:
    l = label to be tagged, as string
    sv = value of label which is currently selected. as string
  
  post:
    tagged version of label has been returned, as string
    
  test:
    l is selected
    l is not selected
  """
  return tag_of(l == sv) + l
  

def file_menu_item_hit(win,x,y,l):
  """
  pre:
    menu item associated with this callback procedure has been hit by user
    win = windowing.Window where mouse-hit occurred
    x,y = x and y offsets of mouse hit from top left-hand corner of window's contents, in points as float
    
  post:
    file menu has been displayed and user has responded
    
  test:
    once thru
  """
  print("File menu item hit at "+str(x)+","+str(y));
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,font_size,"Open",file_open_menu_item_listener)
  menuing.add_separator(m)
  menuing.add_menu_item(m,font_size,"Save",None)
  menuing.add_menu_item(m,font_size,"Save As",file_save_as_menu_item_listener)
  menuing.add_separator(m)
  menuing.add_menu_item(m,font_size,"Close",file_close_menu_item_listener)
  menuing.display(m,win,x,y)
  
  
def file_close_menu_item_listener(win,x,y,l):
  pass


def file_open_menu_item_listener(win,x,y,l):
  pass


def file_save_as_menu_item_listener(win,x,y,l):
  """
  pre:
    menu item associated with this callback procedure has been hit by user
    win = windowing.Window where mouse-hit occurred
    x,y = x and y offsets of mouse hit from top left-hand corner of window's contents, in points as float
    
  post:
    file menu has been displayed and user has responded
    
  test:
    once thru
  """
  print("Save As menu item hit at "+str(x)+","+str(y));
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,font_size,"Save to the Cloud",save_cloud_menu_item_listener)
  menuing.add_menu_item(m,font_size,"Save to Disk",save_disk_menu_item_listener)
  menuing.display(m,win,x,y)
  
  
def font_courier_menu_item_listener(win,x,y,l):
  global font_name
  font_name = "Courier New"


def font_menu_item_hit(win,x,y,l):
  """
  pre:
    menu item associated with this callback procedure has been hit by user
    win = windowing.Window where mouse-hit occurred
    x,y = x and y offsets of mouse hit from top left-hand corner of window's contents, in points as float 
  post:
    font menu has been displayed and user has responded
  """
  print("Font menu item hit at "+str(x)+","+str(y))
  print("  font_name="+font_name)
  m = menuing.new_menu(win)
  menuing.add_menu_item(m,font_size,tagged_label_of("Courier New",font_name), \
                        font_courier_menu_item_listener)
  menuing.add_menu_item(m,font_size,tagged_label_of("Times New Roman",font_name), \
                        font_times_menu_item_listener)
  menuing.display(m,win,x,y)
  
  
def font_times_menu_item_listener(win,x,y,l):
  global font_name
  font_name = "Times New Roman"


def save_cloud_menu_item_listener(win,x,y,l):
  pass


def save_disk_menu_item_listener(win,x,y,l):
  pass


def _test():
  print("test of tag_of",' ')
  assert tag_of(True) == "\u2022 "
  assert tag_of(False) == "  "
  print("OK")
  
  print("test of tagged_label_of",' ')
  sv = "fred"
  assert tagged_label_of("fred",sv) == "\u2022 fred"
  assert tagged_label_of("jim",sv) == "  jim"
  print("OK")
  
  print("test of menu system")
  w = windowing.new_window(font_size,"Menu Example 2",800.0,600.0,1.0)
  menuing.add_menu_bar_item(w,font_size,"File",file_menu_item_hit)
  menuing.add_menu_bar_item(w,font_size,"Font",font_menu_item_hit)
  windowing.show(w,None,None)
  
if __name__ == "__main__":
  _test()
  print("All tests OK")

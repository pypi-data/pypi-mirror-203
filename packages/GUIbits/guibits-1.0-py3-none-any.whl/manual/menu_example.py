from guibits1_0 import menuing, windowing

# author R.N.Bosworth

# version 24 Sep 22  15:36

"""
Example of menu bar.

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

font_size = 20.0

def file_menu_item_hit(win,x,y,l):
  print("File menu item hit at "+str(x)+","+str(y));
  print("Label="+l)

def font_menu_item_hit(win,x,y,l):
  print("Font menu item hit at "+str(x)+","+str(y));
  print("Label="+l)

w = windowing.new_window(font_size,"Menu Example",800.0,600.0,1.0)
menuing.add_menu_bar_item(w,font_size,"File",file_menu_item_hit)
menuing.add_menu_bar_item(w,font_size,"Font",font_menu_item_hit)
windowing.show(w,None,None)

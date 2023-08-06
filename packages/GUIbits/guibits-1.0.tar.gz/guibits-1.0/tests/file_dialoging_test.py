# Test of contractor for displaying file dialogs

# version 28 Jul 22  20:08

# author RNB

from guibits1_0 import file_dialoging

"""
Copyright (C) 2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# test program
# ------------

def prframe(s,v):
  w = v.frameSize().width()
  h = v.frameSize().height()
  print(s+".frameSize()="+"("+str(w)+","+str(h)+")")
  
def prgeom(s,v):
  g = v.geometry()
  x = g.x()
  y = g.y()
  w = g.width()
  h = g.height()
  print(s+".geometry()=("+str(x)+","+str(y)+","+str(w)+","+str(h)+")")

def prhint(s,v):
  w = v.sizeHint().width()
  h = v.sizeHint().height()
  print(s+".sizeHint()="+"("+str(w)+","+str(h)+")")
  
def prmax(s,v):
  w = v.maximumSize().width()
  h = v.maximumSize().height()
  print(s+".maximumSize()="+"("+str(w)+","+str(h)+")")
  
def prmin(s,v):
  w = v.minimumSize().width()
  h = v.minimumSize().height()
  print(s+".minimumSize()="+"("+str(w)+","+str(h)+")")
  
def prsize(s,v):
  w = v.size().width()
  h = v.size().height()
  print(s+".size()="+"("+str(w)+","+str(h)+")")
  

def _test():
    
  print("_display_pathname", end = ' ')
  assert file_dialoging._display_pathname("") == "File System:"
  assert file_dialoging._display_pathname("x") == "x"
  print("OK")
  
  
  print("_is_accessible", end = ' ')
  assert file_dialoging._is_accessible("C:\\TestFolder\\a.txt")
  assert not file_dialoging._is_accessible("C:\\invalid.txt")
  assert file_dialoging._is_accessible("C:\\Program Files")
  assert not file_dialoging._is_accessible("C:\\Documents and Settings")
  print("OK")
  
  
  print("_children_of")
  print("  _children_of(\"\")="+str(file_dialoging._children_of("")))
  print("  _children_of(\"C:\\\")="+str(file_dialoging._children_of("C:\\")))
  print("  _children_of(\"C:\\EmptyFolder\")="+str(file_dialoging._children_of("C:\\EmptyFolder")))
  print("  _children_of(\"C:\\Temp\")="+str(file_dialoging._children_of("C:\\Temp")))
  print("OK")
  
  
  print("show_open_file_dialog")
  #file_dialoging.show_open_file_dialog(None,None,None,None)
  #file_dialoging.show_open_file_dialog(5.9,None,None,None)
  #file_dialoging.show_open_file_dialog(24.0,None,None,None)
  #file_dialoging.show_open_file_dialog(24.0,"",None,None)
  #file_dialoging.show_open_file_dialog(24.0,"Title",None,None)
  reply = file_dialoging.show_open_file_dialog(6.0,"Title",None,file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(24.0,"Title","invalid.py",file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\Temp\\",file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\Users\\User\\diskpart",file_dialoging.SortMode.EARLIEST_FIRST)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\EmptyFolder\\",file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\TestFolder\\",file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\TestFolder\\",file_dialoging.SortMode.EARLIEST_FIRST)
  print("  reply="+str(reply))
  reply = file_dialoging.show_open_file_dialog(12.0,"Title","C:\\TestFolder\\",file_dialoging.SortMode.LATEST_FIRST)
  print("  reply="+str(reply))
  print("OK")
  
  
  print("show_new_folder_dialog")
  #file_dialoging.show_new_folder_dialog(5.9,None,None)
  #file_dialoging.show_new_folder_dialog(6.0,None,None)
  #file_dialoging.show_new_folder_dialog(12.0,"",None)
  #file_dialoging.show_new_folder_dialog(12.0,"a",None)
  reply = file_dialoging.show_new_folder_dialog(12.0,"a","")
  print("  reply="+str(reply))
  reply = file_dialoging.show_new_folder_dialog(12.0,"Create New Folder","z:")
  print("  reply="+str(reply))
  reply = file_dialoging.show_new_folder_dialog(12.0,"Create New Folder 2","C:\\Users")
  print("  reply="+str(reply))
  reply = file_dialoging.show_new_folder_dialog(12.0,"Create New Folder 3","C:\\Bosware\\GUIbits\\GuibitsPackage0_7\\guibits1_0")
  print("  reply="+str(reply))
  print("OK")
  
  
  print("show_save_file_dialog")
  #file_dialoging.show_save_file_dialog(None,None,None,None,None)
  #file_dialoging.show_save_file_dialog(5.9,None,None,None,None)
  #file_dialoging.show_save_file_dialog(6.0,None,None,None,None)
  #file_dialoging.show_save_file_dialog(24.0,"",None,None,None)
  #file_dialoging.show_save_file_dialog(24.0,"Save",None,None,None)
  #file_dialoging.show_save_file_dialog(24.0,"Save",None,[],None)
  reply = file_dialoging.show_save_file_dialog(6.0,"Save",None,[],file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(24.0,"Save","",["abc"],file_dialoging.SortMode.EARLIEST_FIRST)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(14.0,"Save","",["abc","def"],file_dialoging.SortMode.LATEST_FIRST)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(14.0,"Save","Z:",["abc","def"],file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(14.0,"Save","fred.py",["abc","def"],file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(14.0,"Save","C:\\TestFolder\\",["abc","def"],file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  reply = file_dialoging.show_save_file_dialog(14.0,"Save","C:\\TestFolder\\bill.py",["abc","def"],file_dialoging.SortMode.ALPHABETIC)
  print("  reply="+str(reply))
  print("OK")
  
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

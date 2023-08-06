# Test of contractor which allows the client to write text onto the pane of the window

# version 12 Jan 23  18:54

# author RNB

from guibits1_0 import coloring, cursoring, font_styling, windowing, writing

"""
Copyright (C) 2021,2022,2023  R.N.Bosworth

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

_font_size = 18.0
_app_title = "Window with large pane"
 

def window_closing(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown

  """
  print("Callback thread test "+str(win._tnum))
  if win._tnum == 0:
    print("width_in_points_of")
    windowing.set_title(win,"width_in_points_of")
    fname = "Times New Roman"
    print("  fname="+fname)
    fss = font_styling.new_font_styles()
    print("  fss = ()")
    print("  width_in_points_of(win,\" \",fname,fss,24.0)=" + str(writing.width_in_points_of(win," ",fname,fss,24.0)))
    print("  width_in_points_of(win,\"W\",fname,fss,24.0)=" + str(writing.width_in_points_of(win,"W",fname,fss,24.0)))
    print("  width_in_points_of(win,\" W\",fname,fss,24.0)=" + str(writing.width_in_points_of(win," W",fname,fss,24.0)))
    s = "Thankyou"
    print("  s="+s)
    #print("width_in_points_of(win,s,fname,fss,5.9)=" + str(writing.width_in_points_of(win,s,fname,fss,5.9)))
    print("  width_in_points_of(win,s,fname,fss,6.0)=" + str(writing.width_in_points_of(win,s,fname,fss,6.0)))
    print("  width_in_points_of(win,s,fname,fss,18.0)=" + str(writing.width_in_points_of(win,s,fname,fss,18.0)))
    s = "ThankyouThankyou"
    print("  s="+s)
    print("  width_in_points_of(win,s,fname,fss,18.0)=" + str(writing.width_in_points_of(win,s,fname,fss,18.0)))
    font_styling.include(fss,font_styling.FontStyle.BOLD)
    s = "Thankyou"
    print("  s="+s)
    print("  fss = (BOLD)")      
    print("  width_in_points_of(win,s,fname,fss,18.0)=" + str(writing.width_in_points_of(win,s,fname,fss,18.0)))
    fss = font_styling.new_font_styles()
    font_styling.include(fss,font_styling.FontStyle.ITALIC)
    print("  s="+s)
    print("  fss = (ITALIC)")      
    print("  width_in_points_of(win,s,fname,fss,18.0)=" + str(writing.width_in_points_of(win,s,fname,fss,18.0)))
    font_styling.include(fss,font_styling.FontStyle.BOLD)
    print("  s="+s)
    print("  fss = (BOLD,ITALIC)")      
    print("  width_in_points_of(win,s,fname,fss,18.0)=" + str(writing.width_in_points_of(win,s,fname,fss,18.0)))
    print("OK")
    win._tnum += 1
    return False
  elif win._tnum == 1:
    print("write_string")
    windowing.set_title(win,"write_string")
    s = "Thankyou"
    fname = "Times New Roman"
    fss = font_styling.new_font_styles()
    fsize = 6.0
    x = 0.0
    y = 0.0
    c = coloring.new_color(0.0,0.0,0.0)  # BLACK
    writing.write_string(win,s,fname,fss,fsize,x,y,c);
    fsize = 10.0;
    writing.write_string(win,s,fname,fss,fsize,x,y,c);
    x = 72.0
    y = 144.0
    fsize = 24.0
    c = coloring.new_color(0.0,0.0,1.0)  # BLUE
    _xoff = writing.write_string(win,s,fname,fss,fsize,x,y,c)
    print("  _xoff=" + str(_xoff))
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 2:
    print("Test of repeated lines", end=' ')
    windowing.set_title(win,"Test of repeated lines")
    s = "Thankyou"
    fname = "Times New Roman"
    fss = font_styling.new_font_styles()
    c = coloring.new_color(0.0,0.0,0.0) # BLACK
    x = 72.0
    y = 144.0
    fsize = 72.0
    writing.write_string(win,s,fname,fss,fsize,x,y,c)
    writing.write_string(win,s,fname,fss,fsize,x,y + fsize,c)
    print("OK")
    win._tnum += 1
    return False
      
  elif win._tnum == 3:
    print("Test of repeated words", end=' ')
    windowing.set_title(win,"Test of repeated words")
    s = "Thankyou"
    fname = "Times New Roman"
    fss = font_styling.new_font_styles()
    c = coloring.new_color(0.0,1.0,0.0) # GREEN
    x = 72.0
    y = 144.0
    fsize = 72.0
    xoff = writing.write_string(win,s,fname,fss,fsize,x,y,c)
    writing.write_string(win,s,fname,fss,fsize,xoff,y,c)
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 4:
    print("Test of write_string, draw_cursor")
    windowing.set_title(win,"Test of write_string, draw_cursor")
    s = "A very long long long string abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    fname = "Times New Roman"
    fss = font_styling.new_font_styles()
    fsize = 12.0
    x = 72.0
    y = 144.0
    c = coloring.new_color(1.0,0.0,0.0) # RED
    xoff = writing.write_string(win,s,fname,fss,fsize,x,y,c)
    print("  from write_string:_xoff=" + str(xoff))
    cursoring.draw_cursor(win,fsize,xoff,y,c)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 5:
    print("Test of clear_text",end=' ')
    writing.clear_text(win)
    print("OK")
    win._tnum += 1
    return False

  else:
    print("All tests OK")
    return True

def _test():
  print("Main thread tests")
  
  print("Test of width_in_points_of", end=' ')
  #writing.width_in_points_of(None,None,None,None,-1);
  win = windowing.new_window(_font_size,"Test of width_in_points_of",800.0,600.0,1.0)
  s = "Thankyou"
  s2 = "Goodbye"
  fname = "Times New Roman"
  fss = font_styling.new_font_styles()
  #writing.width_in_points_of(win,None,None,None,None)
  #writing.width_in_points_of(win,s,None,None,None)
  #writing.width_in_points_of(win,s,fname,None,None)
  #writing.width_in_points_of(win,s,fname,fss,5.9)
  #writing.width_in_points_of(win,s,fname,fss,72.1)
  #writing.width_in_points_of(win,s,fname,fss,72.0)
  #writing.width_in_points_of(win,s,fname,fss,6.0)
  print("OK")
  
  print("Test of clear_text",end=' ')
  #writing.clear_text(None)
  win = windowing.new_window(_font_size,"Test of writing.write_string",800.0,600.0,1.0)
  writing.clear_text(win)
  print("OK")
  
  print("Test of write_string", end=' ')
  #writing.write_string(None,None,None,None,-1,-1,-1,None);
  win = windowing.new_window(_font_size,"Test of writing.write_string",800.0,600.0,1.0)
  #writing.write_string(win,None,None,None,-1,-1,-1,None);
  s = "Thankyou"
  #writing.write_string(win,s,None,None,-1,-1,-1,None);
  fname = "Times New Roman"
  #writing.write_string(win,s,fname,None,-1,-1,-1,None);
  fss = font_styling.new_font_styles()
  #writing.write_string(win,s,fname,fss,-1,-1,-1,None);
  #writing.write_string(win,s,fname,fss,0.0,-1,-1,None);
  fsize = 1.0
  #writing.write_string(win,s,fname,fss,fsize,-1,-1,None);
  #writing.write_string(win,s,fname,fss,fsize,-0.1,-1,None);
  x = 0.0
  #writing.write_string(win,s,fname,fss,fsize,x,-1,None);
  #writing.write_string(win,s,fname,fss,fsize,x,-0.1,None);
  y = 0.0
  #writing.write_string(win,s,fname,fss,fsize,x,y,None);
  print("OK")
  
  # callback thread tests
  win = windowing.new_window(12.0,"callback tests",720.0,360.0,1.0)
  win._tnum = 0  # number of completed tests
  windowing.show(win,None,window_closing)
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

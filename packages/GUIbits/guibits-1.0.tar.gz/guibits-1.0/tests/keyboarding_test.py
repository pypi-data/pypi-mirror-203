# Test of Contractor for keyboard input.

# author R.N.Bosworth

# version 5 Aug 22  14:05

from guibits1_0 import controlling, keyboarding, type_checking2_0, windowing

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

def character_key_hit(cp):
  type_checking2_0.check_identical(cp,int)
  print("keyboarding.character_key_hit")
  print("  cp=" + hex(cp)+",'"+chr(cp)+"'")
  
def character_key_hit2():
  pass
  
def window_opening(win):
  keyboarding.attach(win,None)
    
def window_opening2(win):
  keyboarding.attach(win,character_key_hit2)
    
def window_opening3(win):
  keyboarding.attach(win,character_key_hit)
  
def action_key_hit(ac):
  """
  pre:
    ac = action code of key (combination) hit by user
    
  post:
    action required by this key-hit has been carried out      
  """
  print("keyboarding_test.action_key_hit")
  print("  ac="+str(ac))
    
def window_closing(win):
  """
  pre:
    the user has pressed the Close button of the window associated with this listener 
    win = Window on which the close event occured

  post:
    returns True iff app is to close
    if True has been returned, clean-up has been done prior to shutdown
  """
  if win._tnum == 0:
    print("Adding controlling attachment")
    controlling.attach(win,action_key_hit)
    print("Please press keyboard and control buttons")
    print("OK")
    win._tnum += 1
    return False
  else:
    print("All tests OK")
    return True

    
def _test():
  """
  print("Tests of _return_code_point")
  win = windowing.new_window(16.0,"Tests of _return_code_point",800.0,500.0,1.0)
  #print("No keyboard callback")
  #windowing.show(win,None,None)
  print("With keyboard callback")
  windowing.show(win,window_opening3,None)
  # needs tests of empty text param
  print("OK")
  """
  print("Tests of keyboarding.attach")
  win = windowing.new_window(16.0,"Tests of keyboarding.attach and key entry",800.0,500.0,1.0)
  win._tnum = 0
  #print("Showing window with no attachments")
  #windowing.show(win,None,None)
  #keyboarding.attach(win,character_key_hit)
  #windowing.show(win,window_opening,None)
  #windowing.show(win,window_opening2,None)
  #print("Showing window with keyboard attachment")
  #windowing.show(win,window_opening3,None)
  print("Showing window with keyboard attachment")
  print("Please press keyboard and control buttons")
  windowing.show(win,window_opening3,window_closing)
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

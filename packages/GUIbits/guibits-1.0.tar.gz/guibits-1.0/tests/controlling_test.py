# Test of Contractor for control key input.

# author R.N.Bosworth

# version 27 Jul 2022  10:31

from guibits1_0 import controlling, windowing

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

def test_action_key_hit(ac):
  """
  pre:
    ac = action code of key (combination) hit by user
    
  post:
    action required by this key-hit has been carried out
  """
  print("test_action_key_hit")
  print("  ac=" + str(ac))
    
def test_action_key_hit2():
  pass
  
def window_opening(win):
  controlling.attach(win,None)
    
def window_opening2(win):
  controlling.attach(win,test_action_key_hit2)
    
def window_opening3(win):
  controlling.attach(win,test_action_key_hit)
    
    
def _test():
  print("Tests of controlling.attach")
  win = windowing.new_window(16.0,"Tests of controlling.attach",800.0,500.0,1.0)
  print("Press ENTER, BACKSPACE, DEL and cursor arrow keys")
  #controlling.attach(win,test_action_key_hit)
  #windowing.show(win,window_opening,None)
  #windowing.show(win,window_opening2,None)
  windowing.show(win,window_opening3,None)
  controlling.attach(win,test_action_key_hit)
  print("OK")  


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

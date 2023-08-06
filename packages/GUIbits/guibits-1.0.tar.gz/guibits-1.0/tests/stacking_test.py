# Test of Bounded structure representing the top n elements of a generic stack.

# author R.N.Bosworth

# version 26 Jul 2022  17:49

from guibits1_0 import stacking

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

def _test():
  print("Tests of instantiation", end=' ')
  #p = stacking.new_stack_top(None)
  #p = stacking.new_stack_top(0)
  p = stacking.new_stack_top(1)
  assert len(p._my_circle) == 1
  assert p._my_circle[0] == None
  assert p._toff == 0
  assert p._boff == 0
  assert p._size == 0
  assert p._max == 1
  p3 = stacking.new_stack_top(3)
  assert len(p3._my_circle) == 3
  assert p3._my_circle[0] == None
  assert p3._my_circle[1] == None
  assert p3._my_circle[2] == None
  assert p3._toff == 0
  assert p3._boff == 0
  assert p3._size == 0
  assert p3._max == 3
  print("OK")
  
  print("Tests of _dec", end=' ')
  assert stacking._dec(1,3) == 0
  assert stacking._dec(0,3) == 2
  print("OK")
  
  print("Tests of _inc", end=' ')
  assert stacking._inc(1,3) == 2
  assert stacking._inc(2,3) == 0
  print("OK")
  
  print("Tests of push, pop, size and clear", end=' ')
  p = stacking.new_stack_top(1)
  #assert stacking.size(None) == 0
  assert stacking.size(p) == 0
  #stacking.push(None,"a")
  stacking.push(p,"a")
  #assert stacking.size(None) == 1
  assert stacking.size(p) == 1
  stacking.push(p,"b")
  assert stacking.size(p) == 1
  #assert stacking.pop(None) == "b"
  assert stacking.pop(p) == "b"
  assert stacking.size(p) == 0
  p = stacking.new_stack_top(2)
  assert stacking.size(p) == 0
  stacking.push(p,"a")
  assert stacking.size(p) == 1
  stacking.push(p,"b")
  assert stacking.size(p) == 2
  stacking.push(p,"c")
  assert stacking.size(p) == 2
  assert stacking.pop(p) == "c"
  assert stacking.size(p) == 1
  assert stacking.pop(p) == "b"
  assert stacking.size(p) == 0
  p = stacking.new_stack_top(2)
  assert stacking.size(p) == 0
  stacking.push(p,"a")
  assert stacking.size(p) == 1
  stacking.push(p,"b")
  assert stacking.size(p) == 2
  stacking.push(p,"c")
  #stacking.clear(None)
  stacking.clear(p)
  assert stacking.size(p) == 0
  #assert stacking.pop(p) == "c"      
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

# Test of latest_listing contractor

# author R.N.Bosworth

# version 26 Jul 2022  14:50

from guibits1_0 import latest_listing

"""
Copyright (C) 2011,2016,2017,2020,2021,2022  R.N.Bosworth

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
  print("Tests of new_list_of_latest", end=' ')
  #p = latest_listing.new_list_of_latest(None)
  p = latest_listing.new_list_of_latest(3)
  assert len(p._my_circle) == 3
  assert p._toff == 0
  assert p._boff == 0
  assert p._size == 0
  assert p._max == 3   
  #p2 = latest_listing.new_list_of_latest(0)
  p3 = latest_listing.new_list_of_latest(1)
  assert len(p3._my_circle) == 1
  assert p3._toff == 0
  assert p3._boff == 0
  assert p3._size == 0
  assert p3._max == 1   
  print("OK")
  
  print("Tests of _residue_of", end=' ')
  assert latest_listing._residue_of( - 2,1) == 0
  assert latest_listing._residue_of( - 1,1) == 0
  assert latest_listing._residue_of(0,1) == 0
  assert latest_listing._residue_of(1,1) == 0
  assert latest_listing._residue_of(2,1) == 0
  assert latest_listing._residue_of( - 2,2) == 0
  assert latest_listing._residue_of( - 1,2) == 1
  assert latest_listing._residue_of(0,2) == 0
  assert latest_listing._residue_of(1,2) == 1
  assert latest_listing._residue_of(2,2) == 0
  print("OK")
 
  print("Tests of _inc", end=' ')
  p = latest_listing.new_list_of_latest(3)
  assert latest_listing._inc(p,1) == 2
  assert latest_listing._inc(p,2) == 0
  print("OK")
  
  print("Tests of _dec", end=' ')
  p = latest_listing.new_list_of_latest(3)
  assert latest_listing._dec(p,1) == 0
  assert latest_listing._dec(p,0) == 2
  print("OK")
  
  
  print("Tests of push and size", end=' ')
  #assert size(None) == 0
  p = latest_listing.new_list_of_latest(1)
  assert latest_listing.size(p) == 0
  #latest_listing.push(None,"a")
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"b")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "b"
  p = latest_listing.new_list_of_latest(2)
  assert latest_listing.size(p) == 0
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"b")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "b"
  assert latest_listing.get(p,1) == "a"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "a"
  assert latest_listing.get(p,1) == "b"
  latest_listing.push(p,"c")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "c"
  assert latest_listing.get(p,1) == "a"
  p = latest_listing.new_list_of_latest(3)
  assert latest_listing.size(p) == 0
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 1
  assert latest_listing.get(p,0) == "a"
  latest_listing.push(p,"b")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "b"
  assert latest_listing.get(p,1) == "a"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "a"
  assert latest_listing.get(p,1) == "b"
  latest_listing.push(p,"a")
  assert latest_listing.size(p) == 2
  assert latest_listing.get(p,0) == "a"
  assert latest_listing.get(p,1) == "b"
  latest_listing.push(p,"c")
  assert latest_listing.size(p) == 3
  assert latest_listing.get(p,0) == "c"
  assert latest_listing.get(p,1) == "a"
  assert latest_listing.get(p,2) == "b"
  latest_listing.push(p,"c")
  assert latest_listing.size(p) == 3
  assert latest_listing.get(p,0) == "c"
  assert latest_listing.get(p,1) == "a"
  assert latest_listing.get(p,2) == "b"
  latest_listing.push(p,"b")
  assert latest_listing.size(p) == 3
  assert latest_listing.get(p,0) == "b"
  assert latest_listing.get(p,1) == "c"
  assert latest_listing.get(p,2) == "a"
  print("OK")
  
  
  print("Tests of get", end=' ')
  p = latest_listing.new_list_of_latest(2)
  #latest_listing.get(None,-1)
  #latest_listing.get(p,-1);
  #latest_listing.get(p,0);
  latest_listing.push(p,"x")
  #latest_listing.get(p,-1);
  assert latest_listing.get(p,0) == "x"
  #latest_listing.get(p,1);
  latest_listing.push(p,"y")
  #latest_listing.get(p,-1);
  assert latest_listing.get(p,0) == "y"
  assert latest_listing.get(p,1) == "x"
  #latest_listing.get(p,2);
  latest_listing.push(p,"z")
  #latest_listing.get(p,-1);
  assert latest_listing.get(p,0) == "z"
  assert latest_listing.get(p,1) == "y"
  #latest_listing.get(p,2);
  print("OK")
    

if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

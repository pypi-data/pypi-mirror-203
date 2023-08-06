# Test of contractor which supports mutable Unicode UTF-32 strings

#version 26 Jul 2022  17:51

# author RNB

from guibits1_0 import unicoding3_0

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

def _test():
  s = unicoding3_0.new_string()
  assert s._string == []
  print("new_string OK")
  
  #assert not unicoding3_0.is_valid_code_point(None)
  assert not unicoding3_0.is_valid_code_point(-1)
  assert  unicoding3_0.is_valid_code_point(0)
  assert  unicoding3_0.is_valid_code_point(0xD7FF)
  assert not  unicoding3_0.is_valid_code_point(0xD800)
  assert not  unicoding3_0.is_valid_code_point(0xDFFF)
  assert  unicoding3_0.is_valid_code_point(0xE000)
  assert  unicoding3_0.is_valid_code_point(0x10FFFF)
  assert not  unicoding3_0.is_valid_code_point(0x110000)
  print("is_valid_code_point OK");
  
  
  #_unicoding3_0.check_in_range(-1);
  unicoding3_0._check_in_range(0);
  print("_check_in_range OK");
    
  #code_point_at(None,0)  
  s = unicoding3_0.new_string()
  unicoding3_0.append(s,ord('a'))
  unicoding3_0.append(s,ord('b'))
  unicoding3_0.append(s,ord('c'))
  #unicoding3_0.code_point_at(s,True)
  #unicoding3_0.code_point_at(s,-1)
  assert unicoding3_0.code_point_at(s,0) == ord('a')
  assert unicoding3_0.code_point_at(s,2) == ord('c')
  #unicoding3_0.code_point_at(s,3)
  print("code_point_at OK")
  
  #assert unicoding3_0.length_of(None) == 0
  s = unicoding3_0.new_string();
  assert unicoding3_0.length_of(s) == 0;
  unicoding3_0.append(s,ord('f'))
  unicoding3_0.append(s,ord('r'))
  unicoding3_0.append(s,ord('e'))
  unicoding3_0.append(s,ord('d'))
  assert unicoding3_0.length_of(s) == 4;
  print("length_of OK")
  
  s1 = None
  #unicoding3_0.append(s1,0)
  s1 = unicoding3_0.new_string()
  #unicoding3_0.append(s1,None)
  unicoding3_0.append(s1,ord('f'))
  unicoding3_0.append(s1,ord('r'))
  unicoding3_0.append(s1,ord('e'))
  unicoding3_0.append(s1,ord('d'))
  #unicoding3_0.append(s1,-1)
  #unicoding3_0.append(s1,'a')
  unicoding3_0.append(s1,ord('a'))
  assert unicoding3_0.length_of(s1) == 5
  assert unicoding3_0.code_point_at(s1,0) == ord('f')
  assert unicoding3_0.code_point_at(s1,1) == ord('r')
  assert unicoding3_0.code_point_at(s1,2) == ord('e')
  assert unicoding3_0.code_point_at(s1,3) == ord('d')
  assert unicoding3_0.code_point_at(s1,4) == ord('a')
  print("append OK")   

  #s = unicoding3_0.string_of(None)
  s = unicoding3_0.string_of("")
  assert unicoding3_0.length_of(s) == 0
  s = unicoding3_0.string_of("fred")
  assert unicoding3_0.length_of(s) == 4
  assert unicoding3_0.code_point_at(s,0) == ord('f')  
  assert unicoding3_0.code_point_at(s,1) == ord('r')  
  assert unicoding3_0.code_point_at(s,2) == ord('e')  
  assert unicoding3_0.code_point_at(s,3) == ord('d')  
  print("string_of OK")
  
  s1 = None
  s2 = unicoding3_0.string_of("def")
  #assert not unicoding3_0.equals(s1,s2)
  s1 = unicoding3_0.string_of("abc")
  assert unicoding3_0.equals(s1,s1)
  s1 = unicoding3_0.string_of("")
  s2 = None
  #assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("x")
  assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("")
  assert unicoding3_0.equals(s1,s2)
  s1 = unicoding3_0.string_of("xyz")
  s2 = unicoding3_0.string_of("yyz")
  assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("xyy")
  assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("xyza")
  assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("xy")
  assert not unicoding3_0.equals(s1,s2)
  s2 = unicoding3_0.string_of("xyz")
  assert unicoding3_0.equals(s1,s2)
  print("equals OK")
  

  #unicoding3_0.append_a_copy(None,unicoding3_0.string_of("abc"))
  s1 = unicoding3_0.string_of("abc")
  s2 = None
  #unicoding3_0.append_a_copy(s1,s2)
  s2 = unicoding3_0.string_of("")
  unicoding3_0.append_a_copy(s1,s2)
  assert unicoding3_0.equals(s1,unicoding3_0.string_of("abc"))
  s2 = unicoding3_0.string_of("def")
  unicoding3_0.append_a_copy(s1,s2)
  assert unicoding3_0.equals(s1,unicoding3_0.string_of("abcdef"))
  print("append_a_copy OK")
  
  s = None
  #unicoding3_0.insert(s,0,ord('x'))
  s = unicoding3_0.string_of("efg")
  #unicoding3_0.insert(s,0,-1)
  #unicoding3_0.insert(s,0,'x')
  #unicoding3_0.insert(s,'a',ord('x'))
  #unicoding3_0.insert(s,-1,ord('x'))
  unicoding3_0.insert(s,0,ord('x'))
  assert unicoding3_0.equals(s,unicoding3_0.string_of("xefg"))
  s = unicoding3_0.string_of("efg")
  unicoding3_0.insert(s,1,ord('x'))
  assert unicoding3_0.equals(s,unicoding3_0.string_of("exfg"))
  s = unicoding3_0.string_of("efg")
  unicoding3_0.insert(s,3,ord('x'))
  assert unicoding3_0.equals(s,unicoding3_0.string_of("efgx"))
  s = unicoding3_0.string_of("efg")
  #unicoding3_0.insert(s,4,ord('x'))
  print("insert OK")
  
  #unicoding3_0.python_string_of(None)
  s = unicoding3_0.new_string()
  assert len(unicoding3_0.python_string_of(s)) == 0
  unicoding3_0.append(s,0x0000)
  unicoding3_0.append(s,0xFFFF)
  unicoding3_0.append(s,0x10000)
  unicoding3_0.append(s,0x10FFFF)
  assert unicoding3_0.length_of(s) == 4

  ps = unicoding3_0.python_string_of(s)
  assert len(ps) == 4
  assert ps[0] == chr(0x0000)
  assert ps[1] == chr(0xFFFF)
  assert ps[2] == chr(0x10000)
  assert ps[3] == chr(0x10FFFF)
  print("python_string_of OK")


  s = None
  #unicoding3_0.remove(s,0)
  s = unicoding3_0.string_of("")
  #unicoding3_0.remove(s,None)
  #unicoding3_0.remove(s,0)
  s = unicoding3_0.string_of("ghi")
  #unicoding3_0.remove(s,-1)
  unicoding3_0.remove(s,0)
  assert unicoding3_0.equals(s,unicoding3_0.string_of("hi"))
  #unicoding3_0.remove(s,2)
  unicoding3_0.remove(s,1)
  assert unicoding3_0.equals(s,unicoding3_0.string_of("h"))
  print("remove OK")
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

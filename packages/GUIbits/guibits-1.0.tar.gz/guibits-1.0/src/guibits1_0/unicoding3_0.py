# contractor which supports mutable Unicode UTF-32 strings

#version 14 Sep 2021  15:20

# author RNB

from . import type_checking2_0

"""
Copyright (C) 2019,2020,2021  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed types

class String:
  pass
  
  
# exposed procedures

def append(s,cp):
  """
  Appends a unicode code point to s
  
  pre:
    s = String to be appended to 
    cp = unicode code point to be appended, as an int
    
  post:
    cp has been appended to s
    
  test:
    s = None
    s = "fred"
      cp = None
      -1
      'a'
      ord('a')
  """
  type_checking2_0.check_identical(s,String)
  type_checking2_0.check_identical(cp,int)
  _check_in_range(cp)
  s._string.append(cp)
  
  
def append_a_copy(s1,s2):
  """
  pre:
    s1 = String to which s2 is to be appended
    s2 = String to be appended to s1
    
  post:
    a copy of s2 has been appended to s1
    
  note:
    this procedure takes time O(length_of(s2))
    
  test:
    s1 = None
    s1 = "abc"
      s2 = None
      s2 = ""
      s2 = "def"
  """
  type_checking2_0.check_identical(s1,String)
  type_checking2_0.check_identical(s2,String)
  for cp in s2._string:
    s1._string.append(cp)
  
  
def code_point_at(s,i):
  """
  pre:
    s = String whose constituent code point is to be found
    i = offset within s of required code point, as an int
    
  post:
    required code point has been returned, as an int

  test:
    s = None
    s = "abc"
      i = True
      i = -1
      i = 0
      i = 2
      i = 3
  """
  type_checking2_0.check_identical(s,String)
  type_checking2_0.check_identical(i,int)
  if (i < 0 or i >= len(s._string)):
    raise Exception("Code point index i is out of range: i = "+ str(i))   
  return s._string[i]

  
def equals(s1,s2):
  """
  pre:
    s1, s2 = Strings to be compared
    
  post:
    returns true iff s1 and s2 have the same Unicode code points in the same order
    
  note:
    this procedure takes time O(length_of(s1))
    
  test:
    s1 = None
    s1 = "abc"
    equals(s1,s1)
    s1 = ""
      s2 = None
      s2 = "x"
      s2 = ""
    s1 = "xyz"
      s2 = "yyz"
      s2 = "xyy"
      s2 = "xyza"
      s2 = "xy"
      s2 = "xyz"
  """
  type_checking2_0.check_identical(s1,String)
  type_checking2_0.check_identical(s2,String)
  if len(s1._string) != len(s2._string):
    return False
  i = 0
  while i < len(s1._string):
    if s1._string[i] != s2._string[i]:
      return False
    i= i + 1
  return True
  
  
def insert(s,i,cp):
  """
  pre:
    s = Unicode string to be inserted into
    i = offset in s where the code point cp is to be inserted, as an int
    cp = code point to be inserted into s, as an int
    
  post:
    cp has been inserted into s at offset i
      
  note:
    this procedure takes time O(length_of(s))
    
  test:
    s = null
    s = "efg"
      cp = -1
      cp = 'x'
      cp = ord('x')
        i = 'a'
        i = -1
        i = 0
        i = 1
        i = 3
        i = 4
  """
  type_checking2_0.check_identical(s,String)
  type_checking2_0.check_identical(i,int)
  type_checking2_0.check_identical(cp,int)
  _check_in_range(cp);
  if i < 0 or i > len(s._string):
    raise Exception("Code point index i is out of range: i=" + str(i))
  s._string.insert(i,cp)
  

def is_valid_code_point(cp):
  """
  pre:
    cp = putative Unicode UTF-32 code point, as an int
    
  post:
    true has been returned iff cp is a valid Unicode UTF-32 code point,
      otherwise false
  
  test:
  cp = None
     -1
     0
     0xD7FF
     0xD800
     0xDFFF
     0xE000
     0x10FFFF
     0x110000
  """
  type_checking2_0.check_identical(cp,int)
  return (cp >= 0 and cp < 0xD800) or (cp > 0xDFFF and cp <= 0x10FFFF)
  
  
def length_of(s):
  """
  pre:
    s = String whose length is to be determined
    
  post:
    length (number of code points) of s has been returned, as an int

  test:
    s = None
    s = ""
    s = "fred"
  """
  type_checking2_0.check_identical(s,String)
  return len(s._string)
  

def new_string():
  """
  post:
    new empty String has been returned
    
  test:
    once thru
  """
  s = String()
  s._string = []
  return s
  

def python_string_of(s):
  """
  pre:
    s = String to be converted to a Python str
    
  post:
    returns python str version of s
    
  note:
    this procedure takes time O(length_of(s))

  test:
    s = None
    s = ""
    s = U+0000,U+FFFF,U+10000,U+10FFFF
  """
  type_checking2_0.check_identical(s,String)
  l = []
  for cp in s._string:
    l.append(chr(cp))
  return "".join(l)
  
  
def remove(s,i):
  """
  pre:
    s = String to be removed from
    i = offset in s at which the code point is to be removed, as an int
    
  post:
    the code point at offset i has been removed from s
      
  note:
    this procedure takes time O(length_of(s)) 
  test:
  s = None
  s = ""
    i = None
    i = 0
  s = "ghi"
    i = -1
       0
       2
       1
  """
  type_checking2_0.check_identical(s,String)
  type_checking2_0.check_identical(i,int)
  if i < 0 or i >= len(s._string):
    raise Exception("Code point offset i is out of range: i=" + str(i))
  s._string[i:i+1] = []


def string_of(ps):
  """
  pre:
    ps = Python str to be converted to String
    
  post:
    String equivalent to ps has been returned
    
  note:
    this procedure takes time of O(length of ps)
    
  test:
    ps = None
    ps = ""
    ps = "fred"
  """
  type_checking2_0.check_identical(ps,str)
  s = new_string();
  for c in ps:
    s._string.append(ord(c))
  return s
  

# private procedures

def _check_in_range(cp):
  """
  pre:
    cp = putative UTF-32 code point to be checked
    
  post:
    if cp is in range,
      procedure returns normally
    or
      a RuntimeException has been thrown
      
  note:
     UTF-32 explicitly prohibits code points greater than U+10FFFF (and also the high and low surrogates U+D800 through U+DFFF).
     
  test:
    cp = -1
       0
  """
  if (not  is_valid_code_point(cp)):
    raise Exception("Invalid UTF-32 code point: U+"+hex(cp))

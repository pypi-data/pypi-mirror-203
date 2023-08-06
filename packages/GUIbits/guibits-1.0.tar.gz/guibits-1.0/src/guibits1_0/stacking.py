# Bounded structure representing the top n elements of a generic stack.

# author R.N.Bosworth

# version 14 Sep 2021 15:12

from . import type_checking2_0
from enum import Enum

"""

Copyright (C) 2011,2019,2021  R.N.Bosworth

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
# -------------

class StackTop:
  pass


# exposed procedures
# ------------------

def clear(st):
  """
  pre:
    st = StackTop which is to be cleared
    
  post:
    st has been cleared of elements
 
  test:
    st = None
    st = valid StackTop
  """
  type_checking2_0.check_identical(st,StackTop)
  st._toff = st._boff = st._size = 0
  

def new_stack_top(n):
  """
  pre:
    n = maximum size of StackTop
    n must be > 0
  
  post:
    StackTop object of size n has been instantiated.
          
  note:
    this method takes time of order n.

  test:
    n = None
    n = 0
        1
  """
  type_checking2_0.check_identical(n,int)
  if n < 1:
    raise Exception("attempt to create StackTop with size < 1: n = " + str(n))

  st = StackTop()
  st._my_circle = []
  for i in range(n):
    st._my_circle.append(None)
  st._toff = st._boff = st._size = 0
  st._max = n
  return st
    
  
def pop(st):
  """
  pre:
    st = StackTop from which item is to be popped
    st must have at least one item
    
  post:
    top element of st has been removed and returned

  test:
    st = None
    stack empty
    stack has one element
    stack has many elements
  """
  type_checking2_0.check_identical(st,StackTop)
  if st._size == 0:
    raise Exception("attempt to pop empty StackTop")    
  else:
    st._toff = _dec(st._toff,st._max)
    st._size -= 1
    return st._my_circle[st._toff]
    
  

def push(st,e):
  """
  pre:
    st = StackTop onto which item is to be pushed
    e = item to be pushed onto top of stack
    
  post:
    e is the top item of stack
    the size of the stack is <= n
    the bottom item of the stack may have been lost

  note: this operation take time O(number of elements in stack)
  test:
    st = None
    stack almost full
    stack full
  """
  type_checking2_0.check_identical(st,StackTop)
  st._my_circle[st._toff] = e
  st._toff = _inc(st._toff,st._max)
  if st._size == st._max:
    st._boff = _inc(st._boff,st._max)
  else:
    st._size += 1


def size(st):
  """
  pre:
    st = StackTop whose size is required
    
  post: 
    number of items in st has been returned

  test:
    st = None
    st = valid StackTop
  """
  type_checking2_0.check_identical(st,StackTop)
  return st._size
  
  
# private members
# ---------------

def _dec(i,max):
  """
  pre:
    i = offset to be decremented
    max = size of circular buffer of which i is an offset

  post:
    returns circurlarly-decremented value of i

  test:
    i = 1
        0
  """
  if i == 0:
    return max - 1
  else:
    return i - 1
    

def _inc(i,max):
  """
  pre:
    i = offset to be incremented
    max = size of circular buffer of which i is an offset

  post:
    returns circularly-incremented value of i

  test:
    i = max-2
        max-1
  """
  if i == max - 1:
    return 0
  else:
    return i + 1

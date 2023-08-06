"""
Contractor which manipulates a ListOfLatest, 
a bounded structure representing the top n elements of a generic list.
Elements are pushed onto the top of the list.
There are no duplicates in the list.
"""

# author R.N.Bosworth

# version 13 Sep 2021  15:32

from . import type_checking2_0

"""
Copyright (C) 2011,2016,2017,2020,2021  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# exported type
# -------------

class ListOfLatest:
    pass
    
    
# exported procedures
# -------------------
    
def get(lol,i):
  """
  pre:  
    lol = ListofLatest to be accessed
    i = offset in list of required element (counting from the top)
   
  post:
    returns required element of this list

  test:
    lol = None
    lol is valid list
      lol is empty
        i = -1
        i = 0
      lol has 1 element
        i = -1
        i = 0
        i = 1
      lol has 2 elements
        i = -1
        i = 0
        i = 1
        i = 2
      another element added to lol (lol has 2 elements)
        i = -1
        i = 0
        i = 1
        i = 2
  """
  type_checking2_0.check_derivative(lol,ListOfLatest)
  type_checking2_0.check_identical(i,int)
  if i < 0 or i >= lol._size:
      raise Exception("Index i is out of bounds: i = "+str(i))
  return lol._my_circle[_residue_of(lol._toff-1-i,lol._size)]
    

def new_list_of_latest(n):
  """
  pre:
    n = maximum size of ListOfLatest
    n > 0
      
  post: 
    ListOfLatest object of size n has been instantiated.
          
  note:
      this method takes time of order n.

  test:
    n = None
    n = 1
        0
  """
  type_checking2_0.check_identical(n,int)
  if n < 1:
    raise Exception("attempt to create ListOfLatest with maximum size < 1: n = " + str(n))
  else:
    lol = ListOfLatest()
    # make a fixed size list
    lol._my_circle = []
    for i in range(n):
       lol._my_circle.append(None)
        
    lol._toff = lol._boff = lol._size = 0
    lol._max = n
  return lol
    

def push(lol,e):
  """
  pre:
    lol = ListOfLatest which is to have an element pushed onto it
    e = element to be pushed onto top of list
    
  post:
    e is the top element of list
    any duplicate of e in the list has been removed
      (A duplicate d of e is one for which d == e)
    the size of the list is <= n
    the bottom element of the list may have been lost
    
  note:
    this operation takes time of order(num of items in list)
    
  test:
    lol = None
    lol is valid list
      list almost empty
        duplicate element
        non-duplicate element
      list almost _full
        duplicate element
        non-duplicate element
      list _full
        duplicate element
        non-duplicate element
  """
  type_checking2_0.check_derivative(lol,ListOfLatest)
  _full = (lol._toff == lol._boff and lol._size != 0)
  _ioff = lol._toff
  _found = False
  while _full or _ioff != lol._boff:
    _ioff = _dec(lol,_ioff)
    if e == lol._my_circle[_ioff]:
      _found = True
      break
    _full = False
  # either _found, and _my_circle[_ioff] is the duplicate
  # or not _found
  if _found:
    _toffminus = _dec(lol,lol._toff)
    while _ioff != _toffminus:
      _ioffplus = _inc(lol,_ioff)
      lol._my_circle[_ioff] = lol._my_circle[_ioffplus]
      _ioff = _ioffplus
    lol._my_circle[_ioff] = e
  else:
    lol._my_circle[lol._toff] = e
    lol._toff = _inc(lol,lol._toff)
    if lol._size == lol._max:
      lol._boff = _inc(lol,lol._boff)
    else:
      lol._size += 1


def size(lol):
  """
  pre:
    lol = ListOfLatest whose size is required
    
  post: 
    number of elements of lol has been returned
  
  test:
    lol = None
    lol is valid list
  """
  type_checking2_0.check_derivative(lol,ListOfLatest)
  return lol._size
  

# private members
# ---------------

def _dec(lol,i):
    """
    pre:
        lol = ListOfLatest whose offset is to be decremented
        i = offset to be decremented
        lol._max = size of circular buffer of which i is an offset
        
    post:
        returns circularly-decremented value of i
        
    test:
        i = 1
            0
    """
    if i == 0:
        return lol._max - 1
    else:
        return i - 1
        
    
def _inc(lol,i):
    """
    pre:
        lol = ListOfLatest whose offset is to be incremented
        i = offset to be incremented
        lol._max = size of circular buffer of which i is an offset
    post:
        returns circularly-incremented value of i

    test:
        i = _max-2
            _max-1
    """
    if i == lol._max - 1:
        return 0
    else:
        return i + 1
        
    
def _residue_of(i,n):
    """
    pre:
        i = integer whose common residue modulo n is to be _found
        n = modulo for which common residue is to be calculated
                  (must be > 0)
    post:
        returns common residue of i modulo n
        This is guaranteed to be in the range 0..n-1
      """
    """

    test:
      n = 1
        i = -2
        i = -1
        i = 0
        i = 1
        i = 2
      n = 2
        i = -2
        i = -1
        i = 0
        i = 1
        i = 2
    """
    r = i%n
    if r < 0:
        return r + n
    else:
        return r
    # frig of the year award

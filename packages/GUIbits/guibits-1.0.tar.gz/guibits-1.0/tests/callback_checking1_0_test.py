# test program for contractor for checking callback functions and methods

# version 25 Jul 2022 15:37

# author RNB

from guibits1_0 import callback_checking1_0
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

def fred():
  pass

def fred2(a):
  pass

def fred3(b,c):
  pass

def fred4(a,c):
  pass

def fred5(a,b):
  pass
  
class Test:
  def james():
    pass

  def jim(self):
    pass

  def jim2(self,a):
    pass

  def jim3(self,b,c):
    pass

  def jim4(self,a,c):
    pass

  def jim5(self,a,b):
    pass
  

def _test():

  print("check_function",end=' ')
  #callback_checking1_0.check_function(None,[])
  #callback_checking1_0.check_function(fred2,[])
  callback_checking1_0.check_function(fred,[])
  #callback_checking1_0.check_function(fred,['a','b'])
  #callback_checking1_0.check_function(fred2,['a','b'])
  #callback_checking1_0.check_function(fred3,['a','b'])
  #callback_checking1_0.check_function(fred4,['a','b'])
  callback_checking1_0.check_function(fred5,['a','b'])
  print("OK")
  
  print("check_method",end=' ')
  t = Test()
  #callback_checking1_0.check_method(None,[])
  #callback_checking1_0.check_method(t.james,[])
  #callback_checking1_0.check_method(t.jim2,[])
  callback_checking1_0.check_method(t.jim,[])
  #callback_checking1_0.check_method(t.jim,['a','b'])
  #callback_checking1_0.check_method(t.jim2,['a','b'])
  #callback_checking1_0.check_method(t.jim3,['a','b'])
  #callback_checking1_0.check_method(t.jim4,['a','b'])
  callback_checking1_0.check_method(t.jim5,['a','b'])
  print("OK")
  
  print("")
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

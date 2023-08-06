#contractor for checking callback functions and methods

# version 13 Sep 2021   12:27

# author RNB

import inspect

"""
Copyright (C) 2020,2021  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed procedures
# ------------------

def check_function(f,ps):
  """
  pre:
    f = putative function to be checked
    ps = list of parameter names for function, as strings
    
  post:
    f has been checked and if it is not a function,
      or has the wrong number of parameters,
        or the parameters have the wrong names
          an exception has been raised
          
  test:
    f is not a function
    f is a function
      ps = []
        f = fred2(a)
        f = fred()
      ps = ['a','b']
        f = fred()
        f = fred2(a)
        f = fred3(b,c)
        f = fred4(a,c)
        f = fred5(a,b)
  """
  if not inspect.isfunction(f):
    raise Exception(str(f) + " is not a function")
  _check_signature(f,ps)


def check_method(f,ps):
  """
  pre:
    f = putative method to be checked
    ps = list of parameter names for method
           (excluding the initial instance object "self" parameter),
             as strings
    
  post:
    f has been checked and if it is not a method,
      or has the wrong number of parameters,
        or the parameters have the wrong names
          an exception has been raised
          
  test:
    f is not a method
    f is a method
      f = james()
      ps = []
        f = jim2(self,a)
        f = jim(self)
      ps = ['a','b']
        f = jim(self)
        f = jim2(self,a)
        f = jim3(self,b,c)
        f = jim4(self,a,c)
        f = jim5(self,a,b)
  """
  if not inspect.ismethod(f):
    raise Exception(str(f) + " is not a method")
  _check_signature(f,ps)

    
# private members
# ---------------
    
def _check_signature(f,ps):
  """
  pre:
    f = method whose signature is to be checked
    ps = list of parameter names for method, as strings
    
  post:
    if f has the wrong number of parameters,
      or the parameters have the wrong names
        an exception has been raised
    
  test:
    ps = []
      f = fred2(a)
      f = fred()
    ps = ['a','b']
      f = fred()
      f = fred2(a)
      f = fred3(b,c)
      f = fred4(a,c)
      f = fred5(a,b)
  """
  sig = inspect.signature(f)
  pcard = len(sig.parameters)
  if pcard != len(ps):
    raise Exception(str(f) + " has the wrong number of parameters: is "+ \
      str(pcard) + ", should be " + str(len(ps)))
  params = list(sig.parameters)
  j = 0
  while j < len(params):
    if params[j] != ps[j]:
      raise Exception(str(f) + " has wrong parameter name: is " + \
        params[j] + ", should be " + ps[j])
    j += 1

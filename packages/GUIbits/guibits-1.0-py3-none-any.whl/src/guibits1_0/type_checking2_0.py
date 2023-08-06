#contractor for checking the type of a variable

# version 13 Sep 2021  12:32

# author RNB

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

def check_derivative(v,t):
  """
  pre:
    v = variable to be checked
    t = type name for required type of v
    
  post:
    either:
      v is an instance of t or a derivative of t and no action has been taken
    or:
      v is not an instance of t or a derivative of t and an exception has been raised
      
  test:
      v = None
      v = "hello"
      v is a valid file
  """
  if not isinstance(v,t):
    raise Exception(str(v) + " is not of type " + str(t) + " or its derivatives")
    

def check_identical(v,t):
  """
  pre:
    v = variable to be checked
    t = type name for required type of v
    
  post:
    either:
      the type is correct and no action has been taken
    or:
      the type is incorrect and an exception has been raised
      
  test:
    t = str
      v = None
      v = str
  """
  if type(v) is not t:
    raise Exception(str(v) + " is not of type " + str(t))

class CursorListener:

# author R.N.Bosworth


# version 30 Sep 2017  12:45
  """
  Listener (Observer) interface for cursor events.

  Copyright (C) 2014,2015,2016,2017  R.N.Bosworth

      This program is free software: you can redistribute it and/or modify
      it under the terms of the GNU Lesser General Public License as published by
      the Free Software Foundation, either version 3 of the License, or
      (at your option) any later version.

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      GNU Lesser General Public License (lgpl.txt) for more details.
  """

def cursor_has_changed():
  """
  pre:
    the cursor has just changed its state in some way
  post:
    any required action has been carried out
  """
  pass
  
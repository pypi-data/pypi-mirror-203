import threading

# The cursor blinking thread.

# version 13 Sep 2021  12:48

# author R.N.Bosworth

"""
Allows the client to instantiate a new thread object which  blinks the cursor 
repeatedly.
To start the thread, use the start() method.
To stop the thread, use the please_drop_dead() method.

Copyright (C) 2010,2014,2015,2016,2017,2020  R.N.Bosworth

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License (lgpl.txt) for more details.


"""

# exported types
# --------------

class _Cursor:
  _is_colored = True
  _my_lock = threading.Lock()
  _my_blinker = None
  _my_window = None


class _CursorBlinker(threading.Thread):

  def run(self):
    """
    pre:
      self = _CursorBlinker which is to be run in a new thread
      
    post:
      the _CursorBlinker thread object has been started in a new thread
      
    test:
      once thru
    """
    e = threading.Event()
    while not self._drop_dead:
      try:
        e.wait(0.5)
        # wait for half a second
        with self._my_cursor._my_lock:
          self._my_cursor._is_colored =  not self._my_cursor._is_colored
        self._my_callback(self._my_cursor)
      except Exception:
        raise Exception("_CursorBlinker:exception")
    
    
  def please_drop_dead(self):
    """
    pre:
      self = _CursorBlinker thread object which is to be stopped
      
    post:
      _CursorBlinker thread object has been politely requested to terminate itself
      
    test:
      once thru
    """
    self._drop_dead = True
    

# constructor
# -----------

"""
  pre:
    cursor = cursor which is to be flipped
    cursor_changed = callback procedure which is to be run whenever the 
                 cursor is flipped

  post:
    cursor blinker has been constructed for the given cursor and callback
    
  test:
    once thru
  """
def new_cursor_blinker(cursor,cursor_changed):
  _cb = _CursorBlinker()
  _cb._my_cursor = cursor
  _cb._my_callback = cursor_changed
  _cb._drop_dead = False
  return _cb

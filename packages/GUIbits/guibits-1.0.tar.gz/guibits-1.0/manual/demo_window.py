import windowing

# Demo program for a window

# version 16 Jun 2021   12:38

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

win = windowing.new_window(20.0,"Demo Window",600.0,450.0,1.0)
windowing.show(win,None,None)

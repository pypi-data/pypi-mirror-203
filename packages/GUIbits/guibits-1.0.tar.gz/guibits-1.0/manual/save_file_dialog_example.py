import file_dialoging

# author R.N.Bosworth

# version 16 Jun 2021   11:57

"""
Svae file dialog example.

Copyright (C) 2015,2019,2020,2021  R.N.Bosworth

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

exs = ["txt","py"]

sm = file_dialoging.SortMode.ALPHABETIC

user_reply = \
file_dialoging.show_save_file_dialog(16.0,"Save","C:\\Users\\User\\Documents\\hello.mle",exs,sm)
print("user_reply="+str(user_reply))
print("OK")

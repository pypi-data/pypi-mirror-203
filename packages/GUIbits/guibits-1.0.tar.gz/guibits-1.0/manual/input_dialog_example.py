import dialoging

# author R.N.Bosworth

# version 16 Jun 21   12:22

"""
Example of input dialog.

Copyright (C) 2021  R.N.Bosworth

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License (gpl.txt) for more details.
"""

user_reply = \
  dialoging.show_input_dialog(16.0,"Address query","Please enter your postcode:")
print("user_reply="+str(user_reply))

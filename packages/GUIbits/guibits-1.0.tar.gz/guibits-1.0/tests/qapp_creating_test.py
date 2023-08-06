# test of contractor for creating a singleton QApplication

# version 26 Jul 2022 17:46

# author RNB

from guibits1_0 import qapp_creating

"""
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

# test program
# ------------

def _test():
  print("test _get_qapp")
  qapp1 = qapp_creating._get_qapp()
  qapp2 = qapp_creating._get_qapp()
  assert qapp1 == qapp2
  print("OK")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

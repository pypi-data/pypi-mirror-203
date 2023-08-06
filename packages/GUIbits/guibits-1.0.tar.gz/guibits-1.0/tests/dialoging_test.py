# Test of Contractor for GUI dialogs.

# author R.N.Bosworth

# version 28 Jul 22  20:08

from guibits1_0 import dialoging

"""
Copyright (C) 2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License (lgpl.txt) for more details.
"""

# test program
# ------------
    
def _test():
  print("Tests of escaped",end=' ')
  assert dialoging.escaped("") == ""
  s = dialoging.escaped("the <p> tag indicates a paragraph & the <b> tag bold")
  assert s == "the &lt;p&gt; tag indicates a paragraph &amp; the &lt;b&gt; tag bold"
  print("OK")
  
  print("Tests of show_message_dialog", end = ' ')
  #dialoging.show_message_dialog(5,None,None)
  #dialoging.show_message_dialog(5.0,None,None)    
  #dialoging.show_message_dialog(10.0,"","")
  #dialoging.show_message_dialog(10.0,"t",11.0)
  #dialoging.show_message_dialog(10.0,"grenoble","")
  dialoging.show_message_dialog(10.0,"grenoble","y")
  #dialoging.show_message_dialog(25.0,None,None)  
  #dialoging.show_message_dialog(6.0,None,None)  
  dialoging.show_message_dialog(10.0,"grenoble","<p>")
  dialoging.show_message_dialog(10.0,"Tests of message dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  dialoging.show_message_dialog(16.0,"Tests of message dialog","A short string")
  dialoging.show_message_dialog(16.0,"Tests of message dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  dialoging.show_message_dialog(24.0,"Tests of message dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  dialoging.show_message_dialog(24.0,"Tests of message dialog","filename1/filename2/filename3/filename4/filename5/filename6/filename7/filename8/filename9")
  dialoging.show_message_dialog(24.0,"Tests of message dialog","a long string with a word:\n\nantidisestablishmentarianism")
  print("OK")
  
  
  print("Tests of show_confirm_dialog")
  #reply = dialoging.show_confirm_dialog(None,None,None)
  #reply = dialoging.show_confirm_dialog(24.1,None,None)
  #reply = dialoging.show_confirm_dialog(24.0,None,None)
  #reply = dialoging.show_confirm_dialog(10.0,"",None)
  #reply = dialoging.show_confirm_dialog(10.0,"x",None)
  #reply = dialoging.show_confirm_dialog(10.0,"grenoble","")
  reply = dialoging.show_confirm_dialog(10.0,"grenoble","y")
  print("reply=" + str(reply))
  reply = dialoging.show_confirm_dialog(10.0,"grenoble","<p>")
  print("reply=" + str(reply))
  reply = dialoging.show_confirm_dialog(10.0,"Tests of confirm dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  print("reply=" + str(reply))
  reply = dialoging.show_confirm_dialog(16.0,"Tests of confirm dialog","A short string")
  print("reply=" + str(reply))
  reply = dialoging.show_confirm_dialog(16.0,"Tests of confirm dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  print("reply=" + str(reply))
  reply = dialoging.show_confirm_dialog(24.0,"Tests of confirm dialog","a very long long long string with a long long word: antidisestablishmentarianism")
  print("reply=" + str(reply))
  print("OK")
  
  print("Tests of show_input_dialog")
  #dialoging.show_input_dialog(5.9,None,None)
  #dialoging.show_input_dialog(6.0,None,None)
  #dialoging.show_input_dialog(24.1,None,None)
  #dialoging.show_input_dialog(24.0,"",None)
  #dialoging.show_input_dialog(24.0,"",None)
  #dialoging.show_input_dialog(10.0,"x",None)
  #dialoging.show_input_dialog(10.0,"florestan","")
  reply = dialoging.show_input_dialog(10.0,"florestan","y")
  print("reply=" + str(reply))
  reply = dialoging.show_input_dialog(10.0,"Name query","Please enter your name:")
  print("reply=" + str(reply))
  reply = dialoging.show_input_dialog(20.0,"Name query","Please enter your name:")
  print("reply=" + str(reply))
  reply = dialoging.show_input_dialog(24.0,"Name query","Please enter your name:")
  print("reply=" + str(reply))
  print("OK")
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

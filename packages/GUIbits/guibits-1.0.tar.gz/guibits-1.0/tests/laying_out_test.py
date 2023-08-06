# test of contractor for laying out PyQt widgets in a horizontal line,
# with left, centre or right alignment

# version 26 Jul 2022  17:56

# author RNB

import PyQt6.QtWidgets
from guibits1_0 import laying_out
from guibits1_0 import qapp_creating

"""
Copyright (C) 2020,2021,2022  R.N.Bosworth

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

def pr(s,v):
  print(s+"="+str(v))

def prmin(s,v):
  w = v.minimumSize().width()
  h = v.minimumSize().height()
  print(s+".minimumSize()="+"("+str(w)+","+str(h)+")")
  
def prhint(s,v):
  w = v.sizeHint().width()
  h = v.sizeHint().height()
  print(s+".sizeHint()="+"("+str(w)+","+str(h)+")")
  
def prgeom(s,v):
  g = v.geometry()
  x = g.x()
  y = g.y()
  w = g.width()
  h = g.height()
  print(s+".geometry()=("+str(x)+","+str(y)+","+str(w)+","+str(h)+")")

def prrect(s,v):
  x = v.x()
  y = v.y()
  w = v.width()
  h = v.height()
  print(s+"=("+str(x)+","+str(y)+","+str(w)+","+str(h)+")")


class TestLayout1223(PyQt6.QtWidgets.QLayout):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(12,23)

class TestSpacerItem3445(PyQt6.QtWidgets.QSpacerItem):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(34,45)

class TestWidget3344(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(33,44)

class TestWidget1223(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(12,23)
    
class TestWidget1324(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(13,24)
    
class TestWidget1425(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(14,25)
    
class TestWidget1524(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(15,24)
    
class TestWidget1623(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(16,23)
    
class TestWidget1724(PyQt6.QtWidgets.QWidget):

  def sizeHint(self):
    return PyQt6.QtCore.QSize(17,24)
    
def _test():
  print("_width_of",end= ' ')
  _qapp = qapp_creating._get_qapp()
  qw = TestWidget3344()
  qw.setMinimumWidth(34)
  qli = PyQt6.QtWidgets.QWidgetItem(qw)
  assert laying_out._width_of(qli) == 34
  ql = laying_out.LineLayout()
  ql._minimum_size = PyQt6.QtCore.QSize(11,22)
  assert laying_out._width_of(ql) == 11
  qsi =  PyQt6.QtWidgets.QSpacerItem(55,66)
  assert laying_out._width_of(qsi) == 55  
  qw2 = TestWidget3344()
  qw2.setMinimumWidth(32)
  qli2 = PyQt6.QtWidgets.QWidgetItem(qw2)
  assert laying_out._width_of(qli2) == 33
  print("OK")
  
  print("_height_of",end= ' ')
  qw = TestWidget3344()
  qw.setMinimumHeight(45)
  qli = PyQt6.QtWidgets.QWidgetItem(qw)
  assert laying_out._height_of(qli) == 45
  ql = laying_out.LineLayout()
  ql._minimum_size = PyQt6.QtCore.QSize(11,22)
  assert laying_out._height_of(ql) == 22
  qsi =  PyQt6.QtWidgets.QSpacerItem(55,66)
  assert laying_out._height_of(qsi) == 66  
  qw2 = TestWidget3344()
  qw2.setMinimumHeight(43)
  qli2 = PyQt6.QtWidgets.QWidgetItem(qw2)
  assert laying_out._height_of(qli2) == 44
  print("OK")
  
  print("_update_minimum_size", end = ' ')
  qs = PyQt6.QtCore.QSize(12,34)
  qli = PyQt6.QtWidgets.QSpacerItem(56,35)
  laying_out._update_minimum_size(qs,qli)
  assert qs.width() == 68
  assert qs.height() == 35
  qli = PyQt6.QtWidgets.QSpacerItem(56,34)
  laying_out._update_minimum_size(qs,qli)
  assert qs.width() == 124
  assert qs.height() == 35
  print("OK")
  
  print("test of instantiating a QWidget",end=' ')
  _qapp = qapp_creating._get_qapp()
  qw = PyQt6.QtWidgets.QWidget()
  assert qw.layout() == None
  print("OK")

  print("_set_parent_widget", end = ' ')
  ql = PyQt6.QtWidgets.QHBoxLayout()
  assert ql.parent() == None
  qw = PyQt6.QtWidgets.QWidget()
  assert qw.parent() == None
  #laying_out._set_parent_widget(ql,qw)
  qw2 = PyQt6.QtWidgets.QWidget()
  ql.setParent(qw2)
  laying_out._set_parent_widget(ql,qw)
  assert qw.parent() == qw2
  qw3 = PyQt6.QtWidgets.QWidget()
  ql2 = PyQt6.QtWidgets.QHBoxLayout(qw3)
  ql3 = PyQt6.QtWidgets.QHBoxLayout()
  ql2.addLayout(ql3)
  ql4 = PyQt6.QtWidgets.QHBoxLayout()
  ql3.addLayout(ql4)
  qw4 = PyQt6.QtWidgets.QWidget()
  laying_out._set_parent_widget(ql4,qw4)
  assert qw4.parent() == qw3  
  print("OK")
  
  print("tests of LineLayout")
  
  print("count",end=' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  qli = TestLayout1223()
  ll.addItem(qli)
  ll.addItem(qli)
  assert ll.count() == 2
  print("OK")
  
  print("itemAt",end=' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  #ll.itemAt(None)
  assert ll.itemAt(-1) == None
  assert ll.itemAt(0) == None
  qli = TestLayout1223()
  ll.addItem(qli)
  assert ll.itemAt(1) == None  
  assert ll.itemAt(0) == qli  
  print("OK")
  
  print("takeAt",end=' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  #ll.takeAt(None)
  assert ll.takeAt(-1) == None
  assert ll.takeAt(0) == None
  qwp = PyQt6.QtWidgets.QWidget()
  ll.setParent(qwp)
  qli = TestLayout1223()
  ll.addItem(qli)
  assert ll.count() == 1
  assert ll._centre_partition == 1
  assert ll._right_partition == 1
  qw = TestWidget3344()
  ll.addWidgetCentre(qw)
  assert ll.count() == 2
  assert ll._centre_partition == 1
  assert ll._right_partition == 2
  qw2 = TestWidget1223()
  ll.addWidgetRight(qw2)
  assert ll.count() == 3
  assert ll._centre_partition == 1
  assert ll._right_partition == 2
  assert ll.takeAt(-1) == None
  assert ll.takeAt(3) == None
  assert ll.takeAt(0) == qli
  assert ll.count() == 2
  assert ll._centre_partition == 0
  assert ll._right_partition == 1
  qwi = ll.takeAt(0)
  qw3 = qwi.widget()
  assert qw3 == qw
  assert ll.count() == 1
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  assert ll.takeAt(0).widget() == qw2
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  assert ll.takeAt(0) == None
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  print("OK")
  
  print("minimumSize",end=' ')
  ll = laying_out.LineLayout()
  assert ll.minimumSize() ==  PyQt6.QtCore.QSize(0,0)
  print("OK")
  
  print("sizeHint",end=' ')
  ll = laying_out.LineLayout()
  assert ll.sizeHint() ==  PyQt6.QtCore.QSize(0,0)
  print("OK")
  
  print("addItem",end=' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  assert ll.parent() == None
  assert ll._minimum_size.width() == 0
  assert ll._minimum_size.height() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  #ll.addItem(None)

  qli = TestLayout1223()
  ll.addItem(qli)
  assert ll.count() == 1
  assert qli.parent() == ll
  assert ll._minimum_size.width() == 12
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 1
  assert ll._right_partition == 1
  
  w = TestWidget3344()
  qli = TestLayout1223()
  ll.addItem(qli) 
  assert ll.count() == 2
  assert qli.parent() == ll
  assert ll._minimum_size.width() == 24
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 2
  assert ll._right_partition == 2
  
  s = TestSpacerItem3445(34,45)
  ll.addItem(s) 
  assert ll.count() == 3
  assert ll._minimum_size.width() == 58
  assert ll._minimum_size.height() == 45
  assert ll._centre_partition == 3
  assert ll._right_partition == 3
  
  wi = PyQt6.QtWidgets.QWidgetItem(w)
  #ll.addItem(wi)
  qwp2 = PyQt6.QtWidgets.QWidget()
  ll.setParent(qwp2)
  ll.addItem(wi)
  assert ll.count() == 4
  assert w.parent() == qwp2
  assert ll._minimum_size.width() == 91
  assert ll._minimum_size.height() == 45
  assert ll._centre_partition == 4
  assert ll._right_partition == 4
  
  wi2 = PyQt6.QtWidgets.QWidgetItem(w)
  ll.addItem(wi2)
  assert ll.count() == 5
  assert w.parent() == qwp2
  assert ll._minimum_size.width() == 124
  assert ll._minimum_size.height() == 45
  assert ll._centre_partition == 5
  assert ll._right_partition == 5
  
  wi3 = PyQt6.QtWidgets.QWidgetItem(w)
  ll.addItem(wi3)
  assert ll.count() == 6
  assert w.parent() == qwp2
  assert ll._minimum_size.width() == 157
  assert ll._minimum_size.height() == 45
  assert ll._centre_partition == 6
  assert ll._right_partition == 6
  
  # clean up ll before abandoning
  assert ll.count() == 6
  ll.takeAt(5)
  ll.takeAt(4)
  ll.takeAt(3)
  ll.takeAt(2)
  ll.takeAt(1)
  ll.takeAt(0)
  assert ll.count() == 0
  print("OK")
  
  print("addWidgetCentre", end = ' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  assert ll.parent() == None
  assert ll._minimum_size.width() == 0
  assert ll._minimum_size.height() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  #ll.addWidgetCentre(None)

  tw = TestWidget1223()
  #ll.addWidgetCentre(tw)
  qwp3 = PyQt6.QtWidgets.QWidget()
  ll.setParent(qwp3)
  ll.addWidgetCentre(tw)
  assert ll.count() == 1
  assert tw.parent() == qwp3
  assert ll._minimum_size.width() == 12
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 0
  assert ll._right_partition == 1
  
  tw2 = TestWidget1223()
  ll.addWidgetCentre(tw2)
  assert ll.count() == 2
  assert tw2.parent() == qwp3
  assert ll._minimum_size.width() == 24
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 0
  assert ll._right_partition == 2

  tw3 = TestWidget3344()
  ll.addWidgetCentre(tw3)
  assert ll.count() == 3
  assert tw2.parent() == qwp3
  assert ll._minimum_size.width() == 57
  assert ll._minimum_size.height() == 44
  assert ll._centre_partition == 0
  assert ll._right_partition == 3
  
  # clean up ll before abandoning
  assert ll.count() == 3
  ll.takeAt(2)
  ll.takeAt(1)
  ll.takeAt(0)
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  print("OK")
  
  print("addWidgetRight", end = ' ')
  ll = laying_out.LineLayout()
  assert ll.count() == 0
  assert ll.parent() == None
  assert ll._minimum_size.width() == 0
  assert ll._minimum_size.height() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  #ll.addWidgetRight(None)

  tw = TestWidget1223()
  #ll.addWidgetRight(tw)
  qwp4 = PyQt6.QtWidgets.QWidget()
  ll.setParent(qwp4)
  ll.addWidgetRight(tw)
  assert ll.count() == 1
  assert tw.parent() == qwp4
  assert ll._minimum_size.width() == 12
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  
  tw2 = TestWidget1223()
  ll.addWidgetRight(tw2)
  assert ll.count() == 2
  assert tw2.parent() == qwp4
  assert ll._minimum_size.width() == 24
  assert ll._minimum_size.height() == 23
  assert ll._centre_partition == 0
  assert ll._right_partition == 0

  tw3 = TestWidget3344()
  ll.addWidgetRight(tw3)
  assert ll.count() == 3
  assert tw2.parent() == qwp4
  assert ll._minimum_size.width() == 57
  assert ll._minimum_size.height() == 44
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  
  # clean up ll before abandoning
  assert ll.count() == 3
  ll.takeAt(2)
  ll.takeAt(1)
  ll.takeAt(0)
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  print("OK")
  
  print("setGeometry",end=' ')
  ll = laying_out.LineLayout()
  qwp5 = PyQt6.QtWidgets.QWidget()
  ll.setParent(qwp5)
  #ll.setGeometry(None)
  qr =  PyQt6.QtCore.QRect(1,2,70,40)
  ll.setGeometry(qr)
  g = ll.geometry()
  assert g.x() == 1
  assert g.y() == 2
  assert g.width() == 70
  assert g.height() == 40
  ms = ll.minimumSize()
  assert ms.width() == 0 
  assert ms.height() == 0
  sh = ll.sizeHint()
  assert sh.width() == 0
  assert sh.height() == 0
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0

  qw = TestWidget1223()
  qwi = PyQt6.QtWidgets.QWidgetItem(qw)
  ll.addItem(qwi)
  assert ll.count() == 1
  assert ll._centre_partition == 1
  assert ll._right_partition == 1
  sh = ll.sizeHint()
  assert sh.width() == 12
  assert sh.height() == 23
  ms = ll.minimumSize()
  assert ms.width() == 12 
  assert ms.height() == 23

  qw2 = TestWidget1324()
  qwi2 = PyQt6.QtWidgets.QWidgetItem(qw2)
  ll.addItem(qwi2)
  assert ll.count() == 2
  assert ll._centre_partition == 2
  assert ll._right_partition == 2
  sh = ll.sizeHint()
  assert sh.width() == 25
  assert sh.height() == 24
  ms = ll.minimumSize()
  assert ms.width() == 25 
  assert ms.height() == 24
    
  qw3 = TestWidget1425()
  ll.addWidgetCentre(qw3)
  assert ll.count() == 3
  assert ll._centre_partition == 2
  assert ll._right_partition == 3
  sh = ll.sizeHint()
  assert sh.width() == 39
  assert sh.height() == 25
  ms = ll.minimumSize()
  assert ms.width() == 39 
  assert ms.height() == 25

  qw4 = TestWidget1524()
  ll.addWidgetCentre(qw4)
  assert ll.count() == 4
  assert ll._centre_partition == 2
  assert ll._right_partition == 4
  sh = ll.sizeHint()
  assert sh.width() == 54 
  assert sh.height() == 25
  ms = ll.minimumSize()
  assert ms.width() == 54 
  assert ms.height() == 25
  
  qw5 = TestWidget1623()
  ll.addWidgetRight(qw5)
  assert ll.count() == 5
  assert ll._centre_partition == 2
  assert ll._right_partition == 4
  sh = ll.sizeHint()
  assert sh.width() == 70 
  assert sh.height() == 25
  ms = ll.minimumSize()
  assert ms.width() == 70 
  assert ms.height() == 25
  
  qw6 = TestWidget1724()
  ll.addWidgetRight(qw6)
  assert ll.count() == 6
  assert ll._centre_partition == 2
  assert ll._right_partition == 4
  sh = ll.sizeHint()
  assert sh.width() == 87 
  assert sh.height() == 25
  ms = ll.minimumSize()
  assert ms.width() == 87 
  assert ms.height() == 25
  
  ll.setGeometry(qr)
  g = ll.geometry()
  assert g.x() == 1
  assert g.y() == 2
  assert g.width() == 70
  assert g.height() == 40
  ms = ll.minimumSize()
  assert ms.width() == 87 
  assert ms.height() == 25
  sh = ll.sizeHint()
  assert sh.width() == 87
  assert sh.height() == 25
  assert ll.count() == 6
  
  # clean up ll before abandoning
  assert ll.count() == 6
  assert ll._centre_partition == 2
  assert ll._right_partition == 4
  ll.takeAt(5)
  ll.takeAt(4)
  ll.takeAt(3)
  ll.takeAt(2)
  ll.takeAt(1)
  ll.takeAt(0)
  assert ll.count() == 0
  assert ll._centre_partition == 0
  assert ll._right_partition == 0
  print("OK")
  
  
if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

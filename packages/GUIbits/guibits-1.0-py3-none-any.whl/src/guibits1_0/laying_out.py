# contractor for laying out PyQt widgets in a horizontal line,
# with left, centre or right alignment

# version 26 Jul 2022  17:55

# author RNB

import PyQt6.QtWidgets
import PyQt6.QtCore
from . import qapp_creating
from . import type_checking2_0

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

# exposed types
# -------------

class LineLayout(PyQt6.QtWidgets.QLayout):
  """
  QLayout which lays out its items in a line from left to right,
  with minimal spacing between them.
  The items are given the greater of their minimum and preferred size, 
  and there is no compression or stretching.
  The items are partitioned into three sublists: 
    zero or more left-aligned items, followed by
    zero or more centre-aligned items, followed by
    zero or more right-aligned items
  Invariants:
    self._centre_partition == offset of centre partition in self._children
    self._right_partition == offset of right partition in self._children
    item.y == self.y
    for left-aligned items:
      item.x == self.x + Sigma all items to left: item.width
    for centre-aligned items:
      item.x == (self.width - Sigma all centred items: item.width)/2
    for right-aligned items:
      item.x == self.width - item.width - Sigma all items to right: item width 
    self._minimal_width = Sigma all items : item.width
    self.width >= Sigma all items : item.width
    self.height >= Max(item.height)
    item.parent() isinstance(QWidget) or item.parent() == None    
  """
  
  def __init__(self):
    """
    pre:
      self = LineLayout which is to be initialized
      
    post:
      self has been initialized
      self_children = []
      self._centre_partition = 0
      self._right_partition = 0
      
    test:
      once thru
    """
    self._minimum_size = PyQt6.QtCore.QSize(0,0)
    self._children = []  
    self._centre_partition = 0  # offset of centre partition in _children
    self._right_partition = 0  # offset of right partition in _children
    PyQt6.QtWidgets.QLayout.__init__(self)
    
    
  def addItem(self,qli):
    """
    pre:
      self = LineLayout to which item is to be added
      qli = QLayoutItem to be added to this LineLayout, left-justified
      self must have a QWidget as ancestor
      
    post:
      qli has been added to self
      if qli is a QLayout, it is given self as parent
      if qli is a QWidget, it is given self's ancestor QWidget as parent
    """
    """
    pre:
      self.parent() = parent of this LineLayout or None
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
        
    post:
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
    """
    """
    test:
      qli = None
      qli = a QLayout, width = 12, height = 23 (check parent, _minimum_width, _minimum_height, partition_offset)
        self has no parent
        self has QWidget parent
      qli = a QSpacerItem, width 34, height 45 (check _minimum_width, _minimum_height, partition_offset)
      qli = a QWidget, width 33, height 44 (check parent, _minimum_width, _minimum_height, partition_offset)
        self has QWidget parent
    """
    type_checking2_0.check_derivative(qli,PyQt6.QtWidgets.QLayoutItem)
    self._children.insert(self._centre_partition,qli)
    self._centre_partition += 1
    self._right_partition += 1
    if isinstance(qli,PyQt6.QtWidgets.QLayout):
      qli.setParent(self)
      item = qli
    elif isinstance(qli,PyQt6.QtWidgets.QSpacerItem):
      item = qli
    elif isinstance(qli,PyQt6.QtWidgets.QWidgetItem):
      widget = qli.widget()
      _set_parent_widget(self,widget)
      item = widget
    # item is QLayout, QSpacerItem or QWidget
    _update_minimum_size(self._minimum_size,item)


  def addWidgetCentre(self,qw):
    """
    pre:
      self = the LineLayout to which qw is to be added, 
               right-aligned
      qw = the QWidget to be added to self
      self must have a QWidget as ancestor
    
    post:
      qw has been added to self, centre-aligned
      qw has been given self's ancestor QWidget as parent
    """
    """
    pre:
      self.parent() = parent of this LineLayout or None
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
      
    post:
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
    """
    """
    test:
      qw = None
      qw = a QWidget, width = 12, height = 23 (check parent, _minimum_width, _minimum_height, _right_partition)
        self has no parent 
        self has QWidget parent
      qw = a QWidget, width 33, height 44 (check parent, _minimum_width, _minimum_height, _right_partition)
        self has QWidget parent
    """
    type_checking2_0.check_derivative(qw,PyQt6.QtWidgets.QWidget)
    qwi = PyQt6.QtWidgets.QWidgetItem(qw)
    self._children.insert(self._right_partition,qwi)
    self._right_partition += 1
    _set_parent_widget(self,qw)
    _update_minimum_size(self._minimum_size,qw)


  def addWidgetRight(self,qw):
    """
    pre:
      self = the LineLayout to which qw is to be added, 
               right-aligned
      qw = the QWidget to be added to self
      self must have a QWidget as ancestor
    
    post:
      qw has been added to self, right-aligned
      qw has been given self's ancestor QWidget as parent
    """
    """
    pre:
      self.parent() = parent of this LineLayout or None
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
      
    post:
      self._minimum_width = minimum width of self
      self._minimum_height = minimum height of self
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
    """
    """
    test:
      qw = None
      qw = a QWidget, width = 12, height = 23 (check parent, _minimum_width, _minimum_height, _right_partition)
        self has no parent 
        self has QWidget parent
      qw = a QWidget, width 33, height 44 (check parent, _minimum_width, _minimum_height, _right_partition)
        self has QWidget parent
    """
    type_checking2_0.check_derivative(qw,PyQt6.QtWidgets.QWidget)
    qwi = PyQt6.QtWidgets.QWidgetItem(qw)
    self._children.append(qwi)
    _set_parent_widget(self,qw)
    _update_minimum_size(self._minimum_size,qw)


  def count(self):
    """
    pre:
      self = LineLayout whose child items are to be counted
      
    post:
      number of child items in self has been returned as an int
      
    test:
      no children
      two children
    """
    return len(self._children)
    

  def itemAt(self,index):
    """
    pre:
      self = LineLayout whose item is requested
      index = index of requested item (0..) as int
      
    post:
      requested QLayoutItem has been returned,
        or None if no such item
      
    test:
      self has no children
        index = None
        index = -1
        index = 0
      self has one child
        index = 1
        index = 0
    """
    type_checking2_0.check_identical(index,int)
    if index < 0 or index >= len(self._children):
      return None
    else:
      return self._children[index]
    
  
  def minimumSize(self):
    """
    pre:
      self = LineLayout whose minimum size is requested
      
    post:
      minimum size of this LineLayout has been returned, as QSize
      
    test:
      once thru
    """
    return self._minimum_size
    
    
  def setGeometry(self, qr):
    """
    pre:
      self = LineLayout whose geometry is to be set
      qr = QRect which specified the new geometry of self
      
    post:
      self's geometry has been set to values specified by qr
      a setGeometry has been executed on self's children, 
        in accordance with the layout invariants
      
    test:
      qr = None
      qr = valid QRect (1,2,70,40)
        no children
        2 left-justified children  of size (12,23), (13,24)
          2 centre-justified children of size (14,25),(15,24)
            2 right justified children of size (16,23),(17,24)
    """
    type_checking2_0.check_derivative(qr,PyQt6.QtCore.QRect)
    PyQt6.QtWidgets.QLayout.setGeometry(self,qr)  # QLayout deals with this

    # initialize new minimum size of self
    newms = PyQt6.QtCore.QSize(0,0)  

    # lay out the left-justified children
    x_offset = qr.x()
    y_offset = qr.y()
    i = 0
    while i < self._centre_partition:
      item =self._children[i]
      if isinstance(item, PyQt6.QtWidgets.QWidgetItem):
        item = item.widget()
      width = _width_of(item)
      height = _height_of(item)
      item.setGeometry(PyQt6.QtCore.QRect(x_offset,y_offset,width,height))
      _update_minimum_size(newms,item)
      x_offset += width
      i += 1
    
    # ensure self width is correct
    if self._minimum_size.width() > qr.width():
      self_width = self._minimum_size.width()
    else:
      self_width = qr.width()
      
    # lay out the centre-justified children
    centre_width = 0
    i = self._centre_partition
    while i < self._right_partition:
      item = self._children[i]
      if isinstance(item, PyQt6.QtWidgets.QWidgetItem):
        item = item.widget()
      centre_width = _width_of(item)
      i +=1
    x_offset = int(qr.x() + (self_width - centre_width)/2)
    y_offset = qr.y()
    i = self._centre_partition
    while i < self._right_partition:
      item = self._children[i]
      if isinstance(item, PyQt6.QtWidgets.QWidgetItem):
        item = item.widget()
      width = _width_of(item)
      height = _height_of(item)
      item.setGeometry(PyQt6.QtCore.QRect(x_offset,y_offset,width,height))
      _update_minimum_size(newms,item)
      x_offset += width
      i += 1
    
    # lay out the right-justified children
    x_offset = qr.x() + self_width
    y_offset = qr.y()
    i = len(self._children)-1
    while i >= self._right_partition:
      item =self._children[i]
      if isinstance(item, PyQt6.QtWidgets.QWidgetItem):
        item = item.widget()
      width = _width_of(item)
      height = _height_of(item)
      x_offset -= width
      item.setGeometry(PyQt6.QtCore.QRect(x_offset,y_offset,width,height))
      _update_minimum_size(newms,item)
      i -= 1
    
    # update the minimum size
    self._minimum_size = newms
    
    
  def sizeHint(self):
    """
    pre:
      self = LineLayout whose size hint is to be accessed
      
    post:
      self's size hint has been returned as a QSize
      
    test:
      once thru    
    """
    return self._minimum_size
    
    
  def takeAt(self, index):
    """
    pre:
      self = LineLayout whose item is to be taken
      index = index of item to be taken (0..) as int
      
    post:
      if item exists,
        it has been deleted from self
        it has been returned as a QLayoutItem
      otherwise,
        None has been returned
    """
    """
    pre:
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
        
    post:
      self._children = list of child items
      self._centre_partition = offset of first centre-justified item
        in self._children, if any
      self._right_partition = offset of first right-justified item
        in self._children, if any
    """    
    """
    test:
      self has no children
        index = None
        index = -1
        index = 0
      self has three children, one left, one centre, one right
        index = -1
        index = 3
        index = 0  (check partitions)    
        index = 0  (check partitions)    
        index = 0  (check partitions)    
        index = 0  (check partitions)    
    """
    type_checking2_0.check_identical(index,int)
    if index < 0 or index >= len(self._children):
      return None
    else:
      if index >= self._right_partition:     # right item
        pass
      elif index >= self._centre_partition:  # centre item
        self._right_partition -= 1
      else:                                  # left item
        self._right_partition -= 1
        self._centre_partition -= 1
      return self._children.pop(index)
        
  
# private members
# ---------------

def _height_of(qli):
  """
  pre:
    qli = QLayoutItem  whose height is to be determined
    
  post:
    the greater of the minimum height and the preferred height
      of qli has been returned
      
  test:
    qli.sizeHint().height = qli.minimumSize().height() - 1
      item is QWidget
    qli.sizeHint().height = qli.minimumSize().height()
      item is QLayout
      item is QSpacerItem
    qli.sizeHint().height = qli.minimumSize().height() + 1
      item is QWidget
  """
  if isinstance(qli, PyQt6.QtWidgets.QWidgetItem):
    qli = qli.widget()
  if qli.sizeHint().height() > qli.minimumSize().height():
    return qli.sizeHint().height()
  else:
    return qli.minimumSize().height()


def _set_parent_widget(ql,qw):
  """
  pre:
    ql = QLayout of which qw is a child
    qw = QWidget which is a child of ql
    
  post:
    if ql has a QWidget ancestor, it has been set as qw's parent
    otherwise, an exception has been raised
    
  test:
    ql has no parent
    ql has QWidget parent
    ql has Qlayout parent, which has QLayout parent, which has QWidget parent
  """
  ancestor = ql.parent()
  while ancestor != None and not isinstance(ancestor,PyQt6.QtWidgets.QWidget):
    ancestor = ancestor.parent()
  # ancestor == None or isinstance(ancestor,PyQt6.QtWidgets.QWidget)
  if ancestor == None:
    raise Exception("Attempt to add a QWidget to a LineLayout without a QWidget parent")
  else:
    qw.setParent(ancestor)


def _update_minimum_size(qs,qli):
  """
  pre:
    qs = Qsize which is to be updated
    qli = QLayoutItem which is updating qs

  post:
    the greater of qli's sizeHint width and minimum width 
      has been added to qs
    if the greater of qli's sizeHint height and minimum height
      was greater than qs's,
        qs has been given qli's height

  test:  
    qs = (12,34)
      qli = (56,35)
      qli = (56,34)
  """
  qli_width = _width_of(qli)    
  qs.setWidth(qs.width()+qli_width)
  qli_height = _height_of(qli)    
  if qli_height > qs.height():
    qs.setHeight(qli_height)
  
  
def _width_of(qli):
  """
  pre:
    qli = QLayoutItem  whose width is to be determined
    
  post:
    the greater of the minimum width and the preferred width
      of qli has been returned
      
  test:
    qli.sizeHint().width = qli.minimumSize().width() - 1
      item is QWidget
    qli.sizeHint().width = qli.minimumSize().width()
      item is QLayout
      item is QSpacerItem
    qli.sizeHint().width = qli.minimumSize().width() + 1
      item is QWidget
  """
  if isinstance(qli, PyQt6.QtWidgets.QWidgetItem):
    qli = qli.widget()
  if qli.sizeHint().width() > qli.minimumSize().width():
    return qli.sizeHint().width()
  else:
    return qli.minimumSize().width()


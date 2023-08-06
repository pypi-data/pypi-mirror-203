# contractor for displaying file dialogs

# version 30 Jul 22  18:21

# author RNB

import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.QtWidgets

from enum import Enum
from . import dialoging, font_size_checking, font_sizing
from . import laying_out
from operator import itemgetter
import os.path
from . import qapp_creating, resolving, type_checking2_0

"""
Copyright (C) 2015,2016,2017,2018,2019,2021,2022  R.N.Bosworth

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

SortMode = Enum('SortMode','ALPHABETIC EARLIEST_FIRST LATEST_FIRST')


# exposed procedures
# ------------------

def show_new_folder_dialog(fsize,t,dir):
  """
  pre:
    fsize = point size of text for dialog message, 
              as float in range 6.0..24.0
    t = title of this dialog, as Python string
    dir = pathname of current directory, as Python string
    
  post:
    dialog has been displayed at centre of screen, and user has entered
      the new folder name and pressed the OK button, or has pressed the 
        Close button or Esc key
    if the user pressed the OK button,
      a new folder has been created in the directory dir, with the name 
        given by the user
      the simple name of the folder has been returned,
        as a Python string 
    if the user pressed the Close button or the Esc key,
      no new folder has been created
      None has been returned 

  test:
    fsize = 5.9
            6.0
            12.0
      t = None
          ""
          "a"
        dir = None
        dir = ""
        dir = invalid directory
        dir = valid directory
        dir = very long name (to test wrapping)
          user reply ""
          user reply is invalid
          user reply already exists
          user reply OK
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("Attempt to show dialog with empty title string")
  type_checking2_0.check_identical(dir,str)
  if not os.path.isdir(dir):
    message = "Attempt to create folder in non-existent directory: \"" +     dir + "\". Reverting to default directory."
    dialoging.show_message_dialog(fsize,"Non-existent directory",message)
    dir = os.path.expanduser("~")
    
  #  now display an input dialog to get the directory name
  prompt = "Current folder: " + dir + "\n\nFolder name:"
  reply = ""
  while reply == "":
    reply = dialoging.show_input_dialog(fsize,t,prompt)
    if reply == None:
      return None
    if reply != "":
      # reply != None and reply != ""     
      pn = os.path.join(dir,reply)
      try:
        os.mkdir(pn)
      except Exception as ex:
        dialoging.show_message_dialog(fsize,"Exception","Exception:"+str(ex))
        reply = ""  # to ensure re-display of dialog
      # reply is valid or ""
  # reply is valid directory name
  return reply
  

def show_open_file_dialog(fsize,t,f,sm):
  """
  pre:
    fsize = point size of text for dialog message, as float in range 6.0..24.0
    t = title of this dialog, as Python string
    f = pathname of default file to be opened as Python string,
        or the empty string for the root directory and no file
        or None for the user's default directory and no file 
    sm = SortMode for displaying the directory
    
  post:
    dialog has been displayed at centre of screen, and user has pressed one of the buttons.
    returns:
        pathname of selected file if the Open button was hit
        None if the Cancel button or Close button was hit
        None if the user pressed the Esc key

  test:
    fsize = None
    fsize = 5.9
    fsize = 6.0
    fsize = 24.0
      t = None
      t = ""
      t = "Title"
        f = None
          sm = None
          sm = SortMode.ALPHABETIC
        f = ""
        f = "invalid.py"
        f = "C:\\temp\\"
          sm = SortMode.ALPHABETIC
        f = "C:\\Users\\User\\diskpart"
          sm = SortMode.EARLIEST_FIRST
        f = "C:\\EmptyFolder\\"
          sm = SortMode.ALPHABETIC
        f = "C:\\TestFolder\\"
          sm = SortMode.ALPHABETIC
          sm = SortMode.EARLIEST_FIRST
          sm = SortMode.LATEST_FIRST
            user presses Open
              valid filename
              invalid filename
              empty filename
            user presses Cancel
            user presses Close
            user hits Esc
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("Attempt to show dialog with empty title string")
  if f != None:
    type_checking2_0.check_identical(f,str)
    if len(f) != 0:
      if not os.path.exists(f):
        message = "Attempt to open non-existent file or directory: \""
        message += str(f)
        message += "\". Reverting to default directory."
        dialoging.show_message_dialog(fsize,"Non-existent file or directory",message)
        f = None
  type_checking2_0.check_identical(sm,SortMode)
  
  # set up a QApplication object
  my_qapp = qapp_creating._get_qapp()

  d = _FixedSizeDialog(parent = None)
  d.setWindowTitle(t)
  d.font_size = fsize
  if f != None:
    (d.curdir,d.curfile) = os.path.split(f)
  else:
    d.curdir = None
    d.curfile = ""
  d.sort_mode = sm
  
  # set up vertical layout
  vl = PyQt6.QtWidgets.QVBoxLayout(d)  # vertical boxed layout
  vl.setSizeConstraint(PyQt6.QtWidgets.QLayout.SizeConstraint.SetFixedSize)
  
  # set layout for top line
  dirl = laying_out.LineLayout()
  
  # add dirl to vl
  vl.addLayout(dirl)
  
  build_look_in_box(d,dirl)

  si = PyQt6.QtWidgets.QSpacerItem(40,20)
  dirl.addItem(si)
  
  build_sorted_combo(d,dirl)
  
  build_file_display_area(d,vl)
    
  # add the file name line
  fl = laying_out.LineLayout()
  vl.addLayout(fl)
  
  build_file_name_box(d,fl)

  # add the Open and Cancel buttons
  ocl = laying_out.LineLayout()
  vl.addLayout(ocl)
  openb = PyQt6.QtWidgets.QPushButton("Open")
  font_sizing.set_font_size(openb,fsize)
  openb.setDefault(True)
  openb.clicked.connect(d.open_hit)
  ocl.addWidgetCentre(openb)
  
  cancelb = PyQt6.QtWidgets.QPushButton("Cancel")
  font_sizing.set_font_size(cancelb,fsize)
  cancelb.clicked.connect(d.cancel_hit)
  ocl.addWidgetCentre(cancelb)
  
  d.exec()
  return d.get_result()
 
  
def show_save_file_dialog(fsize,t,f,exs,sm):
  """
  pre:
    fsize = point size of text for dialog message, 
              as float in range 6.0..24.0
    t = title of this dialog, as Python string
    f = pathname of default file to be saved, as Python string,
        or None for the user's default directory and no file 
    exs = list of file extensions (not including the dot) 
            to be applied to the filename (if not already extended), 
              as Python strings, or the empty list if none
    sm = SortMode for displaying the directory
    
  post:
    dialog has been displayed at centre of screen, 
      and user has pressed one of the buttons.
    returns:
      pathname of selected file if the Save button was hit, 
        as Python string
      None if the Cancel button or the Close button 
        or the Esc key was hit 

  test:
    fsize = None
    fsize = 5.9
    fsize = 6.0
      t = None
    fsize = 24.0
      t = ""
      t = "Save"
        f = None
          exs = None
          exs = []
            sm = None
            sm = SortMode.ALPHABETIC
              user presses Cancel
              user presses Close
              user presses Esc
        f = ""
          exs = ["abc"]
            sm = SortMode.EARLIEST_FIRST
              user presses Save
                empty filename
                invalid filename
                valid filename
          exs = ["abc",def"]
            sm = SortMode.LATEST_FIRST
            user creates new folder
              user presses Save
                valid filename
    fsize = 14.0
        f = "Z:"
          exs = ["abc",def"]
              user presses Save
                valid filename
        f = "fred.py"
              user presses Save
                valid filename
        f = "C:\\TestFolder\\"
              user presses Save
                valid filename
        f = "C:\\TestFolder\\bill.py"
              user presses Save
                valid filename
  """
  type_checking2_0.check_identical(fsize,float)
  font_size_checking.check_window_font_size(fsize)
  type_checking2_0.check_identical(t,str)
  if len(t) == 0:
    raise Exception("Attempt to show dialog with empty title string")
  if f != None:
    type_checking2_0.check_identical(f,str)
    (dir,file) = os.path.split(f)
    if not os.path.isdir(dir):
      message = "Attempt to save in non-existent directory: \""
      message += str(dir)
      message += "\". Reverting to default directory."
      dialoging.show_message_dialog(fsize,"Non-existent directory",message)
      dir = None
  else:
    dir = None
    file = None
  type_checking2_0.check_identical(exs,list)
  type_checking2_0.check_identical(sm,SortMode)
  
  # set up a QApplication object
  my_qapp = qapp_creating._get_qapp()

  # set up dialog
  d = _FixedSizeDialog(parent = None)
  d.setWindowTitle(t)
  d.font_size = fsize
  d.curdir = dir
  d.curfile = file
  d.curtypelist = exs
  d.sort_mode = sm
  
  # set up vertical layout
  vl = PyQt6.QtWidgets.QVBoxLayout(d)  # vertical boxed layout
  vl.setSizeConstraint(PyQt6.QtWidgets.QLayout.SizeConstraint.SetFixedSize)
  
  # set layout for top line
  dirl = laying_out.LineLayout()
  # add this layout to vl
  vl.addLayout(dirl)

  # add widgets to top line
  build_look_in_box(d,dirl)

  newb = PyQt6.QtWidgets.QPushButton("New Folder")
  font_sizing.set_font_size(newb,fsize)
  newb.clicked.connect(d.new_folder_hit)
  dirl.addWidget(newb)
  
  si = PyQt6.QtWidgets.QSpacerItem(40,20)
  dirl.addItem(si)
  
  build_sorted_combo(d,dirl)
  
  build_file_display_area(d,vl)
  
  # add the file name line
  fl = laying_out.LineLayout()
  vl.addLayout(fl)
  
  build_file_name_box(d,fl)

  si2 = PyQt6.QtWidgets.QSpacerItem(40,20)
  fl.addItem(si2)
  type_lab = PyQt6.QtWidgets.QLabel("Type:")
  font_sizing.set_font_size(type_lab,fsize)
  fl.addWidget(type_lab)
  d.typecb = PyQt6.QtWidgets.QComboBox()
  font_sizing.set_font_size(d.typecb,fsize)
  for t in d.curtypelist:
    d.typecb.addItem(t)
  d.typecb.setCurrentIndex(0)
  d.typecb.setEditable(True)
  fl.addWidget(d.typecb)
  

  # add the Save and Cancel buttons
  ocl = laying_out.LineLayout()
  vl.addLayout(ocl)
  saveb = PyQt6.QtWidgets.QPushButton("Save")
  font_sizing.set_font_size(saveb,fsize)
  saveb.setDefault(True)
  saveb.clicked.connect(d.save_hit)
  ocl.addWidgetCentre(saveb)
  
  cancelb = PyQt6.QtWidgets.QPushButton("Cancel")
  font_sizing.set_font_size(cancelb,fsize)
  cancelb.clicked.connect(d.cancel_hit)
  ocl.addWidgetCentre(cancelb)
  d.exec()
  return d.get_result()
 
  
  
# private members
# ---------------

class _FileButton(PyQt6.QtWidgets.QPushButton):

  def file_button_clicked(self):
    """
    pre:
      self = _FileButton which has been clicked by the user
      
    post:
      self.my_dialog's file_hit method has been executed
      
    test:
      once thru
    """
    self.my_dialog.file_hit(self.get_pathname())


  def get_pathname(self):
    """
    pre:
      self = _FileButton whose pathname is to be returned
      
    post:
      pathname of self has been returned
      
    test:
      once thru
    """
    return self.text()[2:-2]


  def directory_button_clicked(self):
    """
    pre:
      self = _FileButton which has been clicked by the user
      
    post:
      self.my_dialog's directory_hit method has been executed
      
    test:
      once thru
    """
    self.my_dialog.directory_hit(self.get_pathname())

    
  def set_dialog(self,qd):
    """
    pre:
      self = _FileButton whose dialog is to be set
      
    post:
      self.my_dialog has been set to qd
      
    test:
      once thru
    """
    self.my_dialog = qd


  def set_pathname(self,pn):
    """
    pre:
      self = _FileButton whose label is to be set
      pn = simple name of file to be set
      
    post:
      self's label has been set to pn with 2 spaces fore and aft
      
    test:
      once thru
    """
    self.setText("  "+pn+"  ")
    
    
  my_dialog = None


class _FixedSizeDialog(PyQt6.QtWidgets.QDialog):

  def cancel_hit(self):
    """
    pre:
      self = _FixedSizeDialog whose Cancel button has been hit
      self.result = None
      
    post:
      the dialog has been closed
      
    test:
      once thru
    """
    self.result = None
    self.reject()
  

  def combo_hit(self,ind):
    """
    pre:
      self = dialog whose combo box has been hit by the user
      self.font_size = font size for this dialog
      self.curdir = directory for this dialog
      ind = index of entry selected by the user (0,1,2,..)
      
    post:
      self's sort mode has been set to the user's requirement
      self's file pane has been reconstructed, according to
        the sort mode selected by the user
        
    test:
      ind = 0
      ind = 1
      ind = 2
    """
    if ind == 0:
      self.sort_mode = SortMode.ALPHABETIC
    elif ind == 1:
      self.sort_mode = SortMode.EARLIEST_FIRST
    elif ind == 2:
      self.sort_mode = SortMode.LATEST_FIRST
    else:
      raise Exception("Invalid index from combo box")
    _new_file_pane(self,self.font_size,self.curdir,self.sort_mode)  
  
  
  def directory_hit(self,lab):
    """
    pre:
      self = dialog whose directory button has been hit
      lab = label of directory button which has been hit
      
    post:
      lab has been appended to the current directory 
        and the "Look in" text area has been updated with the new directory name
        
    test:
      once thru
    """
    self.curdir = os.path.join(self.curdir,lab)
    self.dirtf.setText(_display_pathname(self.curdir))
    _new_file_pane(self,self.font_size,self.curdir,self.sort_mode)

    
  def file_hit(self,lab):
    """
    pre:
      self = dialog whose directory button has been hit
      lab = label of file button which has been hit
      
    post:
      lab has been appended to the current directory 
        and the "File Name" text area has been updated with the new file name
        
    test:
      
    """
    pn = os.path.join(self.curdir,lab)
    self.filetf.setText(lab)
  

  def get_result(self):
    """
    pre:
      self = _FixedSizeDialog whose result is to be obtained
      
    post:
      result of the dialog has been returned
      the result will be the pathname of the user's selected file,
        or None if no selection has been made
        
    test:
      once thru
    """
    return self.result

  
  def go_home(self):
    """
    pre:
      self = dialog whose directory is to be set to home
      self.font_size = font size for self
      self.sort_mode = current sort mode of self
      
    post:
      self's current directory has been set to the root of the filing system
      the current directory and file area have been re-displayed
      
    test:
      once thru
    """
    self.curdir = ""
    self.dirtf.setText(_display_pathname(self.curdir))
    _new_file_pane(self,self.font_size,self.curdir,self.sort_mode)


  def go_up(self):
    """
    pre:
      self = dialog whose directory is to be replaced by its parent
      self.font_size = font size for self
      self.curdir = current directory of self
      self.sort_mode = current sort mode of self
      
    post:
      iff self's directory is not the super-root, 
        self's directory has been replaced by its parent
      the current directory and file area have been re-displayed
        
    test:
      self's directory is the super-root
      self's directory is a windows drive
      self's directory is the unix root
      self's directory is a non-root directory      
    """
    if self.curdir.endswith(":\\") or self.curdir == "/":
      # drive name or unix root
      self.curdir = ""
    else:
      self.curdir = os.path.dirname(self.curdir)
    self.dirtf.setText(_display_pathname(self.curdir))
    _new_file_pane(self,self.font_size,self.curdir,self.sort_mode)


  def open_hit(self):
    """
    pre:
      self = _FixedSizeDialog whose Open button has been hit
    
    post:
      if the file name and directory name are non-empty,
        result of this dialog has been set to the user's selected file
        the dialog has been closed
      else
        a BEL has been sounded
      
    test:
      empty file name
      empty directory name
      non-empty file and directory name
    """
    self.curfile = self.filetf.text()
    if len(self.curfile) > 0 and len(self.curdir) > 0:
      self.result = os.path.join(self.curdir,self.curfile)
      self.accept()
    else:
      print("\u0007")  # BEL
  
  
  def new_folder_hit(self):
    """
    pre:
      self = _FixedSizeDialog whose New Folder button has been hit
    
    post:
      the user has been queried for the name of the new directory,
        and, if necessary, the current directory and file display area 
          have been updated to the user's choice
      
    test:
      reply = None
      reply = invalid directory
      reply = valid directory
    """
    reply = show_new_folder_dialog(self.font_size,"Create New Folder",self.curdir)
    if reply != None:
      self.curdir = os.path.join(self.curdir,reply)
      self.dirtf.setText(_display_pathname(self.curdir))
      _new_file_pane(self,self.font_size,self.curdir,self.sort_mode)


  def save_hit(self):
    """
    pre:
      self = _FixedSizeDialog whose Save button has been hit
    
    post:
      if the current filename and directory name are not empty
        if the user has not specified an extension, and we have an extension specified
          in the Type combo,
            add our extension to the filename
        if the file does not already exist, 
          or the file does exist and the user wishes to overwrite it,
            the pathname of the joined current directory and current file
              has been returned
        else (the user does not wish to save the file)
          None has been returned
      else
        a BEL has been sounded
      
    test:
      empty file name
      non-empty file name
        name has extension
        name does not have extension
          combo box is empty
            user does not edit combo
            user edits combo
          combo box has one item
          combo box has two items
            user does not edit combo
            user edits combo
              file does not already exist
              file already exists
                user declines to overwrite
                user wishes to overwrite
    """
    self.curfile = self.filetf.text()
    if len(self.curfile) > 0 and len(self.curdir) > 0:
      if '.' not in self.curfile and len(self.typecb.currentText()) > 0:
        self.curfile = self.curfile + '.' + self.typecb.currentText() 
      self.result = os.path.join(self.curdir,self.curfile)
      if os.path.exists(self.result):
        yes = dialoging.show_confirm_dialog(self.font_size,"File already exists","File \"" + self.result + "\" already exists.  Do you want to overwrite it?")
        if yes:
          self.accept()
        else:
          self.result = None
          self.accept()
      else:
        self.accept()
    else:
      print("\u0007")  # BEL


  def showEvent(self,qe):
    """
    pre:
      self = _FixedSizeDialog on which this showEvent has occurred
      qe = QShowEvent which has occurred
      
    post:
      the dialog's file name box has been given the focus
      
    test:
      
    """
    self.filetf.setFocus()  # set the cursor in the file name box 
  
  
  curdir = None  # pathname of current directory, as str
  
  curfile = None  # name of current file
  
  curtypelist = []  # list of file extensions
  
  dirtf = None  # text field for current directory
  
  filetf = None  # text field for current file
  
  font_size = 0.0
  
  result = None  # result to be returned, default None
  
  scroll_area = None  # scroll area for file names
  
  sort_mode = SortMode.ALPHABETIC
  
  sortedcb = None
  
  typecb = None
  

def build_file_display_area(d,vl):
  """
  pre:
    d = _FixedSizeDialog to be built in
    d.font_size = font size for these widgets
    d.curdir = current directory 
    d.sort_mode = current sort mode of combo box
    vl = QVBoxLayout in which file display area is to be built
    
  post:
    file display area has been built in vl

  test:
    once thru
  """
  d.scroll_area = PyQt6.QtWidgets.QScrollArea(parent = d)
  d.scroll_area.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignLeft)
  _new_file_pane(d,d.font_size,d.curdir,d.sort_mode)
  vl.addWidget(d.scroll_area)
  
  
def build_file_name_box(d,l):
  """
  pre:
    d = _FixedSizeDialog to be built in
    d.font_size = font size for these widgets
    d.curfile = current file 
    l = LineLayout in which file name box is to be built
    
  post:
    labelled file display box has been built in l

  test:
    once thru
  """
  file_name = PyQt6.QtWidgets.QLabel("File Name:")
  font_sizing.set_font_size(file_name,d.font_size)
  l.addWidget(file_name)
  d.filetf = PyQt6.QtWidgets.QLineEdit()
  font_sizing.set_font_size(d.filetf,d.font_size)
  _set_minimum_width(d.filetf,d.font_size)
  d.filetf.setText(d.curfile)
  l.addWidget(d.filetf)
  
  
def build_look_in_box(d,l):
  """
  pre:
    d = _FixedSizeDialog to be built in
    d.curdir = pathname of current directory as Python string, 
                 or the empty string for the root directory, 
                   or None for the user's default directory
    d.font_size = font size for these widgets
    l = LineLayout into which box is to be built
    
  post:
    a Look In label, text box and an Up and Home button
      have been built in l, left-aligned
    d.curdir = pathname of current directory as Python string, 
                 or the empty string for the root directory
    d.dirtf = directory text field
    
  test:
    d.curdir = None
    d.curdir = ""
    d.curdir = valid directory
  """
  # add widgets to top line
  look_in = PyQt6.QtWidgets.QLabel("Look in:")
  font_sizing.set_font_size(look_in,d.font_size)
  l.addWidget(look_in)
  d.dirtf = PyQt6.QtWidgets.QLineEdit()
  font_sizing.set_font_size(d.dirtf,d.font_size)
  _set_minimum_width(d.dirtf,d.font_size)
  # if client specifies None, move to user directory
  if d.curdir == None:
    d.curdir = os.path.expanduser("~")
    
  d.dirtf.setText(_display_pathname(d.curdir))
  l.addWidget(d.dirtf)
  
  upb = PyQt6.QtWidgets.QPushButton("Up")
  font_sizing.set_font_size(upb,d.font_size)
  upb.clicked.connect(d.go_up)
  l.addWidget(upb)
  
  homeb = PyQt6.QtWidgets.QPushButton("Home")
  font_sizing.set_font_size(homeb,d.font_size)
  homeb.clicked.connect(d.go_home)
  l.addWidget(homeb)


def build_sorted_combo(d,l):
  """
  pre:
    d = _FixedSizeDialog to be built in
    d.font_size = font size for these widgets
    d.sort_mode = current sort mode for combo box
    l = LineLayout into which combo is to be built
    
  post:
    a Sorted label and a combo box have been built in l,
      right-aligned
    d.sortedcb = combo box
    d.sort_mode = selected sort mode of the combo
    
  test:
    d.sort_mode = ALPHABETICAL
    d.sort_mode = EARLIEST_FIRST
    d.sort_mode = LATEST_FIRST
  """
  sorted_lab = PyQt6.QtWidgets.QLabel("Sorted:")
  font_sizing.set_font_size(sorted_lab,d.font_size)
  l.addWidgetRight(sorted_lab)
  d.sortedcb = PyQt6.QtWidgets.QComboBox()
  font_sizing.set_font_size(d.sortedcb,d.font_size)
  d.sortedcb.addItem("Alphabetically")
  d.sortedcb.addItem("Earliest First")
  d.sortedcb.addItem("Latest First")
  d.sortedcb.setCurrentIndex(d.sort_mode.value-1)  # incompatibility between enum values and QCombo indices...
  d.sortedcb.activated.connect(d.combo_hit)
  l.addWidgetRight(d.sortedcb)


def _display_pathname(s):
  """
  pre:
    s = pathname to be displayed (may be empty if super-root)
  
  post:
    displayable pathname has been returned
    
  test:
    s = ""
    s = "x"
  """
  if len(s) == 0:
    return "File System:"
  else:
    return s


def _children_of(f):
  """
  pre:
    f = pathname of directory whose children are to be returned,
          or "" for the super-root
          
  post:
    list of triples has been returned, consisting of 
      (pathname, is_directory, modification date), 
        for each accessible child of f (i.e. files that can be opened,
          directories that can be scanned)
      
  test:
    f = ""
      Windows system
      unix-like system
    f = "C:"
    f = "C:/Empty"
    f = "C:/Temp"
  """
  items = []
  if len(f) == 0:  # f is the super-root
    for i in range(ord('A'),ord('Z')): # try all the possible drives
      drive = chr(i)+':'
      if os.path.exists(drive):
        items.append((drive+"\\",True,0.0))
    if len(items) == 0:  # no drives, so must be unix-like
      return [("/",True,0.0)]
    else:
      return items
  else:           # f is not the super-root
    with os.scandir(f) as it:
      for entry in it:
        pn = os.path.join(f,entry.name)
        if _is_accessible(pn):
          item = (entry.name,entry.is_dir(),entry.stat().st_mtime)
          items.append(item)
    return items
    

def _is_accessible(pn):
  """
  pre:
    pn = pathname to be tested
  
  post:
    returns True iff pn is accessible
    
  test:
    file is accessible
    file is not accessible
    directory is accessible
    directory is not accessible
  """
  try:
    if os.path.isfile(pn):
      open(pn)
      return True
    elif os.path.isdir(pn):
      os.scandir(pn)
      return True
    else:
      return False
  except OSError:
    return False
    
    
def _lower_of(tr):
  """
  pre:
    tr = triple (name,isdir,time) for file/directory item
    
  post:
    the lower-case version of name has been returned
    
  test:
    string with upper-case and lower-case characters
  """
  (name,isdir,time) = tr
  return str.lower(name)
    

def _new_file_pane(fsd,fsize,f,sm):
  """
  pre:
    fsd = _FixedSizeDialog for which new file pane is to be created
    fsize = font size of items in the file pane, as float
    f = directory whose contents should appear in the new file pane
    sm = SortMode for the contents
    
  post:
    new file pane has been created and set in fsd's scroll area
    
  test:
    f is empty
    f has more than one column of items
      sm = ALPHABETIC
      sm = EARLIEST_FIRST
      sm = LATEST_FIRST
  """
  # set up the pane widget
  p = PyQt6.QtWidgets.QWidget(parent = fsd.scroll_area)
  column_height = int(resolving.pixels_per_point(fsd) * fsize * 11.0)
  p.setMinimumWidth(column_height * 4)
  p.setMinimumHeight(column_height)
  p.setMaximumHeight(column_height)
  p.setSizePolicy(PyQt6.QtWidgets.QSizePolicy.Policy.Minimum,PyQt6.QtWidgets.QSizePolicy.Policy.Fixed)
  p.setStyleSheet("QWidget { background-color: white }")
  p.setFocusPolicy(PyQt6.QtCore.Qt.FocusPolicy.StrongFocus)

  # read the directory contents
  children = _children_of(fsd.curdir)
  
  # sort the contents
  sorted_children = []
  
  if sm == SortMode.ALPHABETIC:
    sorted_children = sorted(children,key=_lower_of)
  elif sm == SortMode.EARLIEST_FIRST:
    sorted_children = sorted(children,key=itemgetter(2))
  elif sm == SortMode.LATEST_FIRST:
    sorted_children = sorted(children,key=itemgetter(2),reverse=True)
  else:
    raise Exception("  invalid sort mode: sm="+str(sm))

  # populate the pane with file names, as _FileButtons
  x = 0
  y = 0
  max_width = 0
  next_y = 0
  for item in sorted_children:
    b = _FileButton(parent = p)
    b.set_pathname(item[0])
    b.set_dialog(fsd)
    b.setFlat(True)
    if item[1]:  # directory
      b.setStyleSheet("QWidget { font-size: " + str(int(fsize)) + "pt; background-color: #EEEEEE; border-width: 1px; border-style: solid; border-color: black; }")
      #b.clicked.connect(fsd.directory_hit)
      b.clicked.connect(b.directory_button_clicked)
    else:  # file
      b.setStyleSheet("QWidget { font-size: " + str(int(fsize)) + "pt}")
      #b.clicked.connect(fsd.file_hit)
      b.clicked.connect(b.file_button_clicked)
    bsh = b.sizeHint()
    #prhint("  b",b)
    bw = bsh.width()
    bh = bsh.height()
    next_y = y + bh
    if max_width < bw:
      max_width = bw
    b.setGeometry(x,y,bw,bh)
    
    if next_y+bh > p.size().height():  # vertical overflow
      x += max_width
      y = 0
      max_width = 0
    else:
      y = next_y
      
  if x+max_width > p.minimumWidth():
    p.setMinimumWidth(x+max_width)

  # set the new pane in the scroll area
  fsd.scroll_area.setWidget(p)


def _set_minimum_width(qle,fsize):
  """
  pre:
    qle = QLineEdit whose minimum width is to be set
    fsize = font size of qle, as float
    
  post:
    minimum width of qle has been set to a reasonable width,
      given the font size
      
  test:
    once thru
  """
  new_width =  int(fsize * resolving.pixels_per_point(qle)) * 13.0 + 35.0
  # about 1.5 times the standard width
  qle.setMinimumWidth(int(new_width))

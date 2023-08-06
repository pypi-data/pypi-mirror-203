import io
import json
import os
from guibits1_0 import type_checking2_0, window_bounding

# author R.N.Bosworth

# version 25 Feb 2023  19:09
""" 
Contractor which deals with persistent data for Emily.

Note: test version with tiny page!

Copyright (C) 2016,2017,2018,2021,2022,2023  R.N.Bosworth

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

class Persistents:  # container object for persistent data
   _data = {"current_file_name":None,"menu_font_size":16.0, \
            "splash_screen_on":False,"text_font_name":"Times New Roman", \
            "text_font_size":12.0, \
            "window_bounds":{"x":72.0,"y":72.0,"width":576.0,"height":288.0}, \
            "zoom_factor":1.0}
  
  
# exposed procedures
# ------------------

def get_current_file_name(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    current file name has been returned as str, or None if no current file name

  test:
    file name None
    file name valid
  """
  type_checking2_0.check_derivative(p,Persistents)
  return p._data["current_file_name"]


def get_persistents():
  """ 
  pre:
    true
    
  post:
    a Persistents object containing persistent values
      has been returned
    either:
      the persistents have been read in from the "EmilyPersistents.json" file in the 
        user's default directory
    or:
      it was not possible to read the "EmilyPersistents.json" file
      a default Persistents has been returned
      
  note:
    This object is a singleton.
 
  test:
    _the_persistents  is None
    _the_persistents  is valid
  """
  global _the_persistents
  if _the_persistents == None:
    try:
      # set up defaults
      _the_persistents = Persistents()
      default_directory = os.path.expanduser("~")  # user's default directory
      save_file = open(os.path.join(default_directory,"EmilyPersistents.json"))
      _the_persistents._data = json.load(save_file)
    except Exception:
      pass  # the file was not present
  return _the_persistents
  

def get_horizontal_indent(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    horizontal indent in points has been returned, as float
    
  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return 72.0
  

def get_paper_height(p):
  """ 
  pre:
    p = Persistents container for required persistent value
  post:
    height of paper in points has been returned, as float
    
  Note: test version with tiny page!

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return 841.0
  # slightly smaller to prevent printer probs
  # return 216.0;   // i.e. 1" of print for testing purposes
  

def get_paper_width(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    width of paper in points has been returned, as float
    
  Note: test version with tiny page!

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return 592.0
  # slightly smaller to prevent printer probs
  #return 288.0;  // i.e. 2 inches of print for testing purposes
  

def get_menu_font_size(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of menu_font_size has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return p._data["menu_font_size"]
  

def get_splash_screen_on(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of splash_screen_on has been returned, as bool

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return p._data["splash_screen_on"]
  

def get_text_font_name(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of text_font_name has been returned, as str

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return p._data["text_font_name"]
  

def get_text_font_size(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of font_text_size has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return p._data["text_font_size"]
  

def get_vertical_indent(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    vertical indent in points has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  return 72.0
  

def get_window_bounds(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of window_bounds has been returned, as a window_bounding.WindowBounds

  test:
    once thru with non-zero bounds
  """
  type_checking2_0.check_derivative(p,Persistents) 
  wbd = p._data["window_bounds"]  # window bounds as dict
  wb = window_bounding.new_bounds()
  window_bounding.set_x(wb,wbd["x"])
  window_bounding.set_y(wb,wbd["y"])
  window_bounding.set_width(wb,wbd["width"])
  window_bounding.set_height(wb,wbd["height"])
  return wb
  

def get_zoom_factor(p):
  """ 
  pre:
    p = Persistents container for required persistent value
    
  post:
    value of zoom factor has been returned, as float

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)  
  return p._data["zoom_factor"]
  

def set_current_file_name(p,s):
  """ 
  pre:
    p = Persistents container for required persistent value
    s = file name to which current_file_name is to be updated, as str
          or None
          
  post:
    current_file_name has been updated to required value
    Persistents have been saved to disk

  test:
    s  is null
    s  is non-null
  """
  type_checking2_0.check_derivative(p,Persistents)
  if s != None:
    type_checking2_0.check_identical(s,str)
  p._data["current_file_name"] = s
  _save_persistents()
  

def set_menu_font_size(p,d):
  """ 
  pre:
    p = Persistents container for required persistent value
    d = size to which menu_font_size is to be updated
    
  post:
    menu_font_size has been updated to required value
    Persistents have been saved to disk

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_identical(d,float)  
  p._data["menu_font_size"] = d
  _save_persistents()
  

def set_splash_screen_on(p,b):
  """ 
  pre:
    p = Persistents container for required persistent value
    b = true iff splash_screen is on
    
  post:
    splash_screen_on has been updated to required value
    Persistents have been saved to disk

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_derivative(b,bool)
  p._data["splash_screen_on"] = b
  _save_persistents()
  

def set_text_font_name(p,s):
  """ 
  pre:
    p = Persistents container for required persistent value
    s = name to which text_font_name is to be updated
    
  post:
    text_font_name has been updated to required value
    Persistents have been saved to disk

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_identical(s,str)
  p._data["text_font_name"] = s
  _save_persistents()
  

def set_text_font_size(p,d):
  """ 
  pre:
    p = Persistents container for required persistent value
    d = size to which text_font_size is to be updated
    
  post:
    text_font_size has been updated to required value
    Persistents have been saved to disk

  test:
    once thru
  """
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_identical(d,float)
  p._data["text_font_size"] = d
  _save_persistents()
  

  """ 
  pre:
    p = Persistents container for required persistent value
    wb = window_bounds which are to be set
  post:
    window_bounds has been updated to required value
    Persistents have been saved to disk
  """
""" 
  pre:
    _the_persistents = p
  """
""" 
  test:
    once thru
  """


def set_window_bounds(p,wb):
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_derivative(wb,window_bounding.WindowBounds)
  wb_dict = {"x":window_bounding.get_x(wb),"y":window_bounding.get_y(wb), \
             "width":window_bounding.get_width(wb),"height":window_bounding.get_height(wb)}
  p._data["window_bounds"] = wb_dict
  _save_persistents()
  

  """ 
  pre:
    p = Persistents container for required persistent value
    d = value to which zoom factor is to be updated
    
  post:
    zoom factor has been updated to required value
    Persistents have been saved to disk

  test:
    once thru
  """


def set_zoom_factor(p,d):
  type_checking2_0.check_derivative(p,Persistents)
  type_checking2_0.check_identical(d,float)
  p._data["zoom_factor"] = d
  _save_persistents()
  

# private members
# ---------------

_the_persistents = None
  

def _save_persistents():
  """ 
  pre:
    _the_persistents = persistents object to  be saved
    
  post:
    an attempt has been made to save _the_persistents in user's default directory
      under the name EmilyPersistents.json

  test:
    once thru
  """
  default_directory = os.path.expanduser("~")  # user's default directory
  save_file = open(os.path.join(default_directory,"EmilyPersistents.json"),'w')
  try:
    json.dump(_the_persistents._data,save_file)
  except:
    print("Failed to save persistents")
  
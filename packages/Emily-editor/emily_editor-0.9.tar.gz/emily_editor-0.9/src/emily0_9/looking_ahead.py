""" 
One symbol lookahead stream.  A lookahead does not automatically move forward 
when a symbol is read, thus allowing multiple access of that symbol.
This is extremely convenient for LL(1) parsers.  The current symbol of a 
lookahead is always defined, but it may be the END_OF_STREAM symbol.
"""

# author R.N.Bosworth

# version 8 Mar 23  15:51

from guibits1_0 import type_checking2_0, unicoding3_0
from .import unicode_io

"""
Copyright (C) 2012,2015,2016,2017,2018,2021,2022,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exported constants
# ------------------
END_OF_STREAM =  - 1

# exported types
# --------------

class Lookahead:
  pass
  

# exported procedures
# -------------------

def advance(l):
  """ 
  pre:
    l = Lookahead to be advanced
    
  post:
    l has been advanced by one symbol

  test:
    once thru
  """
  type_checking2_0.check_derivative(l,Lookahead)
  l._current_symbol = unicode_io.read(l._current_stream)
  

def current_symbol_of(l):
  """ 
  pre:
    l = Lookahead whose current symbol is to be accessed
    
  post:
    current symbol of l has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(l,Lookahead)
  return l._current_symbol
  

def lookahead_of(fn):
  """ 
  pre:
    fn = name of file to be used for the Lookahead, as str
    
  post:
    new Lookahead has been returned

  test:
    invalid file name (invalid characters)
    valid file name but file not there
    valid existent file
  """
  type_checking2_0.check_identical(fn,str)
  fl = Lookahead()
  fl._current_stream = unicode_io.new_input_reader(fn)
  fl._current_symbol = unicode_io.read(fl._current_stream)
  return fl
  

def lookahead_of_string(s):
  """ 
  pre:
    s = string to be used for the lookahead, as unicoding3_0.String
    
  post:
    new Lookahead has been returned

  test:
    empty string
    non-empty string
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  fl = Lookahead()
  fl._current_stream = unicode_io.new_string_reader(s)
  fl._current_symbol = unicode_io.read(fl._current_stream)
  return fl

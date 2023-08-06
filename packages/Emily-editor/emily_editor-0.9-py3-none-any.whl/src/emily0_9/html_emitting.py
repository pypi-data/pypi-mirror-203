from guibits1_0 import type_checking2_0
from . import unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 2 Mar 2023  14:51
""" 
Contractor for emitting html elements.

Copyright (C) 2017,2018,2019,2021,2022,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.


"""
""" 
  HTML Grammar version 1 Dec 2018   15:05

  This grammar defines the basic HTML constructs common to any HTML file.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  
  StartTag(Name)  ::==  < Name OptionalSpaces >

  EndTag(Name)  ::==  < / Name OptionalSpaces >

  HtmlCharacter  ::==  ( & a m p ;
                       | & g t ;
                       | & l t ;
                       | any Unicode code point except '&' (U+26), '>' (U+3E) and '<' (U+3C)

Note: the rules for OptionalSpaces, SpaceChar, Separator, Name and NameChar are in the HTML CSS Grammar, as they are common to both HTML and CSS
"""

# exposed procedures
# ------------------

def emit_end_tag(s,w):
  """ 
  pre:
    s = name of end tag, as lower-case Unicode code points
    w = Unicode stream to which end tag is to be emitted
    
  post:
    end tag has been written to w

  syntax:
    EndTag(Name)  ::=  < / Name OptionalSpaces >

  test:
    s = None
    s = vaid non-empty string
      w = None
      w = valid Writer
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  unicode_io.write(ord('<'),w)
  unicode_io.write(ord('/'),w)
  i = 0
  while i < unicoding3_0.length_of(s):
    unicode_io.write(unicoding3_0.code_point_at(s,i),w)
    i += 1
  unicode_io.write(ord('>'),w)
  

def emit_indent(w):
  """ 
  pre:
    w = Writer on which indent is to be emitted
    
  post:
   indent has been written to w

  test:
    w = None
    w = valid Writer
  """
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord(' '),w)
  

def emit_new_line(w):
  """ 
  pre:
    w = Unicode stream to which new line string is to be emitted
    
  post:
    new line string has been written to w

  test:
    w = None
    w = valid Writer
      unix
      windows
      default (unix)
  """
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  emit_string(_LINE_SEPARATOR,w)
  

_LINE_SEPARATOR = unicoding3_0.string_of("\n") # default to Unix


def emit_string(s,w):
  """ 
  pre:
    s = string to be emitted
    w = writer to which the string is to be emitted
    
  post:
    s has been emitted to w

  test:
    s = None
    s = ""
      w = None
      w = valid Writer
    s = "fred"
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  i = 0
  while i < unicoding3_0.length_of(s):
    unicode_io.write(unicoding3_0.code_point_at(s,i),w)
    i += 1
  

def emit_start_tag(s,w):
  """ 
  pre:
    s = name of start tag, as lower-case Unicode code points
    w = Unicode stream to which start tag is to be emitted
    
  post:
    start tag element has been written to w

  syntax:
    StartTag(Name)  ::=  < Name OptionalSpaces >

  test:
    s = None
    s = valid non-empty String
      w = None
      w = valid Writer
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  unicode_io.write(ord('<'),w)
  i = 0
  while i < unicoding3_0.length_of(s):
    unicode_io.write(unicoding3_0.code_point_at(s,i),w)
    i += 1
  unicode_io.write(ord('>'),w)

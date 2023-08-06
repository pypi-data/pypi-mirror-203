# Contractor for the basic grammar of HTML and CSS.

# author R.N.Bosworth

# version 8 Mar 23  15:42

from guibits1_0 import type_checking2_0, unicoding3_0

from .import code_point_testing, looking_ahead, unicode_io

""" 
Copyright (C) 2017,2018,2021,2022,2023  R.N.Bosworth

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
  HTML CSS Grammar version 17.3.18   15:39

  This grammar defines the basic HTML constructs common to HTML5 and CSS.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::=  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  
  OptionalSpaces  ::=  SpaceChar*

  SpaceChar  ::=  (SPACE | TAB | LF | FF | CR)
                  (U+0020 | U+0009 | U+000A | U+000C | U+000D )
                  
  Separator  ::==  SpaceChar OptionalSpaces
  
  Name  ::=  NameChar NameChar*

  NameChar  ::=  ( a .. z | 0 .. 9 )
                 ( U+0061 .. U+007A | U+0030 .. U+0039 )
                 
"""

# exposed procedures
# ------------------

def accept(cp,la):
  """ 
  pre:
    cp = unicode code point which is to be accepted, as an int
    la = looking_ahead.Lookahead which is being parsed
    
  post:
    either:
      cp has been accepted from la
      la has been advanced past cp
    or:
      RuntimeException has been thrown

  test:
    cp = None
    cp = 'A'
      la = None
      la = "B"
      la = "A"
  """
  type_checking2_0.check_identical(cp,int)
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  if looking_ahead.current_symbol_of(la) != cp:
    raise Exception("unexpected code point, expected: U+" + format(cp,'04x') +" found: U+" + format(looking_ahead.current_symbol_of(la),'04x'))
  else:
    looking_ahead.advance(la)
    
  
def accept_name(name,la):
  """ 
  pre:
    name = name to be accepted, as unicoding3_0.String
    la = looking_ahead.Lookahead to be parsed
    
  post:
    either:
      name has been accepted,
    or:
      a parse exception as been raised

  syntax:
    Name  ::=  NameChar NameChar*

  test:
    name = None
      la = None
    name = "jim" (not expected)
      la = None
           valid Lookahead
    name = "fred" (expected)
      la = valid Lookahead
  """
  type_checking2_0.check_derivative(name,unicoding3_0.String)
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  s = parse_name(la)
  if  not unicoding3_0.equals(s,name):
    raise Exception("Unexpected name: expected \"" + unicoding3_0.python_string_of(name) + "\", found \"" + unicoding3_0.python_string_of(s) + "\"")
    

def accept_optional_spaces(la):
  """ 
  pre:
    la = looking_ahead.Lookahead to be parsed
    
  post:
    zero or more space characters have been consumed from la

  syntax:
    OptionalSpaces  ::=  SpaceChar*

  test:
    la = None
    la = "hello"
    la = "  hello"
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  cp = looking_ahead.current_symbol_of(la)
  while code_point_testing.is_space_char(cp):
    looking_ahead.advance(la)
    cp = looking_ahead.current_symbol_of(la)
    

def accept_separator(la):
  """ 
  pre:
    la = looking_ahead.Lookahead which is being parsed
    
  post:
    either:
      accepts separator of one or more Space code points from la
    or:
      an Exception has been raised

  syntax:
    Separator  ::==  SpaceChar OptionalSpaces

  test:
    la = None
         ""
         "a"
         " "
         "   "
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  if  not code_point_testing.is_space_char(looking_ahead.current_symbol_of(la)):
    raise Exception("unexpected code point in HTML separator: U+" +format(looking_ahead.current_symbol_of(la),'04x'))
  accept_optional_spaces(la)
  

def parse_name(la):
  """ 
  pre:
    la = looking_ahead.Lookahead which is being parsed
    
  post:
    either:
      returns HTML name as lower-case unicoding3_0.String
      lookahead has been advanced past Name
    or:
      an Exception has been raised

  syntax:
    Name  ::=  NameChar NameChar*

  test:
    la = None
         "%"
         ""
         "f"
         "fred"
         "FRED"
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  s = unicoding3_0.new_string()
  if  not code_point_testing.is_name_char(looking_ahead.current_symbol_of(la)):
    raise Exception("unexpected code point in HTML name: U+" + format(looking_ahead.current_symbol_of(la),'04x'))
  unicoding3_0.append(s,looking_ahead.current_symbol_of(la))
  looking_ahead.advance(la)
  while code_point_testing.is_name_char(looking_ahead.current_symbol_of(la)):
    unicoding3_0.append(s,looking_ahead.current_symbol_of(la))
    looking_ahead.advance(la)
  return s

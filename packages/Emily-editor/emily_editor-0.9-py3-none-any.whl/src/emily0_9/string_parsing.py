# Contractor to parse an HTML string.

# author R.N.Bosworth

# version 4 Mar 23  16:31

from . import looking_ahead

from guibits1_0 import type_checking2_0, unicoding3_0

""" 
Copyright (C) 2019,2021,2022,2023  R.N.Bosworth

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

def parse_html_character(s,o):
  """ 
  pre:
    s = unicoding3_0.String to be parsed
    o = int offset from which the translation is to start
    
  post:
    either:
      an (escaped) unicode code point has been consumed from s
      a pair of ints has been returned, consisting of the equivalent non-escaped unicode code point and the offset past the consumed (escaped) unicode code point
    or:
      an exception has been raised
      
  syntax:
    HtmlCharacter  ::==  ( & a m p ;
                         | & g t ;
                         | & l t ;
                         | any Unicode code point except '&' (U+26), '>' (U+3E) and '<' (U+3C)

  test:
    l = None
        "&bmp;"
        "&anp;"
        "&amq;"
        "&amp;"
        "&ft;"
        "&gs;"
        "&gt;"
        "&mt;"
        "&lu;"
        "&lt;"
        ">"
        "<"
        "a"
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  type_checking2_0.check_identical(o,int)
  cp = unicoding3_0.code_point_at(s,o)
  if cp == ord('&'):
    o += 1
    cp = unicoding3_0.code_point_at(s,o)
    if cp == ord('a'):
      o = _accept(ord('a'),s,o)
      o = _accept(ord('m'),s,o)
      o = _accept(ord('p'),s,o)
      o = _accept(ord(';'),s,o)
      return (ord('&'),o)
      
    elif cp == ord('g'):
      o = _accept(ord('g'),s,o)
      o = _accept(ord('t'),s,o)
      o = _accept(ord(';'),s,o)
      return (ord('>'),o)
      
    elif cp == ord('l'):
      o = _accept(ord('l'),s,o)
      o = _accept(ord('t'),s,o)
      o = _accept(ord(';'),s,o)
      return (ord('<'),o)
      
    else:
      raise Exception("unexpected code point in HTML escape: U+" + format(cp,'x'))
      
  elif cp == ord('>'):
    raise Exception("illegal code point in text: U+" + format(ord('>'),'x'))
    
  elif cp == ord('<'):
    raise Exception("illegal code point in text: U+" + format(ord('<'),'x'))
    
  else:
    o += 1
    return (cp,o)
    

# private procedures
# ------------------

def _accept(cp,s,o):
  """ 
  pre:
    cp = unicode code point which is to be accepted, as an int
    s = unicoding3_0.String which is being parsed
    o = offset in s of code point to be tested
    
  post:
    either:
      cp has been accepted and consumed from s
      o has been updated past the accepted code point
    or:
      an exception has been raised

  test:
    cp = 'A'
      l = "B"
      l = "A"
  """
  if unicoding3_0.code_point_at(s,o) != cp:
    raise Exception("unexpected code point, expected: U+" + format(cp,'x') + ", found: U+" + format(unicoding3_0.code_point_at(s,o),'x'))
  else:
    o += 1
    return o

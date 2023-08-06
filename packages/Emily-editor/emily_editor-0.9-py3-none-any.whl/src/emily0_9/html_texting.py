from . import texting
from guibits1_0 import type_checking2_0

# author R.N.Bosworth

# version 2 Mar 2023  15:15

""" 
Contractor which allows the client to advance and retreat through HTML text, 
as it appears on the screen,
ignoring tags and dealing with escaped code points.

An "HTML character" is either an escaped or non-escaped Unicode code point.

HTML tags are ignored by this contractor.

So

  "<b>1 &lt; 2</b>" is treated as "1 < 2"

Copyright (C) 2018,2021  R.N.Bosworth

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
  StartTag(Name)  ::=  < Name OptionalSpaces >

  EndTag(Name)  ::=  < / Name OptionalSpaces >

  EscapedHtmlCharacter  ::=  ( & a m p ;
                             | & g t ;
                             | & l t ;
                             | any Unicode code point except '&' (U+26), '>' (U+3E) and '<' (U+3C)
"""

# exposed procedures
# ------------------

def advance(t):
  """ 
  pre:
    t = texting.Text whose cursor is to be advanced
    
  post:
    if t is at end of text, false has been returned
    otherwise,
      true has been returned
      t's cursor has been moved one position towards the end of the text,
        ignoring any HTML tags and treating escaped code points as one position

  test:
    t = None
    t = "<b><i>1&lt;2</i></b>x<b></b>"
      cursor at (0,0)
        call advance as many times as necessary!
  """
  type_checking2_0.check_derivative(t,texting.Text)
  line_offset = texting.cursor_line_offset(t)
  code_point_offset = texting.cursor_code_point_offset(t)
  texting.set_cursor_end(t)
  if line_offset == texting.cursor_line_offset(t) and code_point_offset == texting.cursor_code_point_offset(t):
    # at end of text
    return False
    
  texting.set_cursor(t,line_offset,code_point_offset)
  cp = texting.current_code_point(t)
  texting.advance(t)
  if cp == ord('<'):
    while texting.current_code_point(t) != ord('>'):
      texting.advance(t)
      
    texting.advance(t)
    # text cursor just past '>'
    return advance(t)
    
  if cp == ord('&'):
    while texting.current_code_point(t) != ord(';'):
      texting.advance(t)
      
    texting.advance(t)
    # text cursor just past ';'
    return True
    
  # else cp is a LF, a SPACE or a NonSpaceChar
  return True
  

def delete_after(t):
  """ 
  pre:
    t = texting.Text for which the HTML character following the cursor is to be deleted
    
  post:
    if t is at end of text, false has been returned
    otherwise,
      true has been returned
      the HTML character following t's cursor has been deleted

  test:
    t = None
    t = "<b><i>1&lt;2</i></b>x<b></b>"
      cursor at (0,0)
        call delete_after as many times as necessary!
  """
  type_checking2_0.check_derivative(t,texting.Text)
  line_offset = texting.cursor_line_offset(t)
  code_point_offset = texting.cursor_code_point_offset(t)
  texting.set_cursor_end(t)
  if line_offset == texting.cursor_line_offset(t) and code_point_offset == texting.cursor_code_point_offset(t):
    # at end of text
    return False
    
  texting.set_cursor(t,line_offset,code_point_offset)
  if texting.current_code_point(t) == ord('<'):
    texting.advance(t)
    while texting.current_code_point(t) != ord('>'):
      texting.advance(t)
      
    texting.advance(t)
    # text cursor just past '>'
    return delete_after(t)
    
  if texting.current_code_point(t) == ord('&'):
    texting.delete_after(t)
    while texting.current_code_point(t) != ord(';'):
      texting.delete_after(t)
      
    texting.delete_after(t)
    # escaped HTML character has been deleted
    return True
    
  # else cp is a LF, a SPACE or a NonSpaceChar
  texting.delete_after(t)
  return True
  

def retreat(t):
  """ 
  pre:
    t = texting.Text whose cursor is to be retreated
    
  post:
    if t is at start of text, false has been returned
    otherwise,
      true has been returned
      t's cursor has been moved one position towards the start of the text,
        ignoring any HTML tags and treating escaped code points as one position

  test:
    t = None
    t = "x;<b><i>1&lt;; ;2</i></b>y"
      cursor at end of text
        call retreat as many times as necessary!
    t = "<align>x"
      cursor at end of text
        call retreat as many times as necessary!
  """
  type_checking2_0.check_derivative(t,texting.Text)
  if texting.cursor_line_offset(t) == 0 and texting.cursor_code_point_offset(t) == 0:
    return False
    
  texting.retreat(t)
  if texting.current_code_point(t) == ord('>'):
    texting.retreat(t)
    while texting.current_code_point(t) != ord('<'):
      texting.retreat(t)
      
    # text cursor just before '<'
    return retreat(t)
    
  if texting.current_code_point(t) == ord(';'):
    semicolon_position = texting.cursor_code_point_offset(t)
    # in case it really is a semicolon
    texting.retreat(t)
    cp = texting.current_code_point(t)
    while cp != ord('&') and cp != ord(';') and cp != ord(' ') and cp != ord('>') and texting.cursor_code_point_offset(t) > 0:
      # to ensure termination
      texting.retreat(t)
      cp = texting.current_code_point(t)
      
    # text cursor EITHER just before '&' OR just before ';' OR just before ' ' OR
    # just before '>' OR at start of line 
    # (note ';', ' ' and '>' not allowed in escaped code point)
    if cp != ord('&'):
      texting.set_cursor(t,texting.cursor_line_offset(t),semicolon_position)
      # just before actual ';', as no '&' found
      
    # just before previous code point, escaped or not
    return True
    
  # else current_code_point is a non-escaped HTML Character
  return True

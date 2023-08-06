# Contractor which has procedures for parsing basic html entities.

# author R.N.Bosworth

# version 9 Mar 23  14:28

from guibits1_0 import type_checking2_0, unicoding3_0

from . import html_css_parsing
from . import looking_ahead

""" 
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

def accept_end_tag(name,la):
  """ 
  pre:
    name = name of end tag to be accepted, as unicoding3_0.String
    la = looking_ahead.Lookahead to be parsed
    
  post:
    either:
      end tag has been parsed,
    or:
      a parse exception as been raised

  syntax:
    EndTag(Name)  ::=  < / Name OptionalSpaces >

  test:
    la = None
    la = valid lookahead
      name = None
             ">/html>"
             "<\html>"
             "</html<"
             "</htmm>"
             "</html>"
             "</HTML   >"
  """
  type_checking2_0.check_derivative(name,unicoding3_0.String)
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  html_css_parsing.accept(ord('<'),la)
  html_css_parsing.accept(ord('/'),la)
  html_css_parsing.accept_name(name,la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('>'),la)
  

def accept_start_tag(name,la):
  """ 
  pre:
    name = name of start tag to be accepted, as unicoding3_0.String
    la = looking_ahead.Lookahead to be parsed
    
  post:
    either:
      start tag has been parsed,
    or:
      a parse exception as been raised
  syntax:
    StartTag(Name)  ::=  < Name OptionalSpaces >

  test:
    la = None
    la = valid lookahead
      name = None
             ">html>"
             "<html<"
             "<htmm>"
             "<html>"
             "<HTML   >"
  """
  type_checking2_0.check_derivative(name,unicoding3_0.String)
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  html_css_parsing.accept(ord('<'),la)
  html_css_parsing.accept_name(name,la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('>'),la)
  

def parse_start_tag(la):
  """ 
  pre:
    la = looking_ahead.Lookahead to be parsed
    
  post:
    either:
      string corresponding to contents of tag (minus any trailing spaces) has been returned
      la has been advanced past the end of the tag
    or:
      an Exception has been raised

  syntax:
    StartTag(Name)  ::=  < Name OptionalSpaces >

  test:
    la = None
         "{fred  }"
         "<  >"
         "</fred  >"
         "<jim]"
         "<jim>"
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  s = unicoding3_0.new_string()
  html_css_parsing.accept(ord('<'),la)
  unicoding3_0.append_a_copy(s,html_css_parsing.parse_name(la))
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('>'),la)
  return s
  

def parse_tag(la):
  """ 
  pre:
    la = looking_ahead.Lookahead to be parsed
    
  post:
    either:
      string corresponding to contents of tag (minus any trailing spaces) has been returned
      la has been advanced past the end of the tag
    or:
      an Exception has been raised

  syntax:
    StartTag(Name)  ::=  < Name OptionalSpaces >

    EndTag(Name)  ::=  < / Name OptionalSpaces >

  test:
    la = None
         "{/fred  }"
         "</  >"
         "</fred  >"
         "<jim]"
         "<jim>"
         "</bert>"
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  s = unicoding3_0.new_string()
  html_css_parsing.accept(ord('<'),la)
  if looking_ahead.current_symbol_of(la) == ord('/'):
    unicoding3_0.append(s,ord('/'))
    looking_ahead.advance(la)
  unicoding3_0.append_a_copy(s,html_css_parsing.parse_name(la))
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('>'),la)
  return s

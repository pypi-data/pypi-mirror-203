from guibits1_0 import type_checking2_0
from . import unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 6 Aug 2022  14:19
""" 
Contractor which allows the emitting of css rules.

Copyright (C) 2016,2017,2021,2022,2023  R.N.Bosworth

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
  CSS Grammar version 13.6.17   05:30

  This grammar is a reduced version of the W3C CSS standard, as at April 2016.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::=  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike CSS.
    

  StyleSheet  ::=  OptionalSpaces Rule*
  
  Rule  ::=  Selector OptionalSpaces DeclarationBlock OptionalSpaces
  
  Selector  :==  DotName
  
  DotName  ::=  Name ( . Name | )
                   
  DeclarationBlock  ::=  { OptionalSpaces Declaration OptionalSpaces ; OptionalSpaces 
                          (Declaration OptionalSpaces ; OptionalSpaces)* }

  Declaration  ::=  FontDeclaration | TextAlignmentDeclaration
  
  FontDeclaration  ::=  f o n t - (FontNameDeclarationRest | FontSizeDeclarationRest)
    
  FontNameDeclarationRest  ::=  f a m i l y OptionalSpaces : OptionalSpaces FontName
  
  FontName  ::=  " FontNameCharacter FontNameCharacter* "
  
  FontNameCharacter  ::=   A .. Z | a .. z | SPACE
  
  FontSizeDeclarationRest  ::=  s i z e OptionalSpaces : OptionalSpaces Digit ( | Digit) p t
  
  Digit  ::=  0..9
  
  TextAlignmentDeclaration  ::=  t e x t - a l i g n OptionalSpaces : OptionalSpaces TextAlignValue
  
  TextAlignValue  ::=  l e f t | r i g h t | c e n t e r | j u s t i f y

  (Note that "left" and "right" in this context means "the beginning of the line" and "the end of the line", the actual positioning depending on whether the text is read left-to-right or right-to-left.)
  
  Rules for OptionalSpaces and Name are defined in HTMLGrammar.
"""

# exposed procedures
# ------------------

def emit_style_sheet(n,d,w):
  """ 
  pre:
    n = font name for this document's body, as unicoding3_0.String
    d = font size for this document's body in range 0.0 - 99.0, as float
    w = unicode_io.Writer to which this style sheet is to be emitted
    
  post:
    style sheet for this document has been emitted to w,
      including font name and size, 
        and definitions for <p>, <p.begin>, <p.middle>, <p.end> and <p.justify>

  syntax:
    StyleSheet  ::=  OptionalSpaces Rule*
    
    OptionalSpaces  ::=  SpaceChar*

    SpaceChar  ::=  (SPACE | TAB | LF | FF | CR)
                    (U+0020 | U+0009 | U+000A | U+000C | U+000D )
                    
    Rule  ::=  Selector OptionalSpaces DeclarationBlock OptionalSpaces
    
    Selector  :==  DotName
    
    DotName  ::=  Name ( . Name | )

  test:
    once thru
  """
  type_checking2_0.check_derivative(n,unicoding3_0.String)
  type_checking2_0.check_identical(d,float)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  _emit_font_name_rule(unicoding3_0.string_of("body"),n,w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_font_size_rule(unicoding3_0.string_of("body"),d,w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_text_alignment_rule(unicoding3_0.string_of("p"),unicoding3_0.string_of("left"),w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_text_alignment_rule(unicoding3_0.string_of("p.begin"),unicoding3_0.string_of("left"),w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_text_alignment_rule(unicoding3_0.string_of("p.middle"),unicoding3_0.string_of("center"),w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_text_alignment_rule(unicoding3_0.string_of("p.end"),unicoding3_0.string_of("right"),w)
  _emit_name_string(_LINE_SEPARATOR,w)
  _emit_text_alignment_rule(unicoding3_0.string_of("p.justify"),unicoding3_0.string_of("justify"),w)
  _emit_name_string(_LINE_SEPARATOR,w)
  

# private members
# ---------------
_LINE_SEPARATOR = unicoding3_0.string_of("\n")
# default to Unix

def _emit_font_name_rule(s,n,w):
  """ 
  pre:
    s = selector string for rule, as unicoding3_0.String
    n = font name for rule, as unicoding3_0.String
    w = unicode_io.Writer on which rule is to be emitted
    
  post:
    either:
      appropriate rule has been emitted to w
    or:
      an Exception has been raised

  syntax:
    Rule  ::=  Selector Spaces DeclarationBlock Spaces
    
    Selector  :==  DotName
    
    DotName  ::=  Name ( . Name | )
    
    Name  ::=  NameChar NameChar*

    NameChar  ::=  ( a .. z | 0 .. 9 )
                   ( U+0061 .. U+007A | U+0030 .. U+0039 )
                   
    DeclarationBlock  ::=  { OptionalSpaces Declaration OptionalSpaces ; OptionalSpaces 
                            (Declaration OptionalSpaces ; OptionalSpaces)* }

    Declaration  ::=  FontDeclaration | TextAlignmentDeclaration
    
    FontDeclaration  ::=  f o n t - (FontNameDeclarationRest | FontSizeDeclarationRest)
      
    FontNameDeclarationRest  ::=  f a m i l y OptionalSpaces : OptionalSpaces FontName
    
    FontName  ::=  " FontNameCharacter FontNameCharacter* "
    
    FontNameCharacter  ::=   A .. Z | a .. z | SPACE

  test:
    s = ""
      n = ""
    s = "fred"
      n = "Times New Roman"
  """
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord(' '),w)
  _emit_name_string(s,w)
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord('{'),w)
  unicode_io.write(ord('f'),w)
  unicode_io.write(ord('o'),w)
  unicode_io.write(ord('n'),w)
  unicode_io.write(ord('t'),w)
  unicode_io.write(ord('-'),w)
  unicode_io.write(ord('f'),w)
  unicode_io.write(ord('a'),w)
  unicode_io.write(ord('m'),w)
  unicode_io.write(ord('i'),w)
  unicode_io.write(ord('l'),w)
  unicode_io.write(ord('y'),w)
  unicode_io.write(ord(':'),w)
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord('\"'),w)
  _emit_name_string(n,w)
  unicode_io.write(ord('\"'),w)
  unicode_io.write(ord(';'),w)
  unicode_io.write(ord('}'),w)
  

def _emit_font_size_rule(s,d,w):
  """ 
  pre:
    s = selector string for rule, unicoding3_0.String
    d = font size for rule in range 0.0 - 99.0, as a float
    w = unicode_io.Writer on which rule is to be emitted
    
  post:
    either:
      appropriate rule has been emitted to w
    or:
      IOException has been raised

  syntax:
    Rule  ::=  Selector Spaces DeclarationBlock Spaces
    
    Selector  :==  DotName
    
    DotName  ::=  Name ( . Name | )
    
    Name  ::=  NameChar NameChar*

    NameChar  ::=  ( a .. z | 0 .. 9 )
                   ( U+0061 .. U+007A | U+0030 .. U+0039 )
                   
    FontDeclaration  ::=  f o n t - (FontNameDeclarationRest | FontSizeDeclarationRest)
      
    FontSizeDeclarationRest  ::=  s i z e OptionalSpaces : OptionalSpaces Digit ( | Digit) p t
    
    Digit  ::=  0..9

  test:
    s = ""
      d = 0.0
    s = "jim"
      d = 9.0
    s = "bert"
      d = 10.0
    s = "harold"
      d = 99.0
  """
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord(' '),w)
  _emit_name_string(s,w)
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord('{'),w)
  unicode_io.write(ord('f'),w)
  unicode_io.write(ord('o'),w)
  unicode_io.write(ord('n'),w)
  unicode_io.write(ord('t'),w)
  unicode_io.write(ord('-'),w)
  unicode_io.write(ord('s'),w)
  unicode_io.write(ord('i'),w)
  unicode_io.write(ord('z'),w)
  unicode_io.write(ord('e'),w)
  unicode_io.write(ord(':'),w)
  unicode_io.write(ord(' '),w)
  i = int(d)
  dig0 = i%10
  dig1 = int(i/10)
  if dig1 != 0:
    unicode_io.write(ord('0') + dig1,w)
  unicode_io.write(ord('0') + dig0,w)
  unicode_io.write(ord('p'),w)
  unicode_io.write(ord('t'),w)
  unicode_io.write(ord(';'),w)
  unicode_io.write(ord('}'),w)
  

def _emit_name_string(s,w):
  """ 
  pre:
    s = name string which is to be emitted, as unicoding3_0.String
          (string must be lower case and must not contain '<' or '&')
    w = unicode_io.Writer to which s is to be emitted
    
  post:
    s has been emitted on w

  syntax:
    DotName  ::=  Name ( . Name | )
    
    Name  ::=  NameChar NameChar*

    NameChar  ::=  ( a .. z | 0 .. 9 )
                   ( U+0061 .. U+007A | U+0030 .. U+0039 )

  test:
    empty string
    "cat"
  """
  i = 0
  while i < unicoding3_0.length_of(s):
    unicode_io.write(unicoding3_0.code_point_at(s,i),w)    
    i += 1
  

def _emit_text_alignment_rule(s,a,w):
  """ 
  pre:
    s = selector string for rule, as unicoding3_0.String
    a = alignment value for this selector, unicoding3_0.String
    w = unicode_io.Writer on which rule is to be emitted
    
  post:
    either:
      appropriate rule has been emitted to w
    or:
      an Exception has been raised

  syntax:
    Rule  ::=  Selector OptionalSpaces DeclarationBlock OptionalSpaces
    
    Selector  :==  DotName
    
    DotName  ::=  Name ( . Name | )
                     
    Name  ::=  NameChar NameChar*

    NameChar  ::=  ( a .. z | 0 .. 9 )
                   ( U+0061 .. U+007A | U+0030 .. U+0039 )

    DeclarationBlock  ::=  { OptionalSpaces Declaration OptionalSpaces ; OptionalSpaces 
                            (Declaration OptionalSpaces ; OptionalSpaces)* }

    Declaration  ::=  FontDeclaration | TextAlignmentDeclaration
    
    TextAlignmentDeclaration  ::=  t e x t - a l i g n OptionalSpaces : OptionalSpaces TextAlignValue
    
    TextAlignValue  ::=  l e f t | r i g h t | c e n t e r | j u s t i f y

    (Note that "left" and "right" in this context means "the beginning of the line" and "the end of the line", the actual positioning depending on whether the text is read left-to-right or right-to-left.)
    
  test:
    s = ""
      a = ""
    s = "fred"
      a = "left"
  """
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord(' '),w)
  _emit_name_string(s,w)
  unicode_io.write(ord(' '),w)
  unicode_io.write(ord('{'),w)
  unicode_io.write(ord('t'),w)
  unicode_io.write(ord('e'),w)
  unicode_io.write(ord('x'),w)
  unicode_io.write(ord('t'),w)
  unicode_io.write(ord('-'),w)
  unicode_io.write(ord('a'),w)
  unicode_io.write(ord('l'),w)
  unicode_io.write(ord('i'),w)
  unicode_io.write(ord('g'),w)
  unicode_io.write(ord('n'),w)
  unicode_io.write(ord(':'),w)
  unicode_io.write(ord(' '),w)
  _emit_name_string(a,w)
  unicode_io.write(ord(';'),w)
  unicode_io.write(ord('}'),w)
  

# test program
# ------------

def _test():
  print("Tests of _emit_name_string", end=' ')
  w = unicode_io.new_string_writer()
  s = unicoding3_0.new_string()
  _emit_name_string(s,w)
  assert unicoding3_0.length_of(unicode_io.get_string(w)) == 0
  w = unicode_io.new_string_writer()
  s = unicoding3_0.string_of("cat")
  _emit_name_string(s,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("cat"))
  print("OK")
  
  print("Tests of _emit_font_name_rule", end=' ')
  w = unicode_io.new_string_writer()
  s = unicoding3_0.new_string()
  n = unicoding3_0.new_string()
  _emit_font_name_rule(s,n,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {font-family: \"\";}"))
  s = unicoding3_0.string_of("fred")
  n = unicoding3_0.string_of("Times New Roman")
  w = unicode_io.new_string_writer()
  _emit_font_name_rule(s,n,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  fred {font-family: \"Times New Roman\";}"))
  print("OK")
  
  print("Tests of _emit_font_size_rule", end=' ')
  s = unicoding3_0.new_string()
  w = unicode_io.new_string_writer()
  _emit_font_size_rule(s,0.0,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {font-size: 0pt;}"))
  s = unicoding3_0.string_of("jim")
  w = unicode_io.new_string_writer()
  _emit_font_size_rule(s,9.0,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  jim {font-size: 9pt;}"))
  s = unicoding3_0.string_of("bert")
  w = unicode_io.new_string_writer()
  _emit_font_size_rule(s,10.0,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  bert {font-size: 10pt;}"))
  s = unicoding3_0.string_of("harold")
  w = unicode_io.new_string_writer()
  _emit_font_size_rule(s,99.0,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  harold {font-size: 99pt;}"))
  print("OK")
  
  print("Tests of _emit_text_alignment_rule", end=' ')
  s = unicoding3_0.new_string()
  a = unicoding3_0.new_string()
  w = unicode_io.new_string_writer()
  _emit_text_alignment_rule(s,a,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {text-align: ;}"))
  s = unicoding3_0.string_of("fred")
  a = unicoding3_0.string_of("left")
  w = unicode_io.new_string_writer()
  _emit_text_alignment_rule(s,a,w)
  assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  fred {text-align: left;}"))
  print("OK")
  
  print("Tests of emit_style_sheet", end=' ')
  w = unicode_io.new_output_writer("css.test")
  emit_style_sheet(unicoding3_0.string_of("Palatino"),18.0,w)
  unicode_io.write(unicode_io.END_OF_STREAM,w)
  print("  check file css.test")
  print("OK")
  
  print("")


if __name__ == "__main__":
  import sys
  _test()
  print("All tests OK")

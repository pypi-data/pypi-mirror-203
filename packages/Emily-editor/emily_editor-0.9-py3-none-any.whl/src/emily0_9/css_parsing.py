from guibits1_0 import type_checking2_0
from . import code_point_testing
from . import html_css_parsing
from . import looking_ahead
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 9 Mar 23  15:45
""" 
Contractor for parsing Cascading Style Sheets (simplified syntax!).

Copyright (C) 2016,2017,2018,2021,2022,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.

  CSS Grammar version 17.3.18   15:54

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
  
  Rules for OptionalSpaces and Name are defined in HTMLCSSGrammar.
"""

# exposed types
# -------------

class StyleProperties:
  pass  

# exposed procedures
# ------------------

def alignment_of(sp,s):
  """ 
  pre:
    sp = StyleProperties variable whose alignment properties are to be accessed
    s = unicoding3_0.String whose alignment in sp is to be found
  
  post:
    CSS alignment value corresponding to s in sp has been returned,
      or "left" if no match for s is found

  test:
    sp with mapping from "p.end" to "right"
      s = "p.end"
      s = "p"
  """
  type_checking2_0.check_derivative(sp,StyleProperties)
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  js = sp._text_alignment_map.get(unicoding3_0.python_string_of(s))
  if js == None:
    return unicoding3_0.string_of("left")
  else:
    return unicoding3_0.string_of(js)
    
  
def font_name_of(sp):
  """ 
  pre:
    sp = StyleProperties variable to be examined
  
  post:
    font name of sp has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(sp,StyleProperties)  
  return sp._font_name
  

def font_size_of(sp):
  """ 
  pre:
    sp = StyleProperties variable to be examined
  
  post:
    font size of sp has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(sp,StyleProperties)
  return sp._font_size
  

def parse_style_sheet(la):
  """ 
  pre:
    la = lookahead which is to be parsed
  
  post:
    returns StyleProperties variable corresponding to StyleSheet which has been parsed
      (empty StyleSheet gives default StyleProperties variable)
    la has been advanced past StyleSheet

  syntax:
    StyleSheet  ::=  OptionalSpaces Rule*

  test:
    "      "
    "  p{font-size:10pt;}  p{font-size:8pt;}  "
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  sp = _new_style_properties()
  sp._font_name = unicoding3_0.string_of("Times New Roman")
  sp._font_size = 12.0
  html_css_parsing.accept_optional_spaces(la)
  while code_point_testing.is_name_char(looking_ahead.current_symbol_of(la)):
    _parse_rule(la,sp)
  return sp
  

# private members
# ---------------

def _is_digit(cp):
  """ 
  pre:
    cp = code point to be tested
  
  post:
    returns true iff cp is a Digit

  syntax:
    Digit  ::=  0..9
                ( U+0030 .. U+0039 )

  test:
    cp = '/'
         '0'
         '9'
         ':'
  """
  return (ord('0') <= cp and cp <= ord('9'))
  

def _is_font_name_char(cp):
  """ 
  pre:
    cp = code point to be tested
  
  post:
    returns true iff cp is a CSS font name character

  syntax:
    FontNameCharacter  ::=   A .. Z | a .. z | SPACE

  test:
    cp = @
         A
         Z
         [
         U+0060
         a
         z
         {
         U+001F
         U+0020
         U+0021
  """
  return (ord('A') <= cp and cp <= ord('Z') or ord('a') <= cp and cp <= ord('z') or cp == ord(' '))
  

def _new_style_properties():
  """
  pre:
    True
    
  post:
    a new StyleProperties variable has been returned,
      with default values
      
  test:
    once thru (check values)
  """
  sp = StyleProperties()
  sp._text_alignment_map = dict()  
  # map between selector names and alignment values:
  #   left, right, center, justify
  sp._font_name = None
  sp._font_size = 0.0
  return sp


def _parse_declaration(la,sp,s):
  """ 
  pre:
    la = lookahead which is being parsed
    sp = StyleProperties variable to be updated
    s = selector name for this Declaration
  
  post:
    either
      sp has been updated with contents of Declaration
      lookahead has been advanced past Declaration
    or:
      RuntimeException has been thrown
 
  syntax:
    Declaration  ::=  FontDeclaration | TextAlignmentDeclaration

  test:
    s = "body"
      la = "font-family:\"Times New Roman\""
    s = "p.begin"
      la = "text-align:left"
    s = "p.end"
      la = "complete-load-of-rubbish"
  """
  if looking_ahead.current_symbol_of(la) == ord('f'):
    _parse_font_declaration(la,sp)
  elif looking_ahead.current_symbol_of(la) == ord('t'):
    _parse_text_alignment_declaration(la,s,sp._text_alignment_map)
  else:
    raise Exception("Unexpected declaration: expected FontDeclaration or TextAlignmentDeclaration, " + "found declaration beginning with U+" + format(looking_ahead.current_symbol_of(la),'x'))
  

def _parse_declaration_block(la,sp,s):
  """ 
  pre:
    la = lookahead which is being parsed
    sp = StyleProperties variable to be updated
    s = selector name for this DeclarationBlock

  post:
    either
      sp has been updated with contents of DeclarationBlock
      lookahead has been advanced past DeclarationBlock
    or:
      RuntimeException has been thrown

  syntax:
    DeclarationBlock  ::=  { OptionalSpaces Declaration OptionalSpaces ; OptionalSpaces 
                            (Declaration OptionalSpaces ; OptionalSpaces)* }

  test:
    [  font-family:"Times New Roman"}
    {  zont-family:"Times New Roman"}
    {  font-family:"Times New Roman"  ]
    {  font-family:"Times New Roman"  }
    {font-family:"Times New Roman";}
    {  font-family:"Times New Roman"  ; font-family:"Palatino"  }
    {  font-family:"Times New Roman"  ; font-family:"Palatino"  ;  }
    {  
      font-family:"Times New Roman"  ; 
      font-size:10pt  ;  
      font-family:"Palatino"  ; 
      font-size:20pt    ;
      text-align:left;
      text-align:center;       
    }
  """
  html_css_parsing.accept(ord('{'),la)
  html_css_parsing.accept_optional_spaces(la)
  _parse_declaration(la,sp,s)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord(';'),la)
  html_css_parsing.accept_optional_spaces(la)
  while looking_ahead.current_symbol_of(la) != ord('}'):
    _parse_declaration(la,sp,s)
    html_css_parsing.accept_optional_spaces(la)
    html_css_parsing.accept(ord(';'),la)
    html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('}'),la)
  

def _parse_dot_name(la):
  """ 
  pre:
    la = lookahead which is being parsed
  
  post:
    either:
      returns HTML dot-name as lower-case unicoding3_0.String
      lookahead has been advanced past dot-name
    or:
      RuntimeException has been thrown

  syntax:
    DotName  ::=  Name ( . Name | )

  test:
    "%"
    "f"
    "fred%"
    "fred.jim"
  """
  s = html_css_parsing.parse_name(la)
  if looking_ahead.current_symbol_of(la) == ord('.'):
    unicoding3_0.append(s,(ord('.')))
    looking_ahead.advance(la)
    unicoding3_0.append_a_copy(s,html_css_parsing.parse_name(la))
  return s
  

def _parse_font_declaration(la,sp):
  """ 
  pre:
    la = lookahead which is being parsed
    sp = StyleProperties variable to be updated
  
  post:
    either:
      sp has been updated with contents of FontDeclaration
      lookahead has been advanced past FontDeclaration
    or:
      RuntimeException has been thrown

  syntax:
    FontDeclaration  ::=  f o n t - (FontNameDeclarationRest | FontSizeDeclarationRest)

  test:
    fonu-family : "Times New Roman"
    font=family : "Times New Roman"
    font-family : "Times New Roman"
    font-size : 42.0;
    font-blob : "blobbie"
  """
  html_css_parsing.accept_name(unicoding3_0.string_of("font"),la)
  html_css_parsing.accept(ord('-'),la)
  if looking_ahead.current_symbol_of(la) == ord('f'):
    sp._font_name = _parse_font_name_declaration_rest(la)
  elif looking_ahead.current_symbol_of(la) == ord('s'):
    sp._font_size = _parse_font_size_declaration_rest(la)
  else:
    raise Exception("unexpected code point, expected U+" + format(ord('f'),'x') + " or U+" + format(ord('s'),'x') + ", found U+" + format(looking_ahead.current_symbol_of(la),'x'))
  

def _parse_font_name(la):
  """ 
  pre:
    la = lookahead which is being parsed
  
  post:
    either:
      returns font name as unicoding3_0.String
      lookahead has been advanced past FontName
    or:
      RuntimeException has been thrown

  syntax:
    FontName  ::=  " FontNameCharacter FontNameCharacter* "

  test:
    ''
    ""
    "a"
    "a%"
    "Times Roman'
    "Times Roman"
  """
  s = unicoding3_0.new_string()
  html_css_parsing.accept(ord('\"'),la)
  if  not _is_font_name_char(looking_ahead.current_symbol_of(la)):
    raise Exception("unexpected code point in font name: U+" + format(looking_ahead.current_symbol_of(la),'x'))
  unicoding3_0.append(s,(looking_ahead.current_symbol_of(la)))
  looking_ahead.advance(la)
  while _is_font_name_char(looking_ahead.current_symbol_of(la)):
    unicoding3_0.append(s,(looking_ahead.current_symbol_of(la)))
    looking_ahead.advance(la)
  html_css_parsing.accept(ord('\"'),la)
  return s
  

def _parse_font_name_declaration_rest(la):
  """ 
  pre:
    la = lookahead which is being parsed
  
  post:
    either:
      returns font name as unicoding3_0.String
      lookahead has been advanced past FontNameDeclaration
    or:
      RuntimeException has been thrown

  syntax:
    FontNameDeclarationRest  ::=  f a m i l y OptionalSpaces : OptionalSpaces FontName

  test:
    familz:"New Century Schoolbook"
    family;"New Century Schoolbook"
    family:"New Century Schoolbook"
    family  :  "Gill Sans"
  """
  html_css_parsing.accept_name(unicoding3_0.string_of("family"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord(':'),la)
  html_css_parsing.accept_optional_spaces(la)
  return _parse_font_name(la)
  

def _parse_font_size_declaration_rest(la):
  """ 
  pre:
    la = lookahead which is being parsed
  
  post:
    either:
      returns font size in points as double
      lookahead has been advanced past FontSizeDeclaration
    or:
      RuntimeException has been thrown

  syntax:
    FontSizeDeclarationRest  ::=  s i z e OptionalSpaces : OptionalSpaces Digit ( | Digit) p t

  test:
    tize:0pt
    sjze:0pt
    siye:0pt
    sizf:0pt
    size;0pt
    size:/pt
    size:0pt
    size:9pt
    size::pt
    size:1/pt
    size:10pt
    size:19pt
    size:1:pt
    size:99qt
    size:99pu
    size:99pt
    size  :  99pt
  """
  html_css_parsing.accept_name(unicoding3_0.string_of("size"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord(':'),la)
  html_css_parsing.accept_optional_spaces(la)
  if  not _is_digit(looking_ahead.current_symbol_of(la)):
    raise Exception("unexpected code point in number: U+" + format(looking_ahead.current_symbol_of(la),'x'))
  d = looking_ahead.current_symbol_of(la) - ord('0')
  looking_ahead.advance(la)
  if _is_digit(looking_ahead.current_symbol_of(la)):
    d = d*10.0 + (looking_ahead.current_symbol_of(la) - ord('0'))
    looking_ahead.advance(la)
  html_css_parsing.accept(ord('p'),la)
  html_css_parsing.accept(ord('t'),la)
  return d
  

def _parse_rule(la,sp):
  """ 
  pre:
    la = lookahead which is being parsed
    sp = StyleProperties variable to be updated
  
  post:
    either
      sp has been updated with contents of Rule
      lookahead has been advanced past Rule
    or:
      RuntimeException has been thrown

  syntax:
    Rule  ::=  Selector OptionalSpaces DeclarationBlock OptionalSpaces
  
    Selector  :==  DotName

  test:
    "p.begin   {font-family:\"Palatino\";font-size:40;text-align:left;}  "
    "p.end{text-align:right;}"
  """
  s = _parse_dot_name(la)
  html_css_parsing.accept_optional_spaces(la)
  _parse_declaration_block(la,sp,s)
  html_css_parsing.accept_optional_spaces(la)
  

def _parse_text_alignment_declaration(la,s,m):
  """ 
  pre:
    la = lookahead which is being parsed
    s = selector name for the current rule being parsed
    m = map which contains the current mappings between selector names and alignments
  
  post:
    m has been updated with a new mapping from s to the parsed alignment value
    la has been advanced past the text alignment declaration

  syntax:
    TextAlignmentDeclaration  ::=  t e x t - a l i g n Spaces : Spaces TextAlignValue

  test:
    s = "fred"
      la = "text-aligm:left"
           "text-align:left"
    s = "jim"
      la = "text-align   :   justify"
  """
  html_css_parsing.accept_name(unicoding3_0.string_of("text"),la)
  html_css_parsing.accept(ord('-'),la)
  html_css_parsing.accept_name(unicoding3_0.string_of("align"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord(':'),la)
  html_css_parsing.accept_optional_spaces(la)
  av = _parse_text_align_value(la)
  m[unicoding3_0.python_string_of(s)] = unicoding3_0.python_string_of(av)
  

def _parse_text_align_value(la):
  """ 
  pre:
    la = lookahead which is being parsed
    sp = StyleProperties variable to be updated
  
  post:
    either:
      returns text align value as lower case unicoding3_0.String
      lookahead has been advanced past text align value
    or:
      RuntimeException has been thrown

  syntax:
    TextAlignValue  ::=  l e f t | r i g h t | c e n t e r | j u s t i f y

  test:
    "bollocks"
    "left"
    "LEFT"
    "RIGHT"
    "right"
    "center"
    "CENTER"
    "JUSTify"
    "just_i_f_y"
  """
  s = html_css_parsing.parse_name(la)
  if unicoding3_0.equals(s,unicoding3_0.string_of("left")) or \
     unicoding3_0.equals(s,unicoding3_0.string_of("right")) or \
     unicoding3_0.equals(s,unicoding3_0.string_of("center")) or \
     unicoding3_0.equals(s,unicoding3_0.string_of("justify")):
    return s
  else:
    raise Exception("Unexpected alignment value: " + unicoding3_0.python_string_of(s))

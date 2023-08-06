# Contractor which converts text to tokens.

# author R.N.Bosworth

# version 8 Mar 23  10:56

from guibits1_0 import type_checking2_0, unicoding3_0
from . import code_point_testing, texting

""" 

Copyright (C) 2018,2019,2021,2022,2023  R.N.Bosworth

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
  Text Grammar version 4 Feb 2019   09:29
  
  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive.
  
  Text  ::==  OptionalSpaces TextLine TextLine* END_OF_TEXT
  
  TextLine  ::==  Element* NewLine
  
  Element  ::==  Word | Separator

  Word  ::==  NonSpaceChar NonSpaceChar*
  
  NonSpaceChar is any HtmlCharacter except LF, SPACE, TAB, FF or CR
  
  Separator  ::==  SPACE (U+0020)
  
  Newline  ::==  LF (U+000A)
                                                               
  Note 1: Rule for OptionalSpaces is given in HTMLCSSGrammar.  Rule for HtmlCharacter is given in HTMLGrammar.
  
  Note 2: An Internal Paragraph is a series of TextLines terminated by a blank line or END_OF_TEXT.  Every TextLine of an Internal Paragraph has the same alignment.     
"""
""" 
  Token Grammar version 11 Feb 2019   14:43

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive.
    

  Text  ::==  Token* EndTag
  
  Token  ::==  Word | Separator | NewLine | InternalTag
  
  EndTag  ::==  < e n d >
  
  Word  ::==  NonSpaceChar NonSpaceChar*
  
  NonSpaceChar is any HtmlCharacter except LF, SPACE, TAB, FF or CR
  
  Separator  ::==  SPACE (U+0020)
  
  Newline  ::==  LF (U+000A)
  
  InternalTag  ::==   (this will be extended later)
  
  Note: Rule for HtmlCharacter is given in HTMLGrammar.
"""


# exposed procedures
# ------------------

def get_next_token(t):
  """ 
  pre:
   t = texting.Text that is being parsed to tokens

  post:
    the next token of t has been returned
    t's cursor is just beyond the returned token 

  syntax:
    Text  ::=  Token* EndTag
    
    Token  ::=  Word | Separator | InternalTag
    
    EndPageTag  ::=  < e n d >

  test:
    t = None
    t = "<i> fred"
      call get_next_token 5 times
  """
  type_checking2_0.check_derivative(t,texting.Text)
  if texting.current_code_point(t) == texting.END_OF_TEXT:
    return unicoding3_0.string_of("<end>")
  else:
    return _parse_token(t)
    

# private procedures
# ------------------

def _parse_token(t):
  """ 
  pre:
    t = texting.Text which is being parsed
    
  post:
    the next token of t has been returned
    t's cursor is just beyond the returned token 

  syntax:
    Token  ::==  Word | Separator | NewLine | InternalTag
  
    Word  ::==  NonSpaceChar NonSpaceChar*
    
    NonSpaceChar is any HtmlCharacter except LF, SPACE, TAB, FF or CR
    
    Separator  ::==  SPACE (U+0020)
    
    Newline  ::==  LF (U+000A)
    
    InternalTag  ::==   (this will be extended later)
      
  test:
    text = " fred<b>x\nbert"
      call _parse_token 8 times
  """
  s = unicoding3_0.new_string()
  if texting.current_code_point(t) == ord('\n'):
    texting.advance(t)
    unicoding3_0.append(s,ord('\n'))
  elif code_point_testing.is_space_char(texting.current_code_point(t)):
    texting.advance(t)
    unicoding3_0.append(s,ord(' '))
  elif texting.current_code_point(t) == ord('<'):
    texting.advance(t)
    tag_label = unicoding3_0.new_string()
    while texting.current_code_point(t) != ord('>'):
      unicoding3_0.append(tag_label,texting.current_code_point(t))
      texting.advance(t)
    texting.advance(t)
    unicoding3_0.append(s,ord('<'))
    unicoding3_0.append_a_copy(s,tag_label)
    unicoding3_0.append(s,ord('>'))
  else:  # must be NonSpaceChar - start of Word
    unicoding3_0.append(s,texting.current_code_point(t))
    texting.advance(t)
    while texting.current_code_point(t) != ord('<') and ( not code_point_testing.is_space_char(texting.current_code_point(t)) and texting.current_code_point(t) != texting.END_OF_TEXT):
      unicoding3_0.append(s,texting.current_code_point(t))
      texting.advance(t)
  return s

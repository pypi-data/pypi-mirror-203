from . import html_emitting, texting
from guibits1_0 import type_checking2_0
from . import unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 7 Mar 23  20:14
""" 
Parser which converts an Emily text to an MLE stream.

This parser is written using recursive descent, a la Watt and Brown(2000).

This parser is written as a Contractor, i.e. using pure procedures 
with explicit parameters.

Copyright (C) 2012,2015,2016,2017,2018,2019,2021,2022,2023  R.N.Bosworth

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
  ________________________________________________________________
  
  MLE Grammar version 1 Dec 2018   15:14  (reduced version for text translation only)
  
  This grammar is a reduced version of the HTML grammar given in WHATWG's HTML5 website.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  Parameterization is used to distinguish specialized non-terminals such as tags.

  
  BodyElement  ::==  
    StartTag(body) OptionalSpaces (ParagraphOrBreak  OptionalSpaces)* 
	    EndTag(body)
    (note: paragraphs start and end with a Newline in the Emily text)
    
  ParagraphOrBreak  ::==  (Paragraph | BreakTag)
                    
  BreakTag  ::==  StartTag(br)

  Paragraph  ::==  ParagraphStartTag OptionalSpaces ParagraphText EndTag(p)
  
  ParagraphStartTag  ::==  < p ( > | Separator ( > | ClassAttribute OptionalSpaces > ))
  
  ClassAttribute  ::==  c l a s s OptionalSpaces = 
                          OptionalSpaces " ClassName "
  
  ClassName  ::==  ( b e g i n |  m i d d l e | e n d )
                   
  ParagraphText  ::== (HtmlCharacter | BreakTag OptionalSpaces)*
                      (note: in the Emily internal text,
                       code points remain escaped,
                       words are separated by a single space, 
                       and each BreakTag is replaced by a newline.)
                       
  Note: Rules for OptionalSpaces and Separator are given in the HTMLCSSGrammar.  Rules for HtmlCharacter, StartTag and EndTag are given in the HTMLGrammar.
"""

# exposed procedures
# ------------------

def parse_text(t,w):
  """ 
  pre:
    t = texting.Text to be parsed
    w = unicode_io.Writer through which the HTML output is to be written
    
  post:
    text has been emitted as an MLE page (HTML5 standard)

  syntax:
    Text  ::==  OptionalSpaces TextLine TextLine* END_OF_TEXT
    
    TextLine  ::==  Element* NewLine
    
    Element  ::==  Word | Separator

    Word  ::==  NonSpaceChar NonSpaceChar*
    
    NonSpaceChar is any HtmlCharacter except LF, SPACE, TAB, FF or CR
    
    Separator  ::==  SPACE (U+0020)
    
    Newline  ::==  LF (U+000A)

  test:
    w = None
      t = None
    w = valid Writer
      t = ""
      t = "\n\n"
      t = "the"
      t = "\nthe\ncat\n"
          "\nthe\n\ncat\n"
          "\nthe\n\ncat\n\n\nsat\n\n\n\n"
  """
  type_checking2_0.check_derivative(t,texting.Text)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  loff = texting.cursor_line_offset(t)
  cpoff = texting.cursor_code_point_offset(t)
  texting.set_cursor_start(t)
  in_para = False
  cp = texting.current_code_point(t)
  while cp != texting.END_OF_TEXT:
    if cp == ord('\n'):
      texting.advance(t)
      cp = texting.current_code_point(t)
      if cp == ord('\n') or cp == texting.END_OF_TEXT:
        if not in_para:
          html_emitting.emit_start_tag(unicoding3_0.string_of("br"),w)
          html_emitting.emit_new_line(w)
        else: # in_para
          html_emitting.emit_end_tag(unicoding3_0.string_of("p"),w)
          html_emitting.emit_new_line(w)
          in_para = False
      else:  # NL not followed by NL or EOT
        if in_para:
          html_emitting.emit_start_tag(unicoding3_0.string_of("br"),w)
          html_emitting.emit_new_line(w)
          html_emitting.emit_indent(w)
        else:  # not in_para            
          _emit_paragraph_start_tag(texting.get_alignment(t),w)
          html_emitting.emit_new_line(w)
          html_emitting.emit_indent(w)
          in_para = True
    else:  # not NL
      if not in_para:
        _emit_paragraph_start_tag(texting.get_alignment(t),w)
        html_emitting.emit_new_line(w)
        html_emitting.emit_indent(w)
        in_para = True
      unicode_io.write(cp,w)
      texting.advance(t)
      cp  = texting.current_code_point(t)
  # allow for non-terminated text
  if in_para:
    html_emitting.emit_end_tag(unicoding3_0.string_of("p"),w)
    html_emitting.emit_new_line(w)
    in_para = False
  texting.set_cursor(t,loff,cpoff)
  

# private members
# ---------------

def _emit_paragraph_start_tag(a,w):
  """ 
  pre:
    a = texting.Alignment of paragraph to be emitted
    w = unicode_io.Writer to which paragraph start is to be emitted
    
  post:
    paragraph start tag of Alignment a has been emitted to w

  test:
    a = BEGIN
        MIDDLE
        END
  """
  if a == texting.Alignment.BEGIN:
    html_emitting.emit_start_tag(unicoding3_0.string_of("p class=\"begin\""),w)
  elif a == texting.Alignment.MIDDLE:
    html_emitting.emit_start_tag(unicoding3_0.string_of("p class=\"middle\""),w)
  elif a == texting.Alignment.END:
    html_emitting.emit_start_tag(unicoding3_0.string_of("p class=\"end\""),w)
  else:
    pass

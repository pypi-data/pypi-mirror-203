from . import css_emitting
from . import html_emitting
from . import texting
from . import text_emitting
from guibits1_0 import type_checking2_0
from . import unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 9 Mar 23  15:27
""" 
Contractor for emitting an MLE document.

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
  MLE Grammar version 17.3.18  15:53
  
  This grammar is a reduced version of the HTML grammar given in WHATWG's HTML5 website.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::=  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  Parameterization is used to distinguish specialized non-terminals such as tags.

  
  MleDocument  ::=  OptionalSpaces Doctype OptionalSpaces HtmlElement OptionalSpaces

  Doctype  ::=  < ! d o c t y p e Separator h t m l OptionalSpaces >
  
  HtmlElement  ::=  StartTag(html) OptionalSpaces HeadElement OptionalSpaces BodyElement 
                      OptionalSpaces EndTag(html)

  HeadElement  ::=  StartTag(head) OptionalSpaces MetaTag OptionalSpaces TitleElement 
                      OptionalSpaces StyleElement OptionalSpaces EndTag(head)
                     
  MetaTag  ::=  < m e t a Separator c h a r s e t OptionalSpaces = OptionalSpaces " U T F - 8 " 
                  OptionalSpaces >

  TitleElement  ::=  StartTag(title) Text EndTag(title)

  Text  ::=  EscapedUnicodeCodePoint*

  StyleElement  ::=  StartTag(style) OptionalSpaces StyleSheet OptionalSpaces EndTag(style)
                      (for StyleSheet syntax see CSSGrammar.txt)

  BodyElement  ::=  
    StartTag(body) OptionalSpaces (ParagraphOrBreak  OptionalSpaces)* 
	    EndTag(body)
    (note: paragraphs are separated by a blank line in the Emily text)
    
  ParagraphOrBreak  ::=  (Paragraph | BreakTag)
                    
  BreakTag  ::=  StartTag(br)

  Paragraph  ::=  ParagraphStartTag OptionalSpaces ParagraphText EndTag(p)
  
  ParagraphStartTag  ::=  < p ( > | Separator ( > | ClassAttribute OptionalSpaces > )) (ci)
  
  ClassAttribute  ::==  c l a s s OptionalSpaces = 
                          OptionalSpaces " ClassName "
  
  ClassName  ::==  ( b e g i n |  m i d d l e | e n d | j u s t i f y )
                   
  ParagraphText  ::= (EscapedUnicodeCodePoint | BreakTag OptionalSpaces)*
                      (note: in the Emily internal text,
                       code points remain escaped,
                       words are separated by a single space, 
                       and each BreakTag is followed by a newline.)
                       
  Note: Rules for OptionalSpaces and Separator are given in the HTMLCSSGrammar.  Rules for EscapedUnicodeCodePoint, StartTag and EndTag are given in the HTMLGrammar.
   
  Simplifications from HTML5:
  
   1. No legacy string in Doctype.
   
   2. Html start and end tags mandatory.
   
   3. No attributes in start tag (for the moment).
   
   4. No solidus in start tag.
   
   5. Head contains only title.
   
   6. Body contains only paragraphs and break tags.
   
   7. Paragraph has mandatory end tag.
   
   8. Comments not allowed (for security).
   
   9. Tags and attribute names are case-sensitive.
"""


# exposed procedures
# ------------------

def emit_emily_document(n,d,v,t,w):
  """ 
  pre:
    n = font name for this document's body, as unicoding3_0.String
    d = font size for this document's body in range 0.0 - 99.0, as float
    v = version number of this version of Emily, as unicoding3_0.String
    t = texting.Text which is to be emitted
    w = unicode_io.Writer on which t is to be emitted

  test:
    n = None
    n = valid font name
      d = None
      d = -0.1
      d = 99.1
      d =10.0
        v = None
        v = valid version number string
        t = None
        t = empty text
          w = None
          w = valid Writer
        t = non-empty text
          w = valid Writer
  """
  type_checking2_0.check_derivative(n,unicoding3_0.String)
  type_checking2_0.check_identical(d,float)
  if d < 0.0 or d > 99.0:
    raise Exception("Attempt to emit text with font size < 0.0 or >99.0: d="+str(d))
  type_checking2_0.check_derivative(v,unicoding3_0.String)
  type_checking2_0.check_derivative(t,texting.Text)
  type_checking2_0.check_derivative(w,unicode_io.Writer)
  html_emitting.emit_start_tag(unicoding3_0.string_of("!doctype html"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("html"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("head"),w)
  html_emitting.emit_new_line(w)
  html_emitting. emit_indent(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("meta charset=\"UTF-8\""),w)
  html_emitting.emit_new_line(w)
  html_emitting. emit_indent(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("title"),w)
  vs = unicoding3_0.string_of("Emily version ")
  unicoding3_0.append_a_copy(vs,v)
  unicoding3_0.append_a_copy(vs,unicoding3_0.string_of(" Document"))
  html_emitting.emit_string(vs,w)
  html_emitting.emit_end_tag(unicoding3_0.string_of("title"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("style"),w)
  html_emitting.emit_new_line(w)
  css_emitting.emit_style_sheet(n,d,w)
  html_emitting.emit_end_tag(unicoding3_0.string_of("style"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_end_tag(unicoding3_0.string_of("head"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_start_tag(unicoding3_0.string_of("body"),w)
  html_emitting.emit_new_line(w)
  with t._my_lock:
    text_emitting.parse_text(t,w)
  html_emitting.emit_end_tag(unicoding3_0.string_of("body"),w)
  html_emitting.emit_new_line(w)
  html_emitting.emit_end_tag(unicoding3_0.string_of("html"),w)
  html_emitting.emit_new_line(w)
  unicode_io.write(unicode_io.END_OF_STREAM,w)

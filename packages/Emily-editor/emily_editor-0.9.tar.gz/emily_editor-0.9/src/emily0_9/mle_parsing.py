from . import code_point_testing
from . import css_parsing
from guibits1_0 import font_styling
from . import html_css_parsing
from . import html_parsing
from . import looking_ahead
from . import texting
from guibits1_0 import type_checking2_0
from . import unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 13 Mar 23  12:54
""" 
Contractor which parses an mle file via a code point lookahead to produce an Emily text.

This parser is written using recursive descent, a la Watt and Brown(2000).

Copyright (C) 2012,2015,2016,2017,2018,2019,2021,2023  R.N.Bosworth

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
  MLE Grammar version 1 Dec 2018   15:14
  
  This grammar is a reduced version of the HTML grammar given in WHATWG's HTML5 website.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  Parameterization is used to distinguish specialized non-terminals such as tags.

  
  MleDocument  ::==  OptionalSpaces Doctype OptionalSpaces HtmlElement OptionalSpaces

  Doctype  ::==  < ! d o c t y p e Separator h t m l OptionalSpaces >
  
  HtmlElement  ::==  StartTag(html) OptionalSpaces HeadElement OptionalSpaces BodyElement 
                      OptionalSpaces EndTag(html)

  HeadElement  ::==  StartTag(head) OptionalSpaces MetaTag OptionalSpaces TitleElement 
                      OptionalSpaces StyleElement OptionalSpaces EndTag(head)
                     
  MetaTag  ::==  < m e t a Separator c h a r s e t OptionalSpaces = OptionalSpaces " U T F - 8 " 
                  OptionalSpaces >

  TitleElement  ::==  StartTag(title) Text EndTag(title)

  Text  ::==  HtmlCharacter*

  StyleElement  ::==  StartTag(style) OptionalSpaces StyleSheet OptionalSpaces EndTag(style)
                      (for StyleSheet syntax see CSSGrammar.txt)

  BodyElement  ::==  
    StartTag(body) OptionalSpaces (ParagraphOrBreak  OptionalSpaces)* 
	    EndTag(body)
    (note: paragraphs are separated by a blank line in the Emily text)
    
  ParagraphOrBreak  ::==  (Paragraph | BreakTag)
                    
  BreakTag  ::==  StartTag(br)

  Paragraph  ::==  ParagraphStartTag OptionalSpaces ParagraphText EndTag(p)
  
  ParagraphStartTag  ::==  < p ( > | Separator ( > | ClassAttribute OptionalSpaces > )) (ci)
  
  ClassAttribute  ::==  c l a s s OptionalSpaces = 
                          OptionalSpaces " ClassName "
  
  ClassName  ::==  ( b e g i n |  m i d d l e | e n d )
                   
  ParagraphText  ::== (HtmlCharacter | BreakTag OptionalSpaces)*
                      (note: in the Emily internal text,
                       code points remain escaped,
                       words are separated by a single space, 
                       and each BreakTag is replaced by a newline.)
                       
  Note: Rules for OptionalSpaces and Separator are given in the HTMLCSSGrammar.  Rules for HtmlCharacter, StartTag and EndTag are given in the HTMLGrammar.
   
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

# exposed types
# -------------

class MLEResult:
  pass
  

# exposed procedures
# ------------------

def alignment_of(r,s):
  """ 
  pre:
    r = MLEResult of an mle parse
    s = string whose alignment is to be found
  
  post:
    alignment corresponding to s from r has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(r,MLEResult)
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  return css_parsing.alignment_of(r._my_style_properties,s)
  

def font_name_of(r):
  """ 
  pre:
    r = MLEResult of an mle parse
  
  post:
    font name discovered in parse has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(r,MLEResult)
  return css_parsing.font_name_of(r._my_style_properties)
  

def font_size_of(r):
  """ 
  pre:
    r = MLEResult of an mle parse
  
  post:
    font size discovered in parse has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(r,MLEResult)
  return css_parsing.font_size_of(r._my_style_properties)
  

def parse_mle_document(la):
  """ 
  pre:
    la = lookahead to be parsed
  
  post:
    either:
      Emily document has been parsed from la and the MLEResult returned
    or:
      Exception has been thrown
  
  syntax:
    MLEDocument  ::=  OptionalSpaces Doctype OptionalSpaces HtmlElement OptionalSpaces

  test:
    "<!doctype word><html><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"
    "<!doctype html><itml><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"
    "<!doctype html><html><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"
    "  <!doctype html>  <html>  <head>  <title>Your Grace</title>  <style>  p  { font-family  :  \"Helvetica\"  ;  }  p  {  font-size  :  2pt  ;  }  </style>  </head>  <body>  <p>A word.</p>  </body>  </html>  "
  """
  type_checking2_0.check_derivative(la,looking_ahead.Lookahead)
  html_css_parsing.accept_optional_spaces(la)
  _parse_doctype(la)
  html_css_parsing.accept_optional_spaces(la)
  r = _parse_html_element(la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(looking_ahead.END_OF_STREAM,la)
  return r
  

def text_of(r):
  """ 
  pre:
    r = MLEResult of an mle parse
  
  post:
    text discovered in parse has been returned

  test:
    once thru
  """
  type_checking2_0.check_derivative(r,MLEResult)
  return r._my_text
  

# private procedures
# ------------------

def _emit_hard_line_break(t):
  """ 
  pre:
    t = text whose content is to be extended, with cursor at end
  
  post:
    a hard line break has been emitted to t

  test:
    once thru
  """
  texting.insert_code_point(t,ord('\n'))


def _new_mle_result():
  """
  pre:
    True
    
  post:
    new MLEResult variable has been returned, with default values
    
  test:
    once thru (check values)
  """
  mler = MLEResult()
  mler._my_style_properties = None
  mler._my_text = None
  return mler
  

def _parse_body_element(la,t):
  """ 
  pre:
    la = lookahead to be parsed
    t = text whose content is to be extended, with cursor at end
  
  post:
    either:
      Emily body element has been parsed from la and appended as text to t
    or:
      RuntimeException has been thrown

  syntax:
    BodyElement  ::=  
      StartTag(body) OptionalSpaces (ParagraphOrBreak  OptionalSpaces)* 
        EndTag(body)
      (note: paragraphs are separated by a blank line in the Emily text)

  test:
    "<cody>  </body>"
    "<body>  </aody>"
    "<body>  </body>"
    "<body>  <br>  <p class = "middle">   first  para  </p>  <br>  <p>  1 &lt; 2 &amp; 2 &lt; 3  </p>  <br>  </body>"
  """
  html_parsing.accept_start_tag(unicoding3_0.string_of("body"),la)
  html_css_parsing.accept_optional_spaces(la)
  end_of_body = _parse_paragraph_or_break(la,t)
  while  not end_of_body:
    html_css_parsing.accept_optional_spaces(la)
    end_of_body = _parse_paragraph_or_break(la,t)
    
  
def _parse_class_attribute(la):
  """ 
  pre:
    la = lookahead to be parsed
  
  post:
    either:
      ClassAttribute has been parsed
      name of class element has been returned
    or:
      RuntimeException has been thrown

  syntax:
    ClassAttribute  ::==  c l a s s OptionalSpaces = 
                            OptionalSpaces " ClassName "

  tests:
    form="middle"
    class   -   "middle"
    class   =   'middle'
    class   =   "moddle"
    class   =   "middle'
    class   =   "middle"
    class="begin"
  """
  html_css_parsing.accept_name(unicoding3_0.string_of("class"),la)
  html_css_parsing. accept_optional_spaces(la)
  html_css_parsing.accept(ord('='),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('\"'),la)
  s = _parse_class_name(la)
  html_css_parsing.accept(ord('\"'),la)
  return s
  

def _parse_class_name(la):
  """ 
  pre:
    la = lookahead to be parsed
  
  post:
    either:
      ClassName has been parsed
      class name has been returned
    or:
      RuntimeException has been thrown

  syntax:
    ClassName  ::==  ( b e g i n |  m i d d l e | e n d ) 

  tests:
    "start"
    "begin"
    "middle"
    "end"
  """
  s = html_css_parsing.parse_name(la)
  if unicoding3_0.equals(s,unicoding3_0.string_of("begin")) or unicoding3_0.equals(s,unicoding3_0.string_of("middle")) or unicoding3_0.equals(s,unicoding3_0.string_of("end")) or unicoding3_0.equals(s,unicoding3_0.string_of("justify")):
    return s
  else:
    raise Exception("Unexpected class name: \"" + unicoding3_0.python_string_of(s) + "\"")
    
  
def _parse_doctype(la):
  """ 
  pre:
    la = lookahead to be parsed
  
  post:
    either:
      Doctype has been parsed
    or:
      RuntimeException has been thrown

  syntax:
    Doctype  ::=  < ! d o c t y p e Separator h t m l OptionalSpaces >  !!

  test:
    ">!doctype html>"
    "<£doctype html>"
    "<!doctypf html>"
    "<!doctypehtml>"
    "<!doctype   htmm>"
    "<!doctype   html   <"
    "<!doctype   html   >"
    "<!doctype html>"
  """
  html_css_parsing.accept(ord('<'),la)
  html_css_parsing.accept(ord('!'),la)
  html_css_parsing.accept_name(unicoding3_0.string_of("doctype"),la)
  html_css_parsing.accept_separator(la)
  html_css_parsing.accept_name(unicoding3_0.string_of("html"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('>'),la)
  

def _parse_head_element(la):
  """ 
  pre:
    la = token lookahead to be parsed
  
  post:
    either:
      Emily HeadElement has been parsed from la
      StyleProperties object for this HeadElement has been returned
    or:
      a RuntimeException has been thrown

  syntax:
    HeadElement  ::=  StartTag(head) OptionalSpaces MetaTag OptionalSpaces TitleElement 
                        OptionalSpaces StyleElement OptionalSpaces EndTag(head)

    TitleElement  ::=  StartTag(title) Text EndTag(title)

    Text  ::=  EscapedUnicodeCodePoint*

    StyleElement  ::=  StartTag(style) OptionalSpaces StyleSheet OptionalSpaces EndTag(style)
                        (for StyleSheet syntax see CSSGrammar.txt)

  test:
    "<title></title>
    "<head></head>"
    "<head>  </head>"
    "<head>  <meta charset=\"UTF-7\">"
    "<head>  <meta charset=\"UTF-8\">"
    "<head>  <meta charset=\"UTF-8\">  <title>"
    "<head>  <meta charset=\"UTF-8\">  <title>  </head>"
    "<head>  <meta charset=\"UTF-8\">  <title></title>  </title>"
    "<head>  <meta charset=\"UTF-8\">  <title></title>  </head>"
    "<head>  <meta charset=\"UTF-8\">  <title></title>  <stylf>  </style>  </head>"
    "<head>  <meta charset=\"UTF-8\">  <title></title>  <style>  </styld>  </head>"
    "<head>  <meta charset=\"UTF-8\">  <title>alchemist of the year</title>  <style>  </style>  </head>"
    "<head>  <meta charset=\"UTF-8\">  <title>fred</title>  <style>  p  {font-size:66pt;}  </style>  </head>"
  """
  html_parsing.accept_start_tag(unicoding3_0.string_of("head"),la)
  html_css_parsing.accept_optional_spaces(la)
  _parse_meta_tag(la)
  html_css_parsing.accept_optional_spaces(la)
  html_parsing.accept_start_tag(unicoding3_0.string_of("title"),la)
  while looking_ahead.current_symbol_of(la) != ord('<') and looking_ahead.current_symbol_of(la) != looking_ahead.END_OF_STREAM:
    looking_ahead.advance(la)
  html_parsing.accept_end_tag(unicoding3_0.string_of("title"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_parsing.accept_start_tag(unicoding3_0.string_of("style"),la)
  sp = css_parsing.parse_style_sheet(la)
  html_parsing.accept_end_tag(unicoding3_0.string_of("style"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_parsing.accept_end_tag(unicoding3_0.string_of("head"),la)
  return sp
  

def _parse_html_element(la):
  """
  pre:
    la = token lookahead to be parsed
    w = window on which Emily text is to be displayed
    mlw = maximum line width in points
    mph = maximum page height in points
  
  post:
    either:
      Emily HTML element has been parsed from la and an MLEResult has been returned
    or:
      a RuntimeException has been thrown

  syntax:
    HtmlElement  ::=  StartTag(html) OptionalSpaces HeadElement OptionalSpaces
                        BodyElement OptionalSpaces EndTag(html)

  test:
    "<htmm><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"
    "<html><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></htmk>"
    "<html><head><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"
    "<html><head><title>Your Grace</title><style>p{font-size:42pt;}</style></head><body><p>A word.</p></body></html>"
    "  <html>  <head>  <title>Your Grace</title>  <style>  p  {font-size:  53pt  ;  }  </style>  </head>  <body>  <p>  A phrase.  </p>  </body>  </html>  "
  """
  html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
  html_css_parsing.accept_optional_spaces(la)
  sp = _parse_head_element(la)
  html_css_parsing.accept_optional_spaces(la)
  fss = font_styling.new_font_styles()
  t = texting.new_text()
  _parse_body_element(la,t)
  html_css_parsing.accept_optional_spaces(la)
  html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
  mler = _new_mle_result()
  mler._my_style_properties = sp
  mler._my_text = t
  return mler
  

def _parse_meta_tag(la):
  """ 
  pre:
    la = lookahead to be parsed
  
  post:
    either:
      MetaTag has been parsed
    or:
      RuntimeException has been thrown
  
  syntax:

    MetaTag  ::=  < m e t a Separator c h a r s e t OptionalSpaces = OptionalSpaces 
                    " U T F - 8 " OptionalSpaces >
  test:
    ">meta charset=\"UTF-8\">"
    "<beta charset=\"UTF-8\">"
    "<metacharset=\"UTF-8\">"
    "<meta   charabanc=\"UTF-8\">"
    "<meta charset   -    \"UTF-8\">"
    "<meta charset   =    \'UTF-8\">"
    "<meta charset   =    \"UTE-8\">"
    "<meta charset   =    \"UTF-8\'>"
    "<meta charset   =    \"UTF-8\"<"
    "<meta charset   =    \"utf-8\">"
    "<meta charset=\"UTF-8\">"
  """
  html_css_parsing.accept(ord('<'),la)
  html_css_parsing.accept_name(unicoding3_0.string_of("meta"),la)
  html_css_parsing.accept_separator(la)
  html_css_parsing.accept_name(unicoding3_0.string_of("charset"),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('='),la)
  html_css_parsing.accept_optional_spaces(la)
  html_css_parsing.accept(ord('\"'),la)
  html_css_parsing.accept(ord('U'),la)
  html_css_parsing.accept(ord('T'),la)
  html_css_parsing.accept(ord('F'),la)
  html_css_parsing.accept(ord('-'),la)
  html_css_parsing.accept(ord('8'),la)
  html_css_parsing.accept(ord('\"'),la)
  html_css_parsing.accept(ord('>'),la)
  

def _parse_paragraph_or_break(la,t):
  """ 
  pre:
    la = token lookahead to be parsed
    t = text whose content is to be extended, with cursor at end
  
  post:
    either:
      a paragraph or a break tag has been parsed from la into t
      "false" has been returned
    or:
      the end of the body has been reached, 
        the </body> tag has been accepted, 
      "true" has been returned
    or:
      a RuntimeException has been thrown
  
  syntax:
    ParagraphOrBreak  ::=  (Paragraph | BreakTag)
                      
    BreakTag  ::=  StartTag(br)

    Paragraph  ::=  ParagraphStartTag OptionalSpaces ParagraphText EndTag(p)

    ParagraphStartTag  ::=  < p ( > | Separator ( > | ClassAttribute OptionalSpaces > ))

  tests:
    >p>
    <q>
    <bt>
    <br   <
    <br   >
    <p></p>
    <p>hello</q>
    <p>hello</p>
    <p   >hello</p>
    <p   clunk>hello</p>
    <p   class   =   "middle"   <
    <p   class   =   "justify"   >hello</p>
    <pclass="middle">hello</p>
    <p class="end">hello<br>world</p>
    <p class="end">hello</p><br>world
    <p class="middle">hello</p>
    <p class="muddle">hello</p>
    <p   class   =   "begin"   >   hello   </p   >
    </cody>
    </body>
  """
  paragraph_alignment = texting.Alignment.BEGIN
  html_css_parsing.accept(ord('<'),la)
  if looking_ahead.current_symbol_of(la) == ord('b'):
    looking_ahead.advance(la)
    html_css_parsing.accept(ord('r'),la)
    html_css_parsing.accept_optional_spaces(la)
    html_css_parsing.accept(ord('>'),la)
    _emit_hard_line_break(t)
    texting.set_alignment(t,texting.Alignment.BEGIN)
    return False
  elif looking_ahead.current_symbol_of(la) == ord('p'):
    looking_ahead.advance(la)
    if looking_ahead.current_symbol_of(la) == ord('>'):
      looking_ahead.advance(la)
      paragraph_alignment = texting.Alignment.BEGIN
      texting.set_alignment(t,paragraph_alignment)
    else:
      html_css_parsing.accept_separator(la)
      if looking_ahead.current_symbol_of(la) == ord('>'):
        looking_ahead.advance(la)
        paragraph_alignment = texting.Alignment.BEGIN
        texting.set_alignment(t,paragraph_alignment)
      else:
        class_attribute = _parse_class_attribute(la)
        html_css_parsing.accept_optional_spaces(la)
        html_css_parsing.accept(ord('>'),la)
        if unicoding3_0.equals(class_attribute,unicoding3_0.string_of("begin")):
          paragraph_alignment = texting.Alignment.BEGIN
        elif unicoding3_0.equals(class_attribute,unicoding3_0.string_of("middle")):
          paragraph_alignment = texting.Alignment.MIDDLE
        elif unicoding3_0.equals(class_attribute,unicoding3_0.string_of("end")):
          paragraph_alignment = texting.Alignment.END
        else:
          raise Exception("Unexpected paragraph class attribute: \"" + unicoding3_0.python_string_of(class_attribute))
        texting.set_alignment(t,paragraph_alignment)
  elif looking_ahead.current_symbol_of(la) == ord('/'):
    looking_ahead.advance(la)
    html_css_parsing.accept_name(unicoding3_0.string_of("body"),la)
    html_css_parsing.accept(ord('>'),la)
    return True
  else:
    raise Exception("Unexpected tag label start in MLE body: expected \'p\' or \'b\', found \'" + chr(looking_ahead.current_symbol_of(la)) + "\'")
  _emit_hard_line_break(t)
  texting.set_alignment(t,paragraph_alignment)
  html_css_parsing.accept_optional_spaces(la)
  tagname = _parse_paragraph_text(la,paragraph_alignment,t)
  if not unicoding3_0.equals(tagname,unicoding3_0.string_of("/p")):
    raise Exception("Unexpected tag at end of paragraph: expected </p>, found <" + unicoding3_0.python_string_of(tagname) + ">")
  else:
    _emit_hard_line_break(t)
    texting.set_alignment(t,paragraph_alignment)
  return False
  

def _parse_paragraph_text(la,pa,t):
  """ 
  pre:
    la = token lookahead to be parsed
    pa = alignment of this paragraph: BEGIN, MIDDLE or END
    t = text whose content is to be extended, with cursor at end
  
  post:
    either:
      paragraph text been parsed from la and appended as text to t
      the name of the current tag (following the text) has been returned
    or:
      a RuntimeException has been thrown

  syntax:
    ParagraphText  ::= (EscapedUnicodeCodePoint | BreakTag OptionalSpaces)*
                        (note: in the Emily internal text,
                         code points remain escaped,
                         words are separated by a single space, 
                         and each BreakTag is translated to a newline.)
                         
      BreakTag  ::=  StartTag(br)

  test:
    pa = "middle"
      </p>
      <br><bq>
      <br>a<bs>
      a<br>&lt;b</p>
      ab</p>
      a b</p>
      a  b</p>
      a \t b   cd   </p>
  """
  current_tag = unicoding3_0.new_string()
  is_start_of_line = True
  is_start_of_word = True
  end_of_paragraph_text = False

  while  not end_of_paragraph_text:
    cp = looking_ahead.current_symbol_of(la)
    if cp == ord('<'):
      current_tag = html_parsing.parse_tag(la)
      if unicoding3_0.equals(current_tag,unicoding3_0.string_of("br")):
        texting.set_alignment(t,pa)
        _emit_hard_line_break(t)
        texting.set_alignment(t,pa)
        html_css_parsing.accept_optional_spaces(la)
        is_start_of_line = True
        is_start_of_word = True

      # not a BreakTag, must be end of paragraph text
      else:
        end_of_paragraph_text = True

    # not a tag
    else:
      if code_point_testing.is_space_char(cp):
        html_css_parsing.accept_optional_spaces(la)
        is_start_of_word = True
        
      # not a space char
      else:
        if is_start_of_word:
          if  not is_start_of_line:
            texting.insert_code_point(t,ord(' '))
          is_start_of_line = False
          is_start_of_word = False
        texting.insert_code_point(t,cp)
        looking_ahead.advance(la)
    
  return current_tag

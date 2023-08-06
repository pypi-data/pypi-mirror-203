from enum import Enum
from . import string_parsing
from guibits1_0 import coloring
from guibits1_0 import dialoging
from guibits1_0 import font_styling
from . import html_parsing
from . import looking_ahead
from . import page_laying_out
from . import persisting
from guibits1_0 import printing
from . import rendering
from . import texting
from . import text_tokenizing
from guibits1_0 import type_checking2_0
from guibits1_0 import unicoding3_0
from guibits1_0 import windowing
from guibits1_0 import writing

# author R.N.Bosworth

# version 16 Mar 23  15:16

"""
Contractor to print texts.

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

def print_text(win,t,fn,fsize,fss):
  """ 
  pre:
    win = windowing.Window associated with text to be printed
    t = texting.Text to be printed
    fn = name of font for printing t, as str
    fsize = size of font for printing t, as float
    fss = styles of font for printing t, as font_styling.FontStyles
    
  post:
    either:
      t has been printed on a page of the current default printer,
    or:
      an exception dialog has been displayed to the user

  tests:
    empty text
    text of half a line
      END alignment
    text of two lines
      MIDDLE alignment
    text of two and a half lines
      BEGIN alignment
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_derivative(t,texting.Text)
  type_checking2_0.check_identical(fn,str)
  type_checking2_0.check_identical(fsize,float)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  my_globals = persisting.get_persistents()
  # set external page dimensions
  try:
    pj = printing.set_page_dimensions(persisting.get_paper_width(my_globals),persisting.get_paper_height(my_globals),persisting.get_horizontal_indent(my_globals))
    # note: this must be changed to allow different horizontal and vertical indents
    if pj == None:
      raise Exception("Problem trying to print page.  Page was not printed.")
    
    # set up internal page
    pg = rendering.new_page(win,persisting.get_paper_width(my_globals),persisting.get_paper_height(my_globals),persisting.get_horizontal_indent(my_globals),persisting.get_horizontal_indent(my_globals),fn,fss,fsize,coloring.BLACK)
    with t._my_lock:
      # find text cursor position
      loff = texting.cursor_line_offset(t)
      cpoff = texting.cursor_code_point_offset(t)
      # set text cursor to start of text
      texting.set_cursor_start(t)
      pg._current_line = unicoding3_0.string_of("")
      pg.line_width = 0.0
      pg._current_alignment = texting.get_alignment(t)
      # scan the text token by token, printing each line
      token = text_tokenizing.get_next_token(t)
      while  not unicoding3_0.equals(token,unicoding3_0.string_of("<end>")):
        _print_token(pj,token,texting.get_alignment(t),pg)
        token = text_tokenizing.get_next_token(t)
      _print_token(pj,token,texting.get_alignment(t),pg)
      # deal with <end> token
      # end the print job
      printing.end_printing(pj)
      # restore text cursor
      texting.set_cursor(t,loff,cpoff)
      
  except Exception as ex:
    # display exception message as dialog
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_globals),"Printing problem",str(ex))
      

# private procedures
# ------------------

def _de_escape(s1,s2):
  """ 
  pre:
    s1 = string which is to be appended to
    s2 = string of escaped unicode code points which is to be de-escaped and appended to s1
  post:
    s2 has been de-escaped and appended to s1
  test:
    s1 = ""
      s2 = ""
    s1 = "ab"
      s2 = "1&lt;2"
  """
  i = 0
  while i < unicoding3_0.length_of(s2):
    (code_point,i) = string_parsing.parse_html_character(s2,i)
    unicoding3_0.append(s1,code_point)


def _print_line(pj,pg):
  """ 
  pre:
    pj = current print job
    pg = page for this print
    pg._current_line = line to be printed
    pg._line_width = width of _current_line in points
    pg._text_width = width of text in points
    pg._current_alignment = alignment of line to be printed

  post:
    pg._current_line' has been printed
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = position for next line
    pg._current_line = empty string
    pg._line_width = 0.0

  test:
    line "fred"
      _current_alignment = BEGIN
      _current_alignment = END
      _current_alignment = MIDDLE
  """
  pg._page_position.x_offset = page_laying_out.x_offset_of_line(pg._line_width,pg._text_width,pg._current_alignment)
  _try_line(pj,pg)
  pg._page_position.x_offset = 0.0
  pg._page_position.y_offset += pg._font_size
  pg._current_line = unicoding3_0.new_string()
  pg._line_width = 0.0
  

def _print_token(pj,tk,a,pg):
  """ 
  pre:
    pj = current PrintJob
    tk = token to be printed
    a = alignment of text following tk
    pg = Page on which the token is to be printed,
         with _current_line, _line_width and _current_alignment set up
  post:
    if tk is an <end> token,
      the current line has been printed
    if tk is a Separator token,
      the width in points of the current line, plus the separator, 
          has been measured, and if overflow has occurred,
            the current line has been printed
            a new empty line has been started
    if tk is a Newline token,
      the current line has been printed
      the alignment has been set to a
    if tk is a Word token,
      the width in points of the current line, 
        plus the width in points of the word,
          has been measured, and if overflow has occurred,
            any trailing space has been removed from the current line
            the current line has been printed
            a new line has been started with the word
    y-offset in page has been updated

  test:
    pg._current_alignment = BEGIN
      "the cat sat on the mat."
        "\n"
          a = MIDDLE
            "\n"
              a = END
      "the cat sat on the    \nmat.<end>"
      "the<end>"
      "the<exit>"
  """
  try:
    # first code point of token gives sort
    # Tag
    if unicoding3_0.code_point_at(tk,0) == ord('<'):
      la = looking_ahead.lookahead_of_string(tk)
      label = html_parsing.parse_tag(la)
      if unicoding3_0.equals(label,unicoding3_0.string_of("end")):
        pg._page_position.x_offset = page_laying_out.x_offset_of_line(pg._line_width,pg._text_width,pg._current_alignment)
        _try_line(pj,pg)
      else:
        raise Exception("unexpected tag label when printing text:" + unicoding3_0.python_string_of(label))
        
    # Separator
    elif unicoding3_0.code_point_at(tk,0) == ord(' '):
      space_width = writing.width_in_points_of(pg._my_window," ",pg._font_name,pg._font_styles,pg._font_size)
      #space_width = font_measuring.glyph_width_of(pg._font_metrics,ord(' '))
      if pg._line_width + space_width > pg._text_width:
        _print_line(pj,pg)
        
      else:
        unicoding3_0.append(pg._current_line,ord(' '))
        pg._line_width += space_width
        
    # Newline
    elif unicoding3_0.code_point_at(tk,0) == ord('\n'):
      _print_line(pj,pg)
      pg._current_alignment = a
      
    # Word
    else:
      pg.word_width = page_laying_out.width_in_points_of_escaped(pg._my_window,tk,pg._font_name,pg._font_styles,pg._font_size)
      if pg._line_width + pg.word_width > pg._text_width:
        last_pos = unicoding3_0.length_of(pg._current_line) - 1
        if last_pos >= 0:
          if unicoding3_0.code_point_at(pg._current_line,last_pos) == ord(' '):
            space_width = writing.width_in_points_of(pg._my_window," ",pg._font_name,pg._font_styles,pg._font_size)
            unicoding3_0.remove(pg._current_line,last_pos)
            pg._line_width -= space_width
        _print_line(pj,pg)
        _de_escape(pg._current_line,tk)
        pg._line_width = pg.word_width
      else:
        _de_escape(pg._current_line,tk)
        pg._line_width += pg.word_width
        
  except Exception as ex:
    raise Exception("Unexpected exception when printing token:"+str(ex))


def _try_line(pj,pg):
  """ 
  pre:
    pj = current print job
    pg = page to be printed
  
  post:
    the current line has been printed on the page,
      if above the bottom of the text area

  test:
    line just fits on text area
    line just overlaps end of text area
  """
  if pg._page_position.y_offset + pg._font_size <= pg._text_height:
    printing.print_string(pj,unicoding3_0.python_string_of(pg._current_line),pg._font_name,pg._font_styles,pg._font_size,pg._page_position.x_offset,pg._page_position.y_offset)

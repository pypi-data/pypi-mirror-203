"""
Contractor which renders a text and a cursor on a page on a screen.
All dimensions on the screen are measured in points (1/72 inch a point).
"""

# author R.N.Bosworth

# version 14 Mar 23  15:13

from guibits1_0 import coloring, cursoring, font_styling
from . import html_parsing
from . import looking_ahead
import math
from . import page_laying_out
from guibits1_0 import painting
from . import string_parsing
from . import text_tokenizing
from . import texting
import time
from guibits1_0 import type_checking2_0
from guibits1_0 import unicoding3_0, windowing, writing

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

# exposed constants
# -----------------

TO_END = 999  # > end of text(?)

# exposed types
# -------------

"""
class TextAndScreenCursorPosition:
  """ """ cursor position in the text and on the page """ """
  pass
"""

class CursorPosition:
  """ cursor position in the text and on the page """
  pass
  

class Page:
  """  page which is to be rendered """
  pass
  
  
# exposed procedures
# ------------------

def collapse_to_end(curpos):
  """
  pre:
    curpos = current CursorPosition for start and end of cursor
    
  post:
    cursor is thin and at end position
  
  test:
    curpos = None
    curpos = fat cursor
    curpos = thin cursor
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  curpos._start_text_position.line_offset = curpos._end_text_position.line_offset
  curpos._start_text_position.code_point_offset = \
    curpos._end_text_position.code_point_offset
  curpos._start_page_position.x_offset = curpos._end_page_position.x_offset
  curpos._start_page_position.y_offset = curpos._end_page_position.y_offset


def collapse_to_start(curpos):
  """
  pre:
    curpos = current CursorPosition for start and end of cursor
    
  post:
    cursor is thin and at start position
  
  test:
    curpos = None
    curpos = fat cursor
    curpos = thin cursor
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  curpos._end_text_position.line_offset = curpos._start_text_position.line_offset
  curpos._end_text_position.code_point_offset = \
    curpos._start_text_position.code_point_offset
  curpos._end_page_position.x_offset = curpos._start_page_position.x_offset
  curpos._end_page_position.y_offset = curpos._start_page_position.y_offset


def is_thin(curpos):
  """
  pre:
    curpos = current CursorPosition for start and start of cursor
    
  post:
    return True iff cursor is thin
    
  test:
     curpos = None
     curpos = ((123,234),(124,235)
     curpos = ((123,234),(124,234)
     curpos = ((123,234),(123,235)
     curpos = ((123,234),(123,234)
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  return (curpos._start_text_position.line_offset == \
          curpos._end_text_position.line_offset and \
          curpos._start_text_position.code_point_offset == \
          curpos._end_text_position.code_point_offset)
  

def move_cursor_down(curpos,pg):
  """ 
  pre:
    curpos = current CursorPosition for start and end of cursor
    pg = Page for this cursor
    
  post:
    if possible,
      cursor has been collapsed to its end position, if necessary
      cursor's page position has been moved downwards by one line,
        preserving the desired x-offset to ensure a linear path, as far as possible
      cursor's text position has been set to the equivalent of the page position
      true has been returned
    else
      false has been returned
  """
  """ 
  pre:
    curpos._end_page_position.y_offset = current y-offset of end of cursor in page
    curpos._desired_x_offset = desired x-offset of cursor in page, to give linear path
    pg._EOT_position.y_offset = y-offset of last line of page
    pg._line_list = list of x-offsets and lines for this page
    pg._back_map = map from each glyph-interstice of the page 
                     to the equivalent text position

  post:
    either:
      curpos._start_page_position.y_offset = new y-offset of cursor in page
      curpos._start_page_position.x_offset = desired x-offset of cursor in page
      curpos._desired_x_offset = desired x-offset of cursor in page, to give linear path
      curpos._update_x_offset = false, so _desired_x_offset is used by render_text
      curpos._start_text_position.line_offset = equivalent line offset of page position
      curpos._start_text_position.code_point_offset = 
        equivalent code point offset of page position
      curpos._end_page_position.y_offset = new y-offset of cursor in page
      curpos._end_page_position.x_offset = desired x-offset of cursor in page
      curpos._end_text_position.line_offset = equivalent line offset of page position
      curpos._end_text_position.code_point_offset = 
        equivalent code point offset of page position
      true has been returned
    or:
      false has been returned
  """
  """ 
  test:
    curpos = None
    curpos valid
      pg = None
      pg valid
        font name = Courier New
          font size = 12
            horizontal indent = 72 (1")
              vertical indent = 72 (1")
                page width = 288 (4") (text width = 144 i.e. 2" i.e. 20 glyphs)
                  pg._line_list =
                    "In Xanadu did Kubla"
                    "Khan"
                    "A stately pleasure"
                    "dome decree"
                  pg._back_map = map back to text:
                    "In Xanadu did Kubla Khan"
                    "A stately pleasure dome decree"
                  pg._page_position.y_offset = 36.0 (fourth line)
                    page height = 180 (2.5") (visible text height = 36 i.e. 0.5" i.e. 3 lines)
                      curpos._page position.y_offset = 24.0 (third line)
                    page height = 192 (2.67") (visible text height = 48 i.e. 0.67" i.e. 4 lines)
                      curpos._page position.y_offset = 36.0 (fourth line)
                      curpos._page position.y_offset = 24.0 (third line)
                        curpos._desired_x_offset = 129.6 (end of third line)
                        curpos._desired_x_offset = 28.8 (glyph interstice 4 on third line)
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(pg,Page)
  if curpos._end_page_position.y_offset > (pg._text_height - 2.0*pg._font_size):
    #new position off visible text of page
    return False
  elif _equals_float(curpos._end_page_position.y_offset,pg._EOT_position.y_offset):
    # last non-blank line of page
    return False
  else:
    curpos._end_page_position.y_offset += pg._font_size
    if curpos._update_x_offset:
      curpos._desired_x_offset = curpos._end_page_position.x_offset
    else:
      curpos._end_page_position.x_offset = curpos._desired_x_offset
    curpos._update_x_offset = False  # i.e. keep using _desired_x_offset
    (plo,gio,xoff,yoff) = nearest_glyph_interstice_of(curpos._end_page_position.x_offset,curpos._end_page_position.y_offset,pg)
    (tlo,cpo) = pg._back_map[plo][gio]
    # set up text and page position for thin cursor
    set_thin_cursor_text_and_page(curpos,tlo,cpo,xoff,yoff)
    render_thin_cursor(curpos,pg)
    return True
     

def move_cursor_up(curpos,pg):
  """ 
  pre:
    curpos = current CursorPosition for start and end of cursor
    pg = Page for this cursor
    
  post:
    if possible,
      cursor has been collapsed to its start position, if necessary
      cursor's page position has been moved upwards by one line,
        preserving the desired x-offset to ensure a linear path, as far as possible
      cursor's text position has been set to the equivalent of the page position
      true has been returned
    else
      false has been returned
  """
  """  
  pre:
    curpos._start_page_position.y_offset = current y-offset of cursor in page
    curpos._desired_x_offset = desired x-offset of cursor in page, to give linear path
    pg._page_position.y_offset = y-offset of last line of page
    pg._line_list = list of x-offsets and lines for this page
    pg._back_map = map from each glyph-interstice of the page to the equivalent 
                     text position

  post:
    either:
      curpos._start_page_position.y_offset = new y-offset of cursor in page
      curpos._start_page_position.x_offset = desired x-offset of cursor in page
      curpos._desired_x_offset = desired x-offset of cursor in page, to give linear path
      curpos._update_x_offset = false, so _desired_x_offset is used by render_text
      curpos._start_text_position.line_offset = equivalent line offset of page position
      curpos._start_text_position.code_point_offset = equivalent code point offset of page 
                                                 position
      curpos._end_page_position.y_offset = new y-offset of cursor in page
      curpos._end_page_position.x_offset = desired x-offset of cursor in page
      curpos._desired_x_offset = desired x-offset of cursor in page, to give linear path
      curpos._update_x_offset = false, so _desired_x_offset is used by render_text
      curpos._end_text_position.line_offset = equivalent line offset of page position
      curpos._end_text_position.code_point_offset = equivalent code point offset of page 
                                                 position
      true has been returned
    or:
      false has been returned
  """
  """
  test:
    curpos = None
    curpos valid
      curpos = None
      curpos valid
        pg = None
        pg valid
          font name = Courier New
            font size = 12
              horizontal indent = 72 (1")
                vertical indent = 72 (1")
                  page width = 288 (4") (text width = 144 i.e. 2" i.e. 20 glyphs)
                    pg._line_list =
                      "In Xanadu did Kubla"
                      "Khan"
                      "A stately pleasure"
                      "dome decree"
                    pg._back_map = map back to text:
                      "In Xanadu did Kubla Khan"
                      "A stately pleasure dome decree"
                      page height = 192 (2.67") (visible text height = 48 i.e. 0.67" i.e. 4 lines)
                        tascp._page position.y_offset = 11.9 (just above second line)
                        tascp._page position.y_offset = 12.0 (second line)
                          tascp._desired_x_offset = 28.8 (glyph interstice 4 on second line)
                          tascp._desired_x_offset = 36.0 (beyond end of second line)
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(pg,Page)
  if curpos._start_page_position.y_offset >= pg._font_size:
    curpos._start_page_position.y_offset -= pg._font_size
    if curpos._update_x_offset:
      curpos._desired_x_offset = curpos._start_page_position.x_offset
    else:
      curpos._start_page_position.x_offset = curpos._desired_x_offset
    curpos._update_x_offset = False  # i.e. keep using _desired_x_offset
    (plo,gio,xoff,yoff) = nearest_glyph_interstice_of(curpos._start_page_position.x_offset,curpos._start_page_position.y_offset,pg)
    (tlo,cpo) = pg._back_map[plo][gio]
    # set up text and page position for thin cursor
    set_thin_cursor_text_and_page(curpos,tlo,cpo,xoff,yoff)
    render_thin_cursor(curpos,pg)
    return True
  else:
    return False
    
  
def nearest_glyph_interstice_of(x,y,pg):
  """
  pre:
    (x,y) = desired (x,y) position of the cursor on the Page, in points
              from the tlh corner of the text
    pg = Page on which the nearest glyph interstice is to be found
    
  post:
    the nearest glyph interstice has been returned, as quadruple 
      (page line offset as int, glyph interstice offset in line as int,
       x-offset in text as float, y-offset in text as float)
      
  note: this procedure takes time O(n log n) where n is the number of
          glyphs in the line of the cursor
      
  test:
    pg._font_name = "Courier New"
      pg._font_styles = {}
        pg._font size = 12
          pg._line_list = [(0.0,"")]
            y = 24.0 (line offset 2)
            y = 12.0 (line offset 1)
            y = 0.0 (line offset 0)
            y = -12.0 (line offset -1)
          pg._line_list = [(0.0,""),(72.0,"frodo")]
            y == 6.0 (halfway down first line
              x = 0.0 (at end of text)
              x = 10.0 (well past end of text)
            y == 18.0 (halfway down 2nd line)
              x = 0.0 (well before text)
              x = 71.9 (just before text)
              x = 72.0 (just at start of text)
              x = 72.1 (just after start of text)
              x = 120.0 (well after text)
              x = 108.1 (just after text)
              x = 108.0 (just at end of text)
              x = 107.9 (just before end of text)
              x = 90.0 (at middle of text)
  """
  page_line_offset = math.floor(y/pg._font_size)
  if page_line_offset < 0:
    page_line_offset = 0
  if page_line_offset >= len(pg._line_list):
    page_line_offset = len(pg._line_list) - 1
  (line_start_offset,line) = pg._line_list[page_line_offset]
  x_in_line = x - line_start_offset
  
  # lo and hi are the bounds of the line, relative to the start of the line
  lo = 0
  lo_off = 0.0
  hi = len(line)
  hi_off = writing.width_in_points_of(pg._my_window,line,pg._font_name,pg._font_styles,pg._font_size)
  # limit cursor glyph interstice to line
  if x_in_line <= lo_off:
    page_glyph_offset = lo
    x_offset_in_line = lo_off
  elif x_in_line >= hi_off:
    page_glyph_offset = hi
    x_offset_in_line = hi_off
  else:
    while hi > lo+1:  # must terminate as hi-lo halves each time
      mid = (lo+hi)//2  # floor division
      mid_off = writing.width_in_points_of(pg._my_window,line[:mid],pg._font_name,pg._font_styles,pg._font_size)
      if x_in_line >= mid_off:
        lo = mid
        lo_off = mid_off
      else:
        hi = mid
        hi_off = mid_off
    # hi == lo+1, lo_off <= x_in_line < hi_off
    lo_distance = x_in_line - lo_off
    hi_distance = hi_off - x_in_line
    if lo_distance <= hi_distance:
      page_glyph_offset = lo
      x_offset_in_line = lo_off
    else:
      page_glyph_offset = hi
      x_offset_in_line = hi_off
  return (page_line_offset, \
          page_glyph_offset, \
          line_start_offset+x_offset_in_line, \
          page_line_offset*pg._font_size)
  
  
def new_cursor_position():
  """ 
  pre:
    true
    
  post:
    new CursorPosition with undefined position has been returned

  test:
    once thru
  """
  curpos = CursorPosition()
  curpos._start_text_position = _new_text_position()
  curpos._end_text_position = _new_text_position()
  curpos._start_page_position = _new_page_position()
  curpos._end_page_position = _new_page_position()
  curpos._desired_x_offset =  -1.0
  curpos._update_x_offset = True
  curpos._start_x_offset = -1.0
  curpos._end_x_offset = -1.0
  curpos._in_fat_cursor = False
  curpos._cursor_rectangle_pending = False
  return curpos
  

def new_page(win,w,h,hi,vi,fn,fss,fsize,c):
  """ 
  pre:
    win = windowing.Window with which this page is associated
    w = width of this page in points, as float
    h = height of this page in points, as float
    hi = horizontal indent of this page in points, as float
    vi = vertical indent of this page in points, as float
    fn = font name for this page, as str
    fss = font styles for this page, as font_styling.FontStyleSet
    fsize = font size for this page, as float
    c = font color for this page
    
  post:
    a new page with the specified dimensions and properties has been returned

  test:
    once thru
  """
  """
  post:
    EOT position has been set to (0,0)
    new empty line_list and back_map have been set up
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_identical(w,float)
  type_checking2_0.check_identical(h,float)
  type_checking2_0.check_identical(hi,float)
  type_checking2_0.check_identical(vi,float)
  type_checking2_0.check_derivative(fn,str)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  type_checking2_0.check_derivative(c,coloring.Color)
  pg = Page()
  pg._my_window = win
  pg._width = w
  pg._height = h
  pg._horizontal_indent = hi
  pg._vertical_indent = vi
  pg._text_width = pg._width - 2.0*pg._horizontal_indent
  pg._text_height = pg._height - 2.0*pg._vertical_indent
  pg._current_line = unicoding3_0.new_string()
  pg._line_width = 0.0
  pg._current_alignment = texting.Alignment.BEGIN
  pg._font_name = fn
  pg._font_styles = fss
  pg._font_size = fsize
  pg._text_color = c
  pg._text_position = _new_text_position()
  pg._text_position.line_offset = 0
  pg._text_position.code_point_offset = 0
  pg._page_position = _new_page_position()
  pg._page_position.x_offset = 0.0  
  # x-offset in points of start of current line on page, or 0.0
  pg._page_position.y_offset = 0.0  
  # y-offset in points of start of current line on page
  pg._EOT_position = _new_page_position()
  pg._EOT_position.x_offset = 0.0
  pg._EOT_position.y_offset = 0.0
  # EOT position of empty text
  pg._line_list = [(0.0,"")]  # list of lines on page, as (x-offset as float, line as str)
  pg._back_map = [[(0,0)]]  # map from (page_line,glyph_offset) to (text_line, code_point_offset)
  return pg
  

def render_lines(t,curpos,pg,plo1,plo2):
  """
  pre:
    t = text which is being rendered
    curpos = cursor position in the text
    curpos start position in text <= curpos end position in text
    pg = Page to which text is to be rendered
    pg's back map must be set up for plo1
    plo1 = start page line offset for the render
    plo2 = end page line offset for the render
    if plo2 > last line offset of pg, pg will be rendered to end
    0 <= plo1 <= last line of text on page
    plo2 > 0
    plo2 > plo1
    
  post:
    the portion of text corresponding to the section of the page 
      between plo1 and the line before plo2
        has been rendered to pg
    curpos = cursor position in Text and Page
    any thin cursor has been rendered
    any fat cursor in the range plo1 <= cursor position < plo2 has been rendered

  pre:
    curpos._update_x_offset = True, iff _desired_x_offset is to be updated to the page x-offset

  post:
    curpos._update_x_offset = True
    curpos._desired_x_offset is undefined (-1.0)
    pg._page_position.x_offset = x-offset in points of start of plo2
    pg._page_position.y_offset = y-offset in points of start of plo2
    pg._line_list = list of (x-offset in points, line) for each line of page
    pg._back_map = list of lists of (text line offset, text code point offset)
                     for each glyph interstice in the page

  test:
    t = None
    t = ""
      curpos = None
      curpos = ((0,1),(0,0))
      curpos = ((0,0),(0,0))
        pg = None
        pg = valid page
          plo1 = None
          plo1 = -1
            plo2 = None
            plo2 = 0
          plo1 = 0
            plo2 = 0
          plo1 = 1
            plo2 = 0
            plo2 = 1 (should give plo1 out-of-range)
    t = text of three lines (one right-justified)
      plo1 = 1
        plo2 = 2
      plo1 = 0
        plo2 = TO_END
          cursor position in text is (0,0)
          cursor position in text is (0,0),(0,1) (fat(ish) cursor)
          cursor position in text is (0,4)
            curpos._update_x_offset = true
              curpos._update_x_offset = false
          cursor position in text is (0,5)
            curpos._update_x_offset = false
              curpos._update_x_offset = true
          cursor position in text is (0,8)
            curpos._update_x_offset = true
              curpos._update_x_offset = true
  """
  start_time = time.time()
  type_checking2_0.check_derivative(t,texting.Text)
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(pg,Page)
  type_checking2_0.check_identical(plo1,int)
  type_checking2_0.check_identical(plo2,int)
  if _less_than_text_position(curpos._end_text_position,curpos._start_text_position):
    raise Exception("Attempt to render lines with curpos._end_text_position < curpos._start_page_position")
  if plo1 < 0:
    raise Exception("Attempt to render lines with plo1 < 0")
  if plo2 <= 0:
    raise Exception("Attempt to render lines with plo2 <= 0")
  if plo2 <= plo1:
    raise Exception("Attempt to render lines with plo2 <= plo1")
  win = pg._my_window
  
  # wipe any thin cursor
  cursoring.wipe_cursor(win)
  
  # find start and end positions in text and page
  try:
    (stlo,stcpo) = text_position_of(plo1,0,pg)
  except IndexError:
    raise Exception("Attempt to render lines with plo1 > end of text on page")
  try:
    (etlo,etcpo) = text_position_of(plo2,0,pg)
  except IndexError:
    (etlo,etcpo) = (math.inf,math.inf)
  # set up pg to start of plo1
  pg._text_position.line_offset = stlo
  pg._text_position.code_point_offset = stcpo
  pg._page_position.x_offset = 0.0
  pg._page_position.y_offset = plo1 * pg._font_size
  pg._current_line = unicoding3_0.new_string()
  pg._line_width = 0.0
  
  # set up text cursor to equivalent position in text
  texting.set_cursor(t,stlo,stcpo)
  
  # check cursor
  _fix_cursor_position(curpos,pg)

  # set up initial alignment
  pg._current_alignment = texting.get_alignment(t)
  
  # read tokens until (etlo,etcpo) or <end> is reached
  eot = False
  while (texting.cursor_line_offset(t) != etlo \
    or texting.cursor_code_point_offset(t) != etcpo) \
    and not eot:
    tk = text_tokenizing.get_next_token(t)
    if unicoding3_0.equals(tk,unicoding3_0.string_of("<end>")):
      eot = True
    _render_token(tk,texting.get_alignment(t),curpos,pg)    
  curpos._update_x_offset = True
  render_thin_cursor(curpos,pg)
  end_time = time.time()
  #print("rl="+str(end_time - start_time))


def render_thin_cursor(curpos,pg):
  """ 
  pre:
    curpos = OnScreenCursorPositions of start and end of cursor respectively 
              in text and on page
    start text position <= end text position
    pg = Page on which cursor is to be rendered
  
  post:
    if the cursor is thin,
      if the cursor is totally in the text area of pg
        cursor has been (set up to be eventually) rendered on pg
      else
        an exception has been raised

  test:
    fat cursor
    thin cursor at page position (-1.0,-1.0)
    thin cursor at page position (0.0,0.0)
    thin cursor at page position (36.0,72.0)
      cursor just fits on text area
      cursor just overlaps end of text area
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(pg,Page)
  if _less_than_text_position(curpos._end_text_position,curpos._start_text_position):
    raise Exception("Attempt to render cursor with start position > end position")
  if _equals_text_position(curpos._start_text_position,curpos._end_text_position):
    if curpos._start_page_position.y_offset < 0.0 or \
       curpos._start_page_position.y_offset + pg._font_size > pg._text_height:
         raise Exception("Attempt to render cursor at ("+ \
           str(curpos._start_page_position.x_offset)+","+ \
           str(curpos._start_page_position.y_offset)+ \
           ") which is out of range of text")
    else:
      cursoring.draw_cursor( \
        pg._my_window, \
        pg._font_size, \
        pg._horizontal_indent + curpos._start_page_position.x_offset, \
        pg._vertical_indent + curpos._start_page_position.y_offset, \
        coloring.BLACK)


def set_cursor_position_to_start(curpos):
  """ 
  pre:
    curpos = cursor position which is to be set to start of text
  
  post:
    curpos has been set to the start of the text, 
      and the start of the text on the page

  test:
    once thru with current text position set to (1,2)
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  curpos._start_text_position.line_offset = 0
  curpos._start_text_position.code_point_offset = 0
  curpos._end_text_position.line_offset = 0
  curpos._end_text_position.code_point_offset = 0
  curpos._start_page_position.x_offset = 0.0
  curpos._start_page_position.y_offset = 0.0
  curpos._end_page_position.x_offset = 0.0
  curpos._end_page_position.y_offset = 0.0
  curpos._desired_x_offset =  - 1.0
  curpos._update_x_offset = True
  

def set_text_font_name(pg,fn):
  """ 
  pre:
    pg = Page whose font name is to be changed
    fn = font name in which pg's text is to be rendered from now on, as str
  
  post:
    pg's associated font name has been changed to fn

  test:
    once thru with new font name
  """
  type_checking2_0.check_derivative(pg,Page)
  type_checking2_0.check_derivative(fn,str)
  pg._font_name = fn
  

def set_text_font_size(pg,d):
  """ 
  pre:
    pg = Page whose font size is to be changed
    d = font size in which pg's text is to be rendered from now on
  
  post:
    pg's associated font size has been changed to d

  test:
    once thru with new font size
  """
  type_checking2_0.check_derivative(pg,Page)
  type_checking2_0.check_identical(d,float)
  pg._font_size = d
  

def set_thin_cursor_text_and_page(curpos,lo,cpo,xoff,yoff):
  """
  pre:
    curpos = present position of cursor
    lo = line offset of thin cursor in texting.Text
    cpo = code point offset of thin cursor in texting.Text
    xoff = x-offset of thin cursor on Page, relative to tlh corner of text on page
    yoff = y-offset of thin cursor on Page, relative to tlh corner of text on page
    
  post:
    curpos has been updated with the text and page positions
      of the thin cursor
  
  test:
    once thru
  """
  curpos._start_text_position.line_offset = lo
  curpos._start_text_position.code_point_offset = cpo
  curpos._end_text_position.line_offset = lo
  curpos._end_text_position.code_point_offset = cpo
  curpos._start_page_position.x_offset = xoff
  curpos._start_page_position.y_offset = yoff
  curpos._end_page_position.x_offset = xoff
  curpos._end_page_position.y_offset = yoff


def set_on_screen_to_text(t,curpos):
  """ 
  pre:
    t = text with internal cursor
    curpos = cursor position which is to be set to t's internal cursor
  
  post:
    curpos's text position has been set to t's internal cursor

  test:
    once thru
  """
  type_checking2_0.check_derivative(t,texting.Text)
  type_checking2_0.check_derivative(curpos,CursorPosition)
  curpos._start_text_position.line_offset = texting.cursor_line_offset(t)
  curpos._start_text_position.code_point_offset = texting.cursor_code_point_offset(t)
  curpos._end_text_position.line_offset = texting.cursor_line_offset(t)
  curpos._end_text_position.code_point_offset = texting.cursor_code_point_offset(t)
  

def set_text_to_on_screen_start(curpos,t):
  """ 
  pre:
    curpos = cursor position in text
    t = text whose internal cursor is to be set to 
          curpos's start position in the text
  
  post:
    t's internal cursor has been set to 
      curpos's start position in the text

  test:
    once thru
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(t,texting.Text)
  texting.set_cursor(t,curpos._start_text_position.line_offset, \
                       curpos._start_text_position.code_point_offset)


def set_text_to_on_screen_end(curpos,t):
  """ 
  pre:
    curpos = cursor position in text
    t = text whose internal cursor is to be set to 
          curpos's end position in the text
  
  post:
    t's internal cursor has been set to 
      curpos's end position in the text

  test:
    once thru
  """
  type_checking2_0.check_derivative(curpos,CursorPosition)
  type_checking2_0.check_derivative(t,texting.Text)
  texting.set_cursor(t,curpos._end_text_position.line_offset, \
                       curpos._end_text_position.code_point_offset)


def start_page_line_of(curpos,pg):
  """
  pre:
    curpos = CursorPosition in page
    pg = Page in which cursor is positioned
 
  post:
    returns the start page line for a render_lines scan, 
      when the cursor has been moved forwards in the text
  
  test:
    once thru  
  """
  splo = int(curpos._start_page_position.y_offset/pg._font_size)
  return splo
  

def start_page_line_of_back(curpos,pg):
  """
  pre:
    curpos = CursorPosition in page
    pg = Page in which cursor is positioned
 
  post:
    returns the start page line for a render_lines scan, 
      when the cursor has been moved backwards in the text
  
  test:
    curpos at page line 2
    curpos at page line 1
    curpos at page line 0
  """
  splo = int(curpos._start_page_position.y_offset/pg._font_size)
  if splo > 0:
    splo -= 1
  return splo
  

def text_position_of(lo,go,pg):
  """
  pre:
    lo = line offset of cursor page position
    lo >= 0
    go = glyph offset of cursor page position
    go >= 0
    pg = Page in which cursor is positioned
    pg._back_map = map from page position to the equivalent text position
    
  post:
    returns text position equivalent to cursor page position, as an int pair
  
  test:
    lo non-integer
    lo = -1
    lo = 0
      go non-integer
      go = -1
      go = 0
        pg not a Page
        pg is a Page
    lo = 1
      go = 1
        page position exists
  """
  type_checking2_0.check_identical(lo,int)
  type_checking2_0.check_identical(go,int)
  type_checking2_0.check_derivative(pg,Page)
  if lo < 0:
    raise Exception("Attempt to find text position of negative page line offset")  
  if go < 0:
    raise Exception("Attempt to find text position of negative page glyph offset")
  (tlo,cpo) = pg._back_map[lo][go]
  return (tlo,cpo)
  

# private constants
# -----------------

_LIGHT_BLUE = coloring.new_color(0.9,0.9,1.0)
  

# -------------
# private types
# -------------

""" 
Note: all measurements on the page are done relative to the tlh corner of the text

Invariants:
  1. Negative values for _text_position or _page_position indicate an undefined position.
  2. Either the _text_position or the _page_position must be defined.
  3. If both positions are defined, the text position takes precedence.
"""
  
class _PagePosition:
  """  position in the page as (x-offset:float, y_offset:float)"""
  pass
  

class _TextPosition:
  """ position in the text as (line offset:int, code point offset:int)"""
  pass
  

# private procedures
# ------------------

def _de_escape(s,curpos,pg):
  """ 
  pre:
    s = unicoding3_0.String of escaped unicode code points which is to be 
          de-escaped and appended to pg._current_line
    curpos._start_text_position = curpos's start text position
    curpos._start_page_position = curpos's start page position
    curpos._end_text_position = curpos's end text position
    curpos._end_page_position = curpos's end page position
    curpos._desired_x_offset = desired x-offset of curpos, or -1.0 if undefined
    pg = page which is being rendered to
    pg._font_name = font name for this render, as a str
    pg._font_styles = font_styling.FontStyles for this render
    pg._font_size = font size for this render, as a float
    pg._text_position = current render position in text, as (line_offset, code_point_offset)
    pg._page_position.x_offset = x-offset of start of current line in page, 
                                   or 0.0
    pg._page_position.y_offset = y-offset of start of current line in page
    pg._current_line = unicoding3_0.String which is to be appended to
    pg._my_window = windowing.Window for this render
    pg._back_map = map from (page_line,glyph_offset) to 
      (text_line,code_point_offset) for the text rendered so far
  
  post:
    s has been de-escaped and appended to pg._current_line
    for each de-escaped code point (glyph) of s:
      an entry has been added to the pg._back_map,
        giving the text position for the current glyph interstice
      the cursor start and end points have been updated as necessary

  test:
    font = "Courier New"
      font size = 12
        pg._text_position = (0,0)
          pg._page_position = (0.0,0.0)
            pg._current_line = ""
              pg._back_map = [[(0,0)]]
                s = ""
                  curpos and curpos at (0,0) (0.0,0.0)  
                    (check cursor positions, check _back_map)
        pg._text_position = (1,2)
          pg._page_position = (14.0,12.0)
            pg._current_line = "ab"
              pg._back_map = [[(0,0)],[(0,0)]]
                s = "1&lt;2"
                  curpos at (1,3) (-1.0,-1.0)
                    curpos at (1,7) (-1.0,-1.0)
                      (check cursor page positions, check _back_map)
  """
  i = 0
  while i < unicoding3_0.length_of(s):
    old_offset = i
    (code_point,i) = string_parsing.parse_html_character(s,i)
    width_in_code_points = i - old_offset
    pg._text_position.code_point_offset += width_in_code_points
    _render_glyph(code_point,curpos,pg)
    # update _back_map with current text position
    _update_back_map(pg)


def _ensure_sublist_exists(l,i):
  """
  pre:
    l = list which is to be modified, if necessary
    i = offset in l of sub-list
    
  post:
    l has been updated with an empty sub-list, if necessary,
      otherwise l is left unchanged
     
  test:
  
    
  """
  if i < len(l):
    pass
  elif i == len(l):
    l.append([])
  else:
    raise Exception("Attempt to create sublist in l with out-of-range index. i="+str(i)+", len(l)="+str(len(l)))
  
    
def _equals_float(d1,d2):
  """ 
  pre:
    d1 = first floating-point number
    d2 = second floating-point number
    
  post:
    returns true iff the two floating-point numbers are within 0.01 of each other

  test:
    d1 = 123.4
      d2 = 123.3    
      d2 = 123.401    
      d2 = 123.5    
  """
  return abs(d1 - d2) < 0.01
  

def _equals_text_position(tp1,tp2):
  """ 
  pre:
    tp1 = first position in text
    tp2 = second position in text
  
  post:
    returns true iff the two positions in the text are equal

  test:
    tp1 = (1,2)
      tp2 = (0,2)
      tp2 = (2,2)
      tp2 = (1,1)
      tp2 = (1,3)
      tp2 = (1,2)     
  """
  return (tp1.line_offset == tp2.line_offset) and (tp1.code_point_offset == tp2.code_point_offset)
  

"""
def _find_text_and_page_offset(curpos,lm,lso):
  """ """ 
  pre:
    curpos._desired_x_offset = desired x-offset of cursor on page
    curpos._page_position.y_offset = y-offset of cursor on page
    curpos._text_position.line_offset = offset of line being rendered
    lm = map of glyph-offsets to text code point offsets and relative page x-offsets
          for the current line on the page
    lso = start-offset of current line on the page
  
  post:
    curpos._text_position = position of cursor in internal text
    curpos._page_position = position of cursor on page

  test:
    lso = 20.0
      curpos._text_position.line_offset = -1;
      curpos._current_text_position.line_offset = 0;
        map with single entry (0 -> (0,0.0))
          curpos._desired_x_offset = 19.9
          curpos._desired_x_offset = 20.1
        map with entries (0 -> (0,0.0)), (1 -> (12,34.0)),(2 -> (13,35.0)), (3 -> (14,36.0))
          curpos._desired_x_offset = 19.9
          curpos._desired_x_offset = 54.5
          curpos._desired_x_offset = 54.6
          curpos._desired_x_offset = 56.1      
  """ """
  # relativize the desired position to the current start offset
  rdxo = curpos._desired_x_offset - lso
  # find the nearest page x-offset
  minimum_page_distance = float("infinity")
  i = 0
  while i < len(lm.map):
    ptp = lm.map.get(i)
    difference = abs(rdxo - ptp.page_relative_x_offset)
    if difference < minimum_page_distance:
      # we have a minimum (so far)
      minimum_page_distance = difference
      curpos._page_position.x_offset = ptp.page_relative_x_offset
      curpos._text_position.code_point_offset = ptp.text_code_point_offset    
    i += 1
  # set the line offset
  curpos._text_position.line_offset = curpos._current_text_position.line_offset
  # derelativize the x-offset
  curpos._page_position.x_offset += lso
"""
  
def _fix_cursor_position(curpos,pg):
  """ 
  pre:
    curpos.start_text_position is the start text position of the cursor,
      or (-1,-1) if undef
    curpos.end_text_position is the end text position of the cursor,
      or (-1,-1) if undef
    pg._text_position is the current text position of the render
    pg._page_position.y_offset =  y-offset of the current line on the page,
                                    in points as float
    pg._current_line = current line of render, as a unicoding3_0.String
    pg._font_name = font name for this render, as a str
    pg._font_styles = font_styling.FontStyles for this render
    pg._font_size = font size for this render, as a float
    pg._my_window = windowing.Window for this render
    
  post:
    if curpos's start text position is defined,
      if curpos's start text position corresponds to the current text position
        curpos._start_page_position.x_offset = start x-offset relative to start of line
        curpos._start_page_position.y_offset = start y-offset relative to start of page
        if the cursor is thin,
          curpos._end_page_position.x_offset = end x-offset relative to start of line
          curpos._end_page_position.y_offset = end y-offset relative to start of page
        else (cursor is fat),
          curpos._start_x_offset = start x-offset of cursor rectangle,
                                 relative to start of line
          curpos._in_fat_cursor = True
    if curpos's end text position is defined,
      if curpos's end text position corresponds to the current text position
        curpos._end_page_position.x_offset = x-offset relative to start of line
        curpos._end_page_position.y_offset = y-offset relative to start of page
        if cursor is fat,
          curpos._start_x_offset = start x-offset of cursor rectangle,
                                 relative to start of line
          curpos._end_x_offset = end x-offset of cursor rectangle,
                               relative to start of line
          curpos._in_fat_cursor = False
          curpos._cursor_rectangle_pending = True

  test:
    curpos._start_text_position = (-1,-1)
    curpos._start_text position = (0,1)
        pg._current_line = unicoding3_0.string_of("f")
          pg._font_name = "Courier New"
            pg._font_styles = {}
              pg._font_size = 12.0
                pg._text_position = (0,2)
                pg._text_position = (0,1)
                  pg._page_position.x_offset = 7.2
                    pg._page_position.y_offset = 0.0
                      curpos._end_text_position = (0,1)
                      curpos._end_text_position = (0,2)
                pg._text_position = (0,2)
                  pg._page_position.x_offset = 14.4
                    pg._page_position.y_offset = 0.0
                      curpos._end_text_position = (0,2)
    curpos._end_text_position = (-1,-1)
    curpos._end_text position = (0,3)
      pg._font_name = "Courier New"
        pg._font_styles = {}
          pg._font_size = 12.0
            pg._text_position = (0,2)
              pg._current_line = unicoding3_0.string_of("ff")
            pg._text_position = (0,3)
              pg._current_line = unicoding3_0.string_of("fff")
                pg._page_position.x_offset = 21.6
                  pg._page_position.y_offset = 0.0
  """
  if curpos._start_text_position.line_offset >= 0:
    if _equals_text_position(curpos._start_text_position,pg._text_position):
      line_as_str = unicoding3_0.python_string_of(pg._current_line)
      line_width_in_points = writing.width_in_points_of(pg._my_window,line_as_str,pg._font_name,pg._font_styles,pg._font_size)
      curpos._start_page_position.x_offset = line_width_in_points
      curpos._start_page_position.y_offset = pg._page_position.y_offset
      if _equals_text_position(curpos._start_text_position,curpos._end_text_position):
        # thin cursor
        curpos._end_page_position.x_offset = line_width_in_points
        curpos._end_page_position.y_offset = pg._page_position.y_offset
        curpos._in_fat_cursor = False
        curpos._cursor_rectangle_pending = False
      else:  # fat cursor
        curpos._start_x_offset = line_width_in_points
        curpos._in_fat_cursor = True
        curpos._cursor_rectangle_pending = False
  if curpos._end_text_position.line_offset >= 0:
    if _equals_text_position(curpos._end_text_position,pg._text_position):
      line_as_str = unicoding3_0.python_string_of(pg._current_line)
      line_width_in_points = writing.width_in_points_of(pg._my_window,line_as_str,pg._font_name,pg._font_styles,pg._font_size)
      curpos._end_page_position.x_offset = line_width_in_points
      curpos._end_page_position.y_offset = pg._page_position.y_offset
      if curpos._in_fat_cursor:
        curpos._end_x_offset = line_width_in_points
        curpos._in_fat_cursor = False
        curpos._cursor_rectangle_pending = True


def _less_than_text_position(tp1,tp2):
  """ 
  pre:
    tp1 = first position in text
    tp2 = second position in text
  
  post:
    returns true iff curpos < curpos

  test:
    tp1 = (1,2)
      tp2 = (0,2)
      tp2 = (2,2)
      tp2 = (1,1)
      tp2 = (1,3)
      tp2 = (1,2)     
  """
  return (tp1.line_offset < tp2.line_offset) or \
         (tp1.line_offset == tp2.line_offset) and \
         (tp1.code_point_offset < tp2.code_point_offset)
  

def _new_page_position():
  """
  pre:
    true
    
  post:
    new _PagePosition variable has been returned,
      with undefined position
  
  note: 
    the PagePosition gives the position of the cursor in points 
      wrt the tlh corner of the text on the page
      
  test:
    once thru
  """
  pp = _PagePosition()
  pp.x_offset =  -1.00
  pp.y_offset =  -1.00
  return pp


def _new_text_position():
  """
  pre:
    true
    
  post:
    new _TextPosition variable has been returned,
      with undefined position
      
  note:
    the TextPosition gives the position of the cursor in the text as 
      (text_line_offset, code_point_offset)
    
  test:
    once thru
  """
  tp = _TextPosition()
  tp.line_offset =  -1
  tp.code_point_offset =  -1
  return tp


def _render_cursor_rectangle(x1,x2,pg):
  """
  pre:
    x1,x2 = start and end x-offsets of cursor rectangle in current line, as floats
    x1 < x2
    pg = Page on which curpos is to be rendered
    
  post:
    fat cursor rectangle has been rendered as required
    
  test:
    once thru
  """
  win = pg._my_window
  x = x1 + pg._horizontal_indent
  y = pg._vertical_indent + pg._page_position.y_offset
  w = x2 - x1
  h = pg._font_size
  c = _LIGHT_BLUE
  painting.paint_rectangle(win,x,y,w,h,c)

"""
def _render_cursor_rectangle(curpos,pg):
  """ """
  pre:
    curpos = start and end positions of cursor in text and page
    curpos < curpos
    pg = Page on which curpos is to be rendered
    curpos._in_fat_cursor = True
    curpos._in_fat_cursor = True
    
  post:
    fat cursor rectangle has been rendered as required
    
  test:
    once thru
  """ """
  win = pg._my_window
  x = pg._horizontal_indent + curpos._start_page_position.x_offset
  y = pg._vertical_indent + curpos._start_page_position.y_offset
  w = curpos._end_page_position.x_offset - curpos._start_page_position.x_offset
  h = pg._font_size
  c = _LIGHT_BLUE
  painting.paint_rectangle(win,x,y,w,h,c)
"""

def _render_glyph(cp,curpos,pg):
  """
  pre:
    cp = Unicode code point which is to be rendered
    curpos = start and end positions of cursor
            (Page positions may be undefined)
    pg = Page on which cp is to be rendered
    pg._text_position = position in text just after glyph to be rendered
    pg._page_position.y_offset = current y-offset of render
    
  post:
    cp has been, or shortly will be, rendered on pg
    the cursor has been rendered as necessary
    
  tests:
    once thru with cursor positioned after glyph
  """
  # append cp to current line
  unicoding3_0.append(pg._current_line,cp)
  
  # check cursor
  _fix_cursor_position(curpos,pg)
  

def _render_line(pg,curpos):
  """ 
  pre:
    pg = Page for this render
    pg._current_line = line to be rendered
    pg._line_width = width of current_line in points
    pg._text_width = width of text in points
    pg._current_alignment = alignment of line to be rendered
    pg._line_list = list of lines rendered, as (x_offset as float, line as str)
    pg._text_position.line_offset = offset of line being rendered in text
    pg._text_position.code_point_offset = offset of current code point in text line
    pg._page_position.y_offset = y-offset of line being rendered in page
    pg._my_window = windowing.Window for this render
    curpos._start_x_offset = start position of cursor rectangle
    curpos._end_x_offset = end position of cursor rectangle
    curpos._in_fat_cursor = True, iff render of fat cursor has been started
    
  post:
    if current line is on the page,
      pg._current_line' has been rendered
      (start x_offset,pg._current_line') has been added to the line_map
      if a cursor position was on line,
        its x-offset has been derelativized
    pg.page_position.x_offset = 0.0
    pg.page_position.y_offset = y-offset for next line
    pg._current_line = empty string
    pg._line_width = 0.0
    if the fat cursor is totally or partially on this line,
      it has been rendered

  test:
    line "fred"
      current_alignment = BEGIN
        pg._text_position = (0,0)
      current_alignment = END
        pg._text_position = (1,0)
      current_alignment = MIDDLE
        pg._text_position = (1,4)
  """
  # render the current line
  _try_line(pg,curpos)
  # set up the next line
  pg._page_position.x_offset = 0.0
  pg._page_position.y_offset += pg._font_size
  pg._current_line = unicoding3_0.new_string()
  pg._line_width = 0.0
  

def _render_token(tk,a,curpos,pg):
  """ 
  pre:
    tk = token to be rendered, as 
    a = alignment of text following tk
    curpos._start_text_position = curpos's start text position
    curpos._start_page_position = curpos's start page position or (-1.0,-1.0) 
                                if undefined
    curpos._desired_x_offset = desired x-offset of curpos, or -1 if undefined
    curpos._end_text_position = curpos's end text position
    curpos._end_page_position = curpos's end page position or (-1.0,-1.0) if undefined
    curpos._desired_x_offset = desired x-offset of curpos, or -1 if undefined
    curpos._in_fat_cursor = True, iff current position is inside a fat cursor
    curpos._cursor_rectangle_pending = True, iff a cursor rectangle has been 
                                     determined
    curpos._start_x_offset = cursor rectangle start x-offset relative to start of 
      line, if curpos._in_fat_cursor or curpos._cursor_rectangle_pending
    curpos._end_x_offset = cursor rectangle end x_offset relative to start of line,
      if curpos._cursor_rectangle_pending
    pg = Page to which this token is to be rendered
    pg._text_position = current position of render in text (line, code point)
    pg._line_width = width of current line in points
    pg._page_position.x_offset = 
      x-offset of start of current line in page, or 0.0.
    pg._page_position.y_offset = y-offset of start of current line in page
    pg._current_line = current line being rendered, as unicoding3_0.String
    pg._EOT_position.x_offset = x-offset of start of last line of text
    pg._EOT_position.y_offset = y-offset of start of last line of text
    pg._my_window = window associated with this page
    pg._back_map = map from (page_line,glyph_offset) to 
      (text_line,code_point_offset) for the text rendered so far
  
  post:
    curpos._start_text_position = curpos's start text position
    curpos._start_page_position = curpos's start page position 
                                or (-1.0,-1.0) if undefined
    curpos._end_text_position = curpos's end text position
    curpos._end_page_position = curpos's end page position or (-1.0,-1.0) if undefined
    curpos._desired_x_offset = desired x-offset of curpos, or -1 if undefined
    curpos._in_fat_cursor = True, iff current position is inside a fat cursor
    curpos._cursor_rectangle_pending = True, iff a cursor rectangle has been 
                                     determined
    curpos._start_x_offset = cursor rectangle start x-offset 
                               relative to start of line, 
                                 if curpos._in_fat_cursor or   
                                   curpos._cursor_rectangle_pending
    curpos._end_x_offset = cursor rectangle end x_offset 
                             relative to start of line,
                               if curpos._cursor_rectangle_pending
    pg._text_position = current position of render in text (line, code point)
    pg._page_position.y_offset = y_offset of current position of render in page
    pg._EOT_position.x_offset = end-of-text position x-offset
    pg._EOT_position.y_offset = end-of-text position y-offset
    pg._line_width = width of current line in points
    pg._back_map = map from (page_line,glyph_offset) to 
      (text_line,code_point_offset) for the text rendered so far
    if tk is an <end> token,
      the current line has been rendered
      curpos._start_page_position = curpos's start page position
      curpos._end_page_position = curpos's end page position
    if tk is a Separator token,
      the width in points of the line with a space appended is calculated
      if overflow has occurred,
        the current line has been rendered
        a new empty line has been started
      else
        the space has been appended to the line
    if tk is a Newline token,
      the current line has been rendered
      the alignment has been set to a
    if tk is a Word token,
      the width in points of the line with the word appended is calculated
      if overflow has occurred,
        any trailing space has been removed from the current line
        any pending cursor rectangle has been shortened
        the current line has been rendered
        a new line has been started with the word
      else
        the word has been appended to the line
    
  test:
    pg._current_alignment = BEGIN
      "<finish>"
      "<end>"
      "the"
        curpos = curpos = 0,0
        curpos = 0,1
          curpos = 0,3
      "the cat"
        curpos = 0,4
          curpos = 0,7
      "the cat sat on the mat"<end> (check EOT_position)
        "\n"
          a = MIDDLE
            "\n"
              a = END
                cursor at 0,18
                cursor at 0,19
                cursor at 0,22
                cursor at 1,0
                cursor at 2,0
      "the dogs sat on the"
        curpos = curpos = 0,0
      "the dogs sat on the "
        curpos = curpos = 0,0
  """
  try:
    # first code point of token gives sort
    cp0 = unicoding3_0.code_point_at(tk,0)
    # Tag
    if cp0 == ord('<'):
      la = looking_ahead.lookahead_of_string(tk)
      label = html_parsing.parse_tag(la)
      if unicoding3_0.equals(label,unicoding3_0.string_of("end")):
        _try_line(pg,curpos)
        pg._EOT_position.x_offset = pg._page_position.x_offset
        pg._EOT_position.y_offset = pg._page_position.y_offset
      else:
        raise Exception("unexpected tag label when rendering text:" + unicoding3_0.python_string_of(label))
        
    # Separator
    elif cp0 == ord(' '):
      pg._text_position.code_point_offset += 1
      space_width = writing.width_in_points_of(pg._my_window, ' ', pg._font_name, pg._font_styles, pg._font_size)
      pg._line_width += space_width
      # check for overflow of text width
      if pg._line_width > pg._text_width:
        pg._line_width -= space_width
        # render line and start a new line
        _render_line(pg,curpos)
        # update the _back_map
        _update_back_map(pg)
        # fix the cursor position if at start of new line
        _fix_cursor_position(curpos,pg)
      else:
        _render_glyph(ord(' '),curpos,pg)
        _update_back_map(pg)
        
    #Newline
    elif cp0 == ord('\n'):
      _render_line(pg,curpos)
      pg._current_alignment = a
      pg._text_position.line_offset += 1
      pg._text_position.code_point_offset = 0
      _update_back_map(pg)
      if _equals_text_position(curpos._end_text_position, pg._text_position):
        # render a rectangle of width 0.0 (i.e. do nothing)
        curpos._in_fat_cursor = False
      if curpos._in_fat_cursor:
        # reset cursor start text and page position
        curpos._start_text_position.line_offset = pg._text_position.line_offset
        curpos._start_text_position.code_point_offset = pg._text_position.code_point_offset
        curpos._start_page_position.x_offset = pg._page_position.x_offset
        curpos._start_page_position.y_offset = pg._page_position.y_offset
        # set cursor end page position undef
        curpos._end_page_position.x_offset = -1.0
        curpos._end_page_position.y_offset = -1.0
      else:  # thin cursor
        _fix_cursor_position(curpos,pg)
    
    # Word
    else:
      # remember the current page line width in points
      old_page_line_width = pg._line_width
      word_width = writing.width_in_points_of(pg._my_window, unicoding3_0.python_string_of(tk), pg._font_name, pg._font_styles, pg._font_size)
      pg._line_width += word_width
      # check for overflow of text width
      if pg._line_width > pg._text_width:
        # reset the line width
        pg._line_width = old_page_line_width
        # remove any trailing space
        last_pos = unicoding3_0.length_of(pg._current_line)-1
        if last_pos >= 0:
         if unicoding3_0.code_point_at(pg._current_line,last_pos) == ord(' '):
            unicoding3_0.remove(pg._current_line,last_pos)
            space_width = writing.width_in_points_of(pg._my_window, ' ', pg._font_name, pg._font_styles, pg._font_size)
            pg._line_width -= space_width
            if curpos._in_fat_cursor:
              if curpos._start_x_offset > pg._line_width:
                curpos._in_fat_cursor = False
            if curpos._cursor_rectangle_pending:
              if curpos._end_x_offset > pg._line_width:
                curpos._end_x_offset = pg._line_width
        # render the line without the current word
        _render_line(pg,curpos)
        # update the _back_map
        _update_back_map(pg)
        # fix the cursor position if at start of new line
        _fix_cursor_position(curpos,pg)
        # translate the word to the new line
        _de_escape(tk,curpos,pg)
        pg._line_width = word_width
      else:
        _de_escape(tk,curpos,pg)
  except Exception as inst:
    raise Exception("Unexpected exception when rendering token:"+str(inst))
    
  
def _try_line(pg,curpos):
  """ 
  pre:
    pg = Page to be rendered
    pg._current_line = line of page to be rendered
    pg._page_position.y_offset = current y offset of render on page, 
      in points relative to the tlh corner of the text, as float 
    pg._line_width = width of current line in points as float
    pg._text_width = maximum width of text on page in points as float
    pg._current_alignment = aligment of current line, as texting.Alignment
    pg._font_size = point size of font for this render, as float
    pg._text_height = height of text area on page, in points, as flaot 
    pg._line_list = list of lines rendered on page, as pair (x-offset as float, line as str)
    curpos = position of cursor, in text and page
    curpos._in_fat_cursor = 
      True, iff start position of fat cursor on page has been set,
        relative to the start of line, but end position has not  been found
    curpos._cursor_rectangle_pending = 
      True, iff final cursor rectangle has been created,
        relative to the start of line, but has not been rendered
    if curpos._in_fat_cursor,
      curpos._start_x_offset = start x-offset of cursor rectangle, 
                                 relative to start of line
    if curpos._cursor_rectangle_pending,
      curpos._start_x_offset = start x-offset of cursor rectangle, 
                                 relative to start of line
      curpos._end_x_offset = end x-offset of cursor rectangle,
                               relative to start of line

  post:
    if the current line is above the bottom of the text area,
      the current line has been rendered on the page
      the current line has been added to the line list
      if curpos._cursor_rectangle_pending,
        cursor rectangle has been aligned to the current line
        cursor rectangle has been queued for rendering
      if in_fat_cursor,
        cursor rectangle has been extended to the end of this line,
        cursor rectangle has been aligned to the current line
        non-final cursor rectangle has been queued for rendering
      if cursor is thin,
        the cursor has been aligned to the current line
      curpos._in_fat_cursor = 
        True, iff start position of fat cursor on page has been set,
          relative to the start of line, but end position has not  been found
      curpos._cursor_rectangle_pending = False
      pg._page_position.x_offset = x-offset of end of rendered line,
                                     relative to left-hand edge of text
      pg._page_position.y_offset = y-offset of end of rendered line,
                                     relative to top of text

  test:
    line at (0.0,0.0), cursor at ((0.0,0.0),(0.0,0.0))
    line just overlaps end of text area      
    line just fits on text area (check line list, pg._page_position)
      cursor start at start of previous line
        cursor end at start of previous line
      cursor start at start of line
        cursor end at start of line
      cursor start at start of line
        cursor end at start of line + 7.2
      cursor start at start of previous line
        cursor end at start of previous line + 7.2
    line penultimate of page
      cursor start at start of previous line
        cursor ends on this line
          curpos._in_fat_cursor False
            curpos._cursor_rectangle_pending True
              curpos._start x_offset  = start of this line
                curpos._end_x_offset = end point of cursor on this line
        cursor ends on next line
          curpos._in_fat_cursor True
            curpos._cursor_rectangle_pending False
              curpos._start x_offset = start of this line
      cursor start in this line
        cursor ends on this line, but is fat
          curpos._in_fat_cursor False
            curpos._cursor_rectangle_pending True
              curpos._start x_offset = start offset of cursor in this line
                curpos._end_x_offset = end offset of cursor in this line
  """
  if pg._page_position.y_offset + pg._font_size <= pg._text_height:
    pg._page_position.x_offset = page_laying_out.x_offset_of_line(pg._line_width,pg._text_width,pg._current_alignment)
    line_as_str = unicoding3_0.python_string_of(pg._current_line)
    end_x_offset = \
      writing.write_string(pg._my_window, \
                           line_as_str, \
                           pg._font_name, \
                           pg._font_styles, \
                           pg._font_size, \
                           pg._horizontal_indent + pg._page_position.x_offset, \
                           pg._vertical_indent + pg._page_position.y_offset, \
                           pg._text_color) - pg._horizontal_indent
    page_line_offset = math.floor(pg._page_position.y_offset/pg._font_size)
    _update_list(pg._line_list,page_line_offset,(pg._page_position.x_offset,line_as_str))
    if curpos._cursor_rectangle_pending:
      # align the rectangle
      ax1 = curpos._start_x_offset + pg._page_position.x_offset
      ax2 = curpos._end_x_offset + pg._page_position.x_offset
      _render_cursor_rectangle(ax1,ax2,pg)
      curpos._cursor_rectangle_pending = False
    if curpos._in_fat_cursor:
      y_offset = pg._page_position.y_offset
      ax1 = curpos._start_x_offset + pg._page_position.x_offset
      # this ensures rectangle is aligned to the text line
      ax2 = pg._page_position.x_offset + pg._line_width
      # render the non-final cursor rectangle
      _render_cursor_rectangle(ax1,ax2,pg)
      # set up the cursor rectangle for the next line
      curpos._start_x_offset = 0.0
    else:  # align thin cursor
      if _equals_float(curpos._start_page_position.y_offset,pg._page_position.y_offset):
        curpos._start_page_position.x_offset += pg._page_position.x_offset
      if _equals_float(curpos._end_page_position.y_offset,pg._page_position.y_offset):
        curpos._end_page_position.x_offset += pg._page_position.x_offset
    pg._page_position.x_offset = end_x_offset


def _update_back_map(pg):
  """
  pre:
    pg = page which is being rendered to
    pg._back_map = back map from Page to Text which is being updated
    pg._font_size = font size for this render, as a float
    pg._text_position = current render position in text, as (line_offset, code_point_offset)
    pg._page_position.y_offset = y-offset of start of current line in page
    pg._current_line = unicoding3_0.String representing current line of page
    
  post:
    pg._back_map has been updated with an entry for the glyph interstice
      at the end of the current line
      
  test:
    test:
      pg._font_size = 12.0
        pg._current_line = "a"
          pg._text_position = (0,1)
            pg._page_position.y_offset = 0.0
        pg._current_line = ""
          pg._text_position = (1,0)
            pg._page_position.y_offset = 12.0
        pg._current_line = "b"
          pg._text_position = (1,1)
            pg._page_position.y_offset = 12.0
  """
  page_line_offset = math.floor(pg._page_position.y_offset/pg._font_size)
  _ensure_sublist_exists(pg._back_map,page_line_offset)
  _update_list(pg._back_map[page_line_offset],
     unicoding3_0.length_of(pg._current_line),
     (pg._text_position.line_offset,pg._text_position.code_point_offset))


def _update_list(l,i,v):
  """
  pre:
    l = list to be updated
    i = position in list to be updated (0 <= i <= len(l))
    v = value to be inserted in list at position i
    
  post:
    l has been updated with v at position i
    l may have been extended by one element
    
  test:
    l is empty
      i = 1
      i = 0
        v= 123
      i = 1
        v = 456
      i = 0
        v = 789
  """
  if i < len(l):
    l[i] = v
  elif i == len(l):
    l.append(v)
  else:
    raise Exception("Attempt to update list with out-of-range index. i="+str(i)+", len(l)="+str(len(l)))

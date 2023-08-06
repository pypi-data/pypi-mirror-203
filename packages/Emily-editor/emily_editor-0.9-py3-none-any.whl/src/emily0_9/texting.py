from enum import Enum
import threading
""" 
Contractor which exposes a type Text, which is a series of lines,
indexed from 0.  Each line is a unicoding3_0.String (mutable sequence of 
unicode code points), indexed from 0.
A text always has a least one line (which may be empty).
Lines are separated by NL ('\n').
Each line has an associated alignment.
A text has an associated cursor, which can be used to access the text sequentially in either direction, or randomly.
The Text can be used as a lookahead, by using the procedures
"current_code_point" and "advance".
The type Text has a lock _my_lock, which should be used in 
multi-threading situations.
"""

# author R.N.Bosworth

# version 27 Feb 2023  15:%8

from guibits1_0 import type_checking2_0, unicoding3_0

"""
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

# exposed types
# -------------

Alignment = Enum('Alignment','BEGIN MIDDLE END')

class Text:
  """ 
  Invariants:
    the text always has at least one line (which may be empty)
    the cursor always is in a valid position (in the text or at end of text)
  """
  
  def __init__(self):
    """
    pre:
      self = Text to be initialized
      
    post:
      _my_text = list of Lines containing one empty Line
      _cursor_line = 0
      _cursor_char = 0
      _modified = False
      _first_paragraph = True
      
    test:
      twice thru
    """
    self._my_lock = threading.Lock()
    self._my_text = []
    self._my_text.append(_Line())
    self._cursor_line = 0
    self._cursor_char = 0
    self._modified = False
    self._first_paragraph = True


# exposed constants
# -----------------

END_OF_TEXT =  -1
START_OF_TEXT =  -2


# exposed procedures
# ------------------

def advance(t):
  """ 
  pre:
    t = Text whose cursor is to be advanced
    
  post:
     if t's cursor was before the end of Text,
       it has been moved one position towards the end of the text

  test:
    t = None
    t = ""
    t = "a\nb"
      cursor at start of text
        call advance four times
  """
  type_checking2_0.check_derivative(t,Text)  
  line = t._my_text[t._cursor_line]
  if t._cursor_char < unicoding3_0.length_of(line._my_line):
    t._cursor_char += 1
  else:
    if t._cursor_line < (len(t._my_text)-1):
      t._cursor_char = 0
      t._cursor_line += 1
    else:
      pass  # cursor at end of text
    

def current_code_point(t):
  """ 
  pre:  t = Text to be read
        
  post: returns UTF-32 code point of character at cursor position of t,
          or END_OF_TEXT if the cursor is at the end of t, as an int
  test:
    t = None
    t = ""
    t = "a\nb"
      call current_code_point
      call current_code_point,advance four times
  """
  type_checking2_0.check_derivative(t,Text)
  line = t._my_text[t._cursor_line]
  if t._cursor_char < unicoding3_0.length_of(line._my_line):
    return unicoding3_0.code_point_at(line._my_line,t._cursor_char)
  else:
    if t._cursor_line < len(t._my_text) - 1:
      return ord('\n')
    else:
      return END_OF_TEXT
      

def cursor_code_point_offset(t):
  """ 
  pre:
    t = Text whose cursor's char-offset is to be queried
        
  post: 
    char-offset within the line of t's cursor has been returned, as an int
    
  test:
    t = None
    t = valid Text
      cursor char offset 0
      cursor char offset non-zero
  """
  type_checking2_0.check_derivative(t,Text)
  return t._cursor_char
  

def cursor_line_offset(t):
  """ 
  pre:  
    t = Text whose cursor's line-offset is to be queried
        
  post: 
    line-offset of t's cursor has been returned, as an int

  test:
    t = None
    t = valid Text
      zero line length
      non-zero line length
  """
  type_checking2_0.check_derivative(t,Text)
  return t._cursor_line
  

def delete_after(t):
  """ 
  pre:
    t = Text to be modified
    
  post:
    character after cursor of text t has been deleted, 
      if possible
    returns True iff char has been deleted, else False

  post:
    t._modified = True, if this procedure's action modified the text

  test:
    t = None
    t = valid Text
      cursor two chars before end of non-last line
      cursor at end of non-last line
      cursor at end of text
  """
  type_checking2_0.check_derivative(t,Text)
  line = t._my_text[t._cursor_line]
  
  # if at end of text, do nothing
  if t._cursor_line == len(t._my_text) - 1 \
  and t._cursor_char == unicoding3_0.length_of(line._my_line):
    return False
    
  # if at end of line, combine this line with next
  if t._cursor_char == unicoding3_0.length_of(line._my_line):
    line2 = t._my_text[t._cursor_line + 1]
    unicoding3_0.append_a_copy(line._my_line,line2._my_line)
    t._my_text.pop(t._cursor_line + 1)
    t._modified = True
    
  # otherwise, remove the character after the cursor 
  #   and pull the rest of the line down
  else:
    unicoding3_0.remove(line._my_line,t._cursor_char)
    t._modified = True
    
  return True
  

def get_alignment(t):
  """ 
  pre:
    t = Text whose alignment is to be found
    
  post:
    Alignment of line of t containing the cursor has been returned

  test:
    t = None
    t = valid Text
      current line's alignment = BEGIN
      current line's alignment = BEGIN
      current line's alignment = END
  """
  type_checking2_0.check_derivative(t,Text)
  return t._my_text[t._cursor_line]._my_alignment
  

def has_been_modified(t):
  """ 
  pre:
    t = Text to be tested for modification
    
  post:
    returns True iff t has been modified, else False
    
  test:
    t = None
    t = valid Text
      t has been modified
      t has not been modified
  """
  type_checking2_0.check_derivative(t,Text)
  return t._modified
  

def insert_code_point(t,cp):
  """ 
  pre:  t = Text to be modified
        cp = code point of unicode character to be inserted, as an int
        
  post: character with code point cp has been inserted 
          at cursor position of text t
        cursor position has been incremented

  post:
    t._modified = true

  test:
    insert_code_point(None,None)
    t = empty text
      insert_code_point(t,None)
      insert_code_point(t,-1)
      insert_code_point(t,0x110000)
      insert '\n'
      insert 'a'
    t = text of two lines with MIDDLE alignment
      insert '\n' at (0,0)
      insert '\n' at end of first line
      insert '\n' at middle of first line
      insert 'a' at (0,0)
      insert 'a' at end of first line
      insert 'a' at middle of first line
  """
  type_checking2_0.check_derivative(t,Text)
  type_checking2_0.check_identical(cp,int)
  if cp < 0 or cp > 0x10ffff:
    raise Exception("Attempt to write invalid code point: " + hex(cp))
  if cp == ord('\n'):
    # find alignment of current line
    a = t._my_text[t._cursor_line]._my_alignment
    # split line at cursor point
    s = unicoding3_0.python_string_of(t._my_text[t._cursor_line]._my_line)
    s1 = s[0:cursor_code_point_offset(t)]
    s2 = s[cursor_code_point_offset(t):_line_length(t)]
    # old line is replaced by first substring
    line1 = _Line()
    line1._my_alignment = a
    line1._my_line = unicoding3_0.string_of(s1)
    t._my_text[t._cursor_line] = line1
    # insert new line made from second substring
    line2 = _Line()
    line2._my_alignment = a
    line2._my_line = unicoding3_0.string_of(s2)
    t._cursor_line += 1
    t._my_text.insert(t._cursor_line,line2)
    # cursor is set to start of new line
    t._cursor_char = 0
    
  # non-LF char
  else:
    # insert code point
    unicoding3_0.insert(t._my_text[t._cursor_line]._my_line,t._cursor_char,cp)
    # increment cursor
    t._cursor_char += 1
    
  t._modified = True
  

def new_text():
  """ 
  post: a new variable of type Text has been returned.

  test: once thru
  """
  t = Text()
  # text always has at least one line
  return t
  

def retreat(t):
  """ 
  pre:
    t = Text whose cursor is to be retreated
    
  post:
    if t's cursor was before the start of text, 
      it has been moved one position nearer to the start of text

  test:
    t = None
    t = ""
    t = "a\nb"
      cursor at end of text
        call retreat 4 times
  """
  type_checking2_0.check_derivative(t,Text)
  if t._cursor_char == 0:
    if t._cursor_line == 0:
      pass  # cursor at beginning of text
    else:
      t._cursor_line -= 1
      t._cursor_char = _line_length(t)
  else:
    t._cursor_char -= 1
    
  
def set_alignment(t,a):
  """ 
  pre:
    t = Text whose alignment is to be set
    a = Alignment value to which current line of t is to be set
    
  post:
    alignment of line of t containing the cursor has been set to a

  test:
    t = None
    t = valid text
      a = None
    t = valid Text of several lines 
      a = MIDDLE (check alignment)
  """
  type_checking2_0.check_derivative(t,Text)
  type_checking2_0.check_derivative(a,Alignment)
  t._my_text[t._cursor_line]._my_alignment = a
  

def set_cursor(t,lo,co):
  """ 
  pre:  t = Text whose cursor is to be set
        lo = line offset to which cursor is to be set, as an int
        co = character offset to which cursor is to be set, as an int
        
  post: cursor has been set (as far as is possible) to the client's requirements

  test:
    t = None
    t = valid Text of several lines
      lo = None
      lo = -1
      lo = 0
        co = None
        co = -1
        co = 0  (check values)
      lo = one line past end of text
      lo = last line of text
        co = one character past end of text
        co = last character of text  (check values)
  """
  type_checking2_0.check_derivative(t,Text)
  type_checking2_0.check_identical(lo,int)
  if lo < 0 or lo >= len(t._my_text):
    raise Exception("Attempt to set cursor line offset to invalid value: lo="+str(lo))
  type_checking2_0.check_identical(co,int)
  if co < 0 or co > unicoding3_0.length_of(t._my_text[lo]._my_line):
    raise Exception("Attempt to set cursor character offset to invalid value: co="+str(co))
  t._cursor_line = lo
  t._cursor_char = co
  

def set_cursor_end(t):
  """ 
  pre:
    t = Text whose cursor is to be set
        
  post:
    cursor position has been set to the end of the text

  test:
    t = None
    empty text
    non-empty text with non-empty last line (check value)
  """
  type_checking2_0.check_derivative(t,Text)
  t._cursor_line = len(t._my_text) - 1
  line = t._my_text[t._cursor_line]
  t._cursor_char = unicoding3_0.length_of(line._my_line)
  

def set_cursor_start(t):
  """ 
  pre:
    t = Text whose cursor is to be set
        
  post:
    cursor position has been set to the start of the text

  test:
    t = None
    t = valid text (check value)
  """
  type_checking2_0.check_derivative(t,Text)
  set_cursor(t,0,0)
  

def set_modified(t):
  """ 
  pre:
    t = Text to be marked as modified
    
  post:
    t has been marked as modified

  test:
    t = None
    t = valid text (check value)
  """
  type_checking2_0.check_derivative(t,Text)
  t._modified = True
  

def set_unmodified(t):
  """ 
  pre:
    t = Text to be marked as unmodified
    
  post:
    t has been marked as unmodified

  test:
    t = None
    t = valid text (check value)
  """
  type_checking2_0.check_derivative(t,Text)
  t._modified = False
  

# private types
# -------------

class _Line:
  def __init__(self):
    """
    pre:
      self = _Line to be initialized
      
    post:
      _my_aligment = Alignment.BEGIN
      _my_line = unicoding3_0.new_string()
      
    test:
      twice thru
    """
    self._my_alignment = Alignment.BEGIN
    # default alignment for new line
    self._my_line = unicoding3_0.new_string()


# private procedures
# ------------------

def _line_length(t):
  """ 
  pre:
    t = text whose current line length is to be returned
    
  post:
    returns length of current line of t (line where cursor is positioned)
    Note: the length does not include the final '\n', if present

  test:
    once thru
  """
  return unicoding3_0.length_of(t._my_text[t._cursor_line]._my_line)

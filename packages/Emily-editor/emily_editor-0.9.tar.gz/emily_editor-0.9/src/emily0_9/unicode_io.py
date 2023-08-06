""" 
Contractor for Unicode input and output.
Input and output is performed on a codepoint-by-codepoint basis,
with unicode_io.END_OF_STREAM as stream terminator.
Externally, the Unicode stream is stored in UTF-8 format.
It is also possible to input and output to a unicoding3_0.String,
for testing purposes.
"""

# author R.N.Bosworth

# version 8 Mar 23  11:11

from guibits1_0 import type_checking2_0, unicoding3_0

"""
Copyright (C) 2017,2021,2022  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

# exposed constants
# -----------------

END_OF_STREAM =  - 1


# exposed types
# -------------

class Reader:
  pass
  

class Writer:
  pass
  

# exposed procedures
# ------------------

def get_string(w):
  """ 
  pre:
    w = _StringWriter from which string is to be extracted
    
  post:
    w's string has been returned

  test:
    w is not a _StringWriter
    w is a _StringWriter with a non-empty string
  """
  type_checking2_0.check_derivative(w,_StringWriter)
  return w.get_string()
  

def new_input_reader(fn):
  """ 
  pre:
    fn = filename from which the Unicode stream is to be read, as a str
    
  post:
    either:
      an input Reader object has been returned for the specified filename
    or:
      an Exception has been raised

  test:
    invalid file name (invalid characters)
    valid file name but file not there
    valid existent file
  """
  type_checking2_0.check_derivative(fn,str)
  r = _InputReader()
  try:
    r._my_file = open(fn)
  except:
    raise Exception("Unable to open file:" + fn)
  return r
  

def new_output_writer(fn):
  """ 
  pre:
    fn = filename to which the Unicode stream is to be written, as str
    
  post:
    either:
      an output Writer object has been returned for the specified filename
    or:
      an Exception has been raised

  test:
    file name not str
    invalid file name (invalid characters)
    valid file name but file not there (remove hardware)
    valid existent file
  """
  type_checking2_0.check_identical(fn,str)
  try:
    w = _OutputWriter()
    w._my_file = open(fn,'w')
  except:
    raise Exception("Output file could not be opened")
  return w
  
  
def new_string_reader(s):
  """ 
  pre:
    s = unicoding3_0.String from which the the reader is to be created
    
  post:
    a string Reader object has been returned for the specified string

  test:
    s = None
    s = invalid string
    s = valid unicoding3_0.String
  """
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  sr = _StringReader()
  sr._my_string = s
  sr._pos = 0
  return sr
  

def new_string_writer():
  """ 
  post:
    a string Writer object has been returned

  test:
    once thru
  """
  sw = _StringWriter()
  sw._my_string = unicoding3_0.new_string()
  return sw
    

def read(r):
  """ 
  pre:
    r = Reader from which the next code point is to be read
    
  post:
    either:
      the next code point, or END_OF_STREAM, has been returned from r
    or:
      an IOException has been raised

  test:
    _Reader:
      'a'
      _READER_EOS
    _StringReader:
      U+0000
      "abc"
      U+FFFF
      U+10000
      U+10FFFF
  """
  type_checking2_0.check_derivative(r,Reader)
  return r.read()
  

def write(cp,w):
  """ 
  pre:
    cp = next Unicode code point to be written, or END_OF_STREAM
    w = Writer to which cp is to be written
    
  post:
    either:
      the next code point, or END_OF_STREAM, has been written to w
    or:
      an IOException has been raised

  test:
    cp = -2
    cp = -1
    cp = 0x10ffff
    cp = 0x110000
  """
  type_checking2_0.check_identical(cp,int)
  if cp < END_OF_STREAM or cp > 0x10ffff:
    raise Exception("Attempt to write invalid code point: "+ hex(cp))
  type_checking2_0.check_derivative(w,Writer)
  w.write(cp)
  

# private classes
# ---------------

class _InputReader(Reader):

  def read(self):
    """ 
    pre:
      self = _InputReader from which the next code point is to be read
      
    post:
      either:
        the next code point, or END_OF_STREAM, has been returned from r
      or:
        an IOException has been raised

    test:
      U+0000
      'a'
      U+FFFF
      U+10000
      U+10FFFF
      _READER_EOS
    """
    c = self._my_file.read(1)
    if c == '':
      return END_OF_STREAM
    else:
      return ord(c)
      

class _OutputWriter(Writer):

  def write(self,cp):      
    """ 
    pre:
      self = _OutputWriter on which cp is to be written
      cp = next code point to be written, or END_OF_STREAM
      
    post:
      either:
        the next code point, or END_OF_STREAM, has been written to the underlying stream
      or:
        an IOException has been raised

    test:
      0x0000
      'a'
      0xffff
      0x10000
      0x10ffff
      END_OF_STREAM
    """
    if cp == END_OF_STREAM:
      self._my_file.close()
    else:
      self._my_file.write(chr(cp))    
  
  def get_string(self):
    """ 
    pre:
      self = Writer from which string is required
    post:
      a RuntimeException has been raised
      
    test:
      once thru
    """
    raise Exception("Attempt to get string from a non-string Writer")


class _StringReader(Reader):

  def read(self):
    """
    pre:
      self = Reader from which the next code point is to be read
      
    post:
      the next code point, or END_OF_STREAM, has been returned
      
    test:
      not END_OF_STREAM
      END_OF_STREAM
    """
    if self._pos >= unicoding3_0.length_of(self._my_string):
      return END_OF_STREAM
      
    else:
      cp = unicoding3_0.code_point_at(self._my_string,self._pos)
      self._pos += 1
      return cp


class _StringWriter(Writer):

  def write(self,cp):
    """ 
    pre:
      self = Writer to which cp is to be written
      cp = next code point to be written, or END_OF_STREAM
      
    post:
      the next code point has been written to the underlying string
        (END_OF_STREAM is ignored)

    test:
      'x'
        'y'
          'z'
            END_OF_STREAM
    """
    if cp != END_OF_STREAM:
      unicoding3_0.append(self._my_string,cp)
      

  def get_string(self):
    """ 
    pre:
      self = _StringWriter from which string is to be extracted
      
    post:
      this writer's string has been returned

    test:
      empty string
      non-empty string
    """
    return self._my_string

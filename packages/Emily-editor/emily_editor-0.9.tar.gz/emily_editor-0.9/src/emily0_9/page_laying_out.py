# Contractor to assist with layout of a page.

# author R.N.Bosworth

# version 13 Mar 23  16:59

from guibits1_0 import font_styling, type_checking2_0, unicoding3_0
from guibits1_0 import windowing, writing
from . import looking_ahead
from . import string_parsing
from . import texting

""" 

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

# exposed procedures
# ------------------

def width_in_points_of_escaped(win,s,fn,fss,fsize):
  """ 
  pre:
    win = windowing.Window on which s is to be written
    win must be present on the screen
    s = string to be measured, as a unicoding3_0.String
    fn = name of font for s, as a str
    fss = set of font_styling.FontStyles for s (empty set implies the string should be measured plain)
    fsize = point size of font for s, in range 6.0..72.0, as a float 
  post:
    the length of the de-escaped (i.e. rendered) version s in points, for the given window, font name, font styles and font size, has been returned as a float 

  test:
    win = None
    win not showing
    win is showing
      fn = None
        fss= None
          fsize = None
            s = None
      fn = "Courier New"
        fss = {}
          fsize = 5.9
          fsize = 72.1
          fsize = 10.0
            s = ""
            s = "f"
            s = "fred"
            s = "fredfredfredfredfredfredfredfredfredfred"
            s = "1 &lt; 2"
  """
  type_checking2_0.check_derivative(win,windowing.Window)
  type_checking2_0.check_derivative(s,unicoding3_0.String)
  type_checking2_0.check_identical(fn,str)
  type_checking2_0.check_derivative(fss,font_styling.FontStyles)
  type_checking2_0.check_identical(fsize,float)
  if fsize < 6.0 or fsize > 72.0:
    raise Exception("Attempt to lay out font of size <6.0 or >72.0. fsize="+str(fsize))
  ds = unicoding3_0.new_string()
  o = 0
  while o < unicoding3_0.length_of(s):
    (dcp,o) = string_parsing.parse_html_character(s,o)
    unicoding3_0.append(ds,dcp)
  dstr = unicoding3_0.python_string_of(ds)
  return writing.width_in_points_of(win,dstr,fn,fss,fsize)
  

def x_offset_of_line(l,w,a):
  """ 
  pre:
    l = length of the line in points, as float
    w = width of the text on the page which the line is to be displayed, as float
    a = texting.Alignment of the line
    
  post:
    the x-offset from the start of the text area required to display the line 
      with the given alignment has been returned

  test:
    w = None
    w = 5.0
      l = None
      l = 3.0
        a = None
        a = BEGIN
            MIDDLE
            END
            JUSTIFY
  """
  type_checking2_0.check_identical(l,float)
  type_checking2_0.check_identical(w,float)
  type_checking2_0.check_derivative(a,texting.Alignment)
  if a == texting.Alignment.BEGIN:
    return 0.0
  elif a == texting.Alignment.MIDDLE:
    return (w - l)/2.0
  elif a == texting.Alignment.END:
    return w - l
  else:
    pass
  return 0.0

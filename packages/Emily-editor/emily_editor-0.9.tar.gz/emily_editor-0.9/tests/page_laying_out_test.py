# Test program for Contractor to assist with layout of a page.

# author R.N.Bosworth

# version 13 Mar 23  16:54

from emily0_9 import page_laying_out, texting
from guibits1_0 import font_styling, windowing, unicoding3_0

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

# test program
# ------------

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
  

def window_closing(win):
  #page_laying_out.width_in_points_of_escaped(win,None,None,None,None)
  #page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),None,None,None)
  #page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",None,None)
  fss = font_styling.new_font_styles()
  #page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",fss,None)
  #page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",fss,5.9)
  #page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",fss,72.1)
  assert page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",fss,10.0) == 0.0
  wipoe = page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of("f"),"Courier New",fss,10.0)
  assert _equals_float(wipoe,6.0)
  wipoe = page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of("fred"),"Courier New",fss,10.0) 
  assert _equals_float(wipoe,24.0)
  wipoe = page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of("fredfredfredfredfredfredfredfredfredfred"),"Courier New",fss,10.0) 
  assert _equals_float(wipoe,240.04)
  wipoe = page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of("1 &lt; 2"),"Courier New",fss,10.0) 
  assert _equals_float(wipoe,30.0)
  print("OK")
  print("")
  print("All tests OK")
  return True

print("Tests of page_laying_out.x_offset_of_line", end=' ')
#page_laying_out.x_offset_of_line(None,None,None)
#page_laying_out.x_offset_of_line(3.0,None,None)
#page_laying_out.x_offset_of_line(3.0,5.0,None)
assert page_laying_out.x_offset_of_line(3.0,5.0,texting.Alignment.BEGIN) == 0.0
assert page_laying_out.x_offset_of_line(3.0,5.0,texting.Alignment.MIDDLE) == 1.0
assert page_laying_out.x_offset_of_line(3.0,5.0,texting.Alignment.END) == 2.0
print("OK")


print("Tests of page_laying_out.width_in_points_of_escaped", end=' ')
#page_laying_out.width_in_points_of_escaped(None,None,None,None,None)
win = windowing.new_window(12.0,"Window for test of page_laying_out.width_in_points_of_escaped",800.0,500.0,1.0)
fss = font_styling.new_font_styles()
#assert page_laying_out.width_in_points_of_escaped(win,unicoding3_0.string_of(""),"Courier New",fss,12.0) == 0.0
windowing.show(win,None,window_closing)
print("OK")

print("")
print("All tests OK")

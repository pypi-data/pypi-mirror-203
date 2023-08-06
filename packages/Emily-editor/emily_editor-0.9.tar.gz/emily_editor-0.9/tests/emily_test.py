# test of main class subprocedures for Emily

# author R.N.Bosworth

# version 16 Mar 23  22:05
"""
Copyright (C) 2015,2016,2017,2018,2019,2021,2022,2023  R.N.Bosworth

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License (gpl.txt) for more details.
"""

from emily0_9 import emily, persisting

#------------------------------------------------------------------------------
# test program
# -----------------------------------------------------------------------------

def _print_text(t):
  cpo = texting.cursor_code_point_offset(t)
  lo = texting.cursor_line_offset(t)
  print("-----------------------------------")
  texting.set_cursor_start(t)
  cp = texting.current_code_point(t)
  texting.advance(t)
  while cp != texting.END_OF_TEXT:
    print("" + (chr(cp)))
    cp = texting.current_code_point(t)
    texting.advance(t)
    
  print("-----------------------------------")
  texting.set_cursor(t,lo,cpo)
  
  
print("Tests of emily.build_tagged_label", end=' ')
r = emily.build_tagged_label("fred",False)
assert r == "   fred"
r = emily.build_tagged_label("fred",True)
assert r == "• fred"
print("OK")

print ("Tests of build_tagged_font_size_label", end=' ')
l = emily.build_tagged_font_size_label(10,11)
assert l == "   10 point"  
l = emily.build_tagged_font_size_label(11,11)
assert l == "• 11 point"  
print("OK")

print("Tests of check_file_type")
emily.my_persistents = persisting.get_persistents()
fn = emily.check_file_type("fred.mlf")
print("  fn="+str(fn))
fn = emily.check_file_type("fred.mle")
print("  fn="+str(fn))
print("OK")

print("Tests of int_of",end=' ')
#i = emily.int_of("")
#i = emily.int_of("fred")
i = emily.int_of("  90")
assert i == 90
i = emily.int_of("  909 points")
assert i == 909
print("OK")

print("Tests of name_of",end=' ')
#s = emily.name_of("")
#s = emily.name_of("£££££")
assert emily.name_of("fredfont") == "fredfont"
assert emily.name_of("& Times New Roman") == "Times New Roman"
print("OK")

print("")
print("All tests OK")

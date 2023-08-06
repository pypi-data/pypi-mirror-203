# Test program for Contractor which converts text to tokens.

# author R.N.Bosworth

# version 8 Mar 23  10:53

from emily0_9 import text_tokenizing, texting
from guibits1_0 import unicoding3_0

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

# test program
# ------------

def _equals(s1,s2):
  return unicoding3_0.equals(s1,unicoding3_0.string_of(s2))


print("Tests of _parse_token", end=' ')
t = texting.new_text()
texting.insert_code_point(t,ord(' '))
texting.insert_code_point(t,ord('f'))
texting.insert_code_point(t,ord('r'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('x'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('r'))
texting.insert_code_point(t,ord('t'))
texting.set_cursor_start(t)
s = text_tokenizing._parse_token(t)
assert _equals(s," ")
s = text_tokenizing._parse_token(t)
assert _equals(s,"fred")
s = text_tokenizing._parse_token(t)
assert _equals(s,"<b>")
s = text_tokenizing._parse_token(t)
assert _equals(s,"x")
s = text_tokenizing._parse_token(t)
assert _equals(s,"\n")
s = text_tokenizing._parse_token(t)
assert _equals(s,"bert")
#s = text_tokenizing._parse_token(t) # end of text - should fail
print("OK")

print("Tests of get_next_token", end=' ')
#s = text_tokenizing.get_next_token(None)
t = texting.new_text()
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord(' '))
texting.insert_code_point(t,ord('f'))
texting.insert_code_point(t,ord('r'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('d'))
texting.set_cursor_start(t)
s = text_tokenizing.get_next_token(t)
assert _equals(s,"<i>")
s = text_tokenizing.get_next_token(t)
assert _equals(s," ")
s = text_tokenizing.get_next_token(t)
assert _equals(s,"fred")
s = text_tokenizing.get_next_token(t)
assert _equals(s,"<end>")
s = text_tokenizing.get_next_token(t)
assert _equals(s,"<end>")
print("OK")

print("")
print("All tests OK")

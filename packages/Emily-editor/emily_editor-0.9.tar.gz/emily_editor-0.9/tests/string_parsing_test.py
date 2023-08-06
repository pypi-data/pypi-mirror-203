# Test program for Contractor to parse an HTML string.

# author R.N.Bosworth

# version 4 Mar 23  16:27

from emily0_9 import string_parsing
from guibits1_0 import unicoding3_0

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

print("Tests of string_parsing._accept", end=' ')
cp = ord('A')
s = unicoding3_0.string_of("B")
#o = string_parsing._accept(cp,s,0);
s = unicoding3_0.string_of("A")
o = string_parsing._accept(cp,s,0)
assert o == 1
print("OK")

print("Tests of string_parsing.parse_html_character", end=' ')
#(cp,o) = string_parsing.parse_html_character(None,None)
s = unicoding3_0.string_of("&bmp;")
#(cp,o) = string_parsing.parse_html_character(s,None)
#(cp,o) =string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&anp;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&amq;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&amp;")
(cp,o) = string_parsing.parse_html_character(s,0)
assert cp == ord('&')
assert o == unicoding3_0.length_of(s)
s = unicoding3_0.string_of("&ft;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&gs;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&gt;")
(cp,o) = string_parsing.parse_html_character(s,0)
assert cp == ord('>')
assert o == unicoding3_0.length_of(s)
s = unicoding3_0.string_of("&mt;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&lu;")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("&lt;")
(cp,o) = string_parsing.parse_html_character(s,0)
assert cp == ord('<')
assert o == unicoding3_0.length_of(s)
s = unicoding3_0.string_of(">")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("<")
#(cp,o) = string_parsing.parse_html_character(s,0)
s = unicoding3_0.string_of("a")
(cp,o) = string_parsing.parse_html_character(s,0)
assert cp == ord('a')
assert o == unicoding3_0.length_of(s)
print("OK")

print("")
print("All tests OK")

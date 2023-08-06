# Test program for Contractor for the basic grammar of HTML and CSS.

# author R.N.Bosworth

# version 8 Mar 23  15:40

from emily0_9 import html_css_parsing, looking_ahead, unicode_io
from guibits1_0 import unicoding3_0

""" 
Copyright (C) 2017,2018,2021,2022,2023  R.N.Bosworth

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

print("Tests of accept", end=' ')
#html_css_parsing.accept('A',None)
#html_css_parsing.accept(ord('A'),None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("B"))
#html_css_parsing.accept(ord('A'),la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("A"))
html_css_parsing.accept(ord('A'),la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of accept_optional_spaces", end=' ')
#html_css_parsing.accept_optional_spaces(None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("hello"))
html_css_parsing.accept_optional_spaces(la)
assert looking_ahead.current_symbol_of(la) == ord('h')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("  hello"))
html_css_parsing.accept_optional_spaces(la)
assert looking_ahead.current_symbol_of(la) == ord('h')
print("OK")

print("Tests of accept_separator", end=' ')
#html_css_parsing.accept_separator(None);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(""))
#html_css_parsing.accept_separator(la);
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("a"))
#html_css_parsing.accept_separator(la);
assert looking_ahead.current_symbol_of(la) == ord('a')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(" "))
html_css_parsing.accept_separator(la)
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("   "))
html_css_parsing.accept_separator(la)
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
print("OK")

print("Tests of parse_name", end=' ')
#html_css_parsing.parse_name(None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("%"))
#s = html_css_parsing.parse_name(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.new_string())
#s = html_css_parsing.parse_name(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("f"))
s = html_css_parsing.parse_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("f"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("fred"))
s = html_css_parsing.parse_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("fred"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("FRED"))
#s = html_css_parsing.parse_name(la)
print("OK")

print("Tests of accept_name", end=' ')
#html_css_parsing.accept_name(None,None)
#html_css_parsing.accept_name(unicoding3_0.string_of("fred"),None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("jim"))
#html_css_parsing.accept_name(unicoding3_0.string_of("fred"),la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("fred"))
html_css_parsing.accept_name(unicoding3_0.string_of("fred"),la)
print("OK")

print("")
print("All tests OK")

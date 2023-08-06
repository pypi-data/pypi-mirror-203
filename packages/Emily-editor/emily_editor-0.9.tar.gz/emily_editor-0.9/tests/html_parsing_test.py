# Test program for Contractor which has procedures for parsing basic html entities.

# author R.N.Bosworth

# version 9 Mar 23  14:26

from emily0_9 import html_parsing, looking_ahead
from guibits1_0 import unicoding3_0

""" 
Copyright (C) 2017,2018,2019,2021,2022,2023  R.N.Bosworth

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

print("Tests of html_parsing.accept_end_tag", end=' ')
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(">/html>"))
#html_parsing.accept_end_tag(None,la)
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<\\html>"))
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</html<"))
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</htmm>"))
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</html>"))
html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</HTML  >"))
#html_parsing.accept_end_tag(unicoding3_0.string_of("html"),la)
print("OK")

print("Tests of accept_start_tag", end=' ')
#html_parsing.accept_start_tag(unicoding3_0.string_of("html"),None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(">html>"))
#html_parsing.accept_start_tag(None,la)
#html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html<"))
#html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<htmm>"))
#html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html>"))
html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<HTML  >"))
#html_parsing.accept_start_tag(unicoding3_0.string_of("html"),la)
print("OK")

print("Tests of parse_start_tag", end=' ')
#s = html_parsing.parse_start_tag(None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{fred  }"))
#s = html_parsing.parse_start_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<  >"))
#s = html_parsing.parse_start_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<fred  >"))
s = html_parsing.parse_start_tag(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("fred"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<jim]"))
#s = html_parsing.parse_start_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<jim>"))
s = html_parsing.parse_start_tag(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("jim"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of parse_tag", end=' ')
#s = html_parsing.parse_tag(None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{/fred  }"))
#s = html_parsing.parse_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</  >"))
#s = html_parsing.parse_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</fred  >"))
s = html_parsing.parse_tag(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("/fred"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<jim]"))
#s = html_parsing.parse_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<jim>"))
s = html_parsing.parse_tag(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("jim"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</bert>"))
s = html_parsing.parse_tag(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("/bert"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("")
print("All tests OK")

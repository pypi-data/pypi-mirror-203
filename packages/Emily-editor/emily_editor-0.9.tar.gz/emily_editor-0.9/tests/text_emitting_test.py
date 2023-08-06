# Test of Parser which converts an Emily text to an MLE stream.

# author R.N.Bosworth

# version 7 Mar 23  20:10

from emily0_9 import texting, text_emitting, unicode_io
from guibits1_0 import unicoding3_0

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

# test program
# ------------

print("Tests of _emit_paragraph_start_tag", end=' ')
w = unicode_io.new_string_writer()
text_emitting._emit_paragraph_start_tag(texting.Alignment.BEGIN,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"begin\">"))
w = unicode_io.new_string_writer()
text_emitting._emit_paragraph_start_tag(texting.Alignment.MIDDLE,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"middle\">"))
w = unicode_io.new_string_writer()
text_emitting._emit_paragraph_start_tag(texting.Alignment.END,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"end\">"))
print("OK")

print("Tests of parse_text", end=' ')
#text_emitting.parse_text(None,None)
t = texting.new_text()
#text_emitting.parse_text(t,None)
w = unicode_io.new_string_writer()
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of(""))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<br>\n<br>\n"))
t = texting.new_text()
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('e'))
texting.set_cursor_start(t)
w = unicode_io.new_string_writer()
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"begin\">\n  the</p>\n"))
t = texting.new_text()
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('\n'))
w = unicode_io.new_string_writer()
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"begin\">\n  the<br>\n  cat</p>\n"))
t = texting.new_text()
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('\n'))
w = unicode_io.new_string_writer()
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"begin\">\n  the</p>\n<p class=\"begin\">\n  cat</p>\n"))
t = texting.new_text()
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('s'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
w = unicode_io.new_string_writer()
text_emitting.parse_text(t,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<p class=\"begin\">\n  the</p>\n<p class=\"begin\">\n  cat</p>\n<br>\n<p class=\"begin\">\n  sat</p>\n<br>\n<br>\n<br>\n"))
print("OK")

print("")
print("All tests OK")

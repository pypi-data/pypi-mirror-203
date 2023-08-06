# Test of Contractor for emitting html elements.

# author R.N.Bosworth

# version 2 Mar 2023  14:45

""" 
Contractor for emitting html elements.

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

from emily0_9 import html_emitting, unicode_io
from guibits1_0 import unicoding3_0

# test program
# ------------

print("Tests of html_emitting.emit_end_tag", end=' ')
#html_emitting.emit_end_tag(None,None)
#html_emitting.emit_end_tag(unicoding3_0.string_of("html"),None)
w = unicode_io.new_string_writer()
html_emitting.emit_end_tag(unicoding3_0.string_of("html"),w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("</html>"))
print("OK")

print("Tests of html_emitting.emit_indent", end=' ')
#html_emitting.emit_indent(None)
w = unicode_io.new_string_writer()
html_emitting.emit_indent(w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  "))
print("OK")

print("Tests of html_emitting.emit_new_line", end=' ')
#html_emitting.emit_new_line(None)
w = unicode_io.new_string_writer()
html_emitting.emit_new_line(w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("\n"))
print("OK")

print("Tests of html_emitting.emit_start_tag", end=' ')
#html_emitting.emit_start_tag(None,None)
#html_emitting.emit_start_tag(unicoding3_0.string_of("html"),None)
w = unicode_io.new_string_writer()
html_emitting.emit_start_tag(unicoding3_0.string_of("html"),w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("<html>"))
print("OK")

print("Tests of html_emitting.emit_string", end=' ')
#html_emitting.emit_string(None,None)
s = unicoding3_0.new_string()
#html_emitting.emit_string(s,None)
w = unicode_io.new_string_writer()
html_emitting.emit_string(s,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of(""))
s = unicoding3_0.string_of("fred")
w = unicode_io.new_string_writer()
html_emitting.emit_string(s,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("fred"))
print("OK")

print("")
print("All tests OK")

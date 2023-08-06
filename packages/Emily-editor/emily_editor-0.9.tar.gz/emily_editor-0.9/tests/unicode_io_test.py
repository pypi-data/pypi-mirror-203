# Test program for Contractor for Unicode input and output.

# author R.N.Bosworth

# version 27 Feb 2023  16:03

from emily0_9 import unicode_io
from guibits1_0 import unicoding3_0
"""
Copyright (C) 2017,2021,2022,2023  R.N.Bosworth

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

print("Tests of unicode_io.new_input_reader", end=' ')
#r = unicode_io.new_input_reader("motorbike?%&*")
#r = unicode_io.new_input_reader("motorbike")
r = unicode_io.new_input_reader("motorbike.test")
print("OK")

print("Tests of unicode_io.new_string_reader", end=' ')
#r = unicode_io.new_string_reader(None)
#r = unicode_io.new_string_reader("hello")
r = unicode_io.new_string_reader(unicoding3_0.string_of("hello"))
print("OK")

print("Tests of unicode_io.read", end=' ')
r = unicode_io.new_input_reader("motorbike.test")
c = unicode_io.read(r)
assert c == ord('x')
assert unicode_io.read(r) == ord('y')
assert unicode_io.read(r) == ord('z')
assert unicode_io.read(r) == unicode_io.END_OF_STREAM
r = unicode_io.new_string_reader(unicoding3_0.string_of("\u0000a\uffff\U00010000\U0010ffff"))
assert unicode_io.read(r) == 0
assert unicode_io.read(r) == ord('a')
assert unicode_io.read(r) == 0xffff
cp = unicode_io.read(r)
assert cp == 0x10000
assert unicode_io.read(r) == 0x10ffff
assert unicode_io.read(r) == unicode_io.END_OF_STREAM
print("OK")

print("Tests of unicode_io.new_output_writer", end=' ')
#w = unicode_io.new_output_writer(None)
#w = unicode_io.new_output_writer("motorbike?%&*")
w = unicode_io.new_output_writer("pushbike.test")
print("OK")

print("Tests of unicode_io.new_string_writer", end=' ')
w = unicode_io.new_string_writer()
print("OK")

print("Tests of unicode_io.get_string", end=' ')
#s = unicode_io.get_string(None)
w = unicode_io.new_string_writer()
unicode_io.write(ord('b'),w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == ord('b')
print("OK")

print("Tests of unicode_io.write", end=' ')
w = unicode_io.new_output_writer("pushbike.test")
unicode_io.write(ord('x'),w)
unicode_io.write(ord('y'),w)
unicode_io.write(ord('z'),w)
#unicode_io.write(0x110000,w);
unicode_io.write(unicode_io.END_OF_STREAM,w)
#s = unicode_io.get_string(w)
w = unicode_io.new_string_writer()
#unicode_io.write(-2,w);
unicode_io.write(0x0000,w)
unicode_io.write(unicode_io.END_OF_STREAM,w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == 0x0000
w = unicode_io.new_string_writer()
unicode_io.write(ord('a'),w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == ord('a')
w = unicode_io.new_string_writer()
unicode_io.write(0xffff,w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == 0xffff
w = unicode_io.new_string_writer()
unicode_io.write(0x10000,w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == 0x10000
w = unicode_io.new_string_writer()
unicode_io.write(0x10ffff,w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 1
assert unicoding3_0.code_point_at(s,0) == 0x10ffff
#unicode_io.write(0x110000,w);
w = unicode_io.new_string_writer()
unicode_io.write(unicode_io.END_OF_STREAM,w)
s = unicode_io.get_string(w)
assert unicoding3_0.length_of(s) == 0
print("OK")

print("")  
print("All tests OK")

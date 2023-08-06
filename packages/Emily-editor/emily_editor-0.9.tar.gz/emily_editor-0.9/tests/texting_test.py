# Test program for Contractor which exposes a type Text and associated procedures.

# author R.N.Bosworth

# version 27 Feb 2023   15:32

from emily0_9 import texting

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

print("Tests of texting.new_text",end=' ')
t = texting.new_text()
assert len(t._my_text) == 1
assert t._cursor_line == 0
assert t._cursor_char == 0
assert t._modified == False
assert t._first_paragraph == True
t = texting.new_text()
assert len(t._my_text) == 1
assert t._cursor_line == 0
assert t._cursor_char == 0
assert t._modified == False
assert t._first_paragraph == True  
print("OK")

print("Tests of texting.advance", end=' ')
#texting.advance(None)
t = texting.new_text()
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.set_cursor_start(t)
texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.advance(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 0
texting.advance(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 1
texting.advance(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 1
print("OK")

print("Tests of texting.current_code_point", end=' ')
#texting.current_code_point(None)
t = texting.new_text()
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
print("OK")

print("Tests of texting.get_alignment, texting.set_alignment", end=' ')
#texting.get_alignment(None)
t = texting.new_text()
assert texting.get_alignment(t) == texting.Alignment.BEGIN
#texting.set_alignment(None,None)
#texting.set_alignment(t,None)
texting.set_alignment(t,texting.Alignment.MIDDLE)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.insert_code_point(t,ord('\n'))
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.set_alignment(t,texting.Alignment.END)
assert texting.get_alignment(t) == texting.Alignment.END
print("OK")

print("Tests of texting.insert_code_point", end=' ')
#texting.insert_code_point(None,None)
t = texting.new_text()
#texting.insert_code_point(t,None)
#texting.insert_code_point(t,-1)
#texting.insert_code_point(t,0x110000)
assert texting.has_been_modified(t) == False
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
texting.insert_code_point(t,ord('\n'))
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 0
assert texting.has_been_modified(t) == True
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
assert texting.has_been_modified(t) == False
texting.set_cursor(t,0,0)
texting.insert_code_point(t,ord('a'))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
assert texting.has_been_modified(t) == True
texting.set_cursor(t,0,0)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
assert texting.has_been_modified(t) == True
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
texting.set_cursor(t,0,0)
texting.insert_code_point(t,ord('\n'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.set_cursor(t,0,4)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.insert_code_point(t,ord('\n'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.set_cursor(t,0,2)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.insert_code_point(t,ord('\n'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.insert_code_point(t,ord('a'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.set_cursor(t,0,4)
texting.insert_code_point(t,ord('a'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
t = texting.new_text()
texting.set_alignment(t,texting.Alignment.MIDDLE)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.set_cursor(t,0,2)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
texting.insert_code_point(t,ord('a'))
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
print("OK")

print("Tests of texting.set_unmodified, texting.set_modified, texting.has_been_modified", end=' ')
#texting.has_been_modified(None)
t = texting.new_text()
assert texting.has_been_modified(t) == False
texting.set_cursor(t,0,0)
texting.insert_code_point(t,ord('a'))
assert texting.has_been_modified(t) == True
#texting.set_unmodified(None)
texting.set_unmodified(t)
assert texting.has_been_modified(t) == False
#texting.set_modified(None)
texting.set_modified(t)
assert texting.has_been_modified(t) == True
print("OK")

print("Tests of texting._line_length", end=' ')
t = texting.new_text()
assert texting._line_length(t) == 0
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
assert texting._line_length(t) == 0
texting.set_cursor(t,0,2)
assert texting._line_length(t) == 3
print("OK")

print("Tests of texting.set_cursor, texting.cursor_code_point_offset, texting.cursor_line_offset", end=' ')
#texting.set_cursor(None,None,None)
t = texting.new_text()
#texting.set_cursor(t,None,None)
#texting.set_cursor(t,-1,None)
#texting.set_cursor(t,0,None)
#texting.set_cursor(t,0,-1)
texting.set_cursor(t,0,0)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
#texting.set_cursor(t,2,4)
#texting.set_cursor(t,1,4)
texting.set_cursor(t,1,3)
#assert texting.cursor_line_offset(None) == 1
assert texting.cursor_line_offset(t) == 1
#assert texting.cursor_code_point_offset(None) == 3
assert texting.cursor_code_point_offset(t) == 3
t2 = texting.new_text()
texting.set_cursor(t2,0,0)
assert texting.cursor_line_offset(t2) == 0
assert texting.cursor_code_point_offset(t2) == 0
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 3
print("OK")

print("Tests of texting.retreat", end=' ')
#texting.retreat(None)
t = texting.new_text()
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.set_cursor_end(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 1
texting.retreat(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 0
texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
print("OK")

print("Tests of texting.set_cursor_start, texting.set_cursor_end", end=' ')
#texting.set_cursor_start(None)
#texting.set_cursor_end(None)
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 2
texting.set_cursor_start(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
texting.set_cursor_end(t)
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 2
print("OK")

print("Tests of texting.delete_after", end=' ')
#texting.delete_after(None)
t = texting.new_text()
assert texting.has_been_modified(t) == False
texting.set_cursor_start(t)
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 2
assert texting.has_been_modified(t) == True
texting.set_unmodified(t)
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 2
assert texting.has_been_modified(t) == False
texting.set_cursor(t,0,1)
assert texting.delete_after(t) == True
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
texting.advance(t)
assert texting.cursor_line_offset(t) == 1
texting.advance(t)
assert texting.cursor_code_point_offset(t) == 2
texting.advance(t)
assert texting.has_been_modified(t) == True
texting.set_unmodified(t)
texting.set_cursor(t,0,1)
assert texting.delete_after(t) == True
assert texting.delete_after(t) == True
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 3
assert texting.has_been_modified(t) == True
texting.set_unmodified(t)
texting.set_cursor(t,0,1)
assert texting.delete_after(t) == True
assert texting.delete_after(t) == True
assert texting.delete_after(t) == False
assert texting.delete_after(t) == False
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
assert texting.has_been_modified(t) == True
texting.set_unmodified(t)
texting.set_cursor_end(t)
assert texting.delete_after(t) == False
assert texting.delete_after(t) == False
assert texting.delete_after(t) == False
assert texting.delete_after(t) == False
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == texting.END_OF_TEXT
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
assert texting.has_been_modified(t) == False
print("OK")

print("")
print("All tests OK")

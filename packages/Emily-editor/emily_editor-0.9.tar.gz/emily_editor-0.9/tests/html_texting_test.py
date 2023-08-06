# Test of Contractor which allows the client to advance and retreat through HTML # text, as it appears on the screen,
# ignoring tags and dealing with escaped code points.

# author R.N.Bosworth

# version 2 Mar 23  15:12

"""
Copyright (C) 2018,2021,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""

from emily0_9 import html_texting, texting

# test program
# ------------

print("Tests of advance", end=' ')
# assert html_texting.advance(None)
t = texting.new_text()
texting.set_cursor_start(t)
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('1'))
texting.insert_code_point(t,ord('&'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord('2'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('x'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.set_cursor_start(t)
assert html_texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 7
assert html_texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 11
assert html_texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 12
assert html_texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 21
assert not html_texting.advance(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 28
print("OK")

print("Tests of delete_after", end=' ')
#assert html_texting.delete_after(None)
t = texting.new_text()
texting.set_cursor_start(t)
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('1'))
texting.insert_code_point(t,ord('&'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord('2'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('x'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.set_cursor_start(t)
assert html_texting.delete_after(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 6
assert texting.current_code_point(t) == ord('&')
assert html_texting.delete_after(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 6
assert texting.current_code_point(t) == ord('2')
assert html_texting.delete_after(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 6
assert texting.current_code_point(t) == ord('<')
assert html_texting.delete_after(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 14
assert texting.current_code_point(t) == ord('<')
assert not html_texting.delete_after(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 21
assert texting.current_code_point(t) == texting.END_OF_TEXT
print("OK")

print("Tests of retreat", end=' ')
#assert html_texting.retreat(None)
t = texting.new_text()
texting.set_cursor_start(t)
texting.insert_code_point(t,ord('x'))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('1'))
texting.insert_code_point(t,ord('&'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('t'))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord(' '))
texting.insert_code_point(t,ord(';'))
texting.insert_code_point(t,ord('2'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('/'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('y'))
texting.set_cursor_end(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 26
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 25
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 16
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 15
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 14
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 13
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 9
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 8
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 1
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
assert not html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
t = texting.new_text()
texting.set_cursor_start(t)
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('g'))
texting.insert_code_point(t,ord('n'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('x'))
texting.set_cursor_end(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 8
assert html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 7
assert not html_texting.retreat(t)
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
print("OK")

print("")  
print("All tests OK")

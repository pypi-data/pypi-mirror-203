# Test program for Contractor which deals with persistent data for Emily.

import io
import json
import os
from emily0_9 import persisting
from guibits1_0 import type_checking2_0, window_bounding

# author R.N.Bosworth

# version 28 Feb 23  18:29
""" 
Copyright (C) 2016,2017,2018,2021,2022,2023  R.N.Bosworth

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

"""
Run with EmilyPersistents.json not present in user directory,
then with EmilyPersistents.json present in user directory
"""
print("Tests of persisting.get_current_file_name")
p = persisting.get_persistents()
print("  persisting.get_current_file_name(p)="+ \
     str(persisting.get_current_file_name(p)))
print("  If file name non-None re-run test program with EmilyPersistents.json absent from user directory")
assert persisting.get_current_file_name(p) == None
fn = "abc\u00010000\u00010001\u00010002def"
persisting.set_current_file_name(p,fn)
fn2 = persisting.get_current_file_name(p)
assert fn == fn2
print("OK")

print("Tests of persisting.get_menu_font_size", end=' ')
p = persisting.get_persistents()
assert persisting.get_menu_font_size(p) == 16.0
print("OK")

print("Tests of persisting.get_splash_screen_on", end=' ')
p = persisting.get_persistents()
assert persisting.get_splash_screen_on(p) == False
print("OK")

print("Tests of persisting.get_text_font_name", end=' ')
p = persisting.get_persistents()
assert persisting.get_text_font_name(p) == "Times New Roman"
print("OK")

print("Tests of persisting.get_text_font_size", end=' ')
p = persisting.get_persistents()
assert persisting.get_text_font_size(p) == 12.0
print("OK")

print("Tests of persisting.get_window_bounds", end=' ')
p = persisting.get_persistents()
wb = persisting.get_window_bounds(p)
assert window_bounding.get_x(wb) == 72.0
assert window_bounding.get_y(wb) == 72.0
assert window_bounding.get_width(wb) == 576.0
assert window_bounding.get_height(wb) == 288.0
print("OK")

print("Tests of persisting.get_zoom_factor", end=' ')
p = persisting.get_persistents()
assert persisting.get_zoom_factor(p) == 1.0
print("OK")

print("Tests of persisting._save_persistents")
p = persisting.Persistents()
persisting._save_persistents()
input("check EmilyPersistents.json in user's default directory - should be original values")
persisting.set_current_file_name(p,"fred")
persisting.set_zoom_factor(p,100.0)
persisting._save_persistents()
input("check EmilyPersistents.json in user's default directory - should be new values")
print("OK")

print("Tests of persisting.set_current_file_name")
p = persisting.get_persistents()
persisting.set_current_file_name(p,None)
input("check EmilyPersistents.json in user's default directory - current file name should be null")
persisting.set_current_file_name(p,"C:\\")
assert persisting.get_current_file_name(p) == "C:\\"
input("check EmilyPersistents.json in user's default directory - current file name should be \"C:\\\\\"")
print("OK")

print("Tests of persisting.set_menu_font_size")
p = persisting.get_persistents()
persisting.set_menu_font_size(p,18.0)
assert persisting.get_menu_font_size(p) == 18.0
input("check EmilyPersistents.json in user's default directory - menu font size should be 18.0")
print("OK")

print("Tests of persisting.set_splash_screen_on")
p = persisting.get_persistents()
persisting.set_splash_screen_on(p,True)
assert persisting.get_splash_screen_on(p) == True
input("check EmilyPersistents.json in user's default directory - splash screen should be on")
print("OK")

print("Tests of set_text_font_name")
p = persisting.get_persistents()
persisting.set_text_font_name(p,"John Major")
assert persisting.get_text_font_name(p) == "John Major"
input("check EmilyPersistents.json in user's default directory - text font name should be \"John Major\"")
print("OK")

print("Tests of persisting.set_text_font_size")
p = persisting.get_persistents()
persisting.set_text_font_size(p,99.0)
assert persisting.get_text_font_size(p) == 99.0
input("check EmilyPersistents.json in user's default directory - font size should be 99.0")
print("OK")

print("Tests of set_window_bounds")
p = persisting.get_persistents()
wb = window_bounding.new_bounds()
window_bounding.set_x(wb,5.0)
window_bounding.set_y(wb,6.0)
window_bounding.set_width(wb,7.0)
window_bounding.set_height(wb,8.0)
persisting.set_window_bounds(p,wb)
wb2 = persisting.get_window_bounds(p)
assert window_bounding.get_x(wb2) == 5.0
assert window_bounding.get_y(wb2) == 6.0
assert window_bounding.get_width(wb2) == 7.0
assert window_bounding.get_height(wb2) == 8.0
input("check EmilyPersistents.json in user's default directory - window bounds should be 5,6,7,8")
print("OK")

print("Tests of set_zoom_factor")
p = persisting.get_persistents()
persisting.set_zoom_factor(p,2.0)
assert persisting.get_zoom_factor(p) == 2.0
input("check EmilyPersistents.json in user's default directory - zoom factor should be 2.0")
print("OK")

print("Tests of persisting.get_persistents", end=' ')
p = persisting.get_persistents()
assert p != None
g2 = persisting.get_persistents()
assert g2 != None
assert p == g2
print("OK")

print("Tests of paper dimensions", end=' ')
p = persisting.get_persistents()
assert persisting.get_paper_height(p) == 841.0
assert persisting.get_paper_width(p) == 592.0
assert persisting.get_horizontal_indent(p) == 72.0
assert persisting.get_vertical_indent(p) == 72.0
print("OK")

print("")
print("All tests OK")

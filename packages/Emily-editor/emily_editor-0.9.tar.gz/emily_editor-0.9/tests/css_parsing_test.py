# Test program for Contractor for parsing Cascading Style Sheets (simplified syntax!).

# author R.N.Bosworth

# version 9 Mar 2023  15:43

from emily0_9 import css_parsing, looking_ahead
from guibits1_0 import unicoding3_0

""" 
Contractor for parsing Cascading Style Sheets (simplified syntax!).

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

print("Tests of css_parsing._new_style_properties", end=' ')
sp = css_parsing._new_style_properties()
assert len(sp._text_alignment_map) == 0
assert sp._font_name == None
assert sp._font_size == 0.0
print("OK")

print("Tests of css_parsing._parse_dot_name", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("%"))
#css_parsing._parse_dot_name(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("f"))
assert unicoding3_0.equals(css_parsing._parse_dot_name(la),unicoding3_0.string_of("f"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("fred%"))
assert unicoding3_0.equals(css_parsing._parse_dot_name(la),unicoding3_0.string_of("fred"))
assert looking_ahead.current_symbol_of(la) == ord('%')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("fred.jim"))
assert unicoding3_0.equals(css_parsing._parse_dot_name(la),unicoding3_0.string_of("fred.jim"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of css_parsing._parse_text_align_value", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("bollocks"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("left"))
s = css_parsing._parse_text_align_value(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("left"))
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("LEFT"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("RIGHT"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("right"))
s = css_parsing._parse_text_align_value(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("right"))
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("center"))
s = css_parsing._parse_text_align_value(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("center"))
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("CENTER"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("JUSTify"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("just_i_f_y"))
#s = css_parsing._parse_text_align_value(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("justify"))
s = css_parsing._parse_text_align_value(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("justify"))
print("OK")

print("Tests of css_parsing._parse_text_alignment_declaration", end=' ')
m = dict()
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("text-aligm:left"))
#css_parsing._parse_text_alignment_declaration(la,unicoding3_0.string_of("fred.begin"),m);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("text-align:left"))
css_parsing._parse_text_alignment_declaration(la,unicoding3_0.string_of("fred.begin"),m)
assert m["fred.begin"] == "left"
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("text-align   :   justify"))
css_parsing._parse_text_alignment_declaration(la,unicoding3_0.string_of("jim.just"),m)
assert m["jim.just"] == "justify"
print("OK")

print("Tests of css_parsing._is_font_name_char", end=' ')
assert  not css_parsing._is_font_name_char(ord('@'))
assert css_parsing._is_font_name_char(ord('A'))
assert css_parsing._is_font_name_char(ord('Z'))
assert  not css_parsing._is_font_name_char(ord('['))
assert  not css_parsing._is_font_name_char(ord('`'))
assert css_parsing._is_font_name_char(ord('a'))
assert css_parsing._is_font_name_char(ord('z'))
assert  not css_parsing._is_font_name_char(ord('{'))
assert  not css_parsing._is_font_name_char(ord(''))
assert css_parsing._is_font_name_char(ord(' '))
assert  not css_parsing._is_font_name_char(ord('!'))
print("OK")

print("Tests of css_parsing._parse_font_name", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\'\'"))
#s = css_parsing._parse_font_name(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\"\""))
#s = css_parsing._parse_font_name(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\"a\""))
s = css_parsing._parse_font_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("a"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\"a%\""))
#s = css_parsing._parse_font_name(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\"Times Roman\'"))
#s = css_parsing._parse_font_name(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("\"Times Roman\""))
s = css_parsing._parse_font_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("Times Roman"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of css_parsing._parse_font_name_declaration_rest", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("gamily:\"New Century Schoolbook\""))
#s = css_parsing._parse_font_name_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("family;\"New Century Schoolbook\""))
#s = css_parsing._parse_font_name_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("family:\"New Century Schoolbook\""))
s = css_parsing._parse_font_name_declaration_rest(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("New Century Schoolbook"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("family  :  \"Gill Sans\""))
s = css_parsing._parse_font_name_declaration_rest(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("Gill Sans"))
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of css_parsing._is_digit", end=' ')
assert  not css_parsing._is_digit(ord('/'))
assert css_parsing._is_digit(ord('0'))
assert css_parsing._is_digit(ord('9'))
assert  not css_parsing._is_digit(ord(':'))
print("OK")

print("Tests of css_parsing._parse_font_size_declaration_rest", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("tize:0pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size;0pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:/pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:0pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 0.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:9pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 9.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size::pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:1/pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:10pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 10.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:19pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 19.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:1:pt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:99qt"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:99pu"))
#d = css_parsing._parse_font_size_declaration_rest(la);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size:99pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 99.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("size  :  99pt"))
d = css_parsing._parse_font_size_declaration_rest(la)
assert d == 99.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of css_parsing._parse_font_declaration", end=' ')
sp = css_parsing._new_style_properties()
assert sp._font_name == None
assert sp._font_size == 0.0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("gont-family : \"Times New Roman\""))
#css_parsing._parse_font_declaration(la,sp);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("font=family : \"Times New Roman\""))
#css_parsing._parse_font_declaration(la,sp);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("font-family : \"Times New Roman\""))
css_parsing._parse_font_declaration(la,sp)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Times New Roman"))
assert sp._font_size == 0.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("font-size : 42pt"))
css_parsing._parse_font_declaration(la,sp)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Times New Roman"))
assert sp._font_size == 42.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("font-blob : \"blobbie\""))
#css_parsing._parse_font_declaration(la,sp);
print("OK")

print("Tests of css_parsing._parse_declaration", end=' ')
sp = css_parsing._new_style_properties()
assert sp._font_name == None
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("font-family : \"Times New Roman\""))
css_parsing._parse_declaration(la,sp,unicoding3_0.string_of("body"))
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Times New Roman"))
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("text-align:left"))
css_parsing._parse_declaration(la,sp,unicoding3_0.string_of("p.begin"))
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Times New Roman"))
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 1
assert sp._text_alignment_map["p.begin"] == "left"
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("complete-load-of-rubbish"))
#css_parsing._parse_declaration(la,sp,unicoding3_0.string_of("p.end"));
print("OK")

print("Tests of css_parsing._parse_declaration_block", end=' ')
sp = css_parsing._new_style_properties()
s = unicoding3_0.string_of("fred")
assert sp._font_name == None
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("[  font-family:\"Times New Roman\"}"))
#css_parsing._parse_declaration_block(la,sp,s);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{  zont-family:\"Times New Roman\"}"))
#css_parsing._parse_declaration_block(la,sp,s);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{  font-family:\"Times New Roman\"  ]"))
#css_parsing._parse_declaration_block(la,sp,s);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{  font-family:\"Times New Roman\"  }"))
#css_parsing._parse_declaration_block(la,sp,s);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{font-family:\"Times New Roman\";}"))
css_parsing._parse_declaration_block(la,sp,s)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Times New Roman"))
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{  font-family:\"Times New Roman\"  ;   font-family:\"Palatino\"  }"))
#css_parsing._parse_declaration_block(la,sp,s);
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("{  font-family:\"Times New Roman\"  ;   font-family:\"Palatino\"  ;  }"))
css_parsing._parse_declaration_block(la,sp,s)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Palatino"))
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("" + "{\n" + "  font-family:\"Times New Roman\";\n" + "  font-size:10pt;\n" + "  font-family:\"Palatino\";\n" + "  font-size:20pt;\n" + "  text-align:left;\n" + "  text-align:center;\n" + "}"))
css_parsing._parse_declaration_block(la,sp,s)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Palatino"))
assert sp._font_size == 20.0
assert len(sp._text_alignment_map) == 1
assert sp._text_alignment_map["fred"] == "center"
print("OK")

print("Tests of css_parsing._parse_rule", end=' ')
sp = css_parsing._new_style_properties()
assert sp._font_name == None
assert sp._font_size == 0.0
assert len(sp._text_alignment_map) == 0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("p.begin   {font-family:\"Palatino\";font-size:40pt;text-align:left;}  "))
css_parsing._parse_rule(la,sp)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Palatino"))
assert sp._font_size == 40.0
assert len(sp._text_alignment_map) == 1
assert sp._text_alignment_map["p.begin"] == "left"
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("p.end{text-align:right;}"))
css_parsing._parse_rule(la,sp)
assert unicoding3_0.equals(sp._font_name,unicoding3_0.string_of("Palatino"))
assert sp._font_size == 40.0
assert len(sp._text_alignment_map) == 2
assert sp._text_alignment_map["p.begin"] == "left"
assert sp._text_alignment_map["p.end"] == "right"
print("OK")

print("Tests of parse_style_sheet, font_name_of, font_size_of", end=' ')
#sp = css_parsing.parse_style_sheet(None)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("      "))
sp = css_parsing.parse_style_sheet(la)
#assert unicoding3_0.equals(css_parsing.font_name_of(None),unicoding3_0.string_of("Times New Roman"))
assert unicoding3_0.equals(css_parsing.font_name_of(sp),unicoding3_0.string_of("Times New Roman"))
#assert css_parsing.font_size_of(None) == 12.0
assert css_parsing.font_size_of(sp) == 12.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("  p{font-size:10pt;}  p{font-size:8pt;}  "))
sp = css_parsing.parse_style_sheet(la)
assert unicoding3_0.equals(css_parsing.font_name_of(sp),unicoding3_0.string_of("Times New Roman"))
assert css_parsing.font_size_of(sp) == 8.0
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of css_parsing.alignment_of", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("p.end{text-align:right;}"))
sp = css_parsing.parse_style_sheet(la)
#assert unicoding3_0.equals(css_parsing.alignment_of(None,unicoding3_0.string_of("p.end")),unicoding3_0.string_of("right"))
#assert unicoding3_0.equals(css_parsing.alignment_of(sp,None),unicoding3_0.string_of("right"))
assert unicoding3_0.equals(css_parsing.alignment_of(sp,unicoding3_0.string_of("p.end")),unicoding3_0.string_of("right"))
assert unicoding3_0.equals(css_parsing.alignment_of(sp,unicoding3_0.string_of("p")),unicoding3_0.string_of("left"))
print("OK")

print("")
print("All tests OK")

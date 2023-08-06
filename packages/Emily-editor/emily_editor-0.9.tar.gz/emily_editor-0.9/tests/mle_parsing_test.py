# Test program for Contractor which parses an mle file via a code point lookahead to produce an Emily text.

# author R.N.Bosworth

# version 13 Mar 23  12:27

from guibits1_0 import font_styling, unicoding3_0
from emily0_9 import css_parsing, looking_ahead, mle_parsing, texting, unicode_io

""" 
Copyright (C) 2012,2015,2016,2017,2018,2019,2021,2023  R.N.Bosworth

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

print ("Tests of mle_parsing._new_mle_result", end=' ')
mler = mle_parsing._new_mle_result()
assert mler._my_style_properties == None
assert mler._my_text == None
print ("OK")

fss = font_styling.new_font_styles()
print("Tests of mle_parsing._parse_doctype", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(">!doctype html>"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<£doctype html"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctypf html>"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctypehtml>"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype   htmm>"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype   html   <"))
#mle_parsing._parse_doctype(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype   html   >"))
mle_parsing._parse_doctype(la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype html>"))
mle_parsing._parse_doctype(la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._emit_hard_line_break", end=' ')
t = texting.new_text()
mle_parsing._emit_hard_line_break(t)
assert texting.cursor_code_point_offset(t) == 0
assert texting.cursor_line_offset(t) == 1
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_meta_tag", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(">meta charset=\"UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<beta charset=\"UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<metacharset=\"UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta   charabanc=\"UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   -    \"UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   =    \'UTF-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   =    \"UTE-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   =    \"UTF-8\'>"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   =    \"UTF-8\"<"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset   =    \"utf-8\">"))
#mle_parsing._parse_meta_tag(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<meta charset=\"UTF-8\">"))
mle_parsing._parse_meta_tag(la)
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_class_name", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("start"))
#s = mle_parsing._parse_class_name(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("begin"))
s = mle_parsing._parse_class_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("begin"))
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("middle"))
s = mle_parsing._parse_class_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("middle"))
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("end"))
s = mle_parsing._parse_class_name(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("end"))
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_class_attribute", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("form=\"middle\""))
#s = mle_parsing._parse_class_attribute(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class   -   \"middle\""))
#s = mle_parsing._parse_class_attribute(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class   =   'middle'"))
#s = mle_parsing._parse_class_attribute(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class   =   \"moddle\""))
#s = mle_parsing._parse_class_attribute(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class   =   \"middle'"))
#s = mle_parsing._parse_class_attribute(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class   =   \"middle\""))
s = mle_parsing._parse_class_attribute(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("middle"))
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("class=\"begin\""))
s = mle_parsing._parse_class_attribute(la)
assert unicoding3_0.equals(s,unicoding3_0.string_of("begin"))
assert looking_ahead.current_symbol_of(la) == unicode_io.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_head_element", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<title></title>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head></head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  </head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-7\">"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title>  </head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title></title>  </title>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title></title>  </head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title></title>  <stylf>  </style>  </head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title></title>  <style>  </styld>  </head>"))
#fp = mle_parsing._parse_head_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title>alchemist of the year</title>  <style>  </style>  </head>"))
fp = mle_parsing._parse_head_element(la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(css_parsing.font_name_of(fp),unicoding3_0.string_of("Times New Roman"))
assert css_parsing.font_size_of(fp) == 12.0
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<head>  <meta charset=\"UTF-8\">  <title>fred</title>  <style>  body  {font-size:66pt;}  </style>  </head>"))
fp = mle_parsing._parse_head_element(la)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(css_parsing.font_name_of(fp),unicoding3_0.string_of("Times New Roman"))
assert css_parsing.font_size_of(fp) == 66.0
print("OK")

print("Tests of mle_parsing._parse_paragraph_text", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 0
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<br><bq>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("bq"))
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 0
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<br>a<bs>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("bs"))
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 1
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("a<br>&lt;b</p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 1
assert texting.cursor_code_point_offset(t) == 5
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('&')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('t')
texting.advance(t)
assert texting.current_code_point(t) == ord(';')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("ab</p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 2
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("a b</p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 3
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("a  b</p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 3
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("a \t b   cd   </p>"))
pa = texting.Alignment.MIDDLE
t = texting.new_text()
current_tag = mle_parsing._parse_paragraph_text(la,pa,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert unicoding3_0.equals(current_tag,unicoding3_0.string_of("/p"))
assert texting.cursor_line_offset(t) == 0
assert texting.cursor_code_point_offset(t) == 6
texting.set_cursor_start(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('b')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('c')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_paragraph_or_break", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of(">p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<q>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<bt>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<br   <"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<br   >"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p></p>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p>hello</q>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p>hello</p>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p   >hello</p>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p   clunk>hello</p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p   class   =   \"middle\"   <hello</p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p   class   =   \"justify\"   >hello</p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<pclass=\"middle\">hello</p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p class=\"end\">hello<br>world</p>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('w')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p class=\"end\">hello</p><br>world"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == ord('<')
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == ord('w')
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.END
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
assert looking_ahead.current_symbol_of(la) == ord('w')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p class=\"middle\">hello</p>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p class=\"muddle\">hello</p>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<p   class   =   \"begin\"   >   hello   </p   >"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == False
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</cody>"))
t = texting.new_text()
#end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("</body>"))
t = texting.new_text()
end_of_body = mle_parsing._parse_paragraph_or_break(la,t)
assert end_of_body == True
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of mle_parsing._parse_body_element", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<cody>  </body>"))
t = texting.new_text()
#mle_parsing._parse_body_element(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<body>  </aody>"))
#mle_parsing._parse_body_element(la,t)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<body>  </body>"))
t = texting.new_text()
mle_parsing._parse_body_element(la,t)
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<body></body>"))
t = texting.new_text()
mle_parsing._parse_body_element(la,t)
texting.set_cursor(t,0,0)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<body>  <br>  <p class = \"middle\">    first  para  </p>  <br>  <p>  1 &lt; 2 &amp; 2 &lt; 3  </p>  <br>  </body>"))
t = texting.new_text()
mle_parsing._parse_body_element(la,t)
assert looking_ahead.current_symbol_of(la) == looking_ahead.END_OF_STREAM
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('f')
texting.advance(t)
assert texting.current_code_point(t) == ord('i')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('s')
texting.advance(t)
assert texting.current_code_point(t) == ord('t')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('p')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.MIDDLE
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('1')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('&')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('t')
texting.advance(t)
assert texting.current_code_point(t) == ord(';')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('2')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('&')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('m')
texting.advance(t)
assert texting.current_code_point(t) == ord('p')
texting.advance(t)
assert texting.current_code_point(t) == ord(';')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('2')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('&')
texting.advance(t)
assert texting.current_code_point(t) == ord('l')
texting.advance(t)
assert texting.current_code_point(t) == ord('t')
texting.advance(t)
assert texting.current_code_point(t) == ord(';')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('3')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of _parse_html_element, font_name_of, font_size_of, text_of", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<htmm><head><meta charset=\"UTF-8\"><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"))
#r = mle_parsing._parse_html_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html><head><meta charset=\"UTF-8\"><title>Your Grace</title><style></style></head><body><p>A word.</p></body></htmk>"))
#r = mle_parsing._parse_html_element(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html><head><meta charset=\"UTF-8\"><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"))
r = mle_parsing._parse_html_element(la)
#assert unicoding3_0.equals(mle_parsing.font_name_of(None),unicoding3_0.string_of("Times New Roman"))
assert unicoding3_0.equals(mle_parsing.font_name_of(r),unicoding3_0.string_of("Times New Roman"))
#assert mle_parsing.font_size_of(None) == 12.0
assert mle_parsing.font_size_of(r) == 12.0
t = mle_parsing.text_of(r)
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('A')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('w')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('.')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html><head><meta charset=\"UTF-8\"><title>Your Grace</title><style>body{font-size:14pt;}</style></head><body><p>A word.</p></body></html>"))
r = mle_parsing._parse_html_element(la)
assert unicoding3_0.equals(mle_parsing.font_name_of(r),unicoding3_0.string_of("Times New Roman"))
assert mle_parsing.font_size_of(r) == 14.0
#t = mle_parsing.text_of(None)
t = mle_parsing.text_of(r)
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('A')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('w')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('.')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<html>  <head>  <meta   charset=\"UTF-8\">  <title>Your Grace</title>  <style>  body  {font-size:  16pt  ;  }  body {font-family: \"Courier New\"  ;  }  </style>  </head>  <body>  <p>  A phrase.  </p>  </body>  </html>  "))
r = mle_parsing._parse_html_element(la)
assert unicoding3_0.equals(mle_parsing.font_name_of(r),unicoding3_0.string_of("Courier New"))
assert mle_parsing.font_size_of(r) == 16.0
t = mle_parsing.text_of(r)
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('A')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('p')
texting.advance(t)
assert texting.current_code_point(t) == ord('h')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('a')
texting.advance(t)
assert texting.current_code_point(t) == ord('s')
texting.advance(t)
assert texting.current_code_point(t) == ord('e')
texting.advance(t)
assert texting.current_code_point(t) == ord('.')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of parse_mle_document, alignment_of", end=' ')
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype word><html><head><meta charset=\"UTF-8\"><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"))
#r = mle_parsing.parse_mle_document(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype html><itml><head><meta charset=\"UTF-8\"><title>Your Grace</title><style></style></head><body><p>A word.</p></body></html>"))
#r = mle_parsing.parse_mle_document(la)
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("<!doctype html><html><head><meta charset=\"UTF-8\"><title>Your Grace</title><style>p {text-align: left;} p.begin {text-align: left;} p.middle {text-align: center;} p.end {text-align: right;}</style></head><body><p>A word.</p></body></html>"))
r = mle_parsing.parse_mle_document(la)
assert unicoding3_0.equals(mle_parsing.font_name_of(r),unicoding3_0.string_of("Times New Roman"))
assert mle_parsing.font_size_of(r) == 12.0
#assert unicoding3_0.equals(mle_parsing.alignment_of(None,None),unicoding3_0.string_of("right"))
#assert unicoding3_0.equals(mle_parsing.alignment_of(r,None),unicoding3_0.string_of("right"))
assert unicoding3_0.equals(mle_parsing.alignment_of(r,unicoding3_0.string_of("p.end")),unicoding3_0.string_of("right"))
assert unicoding3_0.equals(mle_parsing.alignment_of(r,unicoding3_0.string_of("p")),unicoding3_0.string_of("left"))
assert unicoding3_0.equals(mle_parsing.alignment_of(r,unicoding3_0.string_of("p.begin")),unicoding3_0.string_of("left"))
assert unicoding3_0.equals(mle_parsing.alignment_of(r,unicoding3_0.string_of("p.middle")),unicoding3_0.string_of("center"))
t = mle_parsing.text_of(r)
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('A')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('w')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('.')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
la = looking_ahead.lookahead_of_string(unicoding3_0.string_of("  <!doctype html>  <html>  <head>  <meta   charset=\"UTF-8\">  <title>Your Grace</title>  <style>  body  { font-family  :  \"Helvetica\"  ;  }  body  {  font-size  :  2pt  ;  }  </style>  </head>  <body>  <p>A word.</p>  </body>  </html>  "))
r = mle_parsing.parse_mle_document(la)
assert unicoding3_0.equals(mle_parsing.font_name_of(r),unicoding3_0.string_of("Helvetica"))
assert mle_parsing.font_size_of(r) == 2.0
t = mle_parsing.text_of(r)
texting.set_cursor_start(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == ord('A')
texting.advance(t)
assert texting.current_code_point(t) == ord(' ')
texting.advance(t)
assert texting.current_code_point(t) == ord('w')
texting.advance(t)
assert texting.current_code_point(t) == ord('o')
texting.advance(t)
assert texting.current_code_point(t) == ord('r')
texting.advance(t)
assert texting.current_code_point(t) == ord('d')
texting.advance(t)
assert texting.current_code_point(t) == ord('.')
texting.advance(t)
assert texting.current_code_point(t) == ord('\n')
texting.advance(t)
assert texting.get_alignment(t) == texting.Alignment.BEGIN
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
texting.advance(t)
assert texting.current_code_point(t) == looking_ahead.END_OF_STREAM
print("OK")  

print("")
print("All tests OK")

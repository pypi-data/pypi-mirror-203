# Test program for Contractor which renders a text and a cursor on a page on a screen.

# author R.N.Bosworth

# version 6 Feb 23  14:15

from emily0_9 import page_laying_out, rendering, texting
from guibits1_0 import coloring, cursoring, font_styling, painting
from guibits1_0 import unicoding3_0, windowing, writing

"""
Copyright (C) 2018,2019,2021,2022,2023  R.N.Bosworth

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
from guibits1_0 import coloring
from guibits1_0 import cursoring
from guibits1_0 import font_styling
import page_laying_out
from guibits1_0 import painting
import rendering
import texting
from guibits1_0 import unicoding3_0
from guibits1_0 import windowing
from guibits1_0 import writing
"""

def _print_pos(curpos):
  print("    curpos._start_text_position.line_offset=" + str(curpos._start_text_position.line_offset))
  print("    curpos._start_text_position.code_point_offset=" + str(curpos._start_text_position.code_point_offset))
  print("    curpos._end_text_position.line_offset=" + str(curpos._end_text_position.line_offset))
  print("    curpos._end_text_position.code_point_offset=" + str(curpos._end_text_position.code_point_offset))
  print("    curpos._start_page_position.x_offset=" + str(curpos._start_page_position.x_offset))
  print("    curpos._start_page_position.y_offset=" + str(curpos._start_page_position.y_offset))
  print("    curpos._end_page_position.x_offset=" + str(curpos._end_page_position.x_offset))
  print("    curpos._end_page_position.y_offset=" + str(curpos._end_page_position.y_offset))
  print("    curpos._desired_x_offset=" + str(curpos._desired_x_offset))
  print("    curpos._update_x_offset=" + str(curpos._update_x_offset))
  print("    curpos._start_x_offset=" + str(curpos._start_x_offset))
  print("    curpos._end_x_offset=" + str(curpos._end_x_offset))
  print("    curpos._in_fat_cursor=" + str(curpos._in_fat_cursor))
  print("    curpos._cursor_rectangle_pending=" + str(curpos._cursor_rectangle_pending))
   

def window_closing(win):
  if win._tnum == 0:
  
    print("Tests of new_page", end=' ')
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    assert pg._text_width == 144.0
    assert pg._text_height == 144.0
    assert unicoding3_0.length_of(pg._current_line) == 0
    assert pg._line_width == 0.0
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._font_name == "Courier New"
    assert  not font_styling.contains(pg._font_styles,font_styling.FontStyle.BOLD)
    assert  not font_styling.contains(pg._font_styles,font_styling.FontStyle.ITALIC)
    assert pg._font_size == 12.0
    assert pg._text_color == coloring.BLACK
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert pg._EOT_position.x_offset == 0.0
    assert pg._EOT_position.y_offset == 0.0
    assert pg._line_list == [(0.0,"")]
    assert pg._back_map == [[(0,0)]]
    print("OK")
    
    print("Tests of horizontal advance")
    fss = font_styling. new_font_styles()
    single_f = "f"
    single_f_width = writing.width_in_points_of(win,single_f,"Times New Roman",fss,24.0)
    print("  single_f_width="+str(single_f_width))
    double_f = "ff"
    double_f_width = writing.width_in_points_of(win,double_f,"Times New Roman",fss,24.0)
    print("  double_f_width="+str(double_f_width))
    test_string = "ffffffffffff"
    print("  test_string="+test_string)
    width_in_points = writing.width_in_points_of(win,test_string,"Times New Roman",fss,24.0)
    print("  width_in_points="+str(width_in_points))
    rendered_width_in_points = writing.write_string(win,test_string,"Times New Roman",fss,24.0,0.0,0.0,coloring.BLACK)
    print("  rendered_width_in_points="+str(rendered_width_in_points))
    print("OK")

    print("Tests of start_page_line_of", end=' ')
    curpos = rendering.new_cursor_position()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos._start_page_position.x_offset = 5.0  
    curpos._start_page_position.y_offset = 24.0
    assert rendering.start_page_line_of(curpos,pg) == 2   
    print("OK")
  
    print("Tests of start_page_line_of_back", end=' ')
    curpos = rendering.new_cursor_position()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos._start_page_position.x_offset = 5.0  
    curpos._start_page_position.y_offset = 24.0
    assert rendering.start_page_line_of_back(curpos,pg) == 1    
    curpos._start_page_position.y_offset = 12.0
    assert rendering.start_page_line_of_back(curpos,pg) == 0   
    curpos._start_page_position.y_offset = 0.0
    assert rendering.start_page_line_of_back(curpos,pg) == 0   
    print("OK")
  
    print("Tests of _fix_cursor_position", end=' ')
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset =  -1
    curpos._start_text_position.code_point_offset =  -1
    curpos._end_text_position.line_offset =  -1
    curpos._end_text_position.code_point_offset =  -1
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_page_position.x_offset == -1.0
    assert curpos._start_page_position.y_offset == -1.0
    assert curpos._end_page_position.x_offset == -1.0
    assert curpos._end_page_position.y_offset == -1.0
    assert curpos._start_x_offset == -1.0
    assert curpos._end_x_offset == -1.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False

    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 1
    pg._current_line = unicoding3_0.string_of("f")
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 2
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert curpos._start_page_position.x_offset == -1.0
    assert curpos._start_page_position.y_offset == -1.0
    assert curpos._end_page_position.x_offset == -1.0
    assert curpos._end_page_position.y_offset == -1.0
    assert curpos._start_x_offset == -1.0
    assert curpos._end_x_offset == -1.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False

    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 1
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 1
    pg._page_position.x_offset = 7.2
    pg._page_position.y_offset = 0.0
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2)
    assert curpos._start_page_position.y_offset == 0.0
    assert rendering._equals_float(curpos._end_page_position.x_offset,7.2)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._start_x_offset == -1.0
    assert curpos._end_x_offset == -1.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
 
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 2
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 2
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_page_position.x_offset == -1.0
    assert curpos._end_page_position.y_offset == -1.0
    assert rendering._equals_float(curpos._start_x_offset,7.2)
    assert curpos._end_x_offset == -1.0
    assert curpos._in_fat_cursor == True
    assert curpos._cursor_rectangle_pending == False
 
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 2
    pg._current_line = unicoding3_0.string_of("ff")
    pg._page_position.x_offset = 14.4
    pg._page_position.y_offset = 0.0
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 2
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2)
    assert curpos._start_page_position.y_offset == 0.0
    assert rendering._equals_float(curpos._end_page_position.x_offset,14.4)
    assert curpos._end_page_position.y_offset == 0.0
    assert rendering._equals_float(curpos._start_x_offset,7.2)
    assert rendering._equals_float(curpos._end_x_offset,14.4)
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == True

    curpos = rendering.new_cursor_position()  # everything undefined
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == -1
    assert curpos._start_text_position.code_point_offset == -1
    assert curpos._end_text_position.line_offset == -1
    assert curpos._end_text_position.code_point_offset == -1
    assert rendering._equals_float(curpos._start_page_position.x_offset,-1.0)
    assert curpos._start_page_position.y_offset == -1.0
    assert rendering._equals_float(curpos._end_page_position.x_offset,-1.0)
    assert curpos._end_page_position.y_offset == -1.0
    assert rendering._equals_float(curpos._start_x_offset,-1.0)
    assert rendering._equals_float(curpos._end_x_offset,-1.0)
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False

    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 3
    curpos._start_page_position.x_offset = 7.2
    curpos._start_page_position.y_offset = 0.0
    curpos._end_page_position.x_offset =  -1.0
    curpos._end_page_position.y_offset =  -1.0
    curpos._start_x_offset = 7.2
    curpos._end_x_offset = -1.0
    curpos._in_fat_cursor = True
    curpos._cursor_rectangle_pending = False
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 2
    pg._current_line = unicoding3_0.string_of("ff")
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 3
    assert curpos._end_page_position.x_offset == -1.0
    assert curpos._end_page_position.y_offset == -1.0

    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 3
    pg._current_line = unicoding3_0.string_of("fff")
    rendering._fix_cursor_position(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 3
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2)
    assert curpos._start_page_position.y_offset == 0.0
    assert rendering._equals_float(curpos._end_page_position.x_offset,21.6)
    assert curpos._end_page_position.y_offset == 0.0
    assert rendering._equals_float(curpos._start_x_offset,7.2)
    assert rendering._equals_float(curpos._end_x_offset,21.6)
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == True
    
    print("OK")
        
    print("Tests of rendering._render_glyph",end=' ')
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 1  # i.e. we've just read 'a'
    pg._current_line = unicoding3_0.new_string()
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 1
    rendering._render_glyph(ord('a'),curpos,pg)
    assert unicoding3_0.equals(pg._current_line,unicoding3_0.string_of('a')) 
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2) 
    assert rendering._equals_float(curpos._start_page_position.y_offset,0.0) 
    assert rendering._equals_float(curpos._end_page_position.x_offset,7.2) 
    assert rendering._equals_float(curpos._end_page_position.y_offset,0.0) 
    print("OK")

    print("Test of _update_back_map",end=' ')
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    assert len(pg._back_map) == 1
    assert len(pg._back_map[0]) == 1
    assert pg._back_map[0][0] ==(0,0)
    pg._current_line = unicoding3_0.string_of("a")
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 1
    pg._page_position.y_offset = 0.0
    rendering._update_back_map(pg)
    assert len(pg._back_map) == 1
    assert len(pg._back_map[0]) == 2
    assert pg._back_map[0][0] ==(0,0)
    assert pg._back_map[0][1] ==(0,1)
   
    pg._current_line = unicoding3_0.string_of("")
    pg._text_position.line_offset = 1
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 12.0
    rendering._update_back_map(pg)
    assert len(pg._back_map) == 2
    assert len(pg._back_map[0]) == 2
    assert pg._back_map[0][0] ==(0,0)
    assert pg._back_map[0][1] ==(0,1)
    assert len(pg._back_map[1]) == 1
    assert pg._back_map[1][0] == (1,0)

    pg._current_line = unicoding3_0.string_of("b")
    pg._text_position.line_offset = 1
    pg._text_position.code_point_offset = 1
    pg._page_position.y_offset = 12.0
    rendering._update_back_map(pg)
    assert len(pg._back_map) == 2
    assert len(pg._back_map[0]) == 2
    assert pg._back_map[0][0] ==(0,0)
    assert pg._back_map[0][1] ==(0,1)
    assert len(pg._back_map[1]) == 2
    assert pg._back_map[1][0] == (1,0)
    assert pg._back_map[1][1] == (1,1)
    print("OK")

    print("Tests of _de_escape", end=' ')
    curpos = rendering.new_cursor_position()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    s = unicoding3_0.new_string()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    rendering._de_escape(s,curpos,pg)
    assert unicoding3_0.length_of(pg._current_line) == 0
    assert len(pg._back_map) == 1
    assert pg._back_map[0][0] == (0,0)    
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0

    pg._current_line = unicoding3_0.string_of("ab")
    pg._text_position.line_offset = 1
    pg._text_position.code_point_offset = 2
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 12.0
    pg._back_map.append([])
    pg._back_map[1].append((1,0))
    pg._back_map[1].append((1,1))
    pg._back_map[1].append((1,2))
    s = unicoding3_0.string_of("1&lt;2")
    curpos._start_text_position.line_offset = 1
    curpos._start_text_position.code_point_offset = 3
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 7
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._de_escape(s,curpos,pg)
    assert unicoding3_0.length_of(pg._current_line) == 5  # "ab1<2"
    assert len(pg._back_map) == 2
    assert pg._back_map[1][0] == (1,0)
    assert pg._back_map[1][1] == (1,1)
    assert pg._back_map[1][2] == (1,2)
    assert pg._back_map[1][3] == (1,3)
    assert pg._back_map[1][4] == (1,7)
    assert pg._back_map[1][5] == (1,8)
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 3
    assert rendering._equals_float(curpos._start_page_position.x_offset,21.6)
    assert curpos._start_page_position.y_offset == 12.0
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 7
    assert rendering._equals_float(curpos._end_page_position.x_offset,28.8)
    assert curpos._end_page_position.y_offset == 12.0
    print("OK")
    
    def _equals_pos(pos1,lo2,go2,xoff2,yoff2):
      (lo1,go1,xoff1,yoff1) = pos1
      return lo1 == lo2 and go1 == go2 and \
                    rendering._equals_float(xoff1,xoff2) and \
                    rendering._equals_float(yoff1,yoff2)
    
    print("Tests of nearest_glyph_interstice_of",end=' ')
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._line_list = [(0.0,"")]
    assert rendering.nearest_glyph_interstice_of(0.0,24.0,pg) == (0,0,0.0,0.0)
    assert rendering.nearest_glyph_interstice_of(0.0,12.0,pg) == (0,0,0.0,0.0)
    assert rendering.nearest_glyph_interstice_of(0.0,0.0,pg) == (0,0,0.0,0.0)
    assert rendering.nearest_glyph_interstice_of(0.0,-12.0,pg) == (0,0,0.0,0.0)
    pg._line_list = [(0.0,""),(72.0,"frodo")] # text 36 points (0.5")wide at 1" indent
    assert rendering.nearest_glyph_interstice_of(0.0,6.0,pg) == (0,0,0.0,0.0)
    assert rendering.nearest_glyph_interstice_of(10.0,6.0,pg) == (0,0,0.0,0.0)
    assert rendering.nearest_glyph_interstice_of(0.0,18.0,pg) == (1,0,72.0,12.0)
    assert rendering.nearest_glyph_interstice_of(71.9,18.0,pg) == (1,0,72.0,12.0)
    assert rendering.nearest_glyph_interstice_of(72.0,18.0,pg) == (1,0,72.0,12.0)
    assert rendering.nearest_glyph_interstice_of(72.1,18.0,pg) == (1,0,72.0,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(120.0,18.0,pg),1,5,108.0,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(108.1,18.0,pg),1,5,108.0,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(108.0,18.0,pg),1,5,108.0,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(107.9,18.0,pg),1,5,108.0,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(104.3,18.0,pg),1,4,100.8,12.0)
    assert _equals_pos(rendering.nearest_glyph_interstice_of(90.0,18.0,pg),1,2,86.4,12.0)
    print("OK")
    
    print("Tests of move_cursor_down",end=' ')
    #rendering.move_cursor_down(None,None)
    curpos = rendering.new_cursor_position()
    #rendering.move_cursor_down(curpos,None)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,288.0,180.0,72.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._page_position.y_offset = 36.0
    curpos._end_page_position.y_offset = 24.0
    assert not rendering.move_cursor_down(curpos,pg)  # off visible text
    
    pg = rendering.new_page(win,288.0,192.0,72.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._line_list = [(0.0,"In Xanadu did Kubla"),(0.0,"Khan"),(0.0,"A stately pleasure"),(0.0,"dome decree")]
    pg._back_map = [[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19)],
                     [(0,20),(0,21),(0,22),(0,23),(0,24)],
                     [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18)],
                     [(1,19),(1,20),(1,21),(1,22),(1,23),(1,24),(1,25),(1,26),(1,27),(1,28),(1,29),(1,30)]]
    pg._page_position.y_offset = 36.0
    curpos._end_page_position.y_offset = 36.0
    assert not rendering.move_cursor_down(curpos,pg)  # off end of text
    
    curpos._end_page_position.y_offset = 24.0  # third line of page
    curpos._desired_x_offset = 129.6  # end of third line of page
    curpos._update_x_offset = False
    assert rendering.move_cursor_down(curpos,pg)
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 30  # end of second line of text
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 30  # end of second line of text
    
    curpos._end_page_position.y_offset = 24.0  # third line of page
    curpos._desired_x_offset = 28.8  # glyph interstice 4 on third line of page    
    curpos._update_x_offset = False
    assert rendering.move_cursor_down(curpos,pg)
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 23  
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 23  
    # code point 23 of second line of text
    
    print("OK")
   
    print("Tests of move_cursor_up", end=' ')
    #rendering.move_cursor_up(None,None)
    curpos = rendering.new_cursor_position()
    #rendering.move_cursor_up(curpos,None)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,288.0,192.0,72.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._line_list = [(0.0,"In Xanadu did Kubla"),(0.0,"Khan"),(0.0,"A stately pleasure"),(0.0,"dome decree")]
    pg._back_map = [[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19)],
                     [(0,20),(0,21),(0,22),(0,23),(0,24)],
                     [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18)],
                     [(1,19),(1,20),(1,21),(1,22),(1,23),(1,24),(1,25),(1,26),(1,27),(1,28),(1,29),(1,30)]]
    pg._page_position.y_offset = 36.0  # last line of page (but not relevant)
    curpos._start_page_position.y_offset = 11.9  # just above second line of page
    assert not rendering.move_cursor_up(curpos,pg)

    curpos._start_page_position.y_offset = 12.0  # on second line of page
    curpos._desired_x_offset = 28.8  # glyph interstice 4 on second line of page
    curpos._update_x_offset = False
    assert rendering.move_cursor_up(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 4
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 4
    # glyph interstice 4 on first line of page
    
    curpos._start_page_position.y_offset = 12.0  # second line of page
    curpos._desired_x_offset = 36.0  # beyond end of second line    
    curpos._update_x_offset = False
    assert rendering.move_cursor_up(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 5  
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 5  
    # glyph interstice 5 on first line of page
    print("OK")

    print("Tests of set_text_font_name", end=' ')
    #rendering.set_text_font_name(None,None)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    assert pg._font_name == "Courier New"
    #rendering.set_text_font_name(pg,None)
    rendering.set_text_font_name(pg,"Times New Roman")
    assert pg._font_name == "Times New Roman"
    print("OK")
  
    print("Tests of set_text_font_size", end=' ')
    #rendering.set_text_font_size(None,None)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    assert pg._font_size == 12.0
    #rendering.set_text_font_size(pg,None)
    rendering.set_text_font_size(pg,43.7)
    assert pg._font_size == 43.7
    print("OK")
  
    win._tnum += 1
    return False

  elif win._tnum == 1:
    print("Tests of render_thin_cursor")
    windowing.clear(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  page dimensions 3.0\" by 4.0\"")
    print("  page with text origin at (36,72) (0.5\", 1.0\")")
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 1
    print("  fat cursor - should not appear")
    rendering.render_thin_cursor(curpos,pg)
    input("  Please enter NL:")
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    print("  thin cursor at (-1.0,-1.0) in the rendered text")
    #rendering.render_thin_cursor(curpos,pg)
    input("  Please enter NL:")
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    rendering.render_thin_cursor(curpos,pg)
    print("  cursor rendered at (0,0) in the rendered text")
    win._tnum += 1
    return False

  elif win._tnum == 2:
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 36.0
    curpos._start_page_position.y_offset = 72.0
    curpos._end_page_position.x_offset = 36.0
    curpos._end_page_position.y_offset = 72.0
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    rendering.render_thin_cursor(curpos,pg)
    print("  cursor rendered at (36,72) in the rendered text")
    win._tnum += 1
    return False

  elif win._tnum == 3:
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 36.0
    curpos._start_page_position.y_offset = 133.0
    curpos._end_page_position.x_offset = 36.0
    curpos._end_page_position.y_offset = 133.0
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  cursor just off page at (36,133) in the rendered text")
    #rendering.render_thin_cursor(curpos,pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 4:
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 36.0
    curpos._start_page_position.y_offset = 132.0
    curpos._end_page_position.x_offset = 36.0
    curpos._end_page_position.y_offset = 132.0
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  cursor just on page at (36,132) in the rendered text")
    rendering.render_thin_cursor(curpos,pg)
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 5:
    print("Test of _render_cursor_rectangle")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  cursor rectangle from (0.0,0.0) to (72.0,0.0)")
    rendering._render_cursor_rectangle(0.0,72.0,pg)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 6:
    print("Tests of _try_line")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._fss = font_styling.new_font_styles()
    win._pg = rendering.new_page(win,216.0,180.0,36.0,72.0,"Courier New",win._fss,12.0,coloring.BLACK)
    print("  page dimensions 3.0\" by 2.5\" (3 lines)")
    print("  page with text origin at (36,72) (0.5\", 1.0\")")
    print("  Line at (0.0,0.0), thin cursor at (0.0,0.0)")
    win._pg._current_line = unicoding3_0.string_of("Test of _try_line")
    win._pg._page_position.y_offset = 0.0
    win._pg._line_width = writing.width_in_points_of(win,"Test of _try_line","Courier New",win._fss,12.0)
    print("  win._pg._line_width="+str(win._pg._line_width))
    win._pg._current_alignment = texting.Alignment.BEGIN
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 0.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 1
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._start_x_offset == 0.0
    assert curpos._end_x_offset == 0.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    assert rendering._equals_float(win._pg._page_position.x_offset,win._pg._line_width)
    assert win._pg._page_position.y_offset == 0.0
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 7:
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._page_position.y_offset += win._pg._font_size
    win._pg._current_line = unicoding3_0.string_of("line 1")
    win._pg._line_width = writing.width_in_points_of(win,"line 1","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.BEGIN
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 0.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    win._pg._page_position.y_offset += win._pg._font_size
    print("  Test of _try_line just on page, cursor on line 0")
    win._pg._current_line = unicoding3_0.string_of("just on page")
    win._pg._line_width = writing.width_in_points_of(win,"just on page","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.END
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 0.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._start_x_offset == 0.0
    assert curpos._end_x_offset == 0.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False

  elif win._tnum == 8:
    print("  Test of _try_line just on page, cursor on line 2")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._current_line = unicoding3_0.string_of("just on page")
    win._pg._line_width = writing.width_in_points_of(win,"just on page","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.END
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 2 * win._pg._font_size
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 2 * win._pg._font_size
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 0.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert rendering._equals_float(curpos._start_page_position.x_offset,57.58)
    assert curpos._start_page_position.y_offset == 2 * win._pg._font_size
    assert rendering._equals_float(curpos._end_page_position.x_offset,57.58)
    assert curpos._end_page_position.y_offset == 2 * win._pg._font_size
    assert curpos._start_x_offset == 0.0
    assert curpos._end_x_offset == 0.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 9:
    print("  Test of _try_line just on page, cursor on line 2 glyph 0-1")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._current_line = unicoding3_0.string_of("just on page")
    win._pg._line_width = writing.width_in_points_of(win,"just on page","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.END
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 2
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 2 *win._pg._font_size
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 1
    curpos._end_page_position.x_offset = 7.2
    curpos._end_page_position.y_offset = 2 * win._pg._font_size
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 7.2
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = True
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 2
    assert curpos._start_text_position.code_point_offset == 0
    assert rendering._equals_float(curpos._start_page_position.x_offset,57.58)
    assert curpos._start_page_position.y_offset == 2 * win._pg._font_size
    assert curpos._end_text_position.line_offset == 2
    assert curpos._end_text_position.code_point_offset == 1
    assert rendering._equals_float(curpos._end_page_position.x_offset,64.78)
    assert curpos._end_page_position.y_offset == 2 * win._pg._font_size
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False

  elif win._tnum == 10:
    print("  Test of _try_line just on page, cursor on line 0 glyph 0-1")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._current_line = unicoding3_0.string_of("just on page")
    win._pg._line_width = writing.width_in_points_of(win,"just on page","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.END
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 1
    curpos._end_page_position.x_offset = 7.2
    curpos._end_page_position.y_offset = 0.0
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 7.2
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 1
    assert curpos._end_page_position.x_offset == 7.2
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 11:
    print("  Test of _try_line line 1, cursor from (0,0) to (1,10)")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._page_position.y_offset = win._pg._font_size
    win._pg._current_line = unicoding3_0.string_of("line 1")
    win._pg._line_width = writing.width_in_points_of(win,"line 1","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.BEGIN
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 10
    curpos._end_page_position.x_offset = 72.0
    curpos._end_page_position.y_offset = win._pg._font_size
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 72.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = True
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 10
    assert curpos._end_page_position.x_offset == 72.0
    assert curpos._end_page_position.y_offset == win._pg._font_size
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 12:
    print("  Test of _try_line line 1, cursor from (1,0) to (2,10)")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._page_position.y_offset = win._pg._font_size
    win._pg._current_line = unicoding3_0.string_of("line 1")
    win._pg._line_width = writing.width_in_points_of(win,"line 1","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.BEGIN
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 1
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = win._pg._font_size
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 10
    curpos._end_page_position.x_offset = 72.0
    curpos._end_page_position.y_offset = 2 * win._pg._font_size
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 72.0
    curpos._in_fat_cursor = True
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == win._pg._font_size
    assert curpos._end_text_position.line_offset == 2
    assert curpos._end_text_position.code_point_offset == 10
    assert curpos._end_page_position.x_offset == 72.0
    assert curpos._end_page_position.y_offset == 2 * win._pg._font_size
    assert curpos._in_fat_cursor == True
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 13:
    print("  Test of _try_line line 1, cursor from (1,0) to (1,10)")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._page_position.y_offset = win._pg._font_size
    win._pg._current_line = unicoding3_0.string_of("line 1")
    win._pg._line_width = writing.width_in_points_of(win,"line 1","Courier New",win._fss,12.0)
    win._pg._current_alignment = texting.Alignment.BEGIN
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 1
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = win._pg._font_size
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 10
    curpos._end_page_position.x_offset = 72.0
    curpos._end_page_position.y_offset = win._pg._font_size
    curpos._start_x_offset = 0.0
    curpos._end_x_offset = 72.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = True
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == win._pg._font_size
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 10
    assert curpos._end_page_position.x_offset == 72.0
    assert curpos._end_page_position.y_offset == win._pg._font_size
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 14:
    print("  Test of _try_line line off page - should not appear")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    win._pg._page_position.y_offset = 3 * win._pg._font_size
    win._pg._current_line = unicoding3_0.string_of("Test of _try_line line off page")
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    x1 = 0.0
    x2 = 0.0
    curpos._in_fat_cursor = False
    curpos._cursor_rectangle_pending = False
    rendering._try_line(win._pg,curpos)
    assert len(win._pg._line_list) == 3
    assert win._pg._line_list[0] == (0.0,"Test of _try_line")
    assert win._pg._line_list[1] == (0.0,"line 1")
    (xoff,line) = win._pg._line_list[2] 
    assert rendering._equals_float(xoff,57.58)
    assert line == "just on page"
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._in_fat_cursor == False
    assert curpos._cursor_rectangle_pending == False
    rendering.render_thin_cursor(curpos,win._pg)
    win._tnum += 1
    return False
    
  elif win._tnum == 15:
    print("Tests of _render_line")
    windowing.clear(win)
    fn = "Courier New"
    fss = font_styling.new_font_styles()
    fsize = 12.0
    win._s = unicoding3_0.string_of("fred")
    win._pg = rendering.new_page(win,216.0,288.0,36.0,72.0,fn,fss,fsize,coloring.BLACK)
    print("  page dimensions 3.0\" by 4.0\"")
    print("  page with text origin at (36,72) (0.5\", 1.0\")")
    win._pg._current_line = win._s
    win._pg._line_width = page_laying_out.width_in_points_of_escaped(win,win._s,fn,fss,12.0)
    print("Test of BEGIN alignment")
    win._pg._current_alignment = texting.Alignment.BEGIN
    print("  render \"fred\" at (7,0)")
    win._pg._text_position.line_offset = 0
    win._pg._text_position.code_point_offset = 0
    win._pg._page_position.y_offset = 7.0 * fsize
    rendering._update_list(win._pg._line_list,0,(0.0,""))
    rendering._update_list(win._pg._line_list,1,(0.0,""))
    rendering._update_list(win._pg._line_list,2,(0.0,""))
    rendering._update_list(win._pg._line_list,3,(0.0,""))
    rendering._update_list(win._pg._line_list,4,(0.0,""))
    rendering._update_list(win._pg._line_list,5,(0.0,""))
    rendering._update_list(win._pg._line_list,6,(0.0,""))
    curpos = rendering.new_cursor_position()
    rendering._render_line(win._pg,curpos)
    assert unicoding3_0.length_of(win._pg._current_line) == 0
    assert win._pg._line_width == 0.0
    assert len(win._pg._line_list) == 8
    assert win._pg._line_list[7] == (0.0,"fred")
    win._tnum += 1
    return False
    
  elif win._tnum == 16:
    print("  test of END alignment")
    win._pg._current_line = win._s
    win._pg._line_width = page_laying_out.width_in_points_of_escaped(win, win._s, win._pg._font_name, win._pg._font_styles, win._pg._font_size)
    win._pg._current_alignment = texting.Alignment.END
    win._pg._text_position.line_offset = 1
    win._pg._text_position.code_point_offset = 0
    curpos = rendering.new_cursor_position()
    print("  render \"fred\" at end of line")
    rendering._render_line(win._pg,curpos)
    assert unicoding3_0.length_of(win._pg._current_line) == 0
    assert win._pg._line_width == 0.0
    assert len(win._pg._line_list) == 9
    (a,b) = win._pg._line_list[8]
    assert rendering._equals_float(a,115.2)
    assert b == "fred"
    (a,b) = win._pg._line_list[8]
    assert rendering._equals_float(a,115.2)
    assert b =="fred"
    win._tnum += 1
    return False
    
  elif win._tnum == 17:
    print("  test of MIDDLE alignment")
    win._pg._current_line = win._s
    win._pg._line_width = page_laying_out.width_in_points_of_escaped(win, win._s, win._pg._font_name, win._pg._font_styles, win._pg._font_size)
    win._pg._current_alignment = texting.Alignment.MIDDLE
    win._pg._text_position.line_offset = 1
    win._pg._text_position.code_point_offset = 4
    curpos = rendering.new_cursor_position()
    print("  render \"fred\" at middle of line")
    rendering._render_line(win._pg,curpos)
    assert unicoding3_0.length_of(win._pg._current_line) == 0
    assert win._pg._line_width == 0.0
    assert len(win._pg._line_list) == 10
    (a,b) = win._pg._line_list[9]
    assert rendering._equals_float(a,57.6)
    assert b == "fred"
    win._tnum += 1
    return False
         
  elif win._tnum == 18:
    print("Tests of _render_token")
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  page is 3\" wide by 4\" deep,")
    print("  with horizontal indent of 0.5\", vertical indent of 1\"")
    windowing.clear(win)
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._fix_cursor_position(curpos,pg)
    rendering._fix_cursor_position(curpos,pg)
    #rendering._render_token(unicoding3_0.string_of("<finish>"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("<end>"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 0  # <end> has no width
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert pg._EOT_position.x_offset == 0.0
    assert pg._EOT_position.y_offset == 0.0
    assert rendering._equals_float(pg._line_width,0.0)
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"")
    assert len(pg._back_map) == 1
    assert len(pg._back_map[0]) == 1
    assert pg._back_map[0][0] == (0,0)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0

    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 3
    assert rendering._equals_float(pg._line_width,21.6)
    assert pg._page_position.y_offset == 0.0
    assert pg._EOT_position.x_offset == 0.0
    assert pg._EOT_position.y_offset == 0.0
    assert len(pg._line_list) == 0
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][2] == (0,2)
    assert pg._back_map[0][3] == (0,3)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0

    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 1
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 3
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 3
    assert rendering._equals_float(pg._line_width,21.6)
    assert pg._page_position.y_offset == 0.0
    assert pg._EOT_position.y_offset == 0.0
    assert len(pg._line_list) == 0
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][2] == (0,2)
    assert pg._back_map[0][3] == (0,3)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 1
    assert rendering._equals_float(curpos._start_page_position.x_offset,7.2)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 3
    assert rendering._equals_float(curpos._end_page_position.x_offset,21.6)
    assert curpos._end_page_position.y_offset == 0.0

    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 4
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 7
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 7
    assert rendering._equals_float(pg._line_width,50.4)
    assert pg._page_position.y_offset == 0.0
    assert pg._EOT_position.y_offset == 0.0
    print("len(pg._line_list)="+str(len(pg._line_list)))
    assert len(pg._line_list) == 0
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][2] == (0,2)
    assert pg._back_map[0][3] == (0,3)
    assert pg._back_map[0][4] == (0,4)
    assert pg._back_map[0][5] == (0,5)
    assert pg._back_map[0][6] == (0,6)
    assert pg._back_map[0][7] == (0,7)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 4
    assert rendering._equals_float(curpos._start_page_position.x_offset,28.8)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 7
    assert rendering._equals_float(curpos._end_page_position.x_offset,50.4)
    assert curpos._end_page_position.y_offset == 0.0
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 18
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 18
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 7
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 8
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 11
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 12
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 14
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 15
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 18
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 19
    rendering._render_token(unicoding3_0.string_of("mat."),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 23
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.MIDDLE,curpos,pg)
    assert pg._current_alignment == texting.Alignment.MIDDLE
    assert pg._text_position.line_offset == 1
    assert pg._text_position.code_point_offset == 0
    assert pg._line_list[0] == (0.0,"the cat sat on the")
    assert pg._line_list[1] == (0.0,"mat.")
    assert pg._back_map[1] == [(0,19),(0,20),(0,21),(0,22),(0,23)]
    assert pg._back_map[2] == [(1,0)]
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.END
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 36.0
    rendering._render_token(unicoding3_0.string_of("<end>"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.END
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 144.0
    assert pg._page_position.y_offset == 36.0
    assert pg._EOT_position.y_offset ==36.0
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 18
    assert rendering._equals_float(curpos._start_page_position.x_offset,129.62)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 18
    assert rendering._equals_float(curpos._end_page_position.x_offset,129.62)
    assert curpos._end_page_position.y_offset == 0.0
    assert pg._back_map[2] == [(1,0)]
    assert pg._back_map[3] == [(2,0)]
    rendering.render_thin_cursor(curpos,pg)
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 19
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 19
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.END,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("mat."),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.MIDDLE,curpos,pg)
    assert pg._current_alignment == texting.Alignment.MIDDLE
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.END,curpos,pg)
    assert pg._current_alignment == texting.Alignment.END
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 36.0
    assert pg._EOT_position.y_offset == 36.0
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 19
    print("curpos._start_page_position.x_offset="+str(curpos._start_page_position.x_offset))
    print("curpos._start_page_position.y_offset="+str(curpos._start_page_position.y_offset))
    assert rendering._equals_float(curpos._start_page_position.x_offset,0.0)
    assert rendering._equals_float(curpos._start_page_position.y_offset,12.0)
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 19
    assert rendering._equals_float(curpos._end_page_position.x_offset,0.0)
    assert rendering._equals_float(curpos._end_page_position.y_offset,12.0)
    assert pg._line_list[0] == (0.0,"the cat sat on the")
    assert pg._line_list[1] == (0.0,"mat.")
    assert pg._line_list[2] == (72.0,"")
    assert pg._back_map[1] == [(0,19),(0,20),(0,21),(0,22),(0,23)]
    assert pg._back_map[2] == [(1,0)]
    assert pg._back_map[3] == [(2,0)]
    rendering.render_thin_cursor(curpos,pg)

    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 22
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 22
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("mat."),texting.Alignment.BEGIN,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    assert pg._current_alignment == texting.Alignment.BEGIN
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 36.0
    assert pg._EOT_position.y_offset == 36.0
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 22
    assert rendering._equals_float(curpos._start_page_position.x_offset,21.6)
    assert curpos._start_page_position.y_offset == 12.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 22
    assert rendering._equals_float(curpos._end_page_position.x_offset,21.6)
    assert curpos._end_page_position.y_offset == 12.0
    rendering.render_thin_cursor(curpos,pg)
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 1
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("mat."),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 36.0
    assert pg._EOT_position.y_offset == 36.0
    assert curpos._start_text_position.line_offset == 1
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 24.0
    assert curpos._end_text_position.line_offset == 1
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 24.0
    rendering.render_thin_cursor(curpos,pg)
    win._tnum += 1
    return False

  elif win._tnum == 19:
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    # page is 3" wide by 4" deep, 
    # with horizontal indent of 0.5", vertical indent of 1"
    windowing.clear(win)
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 2
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = -1.0
    curpos._start_page_position.y_offset = -1.0
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = -1.0
    curpos._end_page_position.y_offset = -1.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("cat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("mat."),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("\n"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("<end>"),texting.Alignment.BEGIN,curpos,pg)
    assert pg._text_position.line_offset == 2
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 36.0
    assert pg._EOT_position.y_offset == 36.0
    assert curpos._start_text_position.line_offset == 2
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 36.0
    assert curpos._end_text_position.line_offset == 2
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 36.0
    rendering.render_thin_cursor(curpos,pg)
    
    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("dogs"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 19
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert pg._line_list == []
    assert len(pg._back_map[0]) == 20
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][19] == (0,19)
    rendering.render_thin_cursor(curpos,pg)

    # start of render
    pg._current_alignment = texting.Alignment.BEGIN
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.y_offset = 0.0
    pg._line_list = []
    pg._back_map = []
    pg._back_map.append([(0,0)])
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._start_page_position.x_offset = 0.0
    curpos._start_page_position.y_offset = 0.0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    curpos._end_page_position.x_offset = 0.0
    curpos._end_page_position.y_offset = 0.0
    rendering._render_token(unicoding3_0.string_of("The"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("dogs"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("sat"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("on"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of("the"),texting.Alignment.BEGIN,curpos,pg)
    rendering._render_token(unicoding3_0.string_of(" "),texting.Alignment.BEGIN,curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 20
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 12.0
    assert len(pg._line_list) == 1
    assert pg._line_list == [(0.0,"The dogs sat on the")]
    assert len(pg._back_map) == 2
    assert len(pg._back_map[0]) == 20
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][19] == (0,19)
    assert pg._back_map[1][0] == (0,20)
    rendering.render_thin_cursor(curpos,pg)
    
    print("OK")
    win._tnum += 1
    return False
  
  elif win._tnum == 20:
    print("Tests of rendering entire text")
    windowing.clear(win)
    cursoring.wipe_cursor(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    t = texting.new_text()
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    #rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    curpos._start_text_position.code_point_offset = 0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"")
    assert len(pg._back_map) == 1
    assert pg._back_map[0] == [(0,0)]
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    
    cursoring.wipe_cursor(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('f'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('j'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('m'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 8
    print("  pg._page_position.x_offset="+str(pg._page_position.x_offset))
    assert rendering._equals_float(pg._page_position.x_offset,57.6)
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"fred jim")
    assert len(pg._back_map) == 1
    assert len(pg._back_map[0]) == 9
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][2] == (0,2)
    assert pg._back_map[0][3] == (0,3)
    assert pg._back_map[0][4] == (0,4)
    assert pg._back_map[0][5] == (0,5)
    assert pg._back_map[0][6] == (0,6)
    assert pg._back_map[0][7] == (0,7)
    assert pg._back_map[0][8] == (0,8)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    input("  Please input NL:")
    
    print("  fat cursor at (0,0),(0,1)")
    cursoring.wipe_cursor(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('f'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('j'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('m'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._end_text_position.code_point_offset = 1  # fat cursor at (0,0),(0,1)
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 1
    assert rendering._equals_float(curpos._end_page_position.x_offset,7.2)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 8
    print("  pg._page_position.x_offset="+str(pg._page_position.x_offset))
    assert rendering._equals_float(pg._page_position.x_offset,57.6)
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"fred jim")
    assert len(pg._back_map) == 1
    assert len(pg._back_map[0]) == 9
    assert pg._back_map[0][0] == (0,0)
    assert pg._back_map[0][1] == (0,1)
    assert pg._back_map[0][2] == (0,2)
    assert pg._back_map[0][3] == (0,3)
    assert pg._back_map[0][4] == (0,4)
    assert pg._back_map[0][5] == (0,5)
    assert pg._back_map[0][6] == (0,6)
    assert pg._back_map[0][7] == (0,7)
    assert pg._back_map[0][8] == (0,8)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 1
    assert rendering._equals_float(curpos._end_page_position.x_offset,7.2)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    input("  Please input NL:")
    
    print("  thin cursor at (0,4)")
    painting. clear_rectangles(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('f'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('j'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('m'))
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 4
    curpos._update_x_offset = True
    curpos._end_text_position.code_point_offset = 4
    curpos._update_x_offset = False
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 4
    assert rendering._equals_float(curpos._start_page_position.x_offset,28.8)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 4
    assert rendering._equals_float(curpos._end_page_position.x_offset,28.8)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 4
    assert rendering._equals_float(curpos._start_page_position.x_offset,28.8)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 4
    assert rendering._equals_float(curpos._end_page_position.x_offset,28.8)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    input("  Please input NL:")
    
    print("  thin cursor at (0,5), no x update for curpos")
    cursoring.wipe_cursor(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('f'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('j'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('m'))
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 5
    curpos._update_x_offset = False
    curpos._end_text_position.code_point_offset = 5
    curpos._update_x_offset = True
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 5
    assert rendering._equals_float(curpos._start_page_position.x_offset,36.0)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 5
    assert rendering._equals_float(curpos._end_page_position.x_offset,36.0)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 5
    assert rendering._equals_float(curpos._start_page_position.x_offset,36.0)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 5
    assert rendering._equals_float(curpos._end_page_position.x_offset,36.0)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    input("  Please input NL:")
    
    print("  thin cursor at (0,8)")
    t = texting.new_text()
    cursoring.wipe_cursor(win)
    texting.insert_code_point(t,ord('f'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('j'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('m'))
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 8
    curpos._end_text_position.code_point_offset = 8
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 8
    assert rendering._equals_float(curpos._start_page_position.x_offset,57.6)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 8
    assert rendering._equals_float(curpos._end_page_position.x_offset,57.6)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 8
    assert rendering._equals_float(curpos._start_page_position.x_offset,57.6)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 8
    assert rendering._equals_float(curpos._end_page_position.x_offset,57.6)
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    
    print("OK")
    win._tnum += 1
    return False
  
  elif win._tnum == 21:
    print("Tests of fat cursor rendering")
    """
    tests:
      three lines, the second one right-justified
        thin cursor at start
        fat cursor over first glyph
        fat cursor nearly to end of first line
        fat cursor past first glyph, nearly to end of first line
        fat cursor past first glyph, at end of first line
        fat cursor past first glyph, at start of second line
        fat cursor past first glyph, nearly at end of second line
        fat cursor past first glyph, at end of second line
        fat cursor past first glyph, at start of third line
        fat cursor past first glyph, nearly at end of third line
        fat cursor past first glyph, at end of third line

    These tests are done here because the fat cursor rendering code
    is distributed around the rendering procedures.
    """
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    t = texting.new_text()
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('1'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.END)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('2'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.BEGIN)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('3'))
    texting.insert_code_point(t,ord('\n'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    print("  thin cursor at (0,0)")
    curpos = rendering.new_cursor_position()
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,0),(0,1)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._end_text_position.code_point_offset = 1
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,0),(0,13)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._end_text_position.code_point_offset = 13
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(0,13)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.code_point_offset = 13
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(0,14)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.code_point_offset = 14
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(1,0)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(1,1)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 1
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(1,13)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 13
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(1,14)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 1
    curpos._end_text_position.code_point_offset = 14
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(2,0)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 0
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(2,1)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 1
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(2,13)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 13
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
        
    print("Please enter NL:",end=' ')
    input()
    print("  fat cursor at (0,1),(2,14)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 2
    curpos._end_text_position.code_point_offset = 14
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)    
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 22:
    """
    tests:
      single text line that wraps on word
        fat cursor past first glyph, nearly to end of first line
        fat cursor past first glyph, at end of first line
        fat cursor past first glyph, at start of second line
        fat cursor past first glyph, nearly at end of second line
        fat cursor past first glyph, at end of second line
        fat cursor past first glyph, at start of third line
      single text line that wraps on space
        fat cursor past first glyph, nearly to end of first line
        fat cursor past first glyph, at end of first line
        fat cursor past first glyph, at start of second line
        fat cursor past first glyph, nearly at end of second line
        fat cursor past first glyph, at end of second line
        fat cursor past first glyph, at start of third line
         
    These tests are done here because the fat cursor rendering code
    is distributed around the rendering procedures.
    """
    print("Tests of fat cursor on wrapped lines")
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    print("  page is 3\" wide by 4\" deep,")
    print("  with horizontal indent of 0.5\", vertical indent of 1\"")
    windowing.clear(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('c'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('o'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('m'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord('.'))
    texting.insert_code_point(t,ord('\n'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    print("  fat cursor at (0,0)(0,18)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 0
    curpos._end_text_position.code_point_offset = 18
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    print("Please enter NL:",end=' ')
    input()

    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    print("  fat cursor at (0,1)(0,19)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.code_point_offset = 19
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    print("Please enter NL:",end=' ')
    input()

    print("  fat cursor at (0,1)(0,20)")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.code_point_offset = 20
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    print("Please enter NL:",end=' ')
    input()

    print("OK")
    win._tnum += 1
    return False
  
  elif win._tnum == 23:
    print("Tests of text_position_of", end=' ')
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    t = texting.new_text()
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('b'))
    texting.insert_code_point(t,ord('\n'))
    texting.insert_code_point(t,ord('c'))
    texting.insert_code_point(t,ord('d'))
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    #rendering.text_position_of(None,None,None)
    #rendering.text_position_of(-1,None,None)
    #rendering.text_position_of(-1,-1,None)
    #rendering.text_position_of(-1,-1,pg)
    #rendering.text_position_of(0,-1,pg)
    assert rendering.text_position_of(0,0,pg) == (0,0)
    assert rendering.text_position_of(1,1,pg) == (1,1)
    print("OK")
    win._tnum += 1
    return False
    
  elif win._tnum == 24:
    print("Tests of render_lines")
    windowing.clear(win)
    #rendering.render_lines(None,None,None,None,None)
    t = texting.new_text()
    print("  empty text, cursor at (0,0)")
    #rendering.render_lines(t,None,None,None,None)
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    #rendering.render_lines(t,curpos,None,None,None)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    #rendering.render_lines(t,curpos,pg,None,None)
    #.render_lines(t,curpos,pg,-1,None)
    #rendering.render_lines(t,curpos,pg,-1,0)
    #rendering.render_lines(t,curpos,pg,0,-1)
    #rendering.render_lines(t,curpos,pg,0,0)
    #rendering.render_lines(t,curpos,pg,2,1)
    #rendering.render_lines(t,curpos,pg,1,1)
    #rendering.render_lines(t,curpos,pg,1,2)
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 1
    #rendering.render_lines(t,curpos,pg,0,1)
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    rendering.render_lines(t,curpos,pg,0,1)
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    rendering.render_thin_cursor(curpos,pg)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"")
    assert len(pg._back_map) == 1
    assert pg._back_map[0] == [(0,0)]
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._end_text_position.line_offset == 0
    assert curpos._end_text_position.code_point_offset == 0
    assert curpos._end_page_position.x_offset == 0.0
    assert curpos._end_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    win._tnum += 1
    return False
    
  elif win._tnum == 25:
    windowing.clear(win)
    t = texting.new_text()
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('1'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.END)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('2'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.BEGIN)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('3'))
    texting.insert_code_point(t,ord('\n'))
    print("  three lines, second one blue")
    curpos = rendering.new_cursor_position()
    rendering.set_cursor_position_to_start(curpos)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    pg._text_color = coloring.new_color(0.0,0.0,1.0)  # BLUE
    rendering.render_lines(t,curpos,pg,1,2)
    win._tnum += 1
    return False
    
  elif win._tnum == 26:
    windowing.clear(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    t = texting.new_text()
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('1'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.END)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('2'))
    texting.insert_code_point(t,ord('\n'))
    texting.set_alignment(t,texting.Alignment.BEGIN)
    texting.insert_code_point(t,ord('T'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('s'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('l'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('n'))
    texting.insert_code_point(t,ord('e'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('3'))
    texting.insert_code_point(t,ord('\n'))
    curpos = rendering.new_cursor_position()
    print("  three lines, all black")
    rendering.set_cursor_position_to_start(curpos)
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    input("Please enter NL:")
    print("  three lines, all blue")
    pg._text_color = coloring.new_color(0.0,0.0,1.0)  # BLUE
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    input("Please enter NL:")
    print("  fattish cursor at (0,0)(0,1)")
    curpos._end_text_position.code_point_offset = 1
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    input("Please enter NL:")
    print("  thin cursor at (0,4)")
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 4
    curpos._end_text_position.code_point_offset = 4
    painting.clear_rectangles(win)  # wipe old cursor
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    print("OK")
    win._tnum += 1
    return False

  elif win._tnum == 27:
    print("Tests of rendering rest of text using render_lines")
    windowing.clear(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos = rendering.new_cursor_position()
    t = texting.new_text()
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering._update_list(pg._line_list,0,(0.0,""))
    rendering._update_list(pg._back_map,0,[])
    rendering._update_list(pg._back_map[0],0,(0,0))
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.line_offset = 0
    curpos._start_text_position.code_point_offset = 1
    curpos._end_text_position.line_offset = 0
    curpos._end_text_position.code_point_offset = 0    
    curpos._start_text_position.code_point_offset = 0
    lo1 = 0
    lo2 = rendering.TO_END
    rendering.render_lines(t,curpos,pg,lo1,lo2)    
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 0
    assert pg._page_position.x_offset == 0.0
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"")
    assert len(pg._back_map) == 1
    assert pg._back_map[0] == [(0,0)]
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    win._tnum += 1
    return False
    
  elif win._tnum == 28:
    cursoring.wipe_cursor(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos = rendering.new_cursor_position()
    t = texting.new_text()
    texting.insert_code_point(t,ord('H'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('p'))
    texting.insert_code_point(t,ord('p'))
    texting.insert_code_point(t,ord('y'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('B'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('y'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering._update_list(pg._line_list,0,(0.0,"Happy Birthday"))
    rendering._update_list(pg._back_map,0,[])
    rendering._update_list(pg._back_map[0],0,(0,0))
    rendering._update_list(pg._back_map[0],1,(0,1))
    rendering._update_list(pg._back_map[0],2,(0,2))
    rendering._update_list(pg._back_map[0],3,(0,3))
    rendering._update_list(pg._back_map[0],4,(0,4))
    rendering._update_list(pg._back_map[0],5,(0,5))
    rendering._update_list(pg._back_map[0],6,(0,6))
    rendering._update_list(pg._back_map[0],7,(0,7))
    rendering._update_list(pg._back_map[0],8,(0,8))
    rendering._update_list(pg._back_map[0],9,(0,9))
    rendering._update_list(pg._back_map[0],10,(0,10))
    rendering._update_list(pg._back_map[0],11,(0,11))
    rendering._update_list(pg._back_map[0],12,(0,12))
    rendering._update_list(pg._back_map[0],13,(0,13))
    rendering._update_list(pg._back_map[0],14,(0,14))
    rendering.set_cursor_position_to_start(curpos)
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 14
    print("  pg._page_position.x_offset="+str(pg._page_position.x_offset))
    assert rendering._equals_float(pg._page_position.x_offset,100.82)
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"Happy Birthday")
    assert len(pg._back_map) == 1
    assert pg._back_map[0] == [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                               (0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14)]
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 0
    assert curpos._start_page_position.x_offset == 0.0
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True
    win._tnum += 1
    return False
    
  elif win._tnum == 29:
    cursoring.wipe_cursor(win)
    fss = font_styling.new_font_styles()
    pg = rendering.new_page(win,216.0,288.0,36.0,72.0,"Courier New",fss,12.0,coloring.BLACK)
    curpos = rendering.new_cursor_position()
    t = texting.new_text()
    texting.insert_code_point(t,ord('H'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('p'))
    texting.insert_code_point(t,ord('p'))
    texting.insert_code_point(t,ord('y'))
    texting.insert_code_point(t,ord(' '))
    texting.insert_code_point(t,ord('B'))
    texting.insert_code_point(t,ord('i'))
    texting.insert_code_point(t,ord('r'))
    texting.insert_code_point(t,ord('t'))
    texting.insert_code_point(t,ord('h'))
    texting.insert_code_point(t,ord('d'))
    texting.insert_code_point(t,ord('a'))
    texting.insert_code_point(t,ord('y'))
    pg._text_position.line_offset = 0
    pg._text_position.code_point_offset = 0
    pg._page_position.x_offset = 0.0
    pg._page_position.y_offset = 0.0
    pg._current_line = unicoding3_0.new_string()
    pg._line_width = 0.0
    rendering._update_list(pg._line_list,0,(0.0,"Happy Birthday"))
    rendering._update_list(pg._back_map,0,[])
    rendering._update_list(pg._back_map[0],0,(0,0))
    rendering._update_list(pg._back_map[0],1,(0,1))
    rendering._update_list(pg._back_map[0],2,(0,2))
    rendering._update_list(pg._back_map[0],3,(0,3))
    rendering._update_list(pg._back_map[0],4,(0,4))
    rendering._update_list(pg._back_map[0],5,(0,5))
    rendering._update_list(pg._back_map[0],6,(0,6))
    rendering._update_list(pg._back_map[0],7,(0,7))
    rendering._update_list(pg._back_map[0],8,(0,8))
    rendering._update_list(pg._back_map[0],9,(0,9))
    rendering._update_list(pg._back_map[0],10,(0,10))
    rendering._update_list(pg._back_map[0],11,(0,11))
    rendering._update_list(pg._back_map[0],12,(0,12))
    rendering._update_list(pg._back_map[0],13,(0,13))
    rendering._update_list(pg._back_map[0],14,(0,14))
    rendering.set_cursor_position_to_start(curpos)
    curpos._start_text_position.code_point_offset = 14
    curpos._end_text_position.code_point_offset = 14
    rendering.render_lines(t,curpos,pg,0,rendering.TO_END)
    assert pg._text_position.line_offset == 0
    assert pg._text_position.code_point_offset == 14
    print("  pg._page_position.x_offset="+str(pg._page_position.x_offset))
    assert rendering._equals_float(pg._page_position.x_offset, 100.82)
    assert pg._page_position.y_offset == 0.0
    assert len(pg._line_list) == 1
    assert pg._line_list[0] == (0.0,"Happy Birthday")
    assert len(pg._back_map) == 1
    assert pg._back_map[0] == [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                               (0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14)]
    assert curpos._start_text_position.line_offset == 0
    assert curpos._start_text_position.code_point_offset == 14
    assert rendering._equals_float(curpos._start_page_position.x_offset,100.82)
    assert curpos._start_page_position.y_offset == 0.0
    assert curpos._update_x_offset == True    
    print("OK")
    win._tnum += 1
    return False
  
  else:
    print("")
    print("All tests OK")
    return True
  
  
# Tests which do not need a window
# --------------------------------
print("")  
print("Tests which do not need a window")
print("")
print("Tests of _equals_float", end=' ')
assert  not rendering._equals_float(123.4,123.3)
assert rendering._equals_float(123.4,123.401)
assert  not rendering._equals_float(123.4,123.5)
print("OK")

print("Tests of _new_page_position", end=' ')
pp = rendering._new_page_position()
assert pp.x_offset == -1.00
assert pp.y_offset == -1.00
print("OK")

print("Tests of rendering._new_text_position", end=' ')
tp = rendering._new_text_position()
assert tp.line_offset == -1
assert tp.code_point_offset == -1
print("OK")

print("Tests of _equals_text_position", end=' ')
tp1 = rendering._new_text_position()
tp1.line_offset = 1
tp1.code_point_offset = 2
tp2 = rendering._new_text_position()
tp2.line_offset = 0
tp2.code_point_offset = 2
assert  not rendering._equals_text_position(tp1,tp2)
tp2.line_offset = 2
tp2.code_point_offset = 2
assert  not rendering._equals_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 1
assert  not rendering._equals_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 3
assert  not rendering._equals_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 2
assert rendering._equals_text_position(tp1,tp2)
print("OK")

print("Tests of _less_than_text_position", end=' ')
tp1 = rendering._new_text_position()
tp1.line_offset = 1
tp1.code_point_offset = 2
tp2 = rendering._new_text_position()
tp2.line_offset = 0
tp2.code_point_offset = 2
assert not rendering._less_than_text_position(tp1,tp2)
tp2.line_offset = 2
tp2.code_point_offset = 2
assert rendering._less_than_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 1
assert not rendering._less_than_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 3
assert rendering._less_than_text_position(tp1,tp2)
tp2.line_offset = 1
tp2.code_point_offset = 2
assert not rendering._less_than_text_position(tp1,tp2)
print("OK")

print("Tests of new_cursor_position", end=' ')
curpos = rendering.new_cursor_position()
assert curpos._start_text_position.line_offset == -1
assert curpos._start_text_position.code_point_offset == -1
assert curpos._end_text_position.line_offset == -1
assert curpos._end_text_position.code_point_offset == -1
assert curpos._start_page_position.x_offset == -1.00
assert curpos._start_page_position.y_offset == -1.00
assert curpos._end_page_position.x_offset == -1.00
assert curpos._end_page_position.y_offset == -1.00
assert curpos._desired_x_offset == -1.0
assert curpos._update_x_offset == True
assert curpos._start_x_offset == -1.0
assert curpos._end_x_offset == -1.0
assert curpos._in_fat_cursor == False
assert curpos._cursor_rectangle_pending == False
print("OK")

print("Tests of collapse_to_end",end=' ')
#rendering.collapse_to_end(None)
curpos = rendering.new_cursor_position()
curpos._start_text_position.line_offset = 123
curpos._start_text_position.code_point_offset = 234
curpos._start_page_position.x_offset = 345.0
curpos._start_page_position.y_offset = 456.0
curpos._end_text_position.line_offset = 567
curpos._end_text_position.code_point_offset = 678
curpos._end_page_position.x_offset = 789.0
curpos._end_page_position.y_offset = 890.0
rendering.collapse_to_end(curpos)
assert curpos._start_text_position.line_offset == 567
assert curpos._start_text_position.code_point_offset == 678
assert curpos._start_page_position.x_offset == 789.0
assert curpos._start_page_position.y_offset == 890.0
assert curpos._end_text_position.line_offset == 567
assert curpos._end_text_position.code_point_offset == 678
assert curpos._end_page_position.x_offset == 789.0
assert curpos._end_page_position.y_offset == 890.0
rendering.collapse_to_end(curpos)
assert curpos._start_text_position.line_offset == 567
assert curpos._start_text_position.code_point_offset == 678
assert curpos._start_page_position.x_offset == 789.0
assert curpos._start_page_position.y_offset == 890.0
assert curpos._end_text_position.line_offset == 567
assert curpos._end_text_position.code_point_offset == 678
assert curpos._end_page_position.x_offset == 789.0
assert curpos._end_page_position.y_offset == 890.0
print("OK")

print("Tests of collapse_to_start",end=' ')
#rendering.collapse_to_start(None)
curpos = rendering.new_cursor_position()
curpos._start_text_position.line_offset = 123
curpos._start_text_position.code_point_offset = 234
curpos._start_page_position.x_offset = 345.0
curpos._start_page_position.y_offset = 456.0
curpos._end_text_position.line_offset = 567
curpos._end_text_position.code_point_offset = 678
curpos._end_page_position.x_offset = 789.0
curpos._end_page_position.y_offset = 890.0
rendering.collapse_to_start(curpos)
assert curpos._start_text_position.line_offset == 123
assert curpos._start_text_position.code_point_offset == 234
assert curpos._start_page_position.x_offset == 345.0
assert curpos._start_page_position.y_offset == 456.0
assert curpos._end_text_position.line_offset == 123
assert curpos._end_text_position.code_point_offset == 234
assert curpos._end_page_position.x_offset == 345.0
assert curpos._end_page_position.y_offset == 456.0
rendering.collapse_to_start(curpos)
assert curpos._start_text_position.line_offset == 123
assert curpos._start_text_position.code_point_offset == 234
assert curpos._start_page_position.x_offset == 345.0
assert curpos._start_page_position.y_offset == 456.0
assert curpos._end_text_position.line_offset == 123
assert curpos._end_text_position.code_point_offset == 234
assert curpos._end_page_position.x_offset == 345.0
assert curpos._end_page_position.y_offset == 456.0
print("OK")

print("Tests of is_thin", end=' ')
#rendering.is_thin(None)
curpos = rendering.new_cursor_position()
curpos._start_text_position.line_offset = 123
curpos._start_text_position.code_point_offset = 234
curpos._end_text_position.line_offset = 124
curpos._end_text_position.code_point_offset = 235
assert not rendering.is_thin(curpos)
curpos._end_text_position.line_offset = 123
curpos._end_text_position.code_point_offset = 235
assert not rendering.is_thin(curpos)
curpos._end_text_position.line_offset = 124
curpos._end_text_position.code_point_offset = 234
assert not rendering.is_thin(curpos)
curpos._end_text_position.line_offset = 123
curpos._end_text_position.code_point_offset = 234
assert rendering.is_thin(curpos)
print("OK")

print("Tests of set_thin_cursor_text_and_page",end=' ')
curpos = rendering.new_cursor_position()
curpos = rendering.new_cursor_position()
rendering.set_thin_cursor_text_and_page(curpos,12,34,45.0,67.0)
assert curpos._start_text_position.line_offset == 12
assert curpos._start_text_position.code_point_offset == 34
assert curpos._start_page_position.x_offset == 45.0
assert curpos._start_page_position.y_offset == 67.0
assert curpos._end_text_position.line_offset == 12
assert curpos._end_text_position.code_point_offset == 34
assert curpos._end_page_position.x_offset == 45.0
assert curpos._end_page_position.y_offset == 67.0
print("OK")

print("Tests of set_cursor_position_to_start", end=' ')
curpos = rendering.new_cursor_position()
rendering.set_cursor_position_to_start(curpos)
assert curpos._start_text_position.line_offset == 0
assert curpos._start_text_position.code_point_offset == 0
assert curpos._end_text_position.line_offset == 0
assert curpos._end_text_position.code_point_offset == 0
assert curpos._start_page_position.x_offset == 0.0
assert curpos._start_page_position.y_offset == 0.0
assert curpos._end_page_position.x_offset == 0.0
assert curpos._end_page_position.y_offset == 0.0
assert curpos._desired_x_offset ==  - 1.00
assert curpos._update_x_offset == True
print("OK")

print("Tests of set_on_screen_to_text", end=' ')
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.insert_code_point(t,ord('\n'))
curpos = rendering.new_cursor_position()
texting.set_cursor(t,2,3)
rendering.set_on_screen_to_text(t,curpos)
assert curpos._start_text_position.line_offset == 2
assert curpos._start_text_position.code_point_offset == 3
assert curpos._end_text_position.line_offset == 2
assert curpos._end_text_position.code_point_offset == 3
assert curpos._start_page_position.x_offset ==  - 1.0
assert curpos._start_page_position.y_offset ==  - 1.0
assert curpos._end_page_position.x_offset ==  - 1.0
assert curpos._end_page_position.y_offset ==  - 1.0
assert curpos._desired_x_offset ==  - 1.0
assert curpos._update_x_offset == True
print("OK")

print("Tests of set_text_to_on_screen_start", end=' ')
curpos = rendering.new_cursor_position()
curpos._start_text_position.line_offset = 1
curpos._start_text_position.code_point_offset = 2
curpos._end_text_position.line_offset = 3
curpos._end_text_position.code_point_offset = 4
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('g'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('j'))
texting.insert_code_point(t,ord('\n'))
rendering.set_text_to_on_screen_start(curpos,t)
assert texting.cursor_code_point_offset(t) == 2
assert texting.cursor_line_offset(t) == 1
print("OK")


print("Tests of set_text_to_on_screen_end", end=' ')
curpos = rendering.new_cursor_position()
curpos._start_text_position.line_offset = 1
curpos._start_text_position.code_point_offset = 2
curpos._end_text_position.line_offset = 3
curpos._end_text_position.code_point_offset = 4
t = texting.new_text()
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('c'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('d'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('f'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('g'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('j'))
texting.insert_code_point(t,ord('\n'))
rendering.set_text_to_on_screen_end(curpos,t)
assert texting.cursor_code_point_offset(t) == 4
assert texting.cursor_line_offset(t) == 3
print("OK")


print("Tests of _update_list", end=' ')
l = []
#rendering._update_list(l,1,123)
rendering._update_list(l,0,123)
assert l[0] == 123
rendering._update_list(l,1,456)
assert l[0] == 123
assert l[1] == 456
rendering._update_list(l,1,789)
assert l[0] == 123
assert l[1] == 789
print("OK")


print("Tests of _ensure_sublist_exists", end=' ')
l = []
#rendering._ensure_sublist_exists(l,1)
rendering._ensure_sublist_exists(l,0)
assert l[0] == []
rendering._ensure_sublist_exists(l,1)
assert l[0] == []
assert l[1] == []
l[0] = [1,2,3]
l[1] = [4,5,6]
rendering._ensure_sublist_exists(l,0)
rendering._ensure_sublist_exists(l,1)
assert l[0] == [1,2,3]
assert l[1] == [4,5,6]
print("OK")


# Tests which do require a window
# -------------------------------
print("")  
print("Tests which do require a window")
print("")
win = windowing.new_window(12.0,"Window for test of rendering",800.0,500.0,1.0)
win._tnum = 0
windowing.show(win,None,window_closing)
print("")
print("All tests OK")

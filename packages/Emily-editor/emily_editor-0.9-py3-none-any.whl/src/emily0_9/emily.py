from guibits1_0 import coloring
from guibits1_0 import controlling
from guibits1_0 import cursoring
from guibits1_0 import dialoging
from enum import Enum
from guibits1_0 import file_dialoging
from guibits1_0 import font_styling
from guibits1_0 import keyboarding
from guibits1_0 import menuing
from guibits1_0 import mousing
from guibits1_0 import painting
from guibits1_0 import type_checking2_0
from guibits1_0 import unicoding3_0
from guibits1_0 import window_bounding
from guibits1_0 import windowing

from . import html_texting
from . import looking_ahead
from . import mle_emitting
from . import mle_parsing
from . import persisting
from . import rendering
from . import text_printing
from . import texting
from . import unicode_io

# author R.N.Bosworth

# version 17 Mar 23  07:04
""" 
Main contractor for Emily.  The procedure "start" runs a new instantiation of Emily.  This means that multiple instances of Emily can run on multiple virtual machines, but note that persistent variables will be common to all instances, which may lead to some interesting situations.

Copyright (C) 2015,2016,2017,2018,2019,2021,2022,2023  R.N.Bosworth

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License (gpl.txt) for more details.
"""

# constants
# ---------
VERSION = "0.9"
RELEASE_YEAR = "2023"
ABOUT_MESSAGE = "Copyright © " + RELEASE_YEAR + "  Richard Bosworth\n" + "\n" + "This program is free software: you can redistribute it and/or modify " + "it under the terms of the GNU General Public License as published by " + "the Free Software Foundation, either version 3 of the License, or " + "(at your option) any later version.\n" + "\n" + "This program is distributed in the hope that it will be useful, " + "but WITHOUT ANY WARRANTY; without even the implied warranty of " + "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the " + "GNU General Public License for more details.\n" + "\n" + "You should have received a copy of the GNU General Public License " + "along with this program.  If not, see <http://www.gnu.org/licenses/>."
DEFAULT_FONT_NAME = "Times New Roman"
DEFAULT_FONT_SIZE = 12.0
PARCHMENT = coloring.new_color(1.0,1.0,0.9)

# variables
# ---------
my_persistents = None  # cache for persistents
my_window = None  # current main window
my_text = None  # current text being edited
my_page = None  # page on which text is rendered
is_loaded = False  # True iff file is loaded
file_name = None  # current file name or None if none

curpos = rendering.new_cursor_position()
# position of start and end of cursor

pivot = rendering.new_cursor_position()
# position of start of mouse-drag

text_font_style = font_styling.new_font_styles()
current_alignment = texting.Alignment.BEGIN
"""  Invariant: current_alignment == alignment of paragraph containing cursor """


"""  Note that a glyph is anything that separates two cursor positions,
     so ' ' and '\n' are glyphs, by our definition """


# main procedure
# --------------

def start(args):
  """ 
  pre:
    args = argument list, with name of this program and possible name of file to be opened
  
  post:
    Emily session has been set up
    font name and size for text have been set up,
      either from the input file, or by default
    the persistent variables for the session have been set up
      either to their default values, or to the values from 
        "EmilyPersistent.json" in the user's default directory
    if args has name of a valid .mle file to be opened, 
      the appropriate file has been loaded as the text
    or
      a new empty text has been set up
    if the supplied filename was invalid,
      an exception has been raised
    the text has been displayed on the screen
    the cursor has been set to the end of the text
  __________________________________________________________ 
  pre:
   file "EmilyPersistent.json" may be present in the user's default directory
  
  post:
    my_window has been set up
    my_persistents has been set up, either from the input file or the defaults
    my_text has been set to a new text
    my_text has been set unmodified
    my_page has been set up from the Persistents or defaults
    the zoom factor of the main window has been set 
    file "EmilyPersistent.json" in the user's default directory has been updated
      with the latest values of the persistent variables
    is_loaded = true, iff a file has been loaded
    file_name = name of current file being edited, or None if none
    curpos = the current cursor position
    the initial screen has been displayed

  test:
    null argument list
    invalid file name
    valid file name
  """
  global file_name
  global my_persistents
  global my_text
  try:
    type_checking2_0.check_derivative(args,list)
    my_persistents = persisting.get_persistents()
    my_text = texting.new_text()
    with my_text._my_lock:
      texting.set_unmodified(my_text)
    if len(args) > 1:
      file_name = args[1]
      file_name = check_file_type(file_name)
    else:
      file_name = None
    build_u_i()
  except Exception as ex:
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Emily: error in input file name", str(ex))
      
  
# callback procedures
# -------------------

def about_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    my_persistents = persistent variables for the Emily app
  
  post:
    the about-pane has been displayed on the screen

  test:
    once thru
  """
  global my_persistents
  dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),title_of(None),ABOUT_MESSAGE)


def action_key_hit(ac):
  """ 
  pre:
    ac = action code for gesture performed by user
    my_window = window for this app
    my_text = current text
    my_page = current page
    my_persistents = persistent variables for the Emily app
    curpos = current cursor position in text and on screen

  post:
    appropriate action has been carried out
    current_alignment has been set to alignment of paragraph in which cursor resides

  test:
    BACKSPACE
      cursor in paragraph (check state of Save menu item)
      cursor at start of paragraph
      cursor at start of text
    DELETE
      cursor in paragraph (check state of Save menu item)
      cursor at end of paragraph
      cursor at end of text
    ENTER
      (check state of Save menu item)
    UP_ARROW
      cursor beyond end of line above
      cursor in middle of line above
      cursor on top line
    DOWN_ARROW
      cursor beyond end of line below
      cursor in middle of line below
      cursor on bottom line
    LEFT_ARROW
      cursor in middle of line
      cursor at start of line
      cursor at start of text
    RIGHT_ARROW
      cursor in middle of line
      cursor at end of line
      cursor at end of text
    CTRL_S
  """
  global curpos
  global current_alignment
  global my_page
  global my_text
  global my_persistents
  if ac == controlling.ActionCode.BACKSPACE:
    with my_text._my_lock:
      rendering.set_text_to_on_screen_start(curpos,my_text)
      if  not html_texting.retreat(my_text):
        print('\u0007')  # BEL
      else:
        html_texting.delete_after(my_text)
        current_alignment = texting.get_alignment(my_text)
        rendering.set_on_screen_to_text(my_text,curpos)
        # curpos has text position set
        start_line = int(curpos._start_page_position.y_offset/my_page._font_size) -1
        if start_line < 0:
          start_line = 0
        rendering.render_lines(my_text,curpos,my_page,start_line,rendering.TO_END)
        # curpos has text and page positions set
        rendering.render_thin_cursor(curpos,my_page)
        texting.set_modified(my_text)
             
  elif ac == controlling.ActionCode.DELETE:
    with my_text._my_lock:
      rendering.set_text_to_on_screen_end(curpos,my_text)
      if  not html_texting.advance(my_text):
        print('\u0007')  # BEL
      else:
        html_texting.retreat(my_text)
        # grand old Duke of York
        html_texting.delete_after(my_text)
        # alignment will always be the same
        render_modified_text()
        
  elif ac == controlling.ActionCode.ENTER:
    with my_text._my_lock:
      rendering.set_text_to_on_screen_end(curpos,my_text)
      texting.insert_code_point(my_text,ord('\n'))
      # internal hard line break
      # note:alignment will always be the same
      render_modified_text()
      
  elif ac == controlling.ActionCode.UP_ARROW:
    if rendering.is_thin(curpos):
      if not rendering.move_cursor_up(curpos,my_page):
        print('\u0007')  # BEL
    else:  # fat cursor
      painting.clear_rectangles(my_window)
      rendering.collapse_to_start(curpos)
      plo1 = rendering.start_page_line_of(curpos,my_page)
      rendering.render_lines(my_text,curpos,my_page,plo1,plo1+1)
      # render the page line of the cursor only
      
  elif ac == controlling.ActionCode.DOWN_ARROW:
    if rendering.is_thin(curpos):
      if not rendering.move_cursor_down(curpos,my_page):
        print('\u0007')  # BEL
    else:  # fat cursor
      painting.clear_rectangles(my_window)
      rendering.collapse_to_end(curpos)
      plo1 = rendering.start_page_line_of(curpos,my_page)
      rendering.render_lines(my_text,curpos,my_page,plo1,plo1+1)
      # render the page line of the cursor only

  elif ac == controlling.ActionCode.LEFT_ARROW:
    with my_text._my_lock:
      rendering.set_text_to_on_screen_start(curpos,my_text)
      if rendering.is_thin(curpos):
        if not html_texting.retreat(my_text):
          print('\u0007')  # BEL
        else:
          rendering.set_on_screen_to_text(my_text,curpos)
          plo1 = rendering.start_page_line_of_back(curpos,my_page)
          rendering.render_lines(my_text,curpos,my_page,plo1,plo1+2)
          # render the present and possible previous cursor page lines
          current_alignment = texting.get_alignment(my_text)
      else:  # fat cursor
        painting.clear_rectangles(my_window)
        rendering.set_on_screen_to_text(my_text,curpos)
        plo1 = rendering.start_page_line_of(curpos,my_page)
        rendering.render_lines(my_text,curpos,my_page,plo1,plo1+1)
        # render the page line of the cursor only
  
  elif ac == controlling.ActionCode.RIGHT_ARROW:
    with my_text._my_lock:
      rendering.set_text_to_on_screen_end(curpos,my_text)
      if rendering.is_thin(curpos):
        if  not html_texting.advance(my_text):
          print('\u0007')  # BEL
        else:
          rendering.set_on_screen_to_text(my_text,curpos)
          plo1 = rendering.start_page_line_of(curpos,my_page)
          rendering.render_lines(my_text,curpos,my_page,plo1,plo1+2)
          # render the present and possible previous cursor page lines
          current_alignment = texting.get_alignment(my_text)
      else:  # fat cursor
        painting.clear_rectangles(my_window)
        rendering.set_on_screen_to_text(my_text,curpos)
        plo1 = rendering.start_page_line_of(curpos,my_page)
        rendering.render_lines(my_text,curpos,my_page,plo1,plo1+1)
        # render the page line of the cursor only
  
  elif ac == controlling.ActionCode.CTRL_S:
    save_file(persisting.get_current_file_name(my_persistents))
      
  else:
    pass


def alignment_bar_item_hit(win,x,y,l):
  """ 
  pre:
    win = window to which this menu is to be added
    (x,y) = position of mouse hit relative to window contents
    my_persistents = persistent variables for the Emily app
    my_text = current text
    curpos = current cursor position in page
  
  post: 
    alignment menu has been built and displayed in win
    current_alignment = alignment of line containing start of cursor in my_text

  test:
    once thru
  """
  global curpos
  global current_alignment
  global my_persistents
  global my_text
  rendering.set_text_to_on_screen_start(curpos,my_text)
  current_alignment = texting.get_alignment(my_text)
  sm = menuing.new_menu(win)
  fs = persisting.get_menu_font_size(my_persistents)
  label = build_tagged_label("Begin",current_alignment == texting.Alignment.BEGIN)
  menuing.add_menu_item(sm,fs,label,begin_alignment_item_hit)
  label = build_tagged_label("Middle",current_alignment == texting.Alignment.MIDDLE)
  menuing.add_menu_item(sm,fs,label,middle_alignment_item_hit)
  label = build_tagged_label("End",current_alignment == texting.Alignment.END)
  menuing.add_menu_item(sm,fs,label,end_alignment_item_hit)
  menuing.display(sm,win,x,y)
    

def begin_alignment_item_hit(win,x,y,l):
  """ 
  pre:
    curpos = position of cursor on the page
    my_text = text being edited
    my_page = page to which my_text is rendered
  
  post: 
    current_alignment =  BEGIN
    the alignment of the paragraph containing the cursor 
      in my_text has been set to BEGIN
    the text and cursor have been re-rendered on my_page

  test:
    once thru
  """
  set_current_alignment(texting.Alignment.BEGIN)
    

def character_key_hit(cp):
  """ 
  pre:
    cp = code point of character key that has just been hit by the user
    my_text = current text
    curpos = current cursor position in text and on screen

  post:
    cp has been inserted in text at required position,
      as an HtmlCharacter
    text and cursor have been re-rendered on screen

  syntax:
    HTML Grammar version 1 Dec 2018   15:05

    This grammar defines the basic HTML constructs common to any HTML file.

    This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::==  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

    Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
    
    The rules are case-sensitive, unlike HTML5.
    
    HtmlCharacter  ::==  ( & a m p ;
                         | & g t ;
                         | & l t ;
                         | any Unicode code point except '&' (U+26), '>' (U+3E) and '<' (U+3C)
  test:
    cp == 'a' (check Save button on menu)
    cp = '&'
    cp = '<'
    cp = '>'
    cp = '%'
  """
  global my_text
  with my_text._my_lock:
    rendering.set_text_to_on_screen_end(curpos,my_text)
    # insert HtmlCharacter
    if cp == ord('>'):
      texting.insert_code_point(my_text,ord('&'))
      texting.insert_code_point(my_text,ord('g'))
      texting.insert_code_point(my_text,ord('t'))
      texting.insert_code_point(my_text,ord(';'))
      
    elif cp == ord('<'):
      texting.insert_code_point(my_text,ord('&'))
      texting.insert_code_point(my_text,ord('l'))
      texting.insert_code_point(my_text,ord('t'))
      texting.insert_code_point(my_text,ord(';'))
      
    elif cp == ord('&'):
      texting.insert_code_point(my_text,ord('&'))
      texting.insert_code_point(my_text,ord('a'))
      texting.insert_code_point(my_text,ord('m'))
      texting.insert_code_point(my_text,ord('p'))
      texting.insert_code_point(my_text,ord(';'))
      
    else:
      texting.insert_code_point(my_text,cp)
      
    render_modified_text()
      

def end_alignment_item_hit(win,x,y,l):
  """ 
  pre:
    curpos = position of cursor on the page
    my_text = text being edited
    my_page = page to which my_text is rendered

  post: 
    current_alignment =  END
    the alignment of the paragraph containing the cursor 
      in my_text has been set to END
    the text and cursor have been re-rendered on my_page

  test:
    once thru
  """
  set_current_alignment(texting.Alignment.END)
    
  
def file_bar_item_hit(win,x,y,l):
  """ 
  pre:
    win = window to which this menu is to be added
    (x,y) = position of mouse hit relative to window contents
    my_text = current text
    is_loaded = true, iff current text was loaded from a file
    my_persistents = persistent variables for the Emily app

  post: 
    file menu has been built and displayed in win

  test:
    new text (not loaded)
    text loaded, not modified
    text loaded, modified
  """
  global my_text
  global my_persistents
  fm = menuing.new_menu(win)
  fs = persisting.get_menu_font_size(my_persistents)
  menuing.add_menu_item(fm,fs,"New",new_item_hit)
  menuing.add_menu_item(fm,fs,"Load",load_item_hit)
  with my_text._my_lock:
    text_has_been_modified = texting.has_been_modified(my_text)
  if text_has_been_modified:
    l = save_item_hit
  else:
    l = None
  menuing.add_menu_item(fm,fs,"Save (Ctrl-S)",l)
  menuing.add_menu_item(fm,fs,"Save As",save_as_item_hit)
  menuing.add_menu_item(fm,fs,"Print",print_item_hit)
  menuing.display(fm,win,x,y)
    
  
def font_bar_item_hit(win,x,y,l):
  """ 
  pre:
    win = window to which this menu is to be added
    (x,y) = position of mouse hit relative to window contents
    my_persistents = persistent variables for the Emily app

  post: 
    font menu has been built and added to win    

  test:
    once thru
  """
  global my_persistents
  fs = persisting.get_menu_font_size(my_persistents)
  fom = menuing.new_menu(win)
  add_font_menu_item(fs,"Arial",fom)
  add_font_menu_item(fs,"Courier New",fom)
  add_font_menu_item(fs,"Times New Roman",fom)
  menuing.add_separator(fom)
  MINIMUM_FONT_SIZE = 9
  MAXIMUM_FONT_SIZE = 48
  STEP1 = 12
  STEP2 = 20
  pfs = MINIMUM_FONT_SIZE
  inc = 1
  while pfs <= MAXIMUM_FONT_SIZE:
    label = build_tagged_font_size_label(pfs,int(persisting.get_text_font_size(my_persistents)))
    menuing.add_menu_item(fom,fs,label,text_font_size_item_hit)
    if pfs == STEP1 or pfs == STEP2:
      inc = inc + inc
    pfs = pfs + inc
  menuing.display(fom,win,x,y)


def font_name_item_hit(win,x,y,l):
  """
  pre:
    l = font name of menu item, possibly preceded by dots and spaces, as str
    my_text = current text
    the menu item associated with this listener has been hit by the user
    my_persistents = persistent variables for the Emily app
    my_page = current page being edited
    curpos = current cursor position

  post:
    the persistent text font name has been modified
    the text in my_window has been redisplayed

  test:
    once thru
  """
  global curpos
  global my_page
  global my_persistents
  global my_text
  fname = name_of(l)
  persisting.set_text_font_name(my_persistents,fname)
  rendering.set_text_font_name(my_page,fname)
  # re-display text and cursor
  with my_text._my_lock:
    rendering.set_text_to_on_screen_end(curpos,my_text)
    rendering.set_on_screen_to_text(my_text,curpos)
    # curpos has text position set
    windowing.clear(win)
    rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
    # curpos has text and page positions set
    rendering.render_thin_cursor(curpos,my_page)
    texting.set_modified(my_text)


def get_latest_version_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    my_persistents = persistent variables for the Emily app

  post:
    Information to get the latest version of Emily has been displayed to the user.

  test:
    once thru
  """
  global _my_persistents
  dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Get latest version","To download the latest version of Emily, go to\n\n" + "https://sourceforge.net/projects/emilyeditor/?source=directory")


def load_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    my_text = current texting.Text
    is_loaded = True, iff current text has been loaded from a file
    my_persistents = persistent variables for the Emily app
    
  post:
    the user has been asked to save the current text, if necessary
    the user has been asked for a file to load
    if the user agrees, the file has been loaded

  test:
    no file to be saved
      user wants to load
    file to be saved
      user declines to load
  """
  global my_persistents
  global my_text
  try:
    # save current text if necessary
    check_save(my_text)
      
    # ask user which file to load
    lf = file_dialoging.show_open_file_dialog(persisting.get_menu_font_size(my_persistents),"Load file",persisting.get_current_file_name(my_persistents),file_dialoging.SortMode.LATEST_FIRST)
    if lf == None:
      raise Exception("Problem opening file. File has not been loaded.")    
    else:
      lf = check_file_type(lf)
      if lf != None:
        load_file(lf)
  except Exception as ex:
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Emily: error while loading input file", str(ex))
    
      
def menu_font_size_menu_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    win = window in which Menu Font Size menu is to be displayed
    (x,y) = position in window contents of hit, as floats
    my_persistents = persistent variables for the Emily app

  post:
    the Menu Font Size menu has been displayed at (x,y) in win,
      using the font size given in the persistents file

  test:
    once thru
  """
  global _my_persistents
  fs = persisting.get_menu_font_size(my_persistents)
  mfsm = build_menu_font_size_menu(fs)
  menuing.display(mfsm,win,x,y)
    

def menu_font_size_item_hit(win,x,y,l):
  """
  pre:
    menu item associated with this callback procedure has been hit by user
    win = windowing.Window where mouse-hit occurred
    x,y = x and y offsets of mouse hit from top left-hand corner of window's contents, in points as float
    l = label of menu item hit by the user, giving required font size as str
    my_persistents = persistent variables for the Emily app
    
  post:
    menu font size has been set to value specified by user
    menu bar and zoom buttons have been modified to the new menu font size
    the font size has been saved in the persistents file

  test:
    once thru
  """
  my_font_size = float(int_of(l))
  global my_persistents
  persisting.set_menu_font_size(my_persistents,my_font_size)
  menuing.set_menu_bar_font_size(win,my_font_size)
  windowing.set_font_size(win,my_font_size)
  
  
def middle_alignment_item_hit(win,x,y,l):
  """ 
  pre:
    curpos = position of cursor on the page
    my_text = text being edited
    my_page = page to which my_text is rendered

  post: 
    current_alignment =  MIDDLE
    the alignment of the paragraph containing the cursor in my_text has been set to MIDDLE
    the text and cursor have been re-rendered on my_page

  test:
    once thru
  """
  set_current_alignment(texting.Alignment.MIDDLE)


def new_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    win = main window of this app
    my_text = current texting.Text
    my_page = current Page
    is_loaded = True, iff current text is loaded

  post:
    the user has been asked to save the current text, if necessary
    a blank Page has been created and displayed

  test:
    no current text
    current text 
      not loaded
        unmodified
        modified
      loaded
        not modified
        modified
  """
  global curpos
  global is_loaded
  global my_page
  global my_persistents
  global my_text
  # save current text if necessary
  check_save(my_text)
    
  # set up new text
  with my_text._my_lock:
    my_text = texting.new_text()
    texting.set_unmodified(my_text)
  is_loaded = False
  # remove any old file name from title
  windowing.set_title(win,title_of(None))
  # clear window
  windowing.clear(win)
  # set the page's text cursor position to (0,0)
  my_page._text_position.line_offset = 0
  my_page._text_position.code_point_offset = 0
  # set the page's page cursor position to (0.0,0.0)
  my_page._page_position.x_offset = 0.0
  my_page._page_position.y_offset = 0.0
  # set cursor start and end to start of text
  rendering.set_cursor_position_to_start(curpos)
  # draw cursor at origin
  cursoring.draw_cursor(win,persisting.get_text_font_size(my_persistents),persisting.get_horizontal_indent(my_persistents),persisting.get_vertical_indent(my_persistents),coloring.BLACK)
    
  
def print_item_hit(win,x,y,l):
  """ 
  pre:
      the menu item associated with this listener has been hit by the user
      win = current window
      my_text = text to be printed
      persisting.get_text_font_name(my_persistents) = font name to be used
      persisting.get_text_font_size(my_persistents) = font size to be used

  post:
      the current text has been printed on the default printer

  test:
    blank text
      Printer problem causing exception
      Printer OK
    text of two or more lines
  """
  global my_persistents
  global my_text
  fss = font_styling.new_font_styles()
  text_printing.print_text(win,my_text,persisting.get_text_font_name(my_persistents),persisting.get_text_font_size(my_persistents),fss)
    
  
def save_as_item_hit(win,x,y,l):
  """ 
  pre:
      the menu item associated with this listener has been hit by the user

  post:
      the user has been asked for the name to save the current text as
      if the user agrees, the text has been saved under the specified name
      The user has been informed of successful or unsuccessful saving

  test:
    user agrees
    user disagrees
  """
  save_file_as()
    
  
def save_item_hit(win,x,y,l):
  """ 
  pre:
    the menu item associated with this listener has been hit by the user
    persisting.get_current_file_name(my_persistents) = default file name

  post:
      the current text has been saved under its default file name

  test:
    once thru
  """
  global my_persistents
  save_file(persisting.get_current_file_name(my_persistents))
    
  
def setup_bar_item_hit(win,x,y,l):
  """ 
  pre:
    win = window to which this menu is to be added
    (x,y) = position of mouse hit relative to window contents
    my_persistents = persistent variables for the Emily app

  post: 
    setup menu has been built and displayed in win

  test:
    once thru
  """
  sm = menuing.new_menu(win)
  global my_persistents
  fs = persisting.get_menu_font_size(my_persistents)
  menuing.add_menu_item(sm,fs,"Menu Font Size",menu_font_size_menu_item_hit)
  menuing.add_menu_item(sm,fs,"Get latest version",get_latest_version_item_hit)
  emily_version = "About Emily " + VERSION
  menuing.add_menu_item(sm,fs,emily_version,about_item_hit)
  menuing.display(sm,win,x,y)
    
    
def text_font_size_item_hit(win,x,y,l):
  """ 
  pre:
    l = font size of menu item, as str
    the menu item associated with this listener has been hit by the user
    my_persistents = persistent variables for the Emily app
    my_page = current page being edited
    my_text = current text being edited
    
  post:
    the persistent text font size has been modified
    the text in my_page has been redisplayed
    curpos = current cursor position

  test:
    once thru
  """
  global curpos
  global my_page
  global my_persistents
  global my_text
  fsize = float(int_of(l))
  persisting.set_text_font_size(my_persistents,fsize)
  rendering.set_text_font_size(my_page,fsize)
  # re-display text and cursor
  with my_text._my_lock:
    rendering.set_text_to_on_screen_end(curpos,my_text)
    rendering.set_on_screen_to_text(my_text,curpos)
    # curpos has text position set
    windowing.clear(win)
    rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
    # curpos has text and page positions set
    rendering.render_thin_cursor(curpos,my_page)
    texting.set_modified(my_text)


def window_closing(win):
  """ 
  pre:
    win = window associated with this callback
    the user has pressed the Close button of win
    my_text = Texting.Text being edited
    my_persistents = persistent variables for the Emily app
    
  post:
    returns true iff app is to close
    if true is returned, clean-up has been done prior to shutdown 

  test:
    text to be saved
    no text to be saved
  """
  global my_persistents
  global my_text
  check_save(my_text)
  wb = persisting.get_window_bounds(my_persistents)
  persisting.set_window_bounds(my_persistents,window_bounding.get_bounds(win))
  wb2 = persisting.get_window_bounds(my_persistents)
  persisting.set_zoom_factor(my_persistents,windowing.zoom_factor_of(win))
  return True


def window_opening(win):
  """
  pre:
    win = window associated with this callback
    curpos = cursor position in Text and Page
    file_name = name of file to be loaded, or None if none
    my_persistents = persistent variables for the Emily app
    text_font_style = text font style for this file
    
  post:
    my_page has been set up according to the persistent variables
    file_name, if not None, has been loaded
    is_loaded = True, iff file has been loaded
    the text, if any, has been displayed on the screen
    the cursor has been set to the end of the text
    text_font_style = current text font style
    controlling and keyboard callbacks have been set up for win
    mousing callbacks have been set up for win
    
  test:
    frame maximized on previous run
    frame midimized on previous run
      persisting.get_current_file_name(my_persistents) == null
      persisting.get_current_file_name(my_persistents) != null
  test:
    file_name = None
    file_name = valid file
  """
  global curpos
  global file_name
  global is_loaded
  global text_font_style
  global my_page
  global my_persistents
  wb = window_bounding.get_bounds(win)
  pwb = persisting.get_window_bounds(my_persistents)
  window_bounding.set_bounds(win,persisting.get_window_bounds(my_persistents))
  wb2 = window_bounding.get_bounds(win)
  my_page = rendering.new_page(win,persisting.get_paper_width(my_persistents),persisting.get_paper_height(my_persistents),persisting.get_horizontal_indent(my_persistents),persisting.get_vertical_indent(my_persistents),persisting.get_text_font_name(my_persistents),text_font_style,persisting.get_text_font_size(my_persistents),coloring.BLACK)
  if file_name != None:
    load_file(file_name)
  else:
    persisting.set_text_font_name(my_persistents,DEFAULT_FONT_NAME)
    persisting.set_text_font_size(my_persistents,DEFAULT_FONT_SIZE)
    is_loaded = False
    # set cursor start and end to start of text
    rendering.set_cursor_position_to_start(curpos)
    # draw cursor at origin
    cursoring.draw_cursor(win,persisting.get_text_font_size(my_persistents),persisting.get_horizontal_indent(my_persistents),persisting.get_vertical_indent(my_persistents),coloring.BLACK)
  controlling.attach(win,action_key_hit)
  keyboarding.attach(win,character_key_hit)
  ml = MouseListener()
  mousing.attach(ml,win)
  show_splash_screen()


# Callback classes
# ----------------

class MouseListener(mousing.MouseListener):
  
  def double_clicked(self,x,y):
    """
    pre:
      the primary mouse button has been clicked (pressed and released) twice in quick succession (< 0.5 sec) by the user
      (x,y) = position in points at which the mouse pointer was double-clicked, relative to the top left-hand corner of the window's pane, as floats 

    post:
      the action required by the user has been carried out

    test:
    """
    print("Start of double_clicked")


  def mouse_clicked(self,x,y):
    """
    pre:
      the primary mouse button has been clicked (pressed and released) once by the user
      (x,y) = position in points at which the mouse pointer was clicked, 
                relative to the top left-hand corner of the window's pane, as floats
      my_page = rendering.Page on which mouse-hit occurred
      my_text = current texting.Text
      curpos = current position of cursor
    
    post:
      the cursor has been replaced by a thin cursor at (x,y) on the Page
        and the equivalent (lo,cpo) in the Text
      
    test:
      empty text
      text of two lines or more
    """
    global my_text
    global my_page
    global curpos
    # relativize (x,y) to tlh corner of text
    x -= my_page._horizontal_indent
    y -= my_page._vertical_indent
    
    # find nearest glyph interstice as (page_line_offset, page_glyph_offset, xoff, yoff)
    (plo,pgo,xoff,yoff) = rendering.nearest_glyph_interstice_of(x,y,my_page)
    
    # convert (plo,glo) to (line_offset, code_point_offset) in Text
    (lo,cpo) = rendering.text_position_of(plo,pgo,my_page)
    
    # set up curpos for thin cursor at point of mouse hit in Text and Page
    rendering.set_thin_cursor_text_and_page(curpos,lo,cpo,xoff,yoff)
    # allow lateral movement
    curpos.update_x_offset = True
    # render the thin cursor
    with my_text._my_lock:
      texting.set_cursor(my_text,lo,cpo)
    rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
    rendering.render_thin_cursor(curpos,my_page)
    
    
  def mouse_dragged(self,x,y):
    """
    pre:
      the mouse has been dragged (moved with the primary mouse-button pressed)
        at least 5 points by the user from its previous position
      (x,y) = position in points to which the mouse pointer was dragged, 
        relative to the top left-hand corner of the window's pane, as floats 
      pivot = start position in Text and Page of this mouse-drag operation
      my_text = current Text being edited
      my_page = current Page being rendered
      my_window = current main window
      curpos = current cursor position
    
    post:
      curpos has been set to the section of text between the pivot and 
        the current mouse position
      curpos._start_text_position <= curpos._end_text_position
    
    test:
    """
    global curpos
    global my_page
    global my_persistents
    global my_text
    global my_window
    global pivot
    x_in_text = x - persisting.get_horizontal_indent(my_persistents)
    y_in_text = y - persisting.get_vertical_indent(my_persistents)
    (lo,go,xoff,yoff) = rendering.nearest_glyph_interstice_of(x_in_text,y_in_text,my_page)
    (tlo,cpo) = rendering.text_position_of(lo,go,my_page)
    mouse_position = rendering.new_cursor_position()
    rendering.set_thin_cursor_text_and_page(mouse_position,tlo,cpo,xoff,yoff)
    if rendering._less_than_text_position(pivot._start_text_position,mouse_position._start_text_position):
      curpos._start_text_position.line_offset = \
        pivot._start_text_position.line_offset
      curpos._start_text_position.code_point_offset = \
        pivot._start_text_position.code_point_offset
      curpos._start_page_position.x_offset = pivot._start_page_position.x_offset
      curpos._start_page_position.y_offset = pivot._start_page_position.y_offset
      curpos._end_text_position.line_offset = mouse_position._start_text_position.line_offset
      curpos._end_text_position.code_point_offset = mouse_position._start_text_position.code_point_offset
      curpos._end_page_position.x_offset = mouse_position._start_page_position.x_offset
      curpos._end_page_position.y_offset = mouse_position._start_page_position.y_offset
    else:
      curpos._start_text_position.line_offset = mouse_position._start_text_position.line_offset
      curpos._start_text_position.code_point_offset = mouse_position._start_text_position.code_point_offset
      curpos._start_page_position.x_offset = mouse_position._start_page_position.x_offset
      curpos._start_page_position.y_offset = mouse_position._start_page_position.y_offset
      curpos._end_text_position.line_offset = pivot._start_text_position.line_offset
      curpos._end_text_position.code_point_offset = pivot._start_text_position.code_point_offset
      curpos._end_page_position.x_offset = pivot._start_page_position.x_offset
      curpos._end_page_position.y_offset = pivot._start_page_position.y_offset
    painting.clear_rectangles(my_window)  # get rid of old fat cursor
    rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)

    
  def mouse_popup(self,x,y,win,window_x,window_y):
    """
    pre:
      the user has gestured that a popup menu should be displayed. On some platforms, this is done by clicking the right mouse button.
      (x,y) = position in points at which the mouse pointer was clicked, relative to the top left-hand corner of the window's pane, as floats
      win = windowing.Window in which the gesture was made
      (window_x,window_y) = position in points required for popup menu, relative to the top left-hand corner of the window's contents, as floats 
    
    post:
      the action (if any) required by the user has been carried out
    
    test:
    """
    print("Start of mouse_popup")


  def mouse_pressed(self,x,y):
    """
    pre:
      the user has pressed the primary mouse-button, signifying the start of a mouse-drag operation
      (x,y) = position in points of the mouse pointer when the mouse button was pressed, relative to the top left-hand corner of the window's pane, as floats 
      my_persistents = persistent variables for the Emily app
      my_page = current page
  
    post: 
      the start and end points of the cursor have been set to the position
        in the Text and Page equivalent to the mouse_pressed position
      the pivot for the mouse-drag has been set to the position
        in the Text and Page equivalent to the mouse_pressed position
      
    test:
      once thru (check pivot)
    """
    global curpos
    global my_page
    global my_persistents
    global pivot
    x_in_text = x - persisting.get_horizontal_indent(my_persistents)
    y_in_text = y - persisting.get_vertical_indent(my_persistents)
    (lo,go,xoff,yoff) = rendering.nearest_glyph_interstice_of(x_in_text,y_in_text,my_page)
    (tlo,cpo) = rendering.text_position_of(lo,go,my_page)
    # set the cursor start and end
    rendering.set_thin_cursor_text_and_page(curpos,tlo,cpo,xoff,yoff)
    # set the pivot start and end
    rendering.set_thin_cursor_text_and_page(pivot,tlo,cpo,xoff,yoff)
    rendering.render_thin_cursor(curpos,my_page)

  def mouse_released(self,x,y):
    """
    pre:
      the user has released the primary mouse-button, signifying the end of a mouse-drag operation
      (x,y) = position in points of the mouse pointer when the mouse button was released, relative to the top left-hand corner of the window's pane, as floats 
    
    post:
      the action (if any) required by the user has been carried out
    
    test:
    """
    print("Start of mouse_released")

  
# sub-procedures
# --------------

def add_font_menu_item(fs,s,m):
  """ 
  pre:
    fs = font size for this menu item
    s = label of this font menu item
    m = menu to which this menu item is to be added
    my_persistents = persistent variables for the Emily app
  
  post:
    specified font menu item has been added to m

  test:
    s == persisting.get_text_font_name(my_persistents)
    s != persisting.get_text_font_name(my_persistents)
  """
  global my_persistents
  label = build_tagged_label(s, s == persisting.get_text_font_name(my_persistents))
  menuing.add_menu_item(m,fs,label,font_name_item_hit)
  

def build_menu_bar(win):
  """ 
  pre:
    my_persistents = persistent variables for the Emily app
    win = window on which this menu bar is to be built
  
  post:
    menu bar has been set up on win

  test:
    once thru
  """
  global my_persistents
  menuing.add_menu_bar_item(win,persisting.get_menu_font_size(my_persistents),"File",file_bar_item_hit)
  menuing.add_menu_bar_item(win,persisting.get_menu_font_size(my_persistents),"Font",font_bar_item_hit)
  menuing.add_menu_bar_item(win,persisting.get_menu_font_size(my_persistents),"Alignment",alignment_bar_item_hit)
  menuing.add_menu_bar_item(win,persisting.get_menu_font_size(my_persistents),"Setup",setup_bar_item_hit)
  

def build_menu_font_size_menu(fs):
  """ 
  pre:
    fs = font size with which menu is to be built, as int
    my_window = current window for this app
  
  post:
    MenuFontSizeMenu has been built and returned

  test:
    once thru with valid fs
  """
  MINIMUM_FONT_SIZE = 9
  MAXIMUM_FONT_SIZE = 24
  global my_window
  mfsm = menuing.new_menu(my_window)
  pfs = MINIMUM_FONT_SIZE
  while pfs <= MAXIMUM_FONT_SIZE:
    label = build_tagged_font_size_label(pfs,fs)
    menuing.add_menu_item(mfsm,fs,label,menu_font_size_item_hit)
    pfs += 1
  return mfsm
  

def build_tagged_font_size_label(pfs,tfs):
  """ 
  pre:
    pfs = point font size to be used in label, as int
    tfs = point font size to be tagged, as int

  post:
    appropriate label has been returned, as str

  test:
    pfs == tfs
    pfs != tfs
  """
  label = "" + str(pfs) + " point"
  return build_tagged_label(label,pfs == tfs)
  

def build_tagged_label(l,b):
  """ 
  pre:
    l = raw label to be possibly tagged, as str
    b = True, iff l is to be tagged
    
  post:
    appropriate label has been returned, as str

  test:
    b = true
    b = false
  """
  label = ""
  if b:
    label +="• "
    # unicode Bullet Point
  else:
    label += "   "
  label += l
  return label
  

def build_u_i():
  """ 
  pre:  
    my_persistents = persistent variables for the Emily app
    my_window = current window for this app

  post:
    my_window has been set up and displayed
    the zoom factor of the window has been set
    is_loaded = false

  test:
    once thru
  """
  global is_loaded
  global my_persistents
  global my_window
  zoom_factor = persisting.get_zoom_factor(my_persistents)
  my_window = windowing.new_window(persisting.get_menu_font_size(my_persistents),title_of(None),persisting.get_paper_width(my_persistents),persisting.get_paper_height(my_persistents),1.0)
  windowing.set_zoom_factor(my_window,zoom_factor)
  build_menu_bar(my_window)
  is_loaded = False
  windowing.show(my_window,window_opening,window_closing)
  
  
def check_file_type(f):
  """
  pre:
    f = filename to be checked, as str
    my_persistents = persistent variables for the Emily app

  post:
    if f is not a file of type .mle,
      returns None
    else
    returns the filename

  test:
     fred.mlf
     fred.mle
  """
  global my_persistents
  if f[-4:] != ".mle":
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Emily: error in file name", "File name " + str(f) + " is not of type .mle")
    return None
  else:
    return f


def check_save(t):
  """ 
  pre:
    t = text which may need saving
    is_loaded = true, iff current text has been loaded from a file
    my_persistents = persistent variables for the Emily app
  
  post:
    if t has been modified, user has been asked whether they want to save it
      and under what name, if necessary

  test:
    text has not been modified
    text has been modified
      user doesn't want to save
      user wants to save
        text is loaded from file
        text is not loaded from file
  """
  global is_loaded
  global my_persistents
  with t._my_lock:
    text_has_been_modified = texting.has_been_modified(t) 
  if text_has_been_modified:
    user_wants_to_save = dialoging.show_confirm_dialog(persisting.get_menu_font_size(my_persistents),"Text has been modified","The text has been modified.  Do you wish to save it?")
    if user_wants_to_save:
      if is_loaded:
        fn = persisting.get_current_file_name(my_persistents)
        saved_o_k = save_file(fn)
        # if successful, inform user
        if saved_o_k:
          show_successful_save_message(fn)       
      # file is not loaded
      else:
        persisting.set_current_file_name(my_persistents,None)
        save_file_as()
        

def int_of(s):
  """
  pre:
    s = string containing an integer
    
  post:
    the first integer encountered in s has been returned as an int
    
  test:
    s = ""
    s = "fred"
    s = "  90"
    s = "  909 points"
  """
  i = 0
  # find start of integer
  while i < len(s) and (s[i] < '0' or s[i] > '9'):
    i += 1
  if i == len(s):
    raise Exception("int_of cannot find an integer in string \""+ s + "\"")
  #convert integer
  res = 0
  while i < len(s) and s[i] >= '0' and s[i] <= '9':
    res = res*10 + ord(s[i])- ord('0')
    i += 1
  return res


def load_file(s):
  """ 
  pre:
    s = name of .mle file to be loaded, as str
    my_persistents = persistent variables for the Emily app
    my_window = Emily's main window
    my_text = text for this instantiation of Emily
    text_font_style = FontStyles set for this text
    my_page = page to which this file is to be rendered
    
  post:
    Either:
      file s has been loaded as a text in Emily
        and displayed on the screen via my_page
      current_alignment has been set to the alignment of the paragraph containing the cursor
      Emily's title has been updated
      text_font_name and text_font_size have been set up with values from the file s
      is_loaded = true
      File menu has been updated to correspond to is_loaded
      the cursor has been rendered at the end of the text
      curpos = current position of cursor
    or 
      an exception has been thrown and displayed to the user

  test:
    file loads successfully
    file fails to load (e.g. from removed memory stick)
  """
  global curpos
  global current_alignment
  global is_loaded
  global my_persistents
  global my_page
  global my_text
  global my_window
  try:
    empty = ""    # blank current file name
    persisting.set_current_file_name(my_persistents,empty)
    # blank window's title
    windowing.set_title(my_window,title_of(empty))
    la = looking_ahead.lookahead_of(s)
    with my_text._my_lock:
      # parse Emily document to my_text
      r = mle_parsing.parse_mle_document(la)
      # set up new text
      my_text = mle_parsing.text_of(r)
      texting.set_unmodified(my_text)
      # set on-screen cursor's line offset and glyph offset (end of text)
      rendering.set_on_screen_to_text(my_text,curpos)
      # set the current alignment to alignment at cursor position (end of text)
      current_alignment = texting.get_alignment(my_text)
      # set up document's font name and size as persistent variables
      #  and in my_page
      font_name = unicoding3_0.python_string_of(mle_parsing.font_name_of(r))
      persisting.set_text_font_name(my_persistents,font_name)
      rendering.set_text_font_name(my_page,persisting.get_text_font_name(my_persistents))
      persisting.set_text_font_size(my_persistents,mle_parsing.font_size_of(r))
      rendering.set_text_font_size(my_page,persisting.get_text_font_size(my_persistents))
      # clear the window
      windowing.clear(my_window)
      # display text
      texting.set_cursor_start(my_text)
      rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
      # this has set curpos to the end of the text
      #   in the text and on the screen
      rendering.render_thin_cursor(curpos,my_page)
      
    # update current file name
    persisting.set_current_file_name(my_persistents,s)
    # update window's title
    windowing.set_title(my_window,title_of(s))
    # update is_loaded and File menu
    is_loaded = True
    #update_file_menu(persisting.get_menu_font_size(my_persistents),my_file_menu);
    
  except Exception as ex:
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Emily: error while loading input file", str(ex))
    
    
def name_of(s):
  """
  pre:
    s = font name, with possible preceding dots and spaces, as str
    the name in s must start with an alphabetic character,
      but may contain any character thereafter
    
  post:
    font name has been returned
    
  test:
    s = ""
    s = "£££££"
    s = "fredfont"
    s = "& Times New Roman"
  """
  # find name
  i = 0
  while i < len(s) and not s[i].isalpha():
    i += 1
  if i == len(s):
    raise Exception("name_of cannot find a name in string \"" + s + "\"")
  # make result equal to name
  res = ""
  while i < len(s):
    res += s[i]
    i += 1
  return res


def print_cursor(oscp):
  print("OnScreenCursorPosition:")
  print("  oscp._text_position.line_offset="+str(oscp._text_position.line_offset))
  print("  oscp._text_position.code_point_offset="+str(oscp._text_position.code_point_offset))
  print("  oscp._page_position.x_offset="+str(oscp._page_position.x_offset))
  print("  oscp._page_position.y_offset="+str(oscp._page_position.y_offset))
  print("  oscp._desired_x_offset="+str(oscp._desired_x_offset))
  print("  oscp._update_x_offset="+str(oscp._update_x_offset))
  print("  oscp._current_text_position.line_offset="+str(oscp._current_text_position.line_offset))
  print("  oscp._current_text_position.code_point_offset="+str(oscp._current_text_position.code_point_offset))
  print("  oscp._current_page_position.x_offset="+str(oscp._current_page_position.x_offset))
  print("  oscp._current_page_position.y_offset="+str(oscp._current_page_position.y_offset))
  print("  oscp._minimum_page_distance="+str(oscp._minimum_page_distance))    


def print_window_bounds(wb):
  print("window bounds:")
  print("  x="+str(window_bounding.get_x(wb)))
  print("  y="+str(window_bounding.get_y(wb)))
  print("  width="+str(window_bounding.get_width(wb)))
  print("  height="+str(window_bounding.get_height(wb)))
  
  
def render_cursor_left_right():
  """ 
  pre:
    my_text = text to be rendered, with cursor at required position in text
    my_page = page on which text is to be rendered
    curpos = current position of cursor
  
  post:
    text and cursor have been rendered on my_page
    current_alignment = alignment of paragraph containing cursor
  
  note:
    this procedure must be called from inside a block synchronized on my_text

  test:
    once thru
  """
  global curpos
  global current_alignment
  global my_page
  global my_text    
  rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
  # curpos has text and page position set
  rendering.set_text_to_on_screen_start(curpos,my_text)
  current_alignment = texting.get_alignment(my_text)
  rendering.render_thin_cursor(curpos,my_page)
  

def render_modified_text():
  """ 
  pre:
    my_text = text which has been modified
    my_text's cursor is at required position of cursor on screen
    my_page = page to which my_text is to be rendered
    my_page's back map has been set up
    curpos's start page position <= 
      y-offset of start of modified portion of text on page

  post:
    my_text has been rendered to my_page with cursor at required position
    my_text has been marked as modified
    curpos = current cursor position in text and screen

  note:
    this procedure must be called from inside a block synchronized on my_text

  test:
    once thru
  """
  global my_page
  global my_text
  global curpos
  rendering.set_on_screen_to_text(my_text,curpos)
  # curpos has text position set
  start_line = rendering.start_page_line_of(curpos,my_page)
  rendering.render_lines(my_text,curpos,my_page,start_line,rendering.TO_END)
  # curpos has text and page positions set
  rendering.render_thin_cursor(curpos,my_page)
  texting.set_modified(my_text)
  

def save_file(s):
  """ 
  pre:
    s = name of file to be saved
    is_loaded = True, iff loaded file is s
    VERSION = current version of Emily
    my_text = text to be output as contents of file
    my_persistents = persistent variables for the Emily app
  
  post:
    Either:
      my_text has not been modified, and no action has been taken
      True has been returned
    Or:
      specified file has been saved from Emily's text
      persisting.get_current_file_name(my_persistents) = s
      my_text state has been set to unmodified
      is_loaded = True
      True has been returned
    Or: 
      an exception has been thrown and displayed to the user
      False has been returned

  test:
    file is not loaded
    file is loaded
      file saves successfully
      file fails to save (e.g. to removed memory stick)
  """
  global is_loaded
  global my_persistents
  global my_text
  if texting.has_been_modified(my_text):
    if not is_loaded:
      save_file_as()
      return True
    else:
      try:
        w = unicode_io.new_output_writer(s)
        font_name = unicoding3_0.string_of(persisting.get_text_font_name(my_persistents))
        mle_emitting.emit_emily_document(font_name,persisting.get_text_font_size(my_persistents),unicoding3_0.string_of(VERSION),my_text,w)
        # if we make it to here, save was successful
        persisting.set_current_file_name(my_persistents,s)
        # text and file are the same
        with my_text._my_lock:
          texting.set_unmodified(my_text)
        return True
          
      except Exception as ex:
        dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"Exception writing output file",str(ex))
        raise ex
        return False
    
  
def save_file_as():
  """
  pre:
    VERSION = current version of Emily
    my_text = text to be output as contents of file
    my_persistents = persistent variables for the Emily app
    my_window = main window of Emily
    persisting.get_current_file_name(my_persistents) = name to save file as, 
      or null if default directory
  
  post:
    either:
      user has declined to save
    or
      either:
        specified file has been saved from Emily's text
        persisting.get_current_file_name(my_persistents) = name of saved file
        my_text state has been set to unmodified
        is_loaded = true
        File menu has been updated to correspond to is_loaded
        the user has been informed that the file has been successfuly saved
      or 
        an exception has been thrown and displayed to the user
    main window title has been modified to correspond to the current file name

  test:
    user disagrees
    user agrees
      file saved OK
      file saving fails
  """
  global is_loaded
  global my_persistents
  global my_text
  global my_window
  # display file saving dialog
  s = file_dialoging.show_save_file_dialog(persisting.get_menu_font_size(my_persistents),"Save As",persisting.get_current_file_name(my_persistents),["mle"],file_dialoging.SortMode.LATEST_FIRST)
  if s != None:
    is_loaded = True  # to force the save
    with my_text._my_lock:
      texting.set_modified(my_text)  # to force the save
    saved_o_k = save_file(s)
    # if successful, inform user
    if saved_o_k:
      show_successful_save_message(s)
    windowing.set_title(my_window,title_of(persisting.get_current_file_name(my_persistents)))
  else:
    dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"File save aborted","Problem saving file.  File has not been saved.")
    
  
def set_current_alignment(a):
  """ 
  pre:
    a = required current alignment
    curpos = position of cursor on the page
    my_text = text being edited
    my_page = page to which my_text is rendered
  
  post: 
    current_alignment = a
    the alignment of the paragraph containing the cursor in my_text has been set to a
    the text and cursor have been re-rendered on my_page

  test:
    once thru
  """
  global current_alignment
  global my_text
  current_alignment = a
  with my_text._my_lock:
    rendering.set_text_to_on_screen_end(curpos,my_text)
    texting.set_alignment(my_text,a)
    rendering.render_lines(my_text,curpos,my_page,0,rendering.TO_END)
  

""" 
  pre:  my_persistents.get_splash_screen_on() = state of splash_screen_on
  post: if splash_screen_on,
          starts a thread which shows the splash screen for 1 sec.
  
  """
def show_splash_screen():
  global my_persistents
  #if (persisting.get_splash_screen_on(my_persistents))
  #SplashScreenThread sst = new SplashScreenThread();
  #sst.start();
  pass
  
  pass
  

""" 
  pre:
    fn = name of file which has been successfully saved
    my_persistents has the required menu font size
  post:
    "successful save" message has been shown and accepted by the user.
  """
""" 
  test:
    once thru
  """
def show_successful_save_message(fn):
  global my_persistents
  mess = "The file \"" + fn + "\" has been successfully saved"
  dialoging.show_message_dialog(persisting.get_menu_font_size(my_persistents),"File successfully saved",mess)
  

""" 
  pre:
    s = name of currently loaded file, or null if none
    VERSION = current version of Emily
  post:
    returns title to be displayed in Emily's title bar
  """
""" 
  test:
    s is null
    s is non-null
  """
def title_of(s):
  title = "Emily " + VERSION
  if s != None:
    title += " - " + s    
  return title
  

# --------------------------------------------------------------------------
# main program
# --------------------------------------------------------------------------

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

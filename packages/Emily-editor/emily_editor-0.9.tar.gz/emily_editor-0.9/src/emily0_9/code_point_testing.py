# Contractor for testing Unicode code points.

# author R.N.Bosworth

# version 25 Feb 2023  19:20

from guibits1_0 import type_checking2_0

"""
Contractor for testing Unicode code points.

Copyright (C) 2018,2021,2022,2023  R.N.Bosworth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (gpl.txt) for more details.
"""
"""
  HTML CSS Grammar version 17.3.18   15:39

  This grammar defines the basic HTML constructs common to HTML5 and CSS.

  This grammar is in EBNF (Extended Backus-Naur Form) using the following meta-symbols:  ::=  is  (  )  |  *.  The equivalent terminal characters are called LPARENTHESIS, RPARENTHESIS, BAR and STAR.

  Non-terminals are in CamelCase.  Terminal names are in UPPER_CASE.  Other symbols represent themselves.
  
  The rules are case-sensitive, unlike HTML5.
  
  
  OptionalSpaces  ::=  SpaceChar*

  SpaceChar  ::=  (SPACE | TAB | LF | FF | CR)
                  (U+0020 | U+0009 | U+000A | U+000C | U+000D )
                  
  Separator  ::==  SpaceChar OptionalSpaces
  
  Name  ::=  NameChar NameChar*

  NameChar  ::=  ( a .. z | 0 .. 9 )
                 ( U+0061 .. U+007A | U+0030 .. U+0039 )
                 
"""

# exposed procedures
# ------------------


def is_name_char(cp):
  """
  pre:
    cp = code point to be tested
  
  post:
    returns true iff cp is an HTML NameChar
  """
  """
  NameChar  ::=  ( a .. z | 0 .. 9 )
                 ( U+0061 .. U+007A | U+0030 .. U+0039 )  !!
  """
  """
  test:
    cp is not an int
    cp = ord('@')
              A
              Z
              [
              U+0060
              a
              z
              {
              /
              0
              9
              :         
  """
  type_checking2_0.check_identical(cp,int)
  return (ord('a') <= cp and cp <= ord('z') or ord('0') <= cp and cp <= ord('9'))
  

def is_space_char(cp):
  """
  pre:
    cp = code point to be tested

  post:
    returns true iff cp is an HTML SpaceChar
  """
  """
  SpaceChar  <-  ( SPACE | TAB | LF | FF | CR )
               ( U+0020 | U+0009 | U+000A | U+000C | U+000D )
  """
  """
  test:
    cp is not an int
    cp = SPACE
         TAB
         LF
         FF
         CR
         ord('!')
  """
  type_checking2_0.check_identical(cp,int)
  return (cp == ord(' ') or cp == ord('\t') or cp == ord('\n') or cp == ord('\f') or cp == ord('\r'))
  
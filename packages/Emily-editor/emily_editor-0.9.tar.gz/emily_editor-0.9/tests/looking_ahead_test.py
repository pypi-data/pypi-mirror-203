# Test program for 0ne symbol lookahead stream.

# author R.N.Bosworth

# version 4 Mar 23  16:05

from emily0_9 import looking_ahead
from guibits1_0 import unicoding3_0

"""
Copyright (C) 2012,2015,2016,2017,2018,2021,2022,2023  R.N.Bosworth

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

print("Tests of file instantiation and reading", end=' ')
#l = looking_ahead.lookahead_of("motorbike?$&*")
#l = looking_ahead.lookahead_of("motorbike")
l = looking_ahead.lookahead_of("motorbike.test")
assert looking_ahead.current_symbol_of(l) == ord('x')
assert looking_ahead.current_symbol_of(l) == ord('x')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == ord('y')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == ord('z')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == looking_ahead.END_OF_STREAM
print("OK")

print("Tests of string instantiation and reading", end=' ')
l = looking_ahead.lookahead_of_string(unicoding3_0.string_of("abc"))
assert looking_ahead.current_symbol_of(l) == ord('a')
assert looking_ahead.current_symbol_of(l) == ord('a')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == ord('b')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == ord('c')
looking_ahead.advance(l)
assert looking_ahead.current_symbol_of(l) == looking_ahead.END_OF_STREAM
print("OK")

print("")
print("All tests OK")

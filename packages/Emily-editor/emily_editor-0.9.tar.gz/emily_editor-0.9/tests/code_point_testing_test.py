# Tests of contractor for testing Unicode code points.

# author R.N.Bosworth

# version 2 Mar 2023  14:50

"""
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
# test program
# ------------

from emily0_9 import code_point_testing

print("Tests of code_point_testing.is_name_char", end=' ')
#code_point_testing.is_name_char('@')
assert  not code_point_testing.is_name_char(ord('@'))
assert  not code_point_testing.is_name_char(ord('A'))
assert  not code_point_testing.is_name_char(ord('Z'))
assert  not code_point_testing.is_name_char(ord('['))
assert  not code_point_testing.is_name_char(ord('`'))
assert code_point_testing.is_name_char(ord('a'))
assert code_point_testing.is_name_char(ord('z'))
assert  not code_point_testing.is_name_char(ord('{'))
assert  not code_point_testing.is_name_char(ord('/'))
assert code_point_testing.is_name_char(ord('0'))
assert code_point_testing.is_name_char(ord('9'))
assert  not code_point_testing.is_name_char(ord(':'))
print("OK")

print("Tests of code_point_testing.is_space_char", end=' ')
#code_point_testing.is_space_char(' ')
assert code_point_testing.is_space_char(ord(' '))
assert code_point_testing.is_space_char(ord('\t'))
assert code_point_testing.is_space_char(ord('\n'))
assert code_point_testing.is_space_char(ord('\f'))
assert code_point_testing.is_space_char(ord('\r'))
assert  not code_point_testing.is_space_char(ord('!'))
print("OK")

print("")
print("All tests OK")

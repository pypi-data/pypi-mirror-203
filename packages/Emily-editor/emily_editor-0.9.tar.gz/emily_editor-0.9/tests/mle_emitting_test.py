#Test program for Contractor for emitting an MLE document.

# author R.N.Bosworth

# version 9 Mar 23  15:24

from emily0_9 import mle_emitting, texting, unicode_io
from guibits1_0 import unicoding3_0

"""
Copyright (C) 2017,2018,2021,2022,2023  R.N.Bosworth

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

print("Tests of emit_emily_document", end=' ')
#mle_emitting.emit_emily_document(None,None,None,None,None)
n = unicoding3_0.string_of("Liberty")
#mle_emitting.emit_emily_document(n,None,None,None,None)
#mle_emitting.emit_emily_document(n,-0.1,None,None,None)
#mle_emitting.emit_emily_document(n,99.1,None,None,None)
d = 10.0
#mle_emitting.emit_emily_document(n,d,None,None,None)
v = unicoding3_0.string_of("99.9")
#mle_emitting.emit_emily_document(n,d,v,None,None)
t = texting.new_text()
#mle_emitting.emit_emily_document(n,d,v,t,None)
w = unicode_io.new_output_writer("test.mle")
mle_emitting.emit_emily_document(n,d,v,t,w)
texting.insert_code_point(t,ord('<'))
texting.insert_code_point(t,ord('a'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('g'))
texting.insert_code_point(t,ord('n'))
texting.insert_code_point(t,ord('b'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('g'))
texting.insert_code_point(t,ord('i'))
texting.insert_code_point(t,ord('n'))
texting.insert_code_point(t,ord('>'))
texting.insert_code_point(t,ord('h'))
texting.insert_code_point(t,ord('e'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('l'))
texting.insert_code_point(t,ord('o'))
texting.insert_code_point(t,ord('\n'))
texting.insert_code_point(t,ord('\n'))
w = unicode_io.new_output_writer("test2.mle")
mle_emitting.emit_emily_document(n,d,v,t,w)
print("OK")

print("")
print("All tests OK")

# Test of Contractor which allows the emitting of css rules.

from emily0_9 import css_emitting, unicode_io
from guibits1_0 import unicoding3_0

# author R.N.Bosworth

# version 1 Mar 23  16:04 

# test program
# ------------

print("Tests of css_emitting._emit_name_string", end=' ')
w = unicode_io.new_string_writer()
s = unicoding3_0.new_string()
css_emitting._emit_name_string(s,w)
assert unicoding3_0.length_of(unicode_io.get_string(w)) == 0
w = unicode_io.new_string_writer()
s = unicoding3_0.string_of("cat")
css_emitting._emit_name_string(s,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("cat"))
print("OK")

print("Tests of css_emitting._emit_font_name_rule", end=' ')
w = unicode_io.new_string_writer()
s = unicoding3_0.new_string()
n = unicoding3_0.new_string()
css_emitting._emit_font_name_rule(s,n,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {font-family: \"\";}"))
s = unicoding3_0.string_of("fred")
n = unicoding3_0.string_of("Times New Roman")
w = unicode_io.new_string_writer()
css_emitting._emit_font_name_rule(s,n,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  fred {font-family: \"Times New Roman\";}"))
print("OK")

print("Tests of css_emitting._emit_font_size_rule", end=' ')
s = unicoding3_0.new_string()
w = unicode_io.new_string_writer()
css_emitting._emit_font_size_rule(s,0.0,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {font-size: 0pt;}"))
s = unicoding3_0.string_of("jim")
w = unicode_io.new_string_writer()
css_emitting._emit_font_size_rule(s,9.0,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  jim {font-size: 9pt;}"))
s = unicoding3_0.string_of("bert")
w = unicode_io.new_string_writer()
css_emitting._emit_font_size_rule(s,10.0,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  bert {font-size: 10pt;}"))
s = unicoding3_0.string_of("harold")
w = unicode_io.new_string_writer()
css_emitting._emit_font_size_rule(s,99.0,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  harold {font-size: 99pt;}"))
print("OK")

print("Tests of css_emitting._emit_text_alignment_rule", end=' ')
s = unicoding3_0.new_string()
a = unicoding3_0.new_string()
w = unicode_io.new_string_writer()
css_emitting._emit_text_alignment_rule(s,a,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("   {text-align: ;}"))
s = unicoding3_0.string_of("fred")
a = unicoding3_0.string_of("left")
w = unicode_io.new_string_writer()
css_emitting._emit_text_alignment_rule(s,a,w)
assert unicoding3_0.equals(unicode_io.get_string(w),unicoding3_0.string_of("  fred {text-align: left;}"))
print("OK")

print("Tests of css_emitting.emit_style_sheet")
w = unicode_io.new_output_writer("css.test")
css_emitting.emit_style_sheet(unicoding3_0.string_of("Palatino"),18.0,w)
unicode_io.write(unicode_io.END_OF_STREAM,w)
print("  check file css.test")
print("OK")

print("")
print("All tests OK")

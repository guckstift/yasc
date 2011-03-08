
import sys
import py_compile

if len(sys.argv) != 3:
	print "usage: pyc.py source output"

py_compile.compile (sys.argv[1], sys.argv[2], doraise=True)

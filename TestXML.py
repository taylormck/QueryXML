#!/usr/bin/env python

"""
To test the program:
    % python TestXML.py >& TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.out
"""

# --- imports ---
import StringIO
import unittest
from XML import XMLSearch, xmlPrint, xmlRead, xmlSolve, et

class TestXML (unittest.TestCase) :
    # -------
    # xmlRead
    # -------

    def test_xmlRead (self) :
        self.assert_(False)

    # --------
    # xmlPrint
    # --------

    def test_xmlPrint_empty (self) :
        w = StringIO.StringIO()
        ans = ()
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "")

    def test_xmlPrint_tuple_1 (self) :
        w = StringIO.StringIO()
        ans = (1, 4)
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "1\n4\n")

    def test_xmlPrint_tuple_2 (self) :
        w = StringIO.StringIO()
        ans = (2, 2, 7)
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_xmlPrint_tuple_trash (self) :
        w = StringIO.StringIO()
        ans = (2, "trash", [1])
        xmlPrint(ans, w)
        self.assert_(w.getvalue() == "2\ntrash\n[1]\n")

    # --------
    # xmlSolve
    # --------

    def test_xmlSolve_1 (self) :
        self.assert_(False)

class TestXMLSearch (unittest.TestCase) :
    # Remember, you can test a tree using et.dump(sourceTree.getroot())
    # and comparing it to a string

    # --------
    # __init__
    # --------

    def test_init (self) :
    	self.assert_(False)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
    	self.assert_(False)

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
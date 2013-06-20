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

    # may have to remove \n from the assert statements

    def test_xmlRead (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        a = ["", ""]
        b = xmlRead(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == "<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>")
        self.assert_(a[1] == "<Team><Cooly></Cooly></Team>")

    def test_xmlRead_empty (self) :
        r = StringIO.StringIO("")
        a = ["", ""]
        b = xmlRead(r, a)
        # the below may be bad because we allow blank lines in input
        self.assert_(b == False)
        self.assert_(a[0] == "")
        self.assert_(a[1] == "")

    def test_xmlRead_whitespace (self) :
        r = StringIO.StringIO("<THU>\n <Team>  \n\n <Cooly>\t</Cooly>\n </Team>\n </THU>\n<Team><Cooly>\t </Cooly> </Team>")
        a = ["", ""]
        b = xmlRead(r, a)
        self.assert_(b == True)
        # xml preserves whitespace, do we want to preserve it? double check
        self.assert_(a[0] == "<THU>\n<Team>\n<Cooly></Cooly>\n</Team>\n</THU>")
        self.assert_(a[1] == "<Team><Cooly></Cooly></Team>")

    def test_xmlRead_text (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<Cooly>test text</Cooly>\n</Team>\n</THU>\n<Team><Cooly>more test text</Cooly></Team>")
        a = ["", ""]
        b = xmlRead(r, a)
        self.assert_(b == True)
        # xml preserves whitespace, so it might also preserve the text? double check
        self.assert_(a[0] == "<THU>\n<Team>\n<Cooly></Cooly>\n</Team>\n</THU>")
        self.assert_(a[1] == "<Team><Cooly></Cooly></Team>")


    # --------
    # xmlPrint
    # --------

    def test_xmlPrint_empty (self) :
        w = StringIO.StringIO()
        ans = () # parens or empty tuple?
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
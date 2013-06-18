#!/usr/bin/env python

# --- imports ---
import StringIO
import unittest
from XML import XMLSearch, xmlPrint, xmlRead, xmlSolve, et

class TestXML (unittest.TestCase):
    # The function tests should go here
    #       (xmlSolve, xmlRead, xmlPrint)
    pass

class TestXMLSearch (unittest.TestCase):
    # The method tests for the xmlSearch class should go here
    #       (__init__ and eval)
    #
    # Remember, you can test a tree using et.dump(sourceTree.getroot())
    # and comparing it to a string
    pass

print "TestXML.py"
unittest.main()
print "Done."
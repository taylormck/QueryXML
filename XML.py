#!/usr/bin/env python
"""
    Search in XML
    
    @author: Taylor McKinney, Eddie
"""
import xml.etree.ElementTree as et


class XMLSearch:
    """A collection of data for a single search query and XML file"""

    def __init__ (self, sourceXMLString, queryXMLString):
        """
            Reads in the XML source and query as strings and parses them into trees
            
            @param sourceXMLString: The XML source as a string
            @param queryXMLString: The XML query as a string
        """
        self.sourceTree = et.fromstring(sourceXMLString)
        self.queryTree = et.fromstring(queryXMLString)

    def eval(self):
        """
            Searches for the query in the XML source
            Returns the number of matches and integer enumeration of each occurrence
            
            @return: (n, k1, ... kn) where n is the number of matches and ki is the ith match
        """
        return (0,)  # TBD, this is a dummy return

def xmlRead (istream, strings):
    """
        Reads a test case from the input stream
        
        @param strings: An array of string objects with at least 2 elements
        @return True if successful, False otherwise
    """
    return False  # TBD, this is a dummy return

def xmlPrint (solution):
    """
        Prints out the elements of a tuple without the formatting or extra symbols
        
        @param solution: A tuple
    """
    pass

def xmlSolve (istream, ostream):
    """
        Reads in test cases from istream and prints the results to the output stream
    """
    pass


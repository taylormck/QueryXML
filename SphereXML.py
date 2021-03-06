#!/usr/bin/env python
"""
Search in XML    
@author: Taylor McKinney, Eduardo Saenz
"""
# --- imports ---
import sys
import xml.etree.ElementTree as et

def xmlEval(sourceRoot, queryRoot):
    """
    Searches for the query in the XML source
    Returns the number of matches and integer enumeration of each occurrence
    @return: (n, k1, ... kn) where n is the number of matches and ki is the ith match
    """
    # for (c, n) in enumerate(sourceTree.iter(), 1):
    #     this will give you each node with their correct number
    #     I suggest using n.set( ... ) to write the counter to each node for later use
    #     or we can do all the work here
    for (c, n) in enumerate(sourceRoot.iter(), 1):
        n.set('id', str(c))

    query = xmlQueryToRegex(queryRoot)
    dummyRoot = et.Element("XML")
    dummyRoot.insert(0, sourceRoot)
    results = dummyRoot.findall(query)
    solution = [len(results)]
    for i in results:
        solution += [int(i.get('id'))]

    return solution  # TBD, this is a dummy return

# I'm considering adding a method to get the string version of the query, as in
# foo(<Team><Cooly></Cooly></Team>) == "Team/Cooly"
def xmlQueryToRegex(queryRoot):
    """
    Takes in a query root and returns the regex to search
    @param queryRoot: Element representing root of query
    @return valid query string
    """
    def helper(node, string) :
        string += node.tag

        for n in node :
            string += "/"
            string = helper(n, string)
            string += "/.."

        return string

    return helper(queryRoot, ".//")

def xmlRead (istream):
    """
    @param istream: an input stream
    @return a valid XML string
    """
    return "<XML>" + istream.read() + "</XML>"

def xmlPrint (solution, ostream):
    """
    Prints out the elements of a tuple without the formatting or extra symbols
    @param solution: A tuple
    """
    for n in solution:
        print >> ostream, n
    print >> ostream, ""

def xmlSolve (istream, ostream):
    """
    Reads in test cases from istream and prints the results to the output stream
    @param istream: an input stream
    @param ostream: an output stream
    """
    root = et.fromstring(xmlRead(istream))
    trees = root.findall("*")
    for i in xrange(0, len(trees), 2):
        solution = xmlEval(trees[i], trees[i + 1])
        xmlPrint(solution, ostream)


"""
Run XML.py
"""


# --- Main ---
xmlSolve(sys.stdin, sys.stdout)

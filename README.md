Search in XML - Python
======================

From Sphere: 1484 Search in XML  
Problem code: PT07H  
http://www.spoj.com/problems/PT07H/  

We are given a valid XML document and a querying pattern of XML,
and are expected to find all occurrences of the pattern in the text of XML documents.
All elements of the XML tree are numbered according to the order in which they appeared,
starting with 1.


Input
-----

There are two parts in the input file:
- A valid XML document with exactly one root element
- A valid XML document as querying patter with exactly one root element

We may assume:
- Ignore all whitespace (consider only a-z, A-Z, '/', '<', and '>')
- XML documents are strictly rooted tree
- Input file is less than 100kb

Output
------

First line consists of an integer n that denotes the number of occurrences.
Each line after contains the id number of the element where the pattern occurs,
printed in increasing order.

Example
-------
####Input:
`<THU>
	<Team>
		<ACRush></ACRush>
		<Jelly></Jelly>
		<Cooly></Cooly>
	</Team>
	<JiaJia>
		<Team>
			<Ahyangyi></Ahyangyi>
			<Dragon></Dragon>
			<Cooly><Amber></Amber></Cooly>
		</Team>
	</JiaJia>
</THU>
<Team><Cooly></Cooly></Team>`

####Output:
2
2
7
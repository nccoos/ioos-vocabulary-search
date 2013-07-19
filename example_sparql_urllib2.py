# example_sparql_urllib2
# Send SPARQL query to SPARQL endpoint, store and output result
# using urllib2
#
# modified from ORA "Learning SPARQL" by Bob DuCharme -- ex358.py
#

import urllib2, json

endpointURL = "http://mmisw.org/ont/"
# Example1 IOOS query http://www.unc.edu/~haines/orrioos.html#Example1
# Find IOOS parameters that have exactMatch or closeMatch to CF terms
query = """
PREFIX ioos: <http://mmisw.org/ont/ioos/parameter/>
SELECT DISTINCT ?parameter ?definition ?unit ?property ?value 
WHERE {?parameter a ioos:Parameter .
       ?parameter ?property ?value .
       ?parameter ioos:Term ?term . 
       ?parameter ioos:Definition ?definition . 
       ?parameter ioos:Units ?unit .
       FILTER (regex(str(?property), "(exactMatch|closeMatch)", "i") && regex(str(?value), "cf", "i") )
      } 
ORDER BY ?parameter
"""
escapedQuery = urllib2.quote(query)
# MMISW uses "?sparql=" instead of "?query="
# default return format is HTML
requestURL = endpointURL + "?sparql=" + escapedQuery
# return format JSON
requestURL = endpointURL + "?form=json&sparql=" + escapedQuery
request = urllib2.Request(requestURL) 
result = urllib2.urlopen(request).read()
j = json.loads(result)
j.keys()

j["names"]

j["values"][0:3]

j

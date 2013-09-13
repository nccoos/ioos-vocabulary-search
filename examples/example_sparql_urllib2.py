# example_sparql_urllib2
# Send SPARQL query to SPARQL endpoint, store and output result
# using urllib2
#
# modified from ORA "Learning SPARQL" by Bob DuCharme -- ex358.py
#

import urllib, urllib2, json

endpointURL = "http://mmisw.org/sparql"

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
params = {
    "query": query,
    "results": "json",
    "output": "json"
    }
queryURL = urllib.urlencode(params)
requestURL = endpointURL + '?' + queryURL
request = urllib2.Request(requestURL) 
# default return format is XML
result = urllib2.urlopen(request).read()

# don't know how to get this is return JSON format using urllib2 or urllib
# j = json.loads(result)
# j.keys()

# j

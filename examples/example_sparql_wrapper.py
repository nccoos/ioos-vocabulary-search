# example_sparql_wrapper
# Send SPARQL query to SPARQL endpoint, store and output result
# using SPARQLWrapper
#
# modified from ORA "Learning SPARQL" by Bob DuCharme -- ex361.py
#

from SPARQLWrapper import SPARQLWrapper, JSON

## This was not the correct endpoint 
# endpointURL = "http://mmisw.org/ont/?sparql"

sparql = SPARQLWrapper("http://mmisw.org/sparql")
queryString = """
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
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
resonse = sparql.query()
j = sparql.query().convert()

j.keys()

j

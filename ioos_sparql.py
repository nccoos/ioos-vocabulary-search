# 

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://mmisw.org/sparql")
sparql.setReturnFormat(JSON)

def do_query(query):
    sparql.setQuery(query)
    results = sparql.query().convert()

def print_query(query):
    

def print_results(results, show_original=False):
    if show_original_result:
        print "-" * 80
        print "%s" % str(results)
    # print header
    variables = results["head"]["vars"]
    print " | ".join(variables)
    # print values
    for result in results["results"]["bindings"]:  
        vals = [result[var]["value"] for var in variables]
        print " | ".join(vals)

def list_exactMatch():
    # what inputs?
    # vocabURL like http://mmisw.org/ont/ioos/parameter
    # term or list of terms in vocabURL
    # 
    # query for exactMatch(es) to a term
    # query for exactMatch(es) for list of terms
    #
    # return list of terms (unique and ordered) or which assoc'd with each input term

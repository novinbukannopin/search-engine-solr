import pysolr

solr_product = pysolr.Solr('http://localhost:8090/solr/product_collect')

def search_function(core, query, rows = 12 ):
    results = core.search(query, rows = rows)
    return results
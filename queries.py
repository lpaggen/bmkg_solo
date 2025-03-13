# this query returns the top 5 breweries with the highest average beer rating
query1 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?breweryName (AVG(?beerRating) AS ?avgRating)
    WHERE {
        ?beer a schema:BreweryProduct ;
            ex:brewedBy ?brewery ;
            ex:beerRating ?beerRating .
        ?brewery schema:name ?breweryName .
    }
    GROUP BY ?breweryName
    ORDER BY DESC(?avgRating)
    LIMIT 5
"""

# this one returns the top 10 breweries with the most beers
query2 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?breweryName (COUNT(?beer) AS ?beerCount)
    WHERE {
        ?beer a schema:BreweryProduct ;
        	ex:brewedBy ?brewery .
        ?brewery schema:name ?breweryName .
    }
    GROUP BY ?breweryName
    ORDER BY DESC(?beerCount)
    LIMIT 10
"""

# this one gets the average alcohol percentage (across all beers)
query3 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT (AVG(?alcoholPercentage) AS ?averageAlcoholPercentage)
    WHERE {
        ?beer a schema:BreweryProduct ;
            ex:alcoholPercentage ?alcoholPercentage .
    }
"""

# this returns the highest % of beer per brewery 
query4 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?breweryName (MAX(?alcoholPercentage) AS ?maxAlcoholPercentage)
    WHERE {
        ?beer a schema:BreweryProduct ;
            ex:brewedBy ?brewery ;
            ex:alcoholPercentage ?alcoholPercentage .
        ?brewery schema:name ?breweryName .
    }
    GROUP BY ?breweryName
    ORDER BY DESC(?maxAlcoholPercentage)
    LIMIT 10
"""

# breweries per province 
query5 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?provinceName (COUNT(DISTINCT ?brewery) AS ?breweryCount)
    WHERE {
        ?brewery a schema:Brewery ;
            ex:locatedInMunicipality ?municipality .
        ?municipality ex:isContainedInProvince ?province .
        ?province schema:name ?provinceName .
    }
    GROUP BY ?provinceName
    ORDER BY DESC(?breweryCount)
"""

# this is part of the code to get the Counter with the most brewed types per province 
query6 = """
    PREFIX ex: <http://example.org/>
    PREFIX schema: <http://schema.org/>
    SELECT ?provinceName ?beerType
    WHERE {
        ?beer a schema:BreweryProduct ;
            ex:beerType ?beerType ;
            ex:brewedBy ?brewery .
        ?brewery ex:locatedInMunicipality ?municipality .
        ?municipality ex:isContainedInProvince ?province .
        ?province schema:name ?provinceName .
    }
    ORDER BY ?provinceName ?beerType
"""
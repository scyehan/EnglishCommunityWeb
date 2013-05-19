from pymongo import Connection
import yql
import urllib
import string
import simplejson as json
con = Connection()
db = con.learner
movie=db.movie
yqlpublic = yql.Public()
for alpha in string.letters[25:26]:
	for page in range(1,2):
		query='USE "https://raw.github.com/yql/yql-tables/master/rottentomatoes/search/rottentomatoes.search.xml" AS mytable;select links.self from mytable where title="%s" and apikey="2wf4n3y52bt59mhb9bmbhwkp" and page=%s'%(alpha,page)
		results = yqlpublic.execute(query)
        for result in results.rows:
            #print result['links']['self']
			html=urllib.urlopen(result['links']['self']+"?apikey=2wf4n3y52bt59mhb9bmbhwkp").read()
			#print json.loads(html)
			#movie.insert(json.loads(html))
			
			
			
	

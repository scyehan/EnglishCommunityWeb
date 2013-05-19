from pymongo import Connection
from readability.readability import Document
import yql
import urllib
con = Connection()
db = con.learner
news = db.news
yqlpublic=yql.Public()
rsscfg=open("rss.cfg","r")
for line in rsscfg.readlines():
    category=line.split(":")
    query = 'select link,pubDate from rss where url ="http://rss.news.yahoo.com/rss/%s"'%category[0]
    results = yqlpublic.execute(query)
    for result in results.rows:
        html = urllib.urlopen(result['link']).read()
        doc = Document(html)
        news.insert({'art_id':0,'content':doc.summary(),'description':"",'hardness':0,'pub_date':result['pubDate'],'ranking':0,'rss_id':category[1],'time_index':1,'tiny_image':"",'title':doc.short_title(),'url':result['link']})



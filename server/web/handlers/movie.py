from web.handlers.base import BaseRequestHandler
from web.settings import REC_URL
import tornado.web
from tornado.web import asynchronous
from tornado import gen
from tornado.httpclient import AsyncHTTPClient,HTTPRequest
import cPickle
import urllib
import simplejson as json
import random
rec_count=6
class MovieIndexHandler(BaseRequestHandler):
    """
        This handler is to return user's personal page
        which contains some recommended news articles
    """   
    @asynchronous
    @gen.engine    
    @tornado.web.authenticated
    def get(self):
        user_id=self.current_user
        request=yield gen.Task(self.db.movie.find,{},limit=100)
        res=request[0][0]
        movies=random.sample(res,rec_count)
        user={'username':self.session.get('username')}
        context=self.get_context({'movies':movies,'user':user})
        self.write(self.render.movieindex(**context))
        self.finish()

    @asynchronous
    @gen.engine    
    #@tornado.web.authenticated
    def post(self):
        #user_id=self.current_user
        request=yield gen.Task(self.db.movie.find,{},limit=100,
                fields={'_id':0,'id':1,'posters':1,'title':1,'genres':1,'synopsis':1})
        
        res=request[0][0]
        movies=random.sample(res,rec_count)
        for movie in movies:
            movie['poster']=movie['posters']['original']
            movie['genre']=movie['genres'][0]
        user={'username':self.session.get('username')}
        print len(movies)
        self.write({'rec':movies})
        self.finish()
        
class MovieHandler(BaseRequestHandler):
    """
        This handler is to return a news article's full text to user
    """
    @asynchronous
    @gen.engine    
    @tornado.web.authenticated
    def get(self):
        user_id=self.current_user
        movie_id=self.get_argument('mid')        
        response=yield gen.Task(self.db.movie.find_one,
                                    {'id':float(movie_id)})
        movie=response[0][0]
        user={'user_id':user_id,'username':self.session.get('username')}
        context=self.get_context({'movie':movie,'user':user})
        self.write(self.render.movie(**context))
        self.finish()
        
    def post(self):
        pass

   


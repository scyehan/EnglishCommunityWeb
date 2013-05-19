'''
Created on 2012-12-3

@author: cqy
'''
import tornado.ioloop
import tornado.web
import tornado.httpserver
from web.settings import SETTINGS
from web.handlers.login import *  
from web.handlers.news import *
from web.handlers.topic import *
from web.handlers.movie import *
from web.handlers.user import *
import tornado.options
from tornado.options import define, options

urls=[
        ('/',IndexHandler),
        ('/login',LoginHandler),
        ('/register',RegisterHandler),
        ('/logout',LogoutHandler),
        ('/myindex', NewsIndexHandler),
        ('/newsindex', NewsIndexHandler),
        ('/news',NewsHandler),
        ('/topic',TopicHandler),
        ('/topic/comment',AddTPCommentHandler),
        ('/addtopic', AddTopicHandler),
        ('/edittopic', EditTopicHandler),
        ('/topicindex',TopicIndexHandler),
        ('/movieindex', MovieIndexHandler),
        ('/movie', MovieHandler),
        ('/mypage',UserIndexHandler),
        #('/words',WordsHandler),
        ('/static/(.*)',tornado.web.StaticFileHandler,{'path':'./web/static'})
    ]

if __name__=="__main__":
    tornado.options.options.logging = "debug"
    app=tornado.web.Application(urls,**SETTINGS)
    server=tornado.httpserver.HTTPServer(app)
    server.listen(8003)
    tornado.ioloop.IOLoop.instance().start()    

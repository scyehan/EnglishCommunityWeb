import tornado.web
from web.utils.session import SessionMixin
from web.settings import render_jinja2,SITE_URL

class BaseRequestHandler(tornado.web.RequestHandler, SessionMixin):
    def prepare(self):
        pass
    
    def on_finish(self):
        pass
    
    def get_current_user(self):
        user = self.session.get('user')
        login = self.session.get('login')
        print user,login
        if not login and user is None:
            return None
        return user           
    
    @property
    def render(self):
        self._render=render_jinja2
        return self._render
    
    @property
    def db(self):
        self._db=self.settings['db']
        return self._db

    
    def get_context(self,kwargs=None):        
        self.context={'site':SITE_URL,
                      'title':'You Learn I Learn',
                      'xsrf_form_html':self.xsrf_form_html}
        if kwargs:
            self.context.update(kwargs)
        return self.context
    

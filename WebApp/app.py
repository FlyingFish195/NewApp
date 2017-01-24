# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define,options

import os.path

define("port",default=5000,help="run on port 5000",type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/",MainHandler),
        ]
        settings=dict(
            cookie_secret="YOU_CANT_GUESS_MY_SECRET",
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            xsrf_cookies=True,
            debug=True,
        )
        super(Application,self).__init__(handlers,**settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return Application()

def main():
    app=make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__=="__main__":
    main()

# -*- coding: utf-8 -*-
import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from admin.admin import admin, User
from model.models import db
from model.models import User as UserModel
from page.pages import *

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

Tornado_Routes = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/detail/(.*)', DeatailHandler),
]

application = tornado.web.Application(Tornado_Routes, **Tornado_Settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

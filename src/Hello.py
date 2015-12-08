#-*- coding: utf-8 -*-
'''
Created on 2015/12/05 

@author: SHIYU
'''
def application(environ,start_respon):
    start_respon('200 OK',[('Content-Type','text/html')])
    return [b'<h1>hello,web!</h1>']
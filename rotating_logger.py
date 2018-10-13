#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 26, 2017

Course work: 

@author: raja

Source:
    https://gist.github.com/ibeex/3257877
'''

# Import necessary modules
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    app.logger.warning('A warning occurred (%d apples)', 77)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    
    content = """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    
    for x in range(10000):
        print(x, content)
        app.logger.error(str(x) + content)
    
    return "start"

if __name__ == '__main__':
    handler = RotatingFileHandler('p:/test/start.log', maxBytes=1000000, backupCount=100)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
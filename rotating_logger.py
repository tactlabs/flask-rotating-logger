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

# 1 MB
MAX_BYTES = 1000000

@app.route('/')
def start():
    app.logger.warning('A warning occurred (%d apples)', 77)
    app.logger.error('Error')
    app.logger.info('Info printed')
    
    content = """
    Korum Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    """
    
    for x in range(4):
        print(x, content)
        app.logger.info(str(x) + content)
    
    return "start"

if __name__ == '__main__':
    handler = RotatingFileHandler('/Users/rajacsp/tactlogs/tout.log', maxBytes=MAX_BYTES, backupCount=100)

    # https://stackoverflow.com/questions/43109355/logging-setlevel-is-being-ignored
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    #handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run()
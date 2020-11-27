# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:48:13 2020

@author: user
"""

import os

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    name = os.environ.get('NAME', 'World') # if 'NAME' doesn't exist, default is 'World'
    return 'Hello {}!'.format(name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
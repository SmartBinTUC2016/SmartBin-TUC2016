#########################################################################
# The MIT License (MIT)                                                 #
# Copyright (c) 2016 Patrick Lai, Josh Manogaran,                       #
#                    Brendan Srinivasalu, Elias Tadros                  #
#                                                                       #
# Permission is hereby granted, free of charge, to any person           #
# obtaining a copy of this software and associated documentation        #
# files (the "Software"), to deal in the Software without restriction,  #
# including without limitation the rights to use, copy, modify, merge,  #
# publish, distribute, sublicense, and/or sell copies of the Software,  #
# and to permit persons to whom the Software is furnished to do so,     #
# subject to the following conditions:                                  #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.#
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  #
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF            #
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION    #
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.       #
#########################################################################

# Library from Armin Ronacher
from flask import *
# Own modules
import database
import comms
import random
# Standard Libraries from Python Software Foundation
import json
import urllib2

# Initialise Flask App
app = Flask(__name__)
app.secret_key = 'hello'

# Declare global variables
page = {}
session = {}

'''
Index Page
'''
@app.route('/')
def index():
    page['title'] = 'Overview'
    page['bins'] = '1'
    num_users = database.get_num_users()
    return render_template('index.html', page = page, num_users = num_users)

'''
Capacity Page
'''
@app.route('/capacity', methods=['GET','POST'])
def get_capacity():
    res = comms.get_data() # Retrieve data

    page['title'] = 'Capacity'
    # Data assignment to page variables
    if res['level'] != '?': # Check whether there was data received
        page['capacity'] = (res['weight']/1000 + res['level'])/2 # Calculate total current capacity
    else:
        page['capacity'] = '?'
    page['level'] = res['level']
    page['user'] = res['user']
    page['weight'] = res['weight']

    # Capacity Checking
    if page['capacity'] == '?':
        page['status'] = 'Connection error'
    elif page['capacity'] < 90:
        page['status'] = 'OK'
    elif page['capacity'] >= 90:
        page['status'] = 'FULL'
    return render_template('capacity.html', page = page)

'''
Users Page
'''
@app.route('/users')
def get_users():
    page['title'] = 'Users'
    users = database.get_users()
    return render_template('users.html', page = page, users = users)

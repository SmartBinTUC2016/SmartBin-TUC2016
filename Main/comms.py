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

import urllib2
import json
import time
import database
import route

# data = {}
'''
Background Process to listen for data sent from Wifi Module
'''
def jsonListener():
    while(True):
        # request_data()
        res = request_data()
        database.updateUser(res['user'])

'''
Requests data from Wifi Module,
data is in JSON format
'''
def request_data():
    res = {}
    try:
        request = urllib2.urlopen('http://192.168.1.49:80', timeout=5)
        res = json.loads(request.read())
    except Exception  as e:
        print e
        res['level'] = '?'
        res['weight'] = '?'
        res['user'] = '?'
    return res

'''
Returns requested data from Wifi Module
'''
def get_data():
    # data['level'] = '?'
    # data['weight'] = '?'
    # data['user'] = '?'
    return request_data()

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

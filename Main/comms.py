import urllib2
import json
import time
import database
import route

data = {}
def jsonListener():
    while(True):
        request_data()
        time.sleep(1)
        database.updateUser()
        time.sleep(1)

def request_data():
    res = {}
    try:
        request = urllib2.urlopen('http://127.0.0.1:6000', timeout=5)
        res = json.loads(request.read())
    except Exception  as e:
        print e
        res['level'] = '?'
        res['weight'] = '?'
        res['user'] = '?'
    global data
    data = res
    return res


def get_data():
    # data['level'] = '?'
    # data['weight'] = '?'
    # data['user'] = '?'
    return request_data()

import urllib2
import json
import time

data = {}
def jsonListener():
    res = {}
    while(True):
        try:
            request = urllib2.urlopen('http://127.0.0.1:6000', timeout=5)
            res = json.loads(request.read())
        except Exception  as e:
            print e
            res['level'] = '?'
            res['weight'] = '?'
            res['user'] = '?'
        # print res
        global data
        data = res
        # print data
        time.sleep(3)
    return

# def set_data(x):
#     global data
#     data = x

def get_data():
    # data['level'] = '?'
    # data['weight'] = '?'
    # data['user'] = '?'
    print data
    return data

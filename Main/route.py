from flask import *
# import configparser
# from comms import *
import random
import json
import urllib2
import socket


app = Flask(__name__)
app.secret_key = 'hello'

page = {}
session = {}
# 192.168.43.218
@app.route('/')
def index():
    page['title'] = 'Overview'
    page['bins'] = '1'
    page['users'] = '1'
    return render_template('index.html', page = page)

@app.route('/capacity', methods=['GET','POST'])
def get_capacity():
    # if urllib2.Request.get_method == 'GET':
    res = {}
    try:
        res = urllib2.urlopen('http://192.168.1.11:80', timeout=3)
        res = json.loads(res.read())
    except Exception as e:
        print e
        res['level'] = '?'
        res['weight'] = '?'
        res['distance'] = '?'

    page['title'] = 'Capacity'
    page['level'] = res['level']
    page['weight'] = res['weight']
    page['distance'] = res['distance']
    if page['level'] == '?':
        page['status'] = 'Connection error'
    elif page['level'] < 90:
        page['status'] = 'OK'
    elif page['level'] >= 90:
        page['status'] = 'FULL'
    return render_template('capacity.html', page = page)

@app.route('/users')
def get_users():
    page['title'] = 'Users'
    return render_template('users.html', page = page)

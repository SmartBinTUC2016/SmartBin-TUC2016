from flask import *
import database
import comms
import random
import json
import urllib2

app = Flask(__name__)
app.secret_key = 'hello'

page = {}
session = {}

# 192.168.43.218
@app.route('/')
def index():
    page['title'] = 'Overview'
    page['bins'] = '1'
    num_users = database.get_num_users()
    return render_template('index.html', page = page, num_users = num_users)

@app.route('/capacity', methods=['GET','POST'])
def get_capacity():
    # if urllib2.Request.get_method == 'GET':
    res = comms.get_data()
    print res

    page['title'] = 'Capacity'
    if res['level'] != '?':
        page['capacity'] = (res['weight']/1000 + res['level'])/2
    else:
        page['capacity'] = '?'
    page['level'] = res['level']
    page['user'] = res['user']
    page['weight'] = res['weight']
    if page['capacity'] == '?':
        page['status'] = 'Connection error'
    elif page['capacity'] < 90:
        page['status'] = 'OK'
    elif page['capacity'] >= 90:
        page['status'] = 'FULL'
    return render_template('capacity.html', page = page)

@app.route('/users')
def get_users():
    page['title'] = 'Users'
    users = database.get_users()
    return render_template('users.html', page = page, users = users)

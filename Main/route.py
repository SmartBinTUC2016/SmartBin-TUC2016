from flask import *
import ConfigParser
from comms import *
import random

app = Flask(__name__)
app.debug = True

page = {}
session = {}

@app.route('/')
def index():
    page['title'] = 'Welcome'
    page['paragraph'] = 'This is the page to manage and view the status of the Smart Bin.'
    return render_template('index.html', page = page)

@app.route('/capacity', methods=['POST','GET'])
def get_capacity():
    page['title'] = 'Capacity'
    level = random.randint(0,100)
    page['level'] = str(level) + "%"
    if level > 80:
        page['status'] = 'Full, needs emptying'
    else:
        page['status'] = 'OK'
    return render_template('capacity.html', page = page)

@app.route('/users')
def get_users():
    page['title'] = 'Users'
    return render_template('users.html', page = page)

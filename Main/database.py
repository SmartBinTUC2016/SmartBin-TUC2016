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

import psycopg2
import psycopg2.extras
import ConfigParser
import comms
import time

#####################################################
##  Database Connect
#####################################################
sessionUser = None
def database_connect():
    # Read the config file
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    # Create a connection to the database
    connection = None
    try:
        connection = psycopg2.connect(database=config.get('DATABASE','database'),
            user=config.get('DATABASE','user'),
            password=config.get('DATABASE','password'),
            host=config.get('DATABASE','host'))
    except psycopg2.OperationalError as e:
        print("""Error, you haven't updated your config.ini or you have a bad
        connection, please try again. (Update your files first, then check
        internet connection)
        """)
        print(e)
    #return the connection to use
    return connection

'''
Get Users
'''
def get_users():
    # Establish connection to the database
    conn = database_connect()
    if conn is None: # Check if a connection was returned
        print 'No Connection'
        return
    # Declare database cursor
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    query = 'SELECT * FROM smartbin.user ORDER BY rubbishcount desc, user_id asc;'

    try:
        cur.execute(query) # Execute query
        res = cur.fetchall() # Fetch all results from database
        cur.close()
        conn.close()
        return res
    except Exception as e:
        print e
    cur.close()
    conn.close()
    return None

'''
Get number of users
'''
def get_num_users():
    conn = database_connect()
    if conn is None:
        print 'No Connection'
        return
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    query = 'SELECT COUNT(*) FROM smartbin.user'

    try:
        cur.execute(query)
        res = cur.fetchall()
        cur.close
        conn.close
        return res
    except Exception as e:
        print e
    cur.close()
    conn.close()
    return None

'''
Update User
'''
def updateUser(user):
    tempUser = user
    global sessionUser
    if sessionUser != tempUser:
        sessionUser = tempUser
        conn = database_connect()
        if conn is None:
            print 'No Connection'
            return
        cur = conn.cursor()
        try:
            query = 'UPDATE smartbin.user SET rubbishcount = rubbishcount + 1 WHERE user_id = %s;'
            cur.execute(query, (sessionUser,))
            conn.commit()
            cur.close()
            conn.close()
            return
        except Exception as e:
            print e
        cur.close()
        conn.close()
    return None

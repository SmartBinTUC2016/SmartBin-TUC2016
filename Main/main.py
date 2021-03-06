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

# Standard Libraries from Python Software Foundation
from multiprocessing import Process
import Queue
import time
# Own modules
from route import *
from database import *
from comms import *

def main():
    page = {'title' : 'IOT Trash Can'}
    datalistener = Process(target=jsonListener,args=()) # Declare background process
    datalistener.start() # Start process
    app.run(host='0.0.0.0', port=8080, debug=True)
    datalistener.join()

if __name__ == "__main__":
    main()

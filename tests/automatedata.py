import requests
import random
import time

def main():
    while (True):
        level = random.randint(1,100)
        weight = random.randint(1,1000)
        user = random.randint(1,5)
        json = ('{{ "level" : {0} , "weight" : {1} , "user" : {2}}}').format(level, weight, user)
        f = open('index.html','w')
        f.write(json)
        f.close()
        print json
        time.sleep(10)


if __name__ == "__main__":
    main()

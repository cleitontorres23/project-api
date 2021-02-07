import requests
import json
import logging


##logging
logging.basicConfig(filename='systemlogging.txt', level=logging.DEBUG)
#logging.debug("checking if its working...")

##this function get the URL with get function and then return status code
def query(url):
    
    req_url = requests.get(url)

    if (req_url.status_code == 200):
        return(req_url.text)
    else:
        print("we have a problem, back off")
    
a = query('https://api.thecatapi.com/v1/images/search?breed_ids=beng')

logging.debug("getting the value in jboss format...")
##get the value as json with json module
values = json.loads(a)

##creating a list to append the url content

my_list = []

for i in values:
    logging.debug("finding the element in the list...")
    my_list.append(i)
    logging.debug("saving in logfile.txt...")
    thecatapi = (str(i.get('breeds')))
    if "temperament" in thecatapi:
        print("The cats breed is: " + str(i.get('breeds')[0]["temperament"]), file = open("logfile.txt", 'a'))
        if "origin" in thecatapi:
            print("The cats origin is: " + str(i.get('breeds')[0]["origin"]), file = open("logfile.txt", 'a'))
            if "description" in thecatapi:
                print("Description: " + str(i.get('breeds')[0]["description"]), file = open("logfile.txt", 'a'))

logging.debug("To see the result our program you can access the ./logfile.txt !")


    

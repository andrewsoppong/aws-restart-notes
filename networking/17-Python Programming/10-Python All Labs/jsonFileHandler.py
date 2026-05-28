#Exercise 2: Creating the JSON file handler module 

import json

#This is a user defined function to read the json file
def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data


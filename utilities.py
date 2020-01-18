import configparser
import os
import json

# get constants
DIR = os.path.join(os.getcwd(), '')

def getConfig():
    # create config
    config = configparser.ConfigParser()

    # check if default config file exist
    if os.path.isfile(DIR + 'config_default.ini'):
        config.read(DIR + 'config_default.ini')

    # check if custom config file exist
    if os.path.isfile(DIR + 'config.ini'):
        config.read(DIR + 'config.ini')

    # return config
    return config

def getSpecialRoles():
    # open json file
    jsonFile = open(DIR + 'specialRoles.json')

    # read json file
    jsonStr = jsonFile.read()

    # load data
    jsonData = json.loads(jsonStr)

    # return data
    return jsonData
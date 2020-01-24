import configparser
import os
import gettext

# get constants
DIR = os.path.join(os.getcwd(), '')

# setup gettext
el = gettext.translation('base', localedir='languages', languages=['de'])
el.install()
_ = el.gettext

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
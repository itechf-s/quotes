import configparser
config = configparser.ConfigParser()
config.read('app.ini')

def get(sec, key) :
    return config[sec][key]
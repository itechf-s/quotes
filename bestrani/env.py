from pathlib import Path
import configparser

BASE_DIR = Path(__file__).resolve().parent.parent
config = configparser.ConfigParser()
config.read(BASE_DIR / 'app.ini')

def get(sec, key) :
    return config[sec][key]
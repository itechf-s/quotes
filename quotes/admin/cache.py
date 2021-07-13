import os, shutil
from bestrani import env

cachePath = env.get('general', 'CACHE_PATH')

def purge():
    if os.path.isdir(cachePath):
        if len(os.listdir(cachePath)) > 0:
            shutil.rmtree(cachePath)
            print('Purged : ', cachePath)
        else:
            print('No need to Purged')
    else:
        print('Already Purged')
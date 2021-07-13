import os, csv
from quotes.models import Quotes

def csvImport(filePath):
    print('file path : ', filePath)
    if os.path.isfile(filePath):
        with open(filePath, newline='') as fObj:
            rows = csv.reader(fObj, delimiter='\t')
            for row in rows:
                qot = {}
                qot['quotes'] = row[0]
                qot['author'] = row[1]
                qot['category'] = row[2]
                qots = Quotes(**qot)
                qots.save()
        os.remove(filePath)
        print('file Exist')
    else:
        print('file Not Exist')

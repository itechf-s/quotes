import os, csv
from quotes.models import Quotes

def csvImport(filePath):
    if os.path.isfile(filePath):
        with open(filePath, newline='') as fObj:
            rows = csv.reader(fObj, delimiter='\t')
            for row in rows:
                try:
                    qot = {}
                    qot['quotes'] = row[0]
                    qot['author'] = row[1]
                    qot['authorSlug'] = row[2]
                    qot['category'] = row[3]
                    qot['categorySlug'] = row[4]
                    qot['locale'] = row[5]
                    qot['quotesTxt'] = row[6]
                    qots = Quotes(**qot)
                    print('in quotes')
                    qots.save()
                except ValueError:
                    print('Value Error')
        print('file Exist')
        os.remove(filePath)
    else:
        print('file Not Exist')
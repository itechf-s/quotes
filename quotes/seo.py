from bestrani import env

imgPrefix = env.get('quotes', 'IMG_PREFIX')
imgDir = env.get('quotes', 'IMG_DIR')
seoDec = env.get('quotes', 'SEO_DESC')

def setMetas(qots, url):
    desc = seoDec
    metas = {}
    if qots != None:
        qot = qots[0]
        imgPath = imgPrefix + imgDir + qot.imagePath
        metas['title'] = qot.imageAlt
        metas['og:site_name'] = 'BestRani'
        metas['og:title'] = qot.imageAlt
        metas['og:type'] = 'article'
        desc = qot.quotes
        desc = qot.desc if qot.desc else desc
        metas['description'] = desc
        metas['og:description'] = desc
        metas['og:url'] = url
        metas['og:image'] = imgPath
        metas['og:image:type'] = 'image/jpeg'
        metas['og:image:width'] = '200'
        metas['og:image:height'] = '200'
        metas['og:locale'] = 'en_US'
        metas['og:locale:alternate'] = 'en_IN'    
        metas['twitter:card'] = 'summary'       
        metas['twitter:site'] = '@BestRani3'       
        metas['twitter:url'] = url      
        metas['twitter:title'] = qot.imageAlt     
        metas['twitter:description'] = desc     
        metas['twitter:image'] = imgPath
        metas['datePublished'] = qot.publishAt.strftime("%Y-%m-%dT%H:%M:%S%z")
        #if qot.updatedAt > qot.publishAt:
        #    metas['dateModified'] = qot.publishAt.strftime("%Y-%m-%dT%H:%M:%S%z")
    return metas
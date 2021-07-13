from django.test import TestCase

# Create your tests here.
pixa = {'total': 262, 'totalHits': 262, 'hits': [{'id': 5883275, 'pageURL': 'https://pixabay.com/es/photos/perro-gato-mascotas-domesticado-5883275/', 'type': 'photo', 'tags': 'perro, gato, mascotas', 'previewURL': 'https://cdn.pixabay.com/photo/2021/01/02/23/55/dog-5883275_150.jpg', 'previewWidth': 150, 'previewHeight': 100, 'webformatURL': 'https://pixabay.com/get/g5625198dafc53868821eae6c13036e5835d4ef9c51ffdac3de9a2a62907fc1922a91cadde7b44a073657e25c05426192e6baca8f97e0ddbce7681d4ee3cb14ae_640.jpg', 'webformatWidth': 640, 'webformatHeight': 427, 'largeImageURL': 'https://pixabay.com/get/g940e8a6113a6d0dec42acf098b2acdb984758fa87534921d26a4913cabe10614fe11b99765ab60f1183a70a075c38e870ffd3289975622ed0373008df895cc58_1280.jpg', 'imageWidth': 4458, 'imageHeight': 2972, 'imageSize': 3545934, 'views': 19673, 'downloads': 14949, 'collections': 73, 'likes': 80, 'comments': 17, 'user_id': 16241500, 'user': 'vaclavzavada', 'userImageURL': 'https://cdn.pixabay.com/user/2020/04/28/16-40-17-588_250x250.jpg'}, {'id': 5709765, 'pageURL': 'https://pixabay.com/es/photos/gato-perro-cachorro-gatito-pareja-5709765/', 'type': 'photo', 'tags': 'gato, perro, cachorro', 'previewURL': 'https://cdn.pixabay.com/photo/2020/11/03/13/04/cat-5709765_150.jpg', 'previewWidth': 150, 'previewHeight': 100, 'webformatURL': 'https://pixabay.com/get/g0785af48e4782b8c1b12d8f33cc9d791b1ea20d5824813e1c95321987ab3b51579e32f6fc864dbd33a5c829130727339a9a5aa0cf2e852e8c6c0e2839ff08dcf_640.jpg', 'webformatWidth': 640, 'webformatHeight': 425, 'largeImageURL': 'https://pixabay.com/get/g768075a4dd23f1c3b6c9b07ce32ecedc9a58d399696368a43f7ea01d404b1e708010605ee3e0e0caaee2ddff8b02adaa4abeede65e567952dc3efc6736724ade_1280.jpg', 'imageWidth': 4213, 'imageHeight': 2799, 'imageSize': 3725569, 'views': 26099, 'downloads': 24521, 'collections': 58, 'likes': 98, 'comments': 58, 'user_id': 13452116, 'user': 'Syaibatulhamdi', 'userImageURL': 'https://cdn.pixabay.com/user/2021/06/21/04-28-11-590_250x250.jpg'}, {'id': 5505067, 'pageURL': 'https://pixabay.com/es/photos/estatuilla-de-perro-5505067/', 'type': 'photo', 'tags': 'estatuilla de perro, estatuilla de gato, figuritas de animales', 'previewURL': 'https://cdn.pixabay.com/photo/2020/08/21/02/49/dog-figurine-5505067_150.jpg', 'previewWidth': 150, 'previewHeight': 100, 'webformatURL': 'https://pixabay.com/get/g6b83c0a02601a48b1446553040bd9451e199231724ddf06bc72df2e537ef9866a5f48e0b4814e72d0f2ca0bb497373ad7ecda6f9198ea403d0092560a9ac6158_640.jpg', 'webformatWidth': 640, 'webformatHeight': 427, 'largeImageURL': 'https://pixabay.com/get/g348fbe34256ed3bf88eb521bb24ca37e6f6691ba1a91d6b94f27bf232ef24814e17878e9ba128fa74e65240dfd1a14adb8d494e1386dcf2a25e3f8710886d5f9_1280.jpg', 'imageWidth': 3456, 'imageHeight': 2304, 'imageSize': 1204425, 'views': 155, 'downloads': 101, 'collections': None, 'likes': 1, 'comments': 0, 'user_id': 16850792, 'user': 'naraefar', 'userImageURL': 'https://cdn.pixabay.com/user/2020/07/03/12-08-34-141_250x250.jpg'}]}

hits = pixa['hits']
for hit in hits:
    print(hit['id'])
    print(hit['pageURL'])
    print(hit['userImageURL'])
    print(hit['user'])
    print(hit['user_id'])
    print(hit['largeImageURL'])
    print(hit['webformatURL'])
    print(hit['previewURL'])
    print(hit['tags'])
    print(hit['type'])

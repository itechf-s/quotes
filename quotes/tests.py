from django.test import TestCase

# Create your tests here.
fontAndWordwrapTxt = '{ 5:(3,5), 6:(4,6), 40:(55,22), 50:(52,24), 55:(51,23) }'
fontAndWordwrap = eval(fontAndWordwrapTxt)
mylen = 50

for len, fontWrap in fontAndWordwrap.items():
    if mylen <= len:
        print('Value : ', len, ' | wrap: ', fontWrap[0], ' word : ', fontWrap[1])
        break
    else:
        print('not found')
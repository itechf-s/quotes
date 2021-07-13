from django.utils import timezone
def activateQuotes(qObj):
    obj = qObj[0]
    obj.isActive = 1
    obj.publishAt = timezone.now()
    obj.save()
    print('activate : ', obj.publishAt)

def deAactivateQuotes(qObj):
    obj = qObj[0]
    obj.isActive = 0
    obj.save()
    print('deactivate : ', obj.publishAt)

def activateImage(imgs, isActive):
    obj = imgs[0]
    obj.isActive = isActive
    obj.save()
    print('Activate/Deactivate : ', obj.id)
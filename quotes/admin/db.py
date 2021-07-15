from django.utils import timezone
def activateQuotes(obj):
    obj.isActive = 1
    obj.isSchd = 0
    obj.publishAt = timezone.now()
    obj.save()
    print('activate : ', obj.publishAt)

def deAactivateQuotes(obj):
    obj.isActive = 0
    obj.save()
    print('deactivate : ')

def scheduleQuotes(obj, isSchd):
    obj.isSchd = isSchd
    obj.save()
    print('schedule/un schedule Quotes : ', obj.publishAt)

def activateImage(imgs, isActive):
    obj = imgs[0]
    obj.isActive = isActive
    obj.save()
    print('Activate/Deactivate Image: ', obj.id)
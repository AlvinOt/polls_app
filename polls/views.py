from django.http import HttpResponse


def indx(req):
    return HttpResponse("Hello djangoers. This is the polls index")

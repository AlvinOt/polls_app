from django.http import HttpResponse


def indx(req):
    return HttpResponse("Hello world. This is django's polls index")

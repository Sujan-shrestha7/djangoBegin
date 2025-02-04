from django.http import HttpResponse

def index(request):
    return HttpResponse(request,"Hello, world. You're at the polls index.")
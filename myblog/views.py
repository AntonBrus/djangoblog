# from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('About works')
    return render(request, 'about.html')
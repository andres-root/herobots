# from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader


def index(request):
    context = {'message': 'testing 2!'}
    return render(request, 'web/index.html', context)

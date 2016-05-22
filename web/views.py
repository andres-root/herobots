# from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def order(request):
    context = {}
    return render(request, 'web/order.html', context)

# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PreorderForm
# from django.template import loader


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def index_en(request):
    context = {}
    return render(request, 'web/en/index.html', context)


def index_fr(request):
    context = {}
    return render(request, 'web/fr/index.html', context)


def order(request):
    context = {}
    return render(request, 'web/order.html', context)


def order_en(request):
    context = {}
    return render(request, 'web/en/order.html', context)


def order_fr(request):
    context = {}
    return render(request, 'web/fr/order.html', context)


def process(request):
    if request.method == 'POST':
        form = PreorderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?success=true')
        else:
            return HttpResponseRedirect('/')

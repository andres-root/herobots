# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PreorderForm
# from django.template import loader


def index(request):
    context = {}
    return render(request, 'web/index.html', context)


def order(request):
    context = {}
    return render(request, 'web/order.html', context)


def process(request):
    if request.method == 'POST':
        form = PreorderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

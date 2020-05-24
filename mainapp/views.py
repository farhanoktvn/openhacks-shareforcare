from django.shortcuts import (
    render,
    HttpResponse,
    get_object_or_404,
    redirect,
)
from django.http import JsonResponse

from .models import (
    Need,
    Extra,
)

def index(request):
    return render(request, 'index.html')

def needsList(request):
    needs = Need.objects.all()
    response = {
        'needs': needs,
    }
    return render(request, 'need-list.html', response)

def needDetail(request, id):
    need = Need.objects.get(pk=id)
    response = {
        'need': need,
    }
    return render(request, 'detail.html', response)

def extrasList(request):
    extras = Extra.objects.all()
    response = {
        'extras': extras,
    }
    return render(request, 'extra-list.html', response)

def extraDetail(request, id):
    extra = Extra.objects.get(pk=id)
    response = {
        'extra': extra,
    }
    return render(request, 'detail.html', response)

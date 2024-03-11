from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_view(request: HttpRequest):
    return HttpResponse(render(request, 'products.html', {}))

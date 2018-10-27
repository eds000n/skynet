# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render(context, request))

def runAlgs(request):
    context = {}
    return JsonResponse({ 'response': 'res' })

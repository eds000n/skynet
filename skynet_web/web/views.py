# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import pylev

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render(context, request))

def runAlgs(request):
    context = {}
    matches = levenshtein()
    return JsonResponse({ 'response': matches })

#async def levenshtein():
def levenshtein():
    input_dataset = "microsft,google,facebook"
    internal_dataset = "microsoft,google,facebook"

    counter = 0
    input_ds_array = input_dataset.split(",")
    for input_ds in input_ds_array:
        minimum=100000
        for internal_ds in internal_dataset.split(","):
            t=pylev.damerau_levenshtein(input_ds, internal_ds) 
            if t<minimum:
                minimum=t
            if minimum==0:
                break
        if minimum<=2:
            counter += 1
    #print "% of matches"
    #print counter*1.0/len(input_ds_array)
    return counter*1.0/len(input_ds_array)


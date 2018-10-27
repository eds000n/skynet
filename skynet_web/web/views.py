# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Company
import pylev
from sklearn.feature_extraction.text import CountVectorizer 
import time

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render(context, request))

def runAlgs(request):
    context = {}
    lev = levenshtein()
    print lev
    return JsonResponse(lev)
    #return JsonResponse({ 'coverage': matches, 'time': 22 })

#async def levenshtein():
def levenshtein():
    start = time.time()
    #input_dataset = "microsft,google,facebook"
    input_dataset = "micrft,google,facebook"
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
    end = time.time()
    return { 'coverage': counter*100.0/len(input_ds_array), 'time': end-start }

def bagOfWords():
    vectorizer = CountVectorizer()
    data_corpus = ["John likes to watch movies. Mary likes movies too.", 
                "John also likes to watch football games."]
    X = vectorizer.fit_transform(data_corpus)
    print(X.toarray())
    print(vectorizer.get_feature_names())

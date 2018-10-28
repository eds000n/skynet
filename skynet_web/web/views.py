# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Company
import pylev
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer

import time, sys

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('web/index.html')
    return HttpResponse(template.render(context, request))

def runAlgs(request):
    context = {}
    internal_ds = getCompanies(-1)
    #print internal_ds[0]
    #print lev
    lev = levenshtein(internal_ds)
    dm = directMatch(internal_ds)
    ml = mlapproach(internal_ds)
    
    return JsonResponse([lev, dm, ml], safe=False)
    #return JsonResponse([dm, ml], safe=False)

def getCompanies(num):
    start = time.time()
    companies = []
    counter = 0
    for c in Company.objects.all():
        companies.append(c.company_name)
        if num!=-1 and counter > num: 
            break
        counter+=1
    end = time.time()
    print end - start
    return companies

#def directMatch(internal_dataset, input_dataset):
def directMatch(internal_dataset):
    start = time.time()
    #input_dataset = ["google", "facebook"]
    input_dataset = ["google", "facebook", "afsdfadsfad", "affinia group inc", "fremont luxury imports", "advantus capital management", "angeles field partners llc", "assembly & test worldwide l"]
    hashedDS = {}
    for internal_ds in internal_dataset:
        hashedDS[internal_ds]=1
    counter = 0
    for input_ds in input_dataset:
        if input_ds in hashedDS:
            counter +=1
    end = time.time()
    memory = sys.getsizeof(hashedDS)
    return { 'algorithm': 'directmatch', 'coverage': counter*100.0/len(input_dataset), 'time': end-start , 'memory': memory}

#async def levenshtein():
def levenshtein(internal_dataset):
    start = time.time()
    #input_dataset = "microsft,google,facebook"
    #input_dataset = "micrft,google,facebook"
    input_dataset = ["google", "facebook", "afsdfadsfad", "affinia group inc", "fremont luxury imports", "advantus capital management", "angeles field partners llc", "assembly & test worldwide l"]
    #internal_dataset = "microsoft,google,facebook"

    counter = 0
    maxlen = 0
    time_exceeded = False
    for input_ds in input_dataset:
        minimum=100000
        if maxlen < len(input_ds):
            maxlen = len(input_ds)
        #for internal_ds in internal_dataset.split(","):
        for internal_ds in internal_dataset:
            if maxlen < len(internal_ds):
                maxlen=len(internal_ds)
            t=pylev.damerau_levenshtein(input_ds, internal_ds) 
            if t<minimum:
                minimum=t
            if minimum==0:
                break
            if time.time() - start > 180:
                time_exceeded = True
                break
        print "distance %d" % (minimum)
        if minimum<=2:
            counter += 1
        if time_exceeded:
            break
    #print "% of matches"
    #print counter*1.0/len(input_ds_array)
    end = time.time()
    memory = sys.getsizeof([1]*maxlen)
    return { 'algorithm': 'levenshtein', 'coverage': counter*100.0/len(input_dataset), 'time': end-start , 'memory': memory}

def bagOfWords():
    vectorizer = CountVectorizer()
    data_corpus = ["John likes to watch movies. Mary likes movies too.", 
                "John also likes to watch football games."]
    X = vectorizer.fit_transform(data_corpus)
    print(X.toarray())
    print(vectorizer.get_feature_names())

def mlapproach(internal_dataset):
    input_dataset = ["google", "facebook", "afsdfadsfad", "affinia group inc", "fremont luxury imports", "advantus capital management", "angeles field partners llc", "assembly & test worldwide l"]
    #input_dataset = ["google", "facebook"]
    start = time.time()
    #t = TfidfVectorizer(min_df=1)
    vect = TfidfVectorizer(min_df=1)


    counter = 0
    for input_ds in input_dataset:
        internal_dataset.insert(0,input_ds);
        tfidf = vect.fit_transform(internal_dataset)
        p=max((tfidf * tfidf.T).A[0][1:])
        del internal_dataset[0]
        if p >=0.5 :
            counter+=1
        if time.time() - start > 180:
            break

    end = time.time()
    memory = sys.getsizeof(internal_dataset)
    return { 'algorithm': 'ml', 'coverage': counter*100.0/len(input_dataset), 'time': end-start , 'memory': memory}

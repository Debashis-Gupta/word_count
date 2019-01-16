
from django.shortcuts import render

import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
   
    wordsize = fulltext.split()
    wordDictionary = {}

    for word in wordsize:
        if word  in wordDictionary:
            wordDictionary[word]+=1

        else:
            wordDictionary[word]=1

    sortedWord = sorted(wordDictionary.items(),key=operator.itemgetter(1),reverse=True)
    print (sortedWord)

    return render(request,'count.html',{'fulltext' : fulltext, 'counts' : len(wordsize), 'sortedWord' : sortedWord })

def aboutus(request):
    return render(request,'about.html')

    
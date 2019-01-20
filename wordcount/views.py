from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['textarea']
    word_list = data.split()
    length = len(word_list)
    
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
            #increase value by 1
        else:
            worddictionary[word] = 1
            #add to dictionary and set value to 1
    sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1),reverse=True)        
    
    return render(request,'count.html',{'fulltext':data, 'words':length,'worddictionary':sorted_list})


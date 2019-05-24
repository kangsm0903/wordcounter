from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def count(request):
    Full = request.GET['fulltext']
    Numb = Full.split()
    Number = len(Full.split())

    dictionary = {}

    for word in Numb:
        if word in dictionary:
            dictionary[word] +=1
        else:
            dictionary[word] =1

    return render(request, "count.html", {'Fulltext': Full, 'Num': Number, 'word_dictionary': dictionary.items})
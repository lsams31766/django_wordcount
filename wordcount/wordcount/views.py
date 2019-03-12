from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter 

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['full_text']
    words_list = full_text.split()
    words_dict = {}
    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    sorted_words = sorted(words_dict.items(), key = itemgetter(1), reverse = True)
    return render(request, 'count.html',{
        'number_words':len(words_list),
        'sorted_words':sorted_words
        })
    
def about(request):
    return render(request, 'about.html')

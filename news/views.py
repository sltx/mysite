from django.shortcuts import render


def news(request):
    context = {}
    return render(request, "news.html", context)
    

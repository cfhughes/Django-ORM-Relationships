from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def blog(request):
    context = {
        'ip' : "3.3.3.3"
    }
    return render(request, 'blog_page.html', context)
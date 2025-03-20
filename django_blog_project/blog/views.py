from django.shortcuts import render

def home(request):
    return render(request, 'blog/base.html')

def posts(request):
    # For now, render a simple placeholder template
    return render(request, 'blog/posts.html')

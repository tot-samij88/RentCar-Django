from django.shortcuts import render

def blog(request):
    data = {
        "title":"Car Articles"
    }
    return render(request, 'blog/blog.html',data)

def single(request):
    data = {
        "title":"single Blog Posts Title"
    }
    return render(request, 'blog/single.html',data)

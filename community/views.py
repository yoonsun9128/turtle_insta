import re
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.models import Articles
# Create your views here.
def post_view(request):
    all_article = Articles.objects.all().order_by('-create_at')
    context = {
        'all_article':all_article
    }
    return render(request,'show.html',context)

def post_write(request):
    if request.method == 'GET':
        return render(request,'write.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Articles.objects.save(title=title, content=content, user = request.user)
        return redirect('community:post_view')

import re
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.models import Articles
# Create your views here.
def post_view(request):
    if request.method == 'GET':
        all_article = Articles.objects.all().order_by('-create_at')
        context = {
            'all_article':all_article
        }
        return render(request,'show.html',context)
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Articles.objects.save(title=title, content=content)
        return redirect('community:post_view')

    return HttpResponse('우선 유알엘 연결 선공?')

def post_write(request):
    if request.method == 'GET':
        return render(request,'write.html')
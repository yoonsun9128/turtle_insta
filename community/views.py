from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from community.models import Articles
# Create your views here.
def post_view(request):
    all_article = Articles.objects.all()
    print(all_article)
    return HttpResponse('우선 유알엘 연결 선공?')
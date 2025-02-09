from django.shortcuts import render, redirect, HttpResponseRedirect
from . import models
from . import forms
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def detail_article(request, id):   
    article = models.Post.objects.get(id=id)
    articles = models.Post.objects.all()
    groups = models.Category.objects.all()
    context = {
        'article': article,
        'articles': articles,
        'groups': groups
    }
    return render(request, 'blog/detail_article.html', context)

@login_required
def kofi(request):
    return render(request, 'blog/kofi.html')





from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(crete_date__lte=timezone.now()).order_by('crete_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})
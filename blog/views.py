from django.shortcuts import render, render_to_response
from models import Post


def posts_view(request):
    posts = Post.objects.all()
    return render_to_response("posts_view.html", {'posts': posts})



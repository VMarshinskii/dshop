from django.shortcuts import render_to_response, Http404, HttpResponse
from models import Post


def posts_view(request):
    posts = Post.objects.all()
    return render_to_response("posts_view.html", {
        'user': request.user,
        'posts': posts
    })


def post_view(request, url):
    try:
        post = Post.objects.get(url=url)
        return render_to_response("post_view.html", {
            'user': request.user,
            'post': post
        })
    except Post.DoesNotExist:
        raise Http404

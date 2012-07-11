"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    item=[]
    for item in post_list:
        items.append(item.title)

    
    return HttpResponse(items)

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if (showComents):
        out='<h1>'+post.title+'</h1>'+'<br>'+post.body
    else:
        out=post.title+'<br>'
    return HttpResponse(out)
    
def post_search(request, term):
    search = Post.objects.filter
    comment_title_contains='<br>'+post.term
    return HttpResponse()

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') # Create your views here.

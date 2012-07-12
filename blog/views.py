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
    for post in post_list:
        item.append(post.title)

    
    return HttpResponse(item)

def post_detail(request, id, showComments=False):
    post=Post.objects.get(pk=id)
    if (showComments):
        out='<h1>'+post.title+'</h1>'+'<br>'+post.body
    else:
        out=post.title+'<br>'
    return HttpResponse(out)
    
def post_search(request, term):
    search = Post.objects.filter(comment_title_contains='<br>'+term)
    return HttpResponse()

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') # Create your views here.

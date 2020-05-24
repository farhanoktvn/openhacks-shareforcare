from django.shortcuts import (
    render,
    HttpResponse,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required

from .models import (
    Post,
    Reply,
)
from .forms import (
    PostForm,
    ReplyForm,
)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def needsList(request):
    needs = Post.objects.filter(type='NE')
    if request.method == "POST":
        form = PostForm(request.POST)
        response = {
            'form': form,
            'needs': needs,
        }
        if form.is_valid():
            message = request.POST['message']
            city = request.POST['city']
            post = Post.objects.create(
                user = request.user,
                name = request.user.first_name,
                message = message,
                city = city,
                type = 'NE',
            )
            return redirect('/post/' + str(post.id) + "/")
        else:
            return render(request, 'need-list.html', response)
    else:
        form = PostForm()
    response = {
        'form': form,
        'needs': needs,
    }
    return render(request, 'need-list.html', response)

@login_required
def extrasList(request):
    extras = Post.objects.filter(type='EX')
    if request.method == "POST":
        form = PostForm(request.POST)
        response = {
            'form': form,
            'extras': extras,
        }
        if form.is_valid():
            message = request.POST['message']
            city = request.POST['city']
            post = Post.objects.create(
                user = request.user,
                name = request.user.first_name,
                message = message,
                city = city,
                type = 'EX',
            )
            return redirect('/post/' + str(post.id) + "/")
        else:
            return render(request, 'extra-list.html', response)
    else:
        form = PostForm()
    response = {
        'form': form,
        'extras': extras,
    }
    return render(request, 'extra-list.html', response)

@login_required
def postDetail(request, id):
    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(post=post)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        response = {
            'form': form,
            'post': post,
            'replies': replies,
        }
        if form.is_valid():
            message = request.POST['message']
            reply = Reply.objects.create(
                user = request.user,
                post = post,
                name = request.user.first_name,
                message = message,
            )
            return redirect('/post/' + str(post.id) + "/")
        else:
            return render(request, 'detail.html', response)
    else:
        form = ReplyForm()
    response = {
        'form': form,
        'post': post,
        'replies': replies,
    }
    return render(request, 'detail.html', response)

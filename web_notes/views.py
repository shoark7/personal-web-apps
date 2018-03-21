from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post

from apis.note_api import parse_post_request


def notesheet(request):
    posts = Post.objects.all()
    return render(request, 'web-notes/note.html', {'posts': posts})


def note_save(request):

    posts = Post.objects.all()
    posts_keys = {post.post_id for post in Post.objects.all()}
    new_posts = {key: value for key, value in request.POST.items() if (key.startswith('name:') \
                 and value.strip())}
    new_posts_keys = set(new_posts)

    # 1. 새로 생성
    for key in (new_posts_keys - posts_keys):
        color, coords = parse_post_request(key)
        Post.objects.create(post_id=key,
                        color=color,
                        text=new_posts[key],
                        coordinates=coords,
                       )

    # 2. 삭제
    for d in (posts_keys - new_posts_keys):
        Post.objects.get(pk=d).delete()

    # 3. 수정
    for key in posts_keys.intersection(new_posts_keys):
        updated = posts.get(pk=key)
        updated.text = new_posts[key]
        updated.save()

    return HttpResponseRedirect(reverse('web-notes:note-sheet'))

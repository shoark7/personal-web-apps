from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

from apis.note_api import parse_post_request


def notesheet(request):
    posts = Post.objects.all()
    return render(request, 'web-notes/note.html', {'posts': posts})


def note_save(request):
    if request.method == 'POST':

        posts = Post.objects.all()
        posts_keys = set(Post.objects.all())
        new_posts = {key: value for key, value in request.POST.items() if (key.startswith('name:') \
                     and value.strip())}
        new_posts_keys = set(new_posts)

        # 1. 새로 생성
        for new in (new_posts_keys - posts_keys):
            print(new)
            post_id, color, coords = parse_post_request(new)
            Post.objects.create(post_id=post_id,
                                color=color,
                                text=new_posts[new],
                                coordinates=coords,
                               )

        # 2. 삭제
        for d in (posts_keys - new_posts_keys):
            pass

        # 3. 수정
        for upd in posts_keys.intersection(new_posts_keys):
            pass


        return HttpResponse("200 post")
    return HttpResponse("200 get")

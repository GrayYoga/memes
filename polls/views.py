import datetime
import os
import urllib
from time import sleep

import vk_requests
from django.shortcuts import render
from django.http import HttpResponse, Http404

from polls.models import Memo


def index(request):
    # all = Memo.objects.all("-id")
    # min = all.last().id
    # max = all.first().id

    random_memo = Memo.objects.all().first()
    print(random_memo)
    # return HttpResponse(f"{random_memo if random_memo else 'Memes empty'}")
    return render(request, 'memo.html', {'memo': random_memo})


def load(request):
    api = vk_requests.create_api(
        service_token="9b5bcc15c700005782006cef63a910a4f0b4415d08c8a12539549407de684a8e08e29ea895b95f741c2b9")
    count = 0
    for album in [281940823, 283939598, 274262016]:
        photos = api.photos.get(owner_id=-197700721, album_id=album)
        for photo in photos["items"]:
            big = list(filter(lambda x: x['type'] == 'r', photo["sizes"]))[0]
            if photo['user_id'] < 1000:
                continue
            user = api.users.get(user_ids=photo['user_id'])[0]
            print(f"author {user['id']} {user['first_name']} {user['last_name']} {photo['album_id']}-{photo['id']}.jpg")
            urllib.request.urlretrieve(big["url"], f"polls/files/{photo['album_id']}-{photo['id']}.jpg")
            Memo(
                meme_id=photo['id'],
                author_id=user['id'],
                url=f"{photo['album_id']}-{photo['id']}.jpg",
                likes=0,
            ).save()
            count += 1
            sleep(0.2)
    return HttpResponse(f"Loading {count} files successfully")


def skip(request, meme_id):
    memes = Memo.objects.all()
    for i in range(0, memes.count()-1):
        if memes[i].meme_id == meme_id:
            print(f"Found next of id={meme_id}, this is {memes[i + 1].meme_id}")
            return render(request, 'memo.html', {'memo': memes[i + 1]})
    return render(request, 'memo.html', {'memo': memes.first()})


def like(request, meme_id):
    # print("------------")
    # print(Memo.objects.get(meme_id=meme_id).meme_id)
    # print("------------")
    Memo.objects.get(meme_id=meme_id).like().save()
    memes = Memo.objects.all()
    for i in range(0, memes.count()-1):
        print(f"Step {i} Meme:", memes[i].meme_id, memes[i].url)
        if memes[i].meme_id == meme_id:
            print(f"Found next of id={meme_id} on step {i}, this is {memes[i + 1].meme_id}")
            return render(request, 'memo.html', {'memo': memes[i + 1]})
    return render(request, 'memo.html', {'memo': memes.first()})

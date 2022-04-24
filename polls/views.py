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
    # VK loader
    # api = vk_requests.create_api(
    #     service_token="9b5bcc15c700005782006cef63a910a4f0b4415d08c8a12539549407de684a8e08e29ea895b95f741c2b9")
    # count = 0
    # for album in [281940823, 283939598, 274262016]:
    #     photos = api.photos.get(owner_id=-197700721, album_id=album)
    #     for photo in photos["items"]:
    #         big = list(filter(lambda x: x['type'] == 'r', photo["sizes"]))[0]
    #         if photo['user_id'] < 1000:
    #             continue
    #         user = api.users.get(user_ids=photo['user_id'])[0]
    #         print(f"author {user['id']} {user['first_name']} {user['last_name']} {photo['album_id']}-{photo['id']}.jpg")
    #         urllib.request.urlretrieve(big["url"], f"polls/files/{photo['album_id']}-{photo['id']}.jpg")
    #         Memo(
    #             meme_id=photo['id'],
    #             author_id=user['id'],
    #             url=f"{photo['album_id']}-{photo['id']}.jpg",
    #             likes=0,
    #         ).save()
    #         count += 1
    #         sleep(0.2)

    # another resourse loader
    urls = ("1487222271_uvesobtrbhc.jpg\n"
            "1487222224_zcdf4fh9iyo.jpg\n"
            "1487222216_rpaisnizmmq.jpg\n"
            "1487222276_nmukdgh7u7u.jpg\n"
            "1487222227_jqwffj7o1ey.jpg\n"
            "1487222285_vr350inwxsm.jpg\n"
            "1487222261_8254897_2154226_01.jpg\n"
            "1487222254_sdttztuemu.jpg\n"
            "1487222298_1486230195_e-news.su_10.jpg\n"
            "1487222277_9184024.jpg\n"
            "1487222265_rj3f8m.jpg\n"
            "1487222243_eqxi8u.jpg\n"
            "1487222312_zhdun_136888017_orig_.jpg\n"
            "1487222244_zhdun_136636967_orig_.jpg\n"
            "1487222297_46vndo.jpg\n"
            "1487222280_ui.jpg\n"
            "1487222307_iuu.jpg\n"
            "1487222239_4-74.jpg\n"
            "1487222222_ki.jpg\n"
            "1487222238_yiidhp.jpg\n"
            "1487222282_zhdun_135960132_orig_.jpg\n"
            "1487223218_1486717813138325456.jpg\n"
            "1487223191_1486545201173252509.jpg\n"
            "1487223193_1486527829146093266.jpg\n"
            "1487223160_1486290752110939577.jpg\n"
            "1487223161_1486290468175961407.jpg\n"
            "1487223141_148588718817449800.jpg\n"
            "1487223156_148580280711792649.jpg\n"
            "1487223200_148571343812819165.jpg\n"
            "1487223199_1485625949144691110.jpg\n"
            "1487223219_1485268700192754026.jpg\n"
            "1487237108_010ppymjtfc.jpg\n"
            "1488264304_t093a7zmamy.jpg.52aacc58a5e8814dfd25a4b6b0f1b746.jpg\n"
            "1487572027_9800.jpg\n"
            "1487482721_jfrbgoyrqik.jpg\n"
            "1487405890_i.jpg\n"
            "1486447487_1486316914_64.jpg\n"
            "1486446422_1459844605_strannye-statui.jpg\n")
    count = 0
    for url in urls.split("\n"):
        splitted_url = url.split("_")
        print(f"{count} author {splitted_url[0][:8]} {url}")
        print(f"https://zaebov.net/uploads/posts/2017-02/{url}", f"static/{url}")
        urllib.request.urlretrieve(f"https://zaebov.net/uploads/posts/2017-02/{url}", f"static/{url}")
        Memo(
            meme_id=splitted_url[0],
            author_id=splitted_url[0][:8],
            url=url,
            likes=0,
        ).save()
        count += 1
        sleep(0.2)
    return HttpResponse(f"Loading {count} files successfully")


def skip(request, meme_id):
    memes = Memo.objects.all()
    for i in range(0, memes.count() - 1):
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
    for i in range(0, memes.count() - 1):
        print(f"Step {i} Meme:", memes[i].meme_id, memes[i].url)
        if memes[i].meme_id == meme_id:
            print(f"Found next of id={meme_id} on step {i}, this is {memes[i + 1].meme_id}")
            return render(request, 'memo.html', {'memo': memes[i + 1]})
    return render(request, 'memo.html', {'memo': memes.first()})

import os
from datetime import datetime
from time import sleep

import vk_requests
import urllib.request

from polls.models import Memo

if __name__ == "__main__":
    api = vk_requests.create_api(
        service_token="9b5bcc15c700005782006cef63a910a4f0b4415d08c8a12539549407de684a8e08e29ea895b95f741c2b9")

    for album in [281940823, 283939598, 274262016]:
        photos = api.photos.get(owner_id=-197700721, album_id=album)
        for photo in photos["items"]:
            big = list(filter(lambda x: x['type'] == 'r', photo["sizes"]))[0]
            # print(photo)

            if photo['user_id'] < 1000:
                continue
            user = api.users.get(user_ids=photo['user_id'])[0]
            print(f"author {user['id']} {user['first_name']} {user['last_name']} {photo['album_id']}-{photo['id']}.jpg")
            urllib.request.urlretrieve(big["url"], f"files/{photo['album_id']}-{photo['id']}.jpg")

            sleep(0.1)

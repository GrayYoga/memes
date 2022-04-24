from django.db import models


class Memo(models.Model):
    meme_id = models.IntegerField()
    author_id = models.IntegerField()
    url = models.CharField(max_length=1200)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def like(self):
        self.likes += 1
        return self

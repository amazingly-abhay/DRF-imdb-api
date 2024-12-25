from django.db import models


class StreamingPlatform(models.Model):
    name=models.CharField(max_length=100)
    about=models.TextField()
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title=models.CharField(max_length=200)
    storyline=models.TextField()
    platform=models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE)
    active=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
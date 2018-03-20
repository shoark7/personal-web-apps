from django.db import models


class Post(models.Model):
    post_id = models.CharField(max_length=20)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=30, default="rgb(255,255,165)")
    coordinates = models.TextField()

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text[:15]

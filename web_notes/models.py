from django.db import models


class Post(models.Model):
    post_id = models.CharField(max_length=70, primary_key=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=30, default="#ffffa5")
    coordinates = models.TextField()

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.post_id

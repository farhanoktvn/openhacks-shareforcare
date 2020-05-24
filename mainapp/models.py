from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

POST_TYPE = (
    ('NE', 'Needs'),
    ('EX', 'Extras'),
)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=280, null=False)
    city = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=POST_TYPE, default='NE')

    def __str__(self):
        return self.name + " - /" + self.message[:10] + "/ - " + self.city + " - " + self.type

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=280, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - /" + self.message[:10] + "/ - reply"

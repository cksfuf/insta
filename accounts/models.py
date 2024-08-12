from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500 ,500],
        crop=['middle', 'center'],
        upload_to='profile'
    )

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # symetrical=True 는 싸이월드 일촌 개념. 팔로우 팔로워 처럼 단방향이 아닌 양방향 관계
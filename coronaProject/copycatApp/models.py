from django.db import models

# Create your models here.
class News(models.Model):
    number = models.IntegerField(default =1)
    title = models.CharField(max_length=70)
    manager = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    # 게시글 포스트에 이미지 추가
    cardnews = models.ImageField(blank = True, null = True)

    def __str__(self):
        return self.title
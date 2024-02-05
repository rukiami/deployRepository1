from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
    
from django.db import models

class Event(models.Model):
    # ここにフィールドを定義します
    title = models.CharField(max_length=200)
    date = models.DateField()
    image_url = models.URLField(blank=True, null=True)
    store_link = models.URLField(blank=True, null=True)
    map_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title  # 管理画面などでオブジェクトを表示する際の文字列
    # some_field_name  # 'title' フィールドがあると仮定

# class Shop(models.Model):
#     name = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)  # ジャンルフィールドの追加
#     location = models.TextField()  # 場所フィールドの追加
#     date_added = models.DateField(auto_now_add=True)  # 日付フィールドの追加

#     def __str__(self):
#         return self.nam       

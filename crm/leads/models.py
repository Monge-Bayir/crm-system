from django.db import models

class Leads(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, default='+79620620702')
    email = models.EmailField(default='example@mail.ru')

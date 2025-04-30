from django.db import models


class Leads(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, default='+79620620702')
    email = models.EmailField(default='example@mail.ru')

    # 🔁 обратная связь к Ads через строку и unique related_name
    ads = models.ForeignKey('ads.Ads', on_delete=models.CASCADE, related_name='leads')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db.models.signals import post_save
from django.dispatch import receiver
from ads.models import Ads
from leads.models import Leads

@receiver(post_save, sender=Leads)
def update_ads_on_lead_save(sender, instance, **kwargs):
    ads = instance.ads
    if ads:
        ads.update_statistics()
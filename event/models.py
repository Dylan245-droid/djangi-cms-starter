from django.db import models
from django.utils.translation import gettext_lazy as _
from cms.models import CMSPlugin


# Create your models here.

class Event(models.Model):
    name = models.CharField(_("Nom de l'événement"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("Image"), max_length=100, upload_to='images/event/', blank=True)
    date = models.DateField(_("Date"))
    time = models.TimeField(_("Heure"), blank=True)
    
    def __str__(self):
        return self.name


class EventPluginModel(CMSPlugin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name

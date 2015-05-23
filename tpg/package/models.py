from django.db import models
from django.utils.translation import ugettext_lazy as _

class Package(models.Model):
    name = models.CharField(_("name"),max_length=250)
    start_time = models.DateTimeField(_("Start Time"))
    expired_time = models.DateTimeField(_("Expired Time"))

    class Meta:
        verbose_name = _("Package")

    def __unicode__(self):
        return self.name

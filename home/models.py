# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Items(models.Model):

    #__Items_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Items_FIELDS__END

    class Meta:
        verbose_name        = _("Items")
        verbose_name_plural = _("Items")


class Bp(models.Model):

    #__Bp_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Bp_FIELDS__END

    class Meta:
        verbose_name        = _("Bp")
        verbose_name_plural = _("Bp")


class Ordr(models.Model):

    #__Ordr_FIELDS__
    docentry = models.IntegerField(null=True, blank=True)
    cardcode = models.CharField(max_length=255, null=True, blank=True)
    cardname = models.CharField(max_length=255, null=True, blank=True)
    docdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Ordr_FIELDS__END

    class Meta:
        verbose_name        = _("Ordr")
        verbose_name_plural = _("Ordr")


class Rdr1(models.Model):

    #__Rdr1_FIELDS__
    itemname = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    linetotal = models.IntegerField(null=True, blank=True)

    #__Rdr1_FIELDS__END

    class Meta:
        verbose_name        = _("Rdr1")
        verbose_name_plural = _("Rdr1")



#__MODELS__END

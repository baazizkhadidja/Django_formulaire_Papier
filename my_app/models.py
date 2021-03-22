# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class table_ins(models.Model):
    nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 30)

    class Meta :
        managed = False
        db_table = 'table_ins'


class Accounts(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    lat = models.FloatField(default=0.0)
    longit = models.FloatField(default=0.0)
    primary_poc = models.CharField(max_length=30, default="")
    sales_rep_id = models.IntegerField(blank=True, default=0)

    class Meta:
        managed = False
        db_table = 'accounts'


class Orders(models.Model):
    account_id = models.PositiveSmallIntegerField(blank=True, null=True)
    occurred_at = models.DateField(blank=True, null=True)
    standard_qty = models.IntegerField(blank=True, null=True)
    gloss_qty = models.IntegerField(blank=True, null=True)
    poster_qty = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    standard_amt_usd = models.FloatField(blank=True, null=True)
    gloss_amt_usd = models.FloatField(blank=True, null=True)
    poster_amt_usd = models.FloatField(blank=True, null=True)
    total_amt_usd = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Region(models.Model):
    id = models.IntegerField(blank=True, primary_key = True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class SalesReps(models.Model):
    id = models.IntegerField(blank=True, primary_key = True)
    name = models.CharField(max_length=30, blank=True, null=True)
    regio_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_reps'


class WebEvents(models.Model):
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    occurred_at = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_events'

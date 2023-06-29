from django.db import models


class Weight(models.Model):
    weight_kg = models.FloatField()
    date = models.DateField()


"""
class Hip(models.Model):
    hip = models.IntegerField()
    date = models.DateField()


class Wrist(models.Model):
    wrist = models.IntegerField()
    date = models.DateField()


class Neck(models.Model):
    neck = models.IntegerField()
    date = models.DateField()


class Forearm(models.Model):
    forearm = models.IntegerField()
    date = models.DateField()


class Waist(models.Model):
    waist = models.IntegerField()
    date = models.DateField()


class Shin(models.Model):
    shin = models.IntegerField()
    date = models.DateField()


class Thigh(models.Model):
    thigh = models.IntegerField()
    date = models.DateField()
"""
from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title

class Rank(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Cadet(models.Model):
    lastname = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    birthdate = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.lastname + " " + self.firstname

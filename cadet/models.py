from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title

class Rank(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=128)
    hours = models.IntegerField()
    term = models.IntegerField(null=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    theme = models.CharField(max_length=128)
    hours = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.theme

class Cadet(models.Model):
    lastname = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    birthdate = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.lastname + " " + self.firstname

class Mark(models.Model):
    value = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    cadet = models.ForeignKey(Cadet, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.value

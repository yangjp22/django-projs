from django.db import models

# Create your models here.
class Person(models.Model):
    SHIRT_SIZE = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large")
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=20)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name="Musician")
    name = models.CharField(max_length=20)
    release_date = models.DateField()
    num_start = models.IntegerField(default=0)


class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField("Runner Name", max_length=20)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

    def __str__(self):
        return self.name
    

class Group(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invited_reason = models.CharField(max_length=20)


class Ox(models.Model):
    horn_length = models.IntegerField(default=0)

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=20)

    def __str__(self):
        return self.name
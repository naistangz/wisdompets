from django.db import models
# Contains base class Model


# Defining Pet model by creating a class called Pet, inheriting from Model class in models
class Pet(models.Model):
    # Creating constant called SEX_CHOICES with tuples. First value stored in database, second value displayed as tring
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


# many to many relationship because a pet can have many vaccines and the same vaccine can be applied to many pets
class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # method tells django what the string representation should be for this model
    def __str__(self):
        return self.name



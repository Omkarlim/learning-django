from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    """Model definition for Pet."""
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

    # TODO: Define fields here

    class Meta:
        """Meta definition for Pet."""

        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        """Unicode representation of Pet."""
        pass

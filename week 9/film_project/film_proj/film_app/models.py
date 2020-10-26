from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def delete_director(self):
        self.delete()
        self.save()

    def __str__(self):
        return self.first_name



class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='created_films')
    available_in_countries = models.ManyToManyField(Country, related_name='available_films')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)


    def delete_film(self):
        self.delete()
        self.save()
       

    def __str__(self):
        return self.title




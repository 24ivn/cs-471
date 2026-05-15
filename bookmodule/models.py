from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.title



class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city}, {self.street}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Task 2: Many-to-Many relation
    addresses = models.ManyToManyField(Address) 

    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/') 

    def __str__(self):
        return self.title
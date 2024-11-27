from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField (default = 0.0)
    edition = models.SmallIntegerField (default = 1)

class Address(models.Model):
    city = models.CharField(max_length = 50 )

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length = 50)
    age =models.SmallIntegerField(default = 7)
    address = models.ForeignKey(Address , on_delete= models.CASCADE,null=True)

    


class Student2(models.Model):
    name = models.CharField(max_length = 50)
    age =models.SmallIntegerField(default = 7)
    address2 = models.ManyToManyField(Address)


class Products(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    productImage = models.FileField(upload_to='products/')  # File uploads will go to 'media/uploads/'


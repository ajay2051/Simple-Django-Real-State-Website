from django.db import models



class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    area = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()


    class Meta:
        ordering = ('title',)


    def __str__(self):
        return self.title


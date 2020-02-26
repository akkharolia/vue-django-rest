from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(blank=True,max_length=500)
    price = models.FloatField(blank=True,default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=False,default='0')
    quantity = models.IntegerField(default=1,editable=False)

    def __str__(self):
        return self.title+'   '+str(self.id)

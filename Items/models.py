from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)
    def __str__(self): return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images',blank=True, null=True)

    def __str__(self): return self.name
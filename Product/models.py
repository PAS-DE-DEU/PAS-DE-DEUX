from django.db import models
from Category.models import Category
from colorful.fields import RGBColorField
from django.urls import reverse

# Create your models here.

SIZE_CHOICES = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
)

class product(models.Model): 
    product_name = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1024, null=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Size = models.CharField(max_length=128, choices=SIZE_CHOICES)
    color = RGBColorField(default='#fff')
    price = models.IntegerField(null=False)
    product_offer = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return  self.product_name
    
    def get_url(self):
        return reverse('product-detail', args=[self.category, self.slug])
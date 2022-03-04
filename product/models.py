from io import BytesIO
from tokenize import blank_re
from django.db import models
from PIL import Image
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    image = models.ImageField(upload_to="uploads/",blank=True,null=True)
    thumbnail = models.ImageField(upload_to="uploads/",blank=True,null=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+ self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+ self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000'+self.image.url     
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io =BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail = File(thumb_io,name=image.name)
        return thumbnail


from django.db import models
from PIL import Image

# Create your models here.

def upload_path(instance, filname):
    return '/'.join(['image', str(instance), filname])


class FoodCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    image = models.ImageField(blank=True,null=True, upload_to=upload_path)


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>400 or img.width>400:
            img_resize=(400,400)
            img.thumbnail(img_resize)
            img.save(self.image.path)


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    number=models.IntegerField()
    name = models.CharField(max_length=100)
    shordesc = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True,upload_to=upload_path)
    # category =models.ForeignKey(FoodCategory,on_delete=models.CASCADE)
    category_id = models.IntegerField()


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>400 or img.width>400:
            img_resize=(300,300)
            img.thumbnail(img_resize)
            img.save(self.image.path)




class FavoriteFoods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shordesc = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True,upload_to=upload_path)
    # category =models.ForeignKey(FoodCategory,on_delete=models.CASCADE)


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height>600 or img.width>600:
            img_resize=(600,600)
            img.thumbnail(img_resize)
            img.save(self.image.path)

from django.contrib import admin
from .models import Food,FoodCategory,FavoriteFoods
# Register your models here.
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(FavoriteFoods)
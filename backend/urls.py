from rest_framework import routers
from django.urls import path, include
from .views import FoodApi,FootCategoryApi,FavoriteFoodsApi

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'foods-category', FootCategoryApi)
router.register(r'foods',FoodApi,basename='addfood')
router.register(r'favorite-food',FavoriteFoodsApi,basename='Favorite')

# router.register(r'banner', Bannerapi)
urlpatterns = [
    path('', include(router.urls)),
    # path('add-food/', views.FoodApi.as_view()),
    # path('add-food-category/', views.addFoodCategory),
    # path('get-food/', views.getFood),
    # path('get-food-category/<int:pk>/', views.getFoodCategory)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
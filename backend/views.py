from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics,filters
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from backend.models import Food, FoodCategory,FavoriteFoods
from backend.serializers import FoodCategorySerializer,FoodSerializers,FavoriteFoodSerializers
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
#
class FootCategoryApi(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all().order_by('id')
    serializer_class = FoodCategorySerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']





class FoodApi(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializers

    filter_backends = [filters.SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    # search_fields=['category']

class FavoriteFoodsApi(viewsets.ModelViewSet):
    queryset = FavoriteFoods.objects.all().order_by('id')
    serializer_class = FavoriteFoodSerializers

    filter_backends = [filters.SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']





    #
    # def get_queryset(self):
    #     queryset = Food.objects.all()
    #     id = self.request.query_params.get('category')
    #     if id is not None:
    #         queryset = queryset.filter(purchaser__username=id)
    #     return queryset




# @api_view(['GET', 'POST', 'DELETE'])
# @api_view(['POST'])
# def addFood(request):
#     try:
#         food=Food.objects.all()
#     except Food.DoesNotExit:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#
#     food_data=JSONParser().parse(request)
#     food_serializers=FoodSerializers(data=food_data)
#     if food_serializers.is_valid():
#         food_serializers.save()
#         return JsonResponse(food_serializers.data,safe=False)
#     return JsonResponse(food_serializers.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET'])
# def getFood(request):
#     print("Food section")
#     getFood_data=Food.objects.filter(category_id=2)
#     # print(getFood_data)
#     print("Food ")
#     food_serializers = FoodSerializers(getFood_data, many=True)
#     return JsonResponse(food_serializers.data, safe=False)
    # return JsonResponse({})

#
# @api_view(['POST'])
# def addFoodCategory(request):
#     try:
#         food_category = FoodCategory.objects.all()
#     except FoodCategory.DoesNotExit:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#
#     foodCategory_data = JSONParser().parse(request)
#     food_categoru_serializers = FoodCategorySerializer(data=food_category)
#     if food_categoru_serializers.is_valid():
#         food_categoru_serializers.save()
#         return JsonResponse(food_categoru_serializers.data, safe=False)
#     return JsonResponse(food_categoru_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def getFoodCategory(request, pk):
#     getFoodCategory_data = FoodCategory.objects.get(pk=pk)
#     food_categoru_serializers = FoodCategorySerializer(getFoodCategory_data, many=True)
#     return JsonResponse(food_categoru_serializers.data, safe=False)

#
# @api_view(['GET', 'POST', 'DELETE'])
#
# def addFood_category(request, pk=0):
#     try:
#         food_category = FoodCategory.objects.all()
#         food_serializers = FoodSerializers(food_category, many=True)
#     except Food.DoesNotExit:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#
#     food_category_serializers = FoodCategorySerializer(food_category, many=True)
#     return JsonResponse(food_category_serializers.data, safe=False)
#
# @api_view([ 'POST', 'DELETE'])
# def add_food(request, pk=0,format=None):
#
#     #creat an object form stundent model
#     try:
#         food = Food.objects.all()
#     except Food.DoesNotExist:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#
#
#     if request.method == 'POST':
#         food_data = JSONParser().parse(request)
#         food_serializer = FoodSerializers(data=food_data)
#         if food_serializer.is_valid():
#             food_serializer.save()
#             return JsonResponse(food_serializer.data,safe=False)
#         return JsonResponse(food_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     elif request.method == 'DELETE':
#         student = Food.objects.get(studentId=pk)
#         student.delete()
#         return JsonResponse("Food Was Deleted Successfully", safe=False)
#
#
#
# @api_view(['GET', 'POST', 'DELETE'])
# def add_food_category(request, pk=0,format=None):
#
#     #creat an object form food category model
#     try:
#         food_category = Food.objects.all()
#     except FoodCategory.DoesNotExist:
#         return JsonResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         food_category_serializer = FoodSerializers(food_category,many=True)
#         return JsonResponse(food_category_serializer.data,safe=False)
#
#     elif request.method == 'POST':
#         food_category_data = JSONParser().parse(request)
#         food_category_serializer = FoodSerializers(data=food_category_data)
#         if food_category_serializer.is_valid():
#             food_category_serializer.save()
#             return JsonResponse(food_category_serializer.data,safe=False)
#         return JsonResponse(food_category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     elif request.method == 'DELETE':
#         student = FoodCategory.objects.get(studentId=pk)
#         student.delete()
#         return JsonResponse("Food category Was Deleted Successfully", safe=False)




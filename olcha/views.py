from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from olcha.models import Category,Group,Product,Comment
from olcha.serializers import ProductModelSerializer,CommentModelSerializer,UserModelSerializer
from rest_framework import generics



# Create your views here.

"""  1 st  and 2 nd version  Barcha ma'lumotlarni bitta viewda chiqarish uchun """

# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer
#     permission_classes = [AllowAny]


class CategoryListView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializers = CategoryModelSerializer(categories, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    

class ProductListView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializers = ProductModelSerializer(products,many=True,context = {'request':request})
        return Response(serializers.data,status=status.HTTP_200_OK)


class CommentListView(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        serializers = CommentModelSerializer(comments,many = True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializers = UserModelSerializer(users,many=True,context = {'request':request})
        return Response(serializers.data,status = status.HTTP_200_OK)

""" 3rd version Barcha malumotlarni aloxida aloxida viewlarda ciqarish uchun """
"""
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializers = CategoryModelSerializer(categories, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = CategoryModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializers = CategoryModelSerializer(category)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        category = self.get_object(slug)
        serializer = CategoryModelSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        category = self.get_object(slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializers = GroupModelSerializer(instance=groups, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    serializer_class = GroupModelSerializer
    def post(self, request):
        serializers = GroupModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class GroupDetailView(APIView):
    def get_object(self, slug):
        try:
            return Group.objects.get(slug=slug)
        except Group.DoesNotExist:
            return None

    def get(self, request, slug):
        group = get_object_or_404(Group, slug=slug)
        serializers = GroupModelSerializer(group)
        return Response(serializers.data, status=status.HTTP_200_OK)
        

    def put(self, request, slug):
        group = self.get_object(slug)
        serializer = GroupModelSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        group = self.get_object(slug=slug)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializers = ProductModelSerializer(instance=products, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    serializer_class = ProductModelSerializer
    def post(self, request):
        serializers = ProductModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
"""










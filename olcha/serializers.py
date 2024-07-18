from rest_framework import serializers
from django.contrib.auth.models import User

from olcha.models import Category,Group,Product,Image,Comment

""" First version,API dagi category da hamma ma'lumotlar birdan ciqadi group va
 undagi product lar bn.Bunda faqat serializerda logika qilindi va malumotlarni bitta viewda ciqarildi """

# class ImageModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['image']

# class ProductModelSerializer(serializers.ModelSerializer):
#     images = ImageModelSerializer(many = True,read_only=True)
    
#     class Meta:
#         model = Product
#         fields = ['product_name','description','price','quantity','rating','discount','slug','images']

# class GroupModelSerializer(serializers.ModelSerializer):
#     images = ImageModelSerializer(many = True,read_only=True)
#     products = ProductModelSerializer(many=True,read_only=True)
#     class Meta:
#         model = Group
#         fields = ['group_name','slug','images','products']

# class CategoryModelSerializer(serializers.ModelSerializer):
#     images = ImageModelSerializer(many = True,read_only=True)
#     groups = GroupModelSerializer(many = True,read_only=True)
#     class Meta:
#         model = Category
#         fields = ['id','category_name','images','groups']


""" 2nd version, malumotlarni serializer  funksiyalardan foydalanib  olish  va malumotlarni bitta viewda chiqarish uchun"""


"""
class  ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image','is_primary']

class ProductModelSerializer(serializers.ModelSerializer):
    primary_image =  serializers.SerializerMethodField(method_name='yoo')
    all_images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['product_name','description','price','quantity','rating','discount','slug','primary_image','all_images']
    
    

    def get_all_images(self, instance):
        images = Image.objects.all().filter(product=instance)
        all_images = []
        request = self.context.get('request')

        for image in images:
            all_images.append(request.build_absolute_uri(image.image.url))

        return all_images

    
    def yoo(self,instance):
        image = Image.objects.filter(product=instance,is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)

        return None
class GroupModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(method_name='moo')
    products = ProductModelSerializer(many = True, read_only=True)
    class Meta:
        model = Group
        fields = ['id','group_name','slug','image','products']

    def moo(self,instance):
        image = Image.objects.filter(group=instance, is_primary=True).first()
        request = self.context.get('request')
        
        if image:
        
            image_url = image.image.url
            return request.build_absolute_uri(image_url)

        return None
     

class CategoryModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(method_name='foo')
    groups = GroupModelSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name','slug','image','groups']
    
    def foo(self,instance):
        image = Image.objects.filter(category=instance, is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)

        return None
    # def get_image(self,instance):
    #     image = Image.objects.filter(category=instance,is_primary=True).first()
    #     if image:
    #         serializer = ImageModelSerializer(image)
    #         return serializer.data.get('image')
    #     return None

 """   

""" 3rd version barcha malumotlarni aloxida aloxida chiqarish uchun aloxida serializerlardan foydanlanildi """

"""
class  ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class GroupModelSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name')
    category_slug = serializers.CharField(source='category.slug')

    images = ImageModelSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id','group_name','slug','images','category_name','category_slug']
    

class CategoryModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','category_name','slug','images']


class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many=True,read_only=True)
    group_name = serializers.CharField(source='group.group_name')
    group_slug = serializers.CharField(source='group.slug')

    class Meta:
        model = Product
        fields = ['id','product_name','description','price','quantity','rating','discount','slug','group_name','group_slug','images']


"""

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class CommentModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username')
    product_name = serializers.CharField(source='product.product_name')
    class Meta:
        model = Comment
        fields = ['username','message','file','product_name']
        # extra_fields = ['username']
class  ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class ProductModelSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.group_name')
    category_name = serializers.CharField(source='group.category.category_name')
    comments = CommentModelSerializer(many = True,read_only=True)
    primary_image = serializers.SerializerMethodField()
    all_images = serializers.SerializerMethodField()


    def get_primary_image(self,instance):
        image = Image.objects.filter(product=instance,is_primary=True).first()
        request = self.context.get('request')
        if image:
            image_url = image.image.url
            return request.build_absolute_uri(image_url)
        
        return None

    def get_all_images(self,instance):
        images = Image.objects.filter(product=instance).all()
        request = self.context.get('request')
        all_images = []
        if images:
            for image in images:
                all_images.append(request.build_absolute_uri(image.image.url))

            return all_images




    class Meta:
        model  = Product
        fields = '__all__'
        extra_fields = ['category_name','group_name','primary_image','all_images','comments']
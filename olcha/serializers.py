from rest_framework import serializers

from olcha.models import Category,Group,Product,Image

""" First version,API dagi category da hamma ma'lumotlar birdan ciqadi group va
 undagi product lar bn.Bunda faqat serializerda logika qilindi va malumotlarni bitta viewda ciqarildi """

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many = True,read_only=True)
    
    class Meta:
        model = Product
        fields = ['product_name','description','price','quantity','rating','discount','slug','images']

class GroupModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many = True,read_only=True)
    products = ProductModelSerializer(many=True,read_only=True)
    class Meta:
        model = Group
        fields = ['group_name','slug','images','products']

class CategoryModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many = True,read_only=True)
    groups = GroupModelSerializer(many = True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','category_name','images','groups']


""" 2nd version, malumotlarni serializer  funksiyalardan foydalanib  olish  va malumotlarni bitta viewda chiqarish uchun"""

"""

class  ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image','is_primary']

class ProductModelSerializer(serializers.ModelSerializer):
    product_images =  serializers.SerializerMethodField(method_name='yoo')
    class Meta:
        model = Product
        fields = ['product_name','description','price','quantity','rating','discount','slug','product_images']
    
    def yoo(self,instance):
        images = Image.objects.filter(product=instance)
        if images:
            serializer = ImageModelSerializer(images)
            return serializer.data.get('images')
        return None
class GroupModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    products = ProductModelSerializer(many = True, read_only=True)
    class Meta:
        model = Group
        fields = ['id','group_name','slug','image','products']

    def get_image(self,instance):
        image = Image.objects.filter(group=instance,is_primary=True).first()
        if image:
            serializer = ImageModelSerializer(image)
            return serializer.data.get('image')
        return None
     

class CategoryModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    groups = GroupModelSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name','slug','image','groups']
    
    def get_image(self,instance):
        image = Image.objects.filter(category=instance,is_primary=True).first()
        if image:
            serializer = ImageModelSerializer(image)
            return serializer.data.get('image')
        return None
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


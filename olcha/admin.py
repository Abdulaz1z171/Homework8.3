from django.contrib import admin
from olcha.models import  Product,Category,Group,Image

# Register your models here.

admin.site.register(Product)


admin.site.register(Image)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    
    list_display = ['category_name','slug']
    prepopulated_fields = {'slug':('category_name',)}


@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    
    list_display = ['group_name','slug']
    prepopulated_fields = {'slug':('group_name',)}
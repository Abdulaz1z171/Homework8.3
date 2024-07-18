
from django.urls import path,include
from olcha import views



urlpatterns = [
    # 1 st and 2nd version Barcha malumotlarni bitta viewda ciqarish uchun
    path('category-list/',views.CategoryListView.as_view(), name = 'category_list'),
    path('products/',views.ProductListView.as_view(),name = 'products'),
    path('comments/',views.CommentListView.as_view(),name = 'comments'),
    path('users/',views.UserListView.as_view(), name = 'users')
    

    #  3rd version                       xar bir categoriyani aloxida aloxida viewlarda chiqarish  
    # path('category/<slug:slug>/',views.CategoryDetailView.as_view(),name = 'category_detail'),
    # path('category-list/',views.CategoryListView.as_view(), name = 'category_list'),
    # path('groups/',views.GroupListView.as_view(),name = 'group_list'),
    # path('group/<slug:slug>/',views.GroupDetailView.as_view(),name = 'group_detail'),
    # path('products/',views.ProductListView.as_view(),name = 'productt_list'),

]

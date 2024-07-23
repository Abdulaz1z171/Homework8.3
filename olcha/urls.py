
from django.urls import path,include
from olcha import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('categories', views.CategoryModelViewSet,basename = 'category')


urlpatterns = [
    # 1 st and 2nd version Barcha malumotlarni bitta viewda ciqarish uchun
    path('category-list/',views.CategoryListView.as_view(), name = 'category_list'),
    path('products/',views.ProductListView.as_view(),name = 'products'),
    path('comments/',views.CommentListView.as_view(),name = 'comments'),
    path('users/',views.UserListView.as_view(), name = 'users'),
    path('register/',views.register.as_view(), name = 'register'),
    path('category-list-generic-api-view/',views.CategoryList.as_view(),name = 'category-list'),
    path('category-detail-generic-api-view/<int:pk>/',views.CategoryDetail.as_view(),name = 'category-list'),
    path('category-add-generic-api-view/',views.CategoryAdd.as_view(),name = 'category-add'),
    path('category-delete-generic-api-view/<int:pk>/',views.CategoryDelete.as_view(),name = 'category-delete'),
    path('category-list-create-generic-api-view/',views.CategoryListCreate.as_view(),name = 'category-list-create'),
    path('category-update-generic-api-view/<int:pk>/',views.CategoryChange.as_view(),name = 'category-update'),
    path('modelviewset/',include(router.urls))

    

    #  3rd version                       xar bir categoriyani aloxida aloxida viewlarda chiqarish  
    # path('category/<slug:slug>/',views.CategoryDetailView.as_view(),name = 'category_detail'),
    # path('category-list/',views.CategoryListView.as_view(), name = 'category_list'),
    # path('groups/',views.GroupListView.as_view(),name = 'group_list'),
    # path('group/<slug:slug>/',views.GroupDetailView.as_view(),name = 'group_detail'),
    # path('products/',views.ProductListView.as_view(),name = 'productt_list'),

]

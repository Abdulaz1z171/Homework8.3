
from django.urls import path,include
from olcha import views


urlpatterns = [
    path('category-list/',views.CategoryListView.as_view(), name = 'category_list'),
    path('category/<slug:slug>/',views.CategoryDetailView.as_view(),name = 'category_detail'),
    path('groups/',views.GroupListView.as_view(),name = 'group_list'),
    path('group/<slug:slug>/',views.GroupDetailView.as_view(),name = 'group_detail')

]

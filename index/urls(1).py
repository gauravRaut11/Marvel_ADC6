
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('items/<int:pk>/',views.delete_item),
    path('upload/items/', views.Item_list),
    path('', views.upload_item),
]

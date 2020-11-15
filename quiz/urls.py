from django.urls import path
from . import views
import re
urlpatterns = [
    path('',views.home,name='home'),
    path('json/',views.json,name='json'),
    #path('list', views.list, name='list'),#全シフトデータ
    #path('add_problems', views.add_problems, name='add_problems'),#全シフトデータ
]
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_person, name='add_person'),
    path('', views.people_list, name='people_list'),
]
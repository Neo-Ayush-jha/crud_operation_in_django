from django.contrib import admin
from django.urls import path
from school.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("/delete/<int:id>/",deleteF,name="delete"),
    path("/edit/<int:id>/",editStudent,name="edit"),
    path("search/",search,name="search"),
    path("filter-city/",filter,name="filter")
]

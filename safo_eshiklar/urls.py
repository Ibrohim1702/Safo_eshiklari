from django.urls import path

from safo_eshiklar.models import Category

urlpatterns = [
    # path('', index, name="home"),
    path('ctg/<key>/', Category, name="ctg")
]

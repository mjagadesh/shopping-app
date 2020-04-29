from django.conf.urls import url
from django.urls import path
from .import views
from django.urls import include, path
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'shopping',views.ShoppingDetails)

urlpatterns = [
url('', include(router.urls)),
]

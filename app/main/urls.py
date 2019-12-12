from django.urls import path, include
from rest_framework import routers
from bank import views as bank_views 
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', bank_views.UserViewSet)
router.register(r'groups',bank_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]

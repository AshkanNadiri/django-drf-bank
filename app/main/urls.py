from django.urls import path, include
from rest_framework import routers
from bank import views as bank_views 


router = routers.DefaultRouter()
router.register(r'users', bank_views.UserSerializer, name = 'user')
router.register(r'groups',bank_views.GroupSerializer, name = 'groups')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

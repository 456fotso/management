from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students.views import StudentViewSet, home

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),   # 👈 route racine
    path('api/', include(router.urls)),
]

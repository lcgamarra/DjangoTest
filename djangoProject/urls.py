"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

from djangoProject.views import MusicalWorkListView
from djangoProject.views import MWMetaViewSet

# router = routers.DefaultRouter()
# router.register(r'meta', views.MWMetaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MusicalWorkListView.as_view()),
    path('meta/<iswc>/', MWMetaViewSet.as_view({'get': 'list', 'set': 'permission_denied'}))
    # path('', include(router.urls))
]

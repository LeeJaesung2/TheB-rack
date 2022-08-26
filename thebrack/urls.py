"""thebrack URL Configuration

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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('',include('pwa.urls')),
    path('status',views.post, name='post'),
    #path('status/<int:bycicle_position>',views.get, name='get'),
    path('status/<int:bycicle_position>',views.update, name='update'),
    path('position/<int:bycicle_position>', views.rack, name="rack"),
    path('remove',views.remove, name="remove"),
    path('user/', include('user.urls')),
]

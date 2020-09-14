"""wisdompets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # matching a url with an empty path or root URL, then dispatching to the home function from the views module and lastly naming the pattern home
    path('', views.home, name='home'),
    # creating route for looking at individual pets, using capture group
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
]
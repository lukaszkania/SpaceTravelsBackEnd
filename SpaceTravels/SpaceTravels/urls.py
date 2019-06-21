"""SpaceTravels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('tourists.urls')), # Showing Django where he should searching for urlpatterns 
    path('', include('SpaceTravels.views')), # Pointing into urlpatterns in views.py file in main folder
    path('api-tourists/', include('tourists.api.urls')), # Pointing on our api urls in tourists app
    path('api-flights/', include('flights.api.urls')), # Pointing on our api urls in flights app
]

"""
URL configuration for music_streaming_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path

from music import views
from music.views import add_song

from admin.views import login_view, signup

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('add-song/', login_required(add_song), name='add_song'),
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
]

"""Intelligence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users.views import user
from songplayer.views import songs,artists,genres,albums,search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/user/$',user),
    url(r'^api/v1/songs/$',songs),
    url(r'^api/v1/genres/$',genres),
    url(r'^api/v1/albums/$',albums),
    url(r'^api/v1/artists/$',artists),
    url(r'^api/v1/search/$',search)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('account', include('testdb.urls')),
]
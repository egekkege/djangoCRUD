"""
URL configuration for djangoProject project.

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
from testdb import views
from testdb.views import PeopleUpdateView
from testdb.views import PeopleDeleteView
from testdb.views import PeopleCreateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('users/', include('testdb.urls')),
    #path('my-url/', views.my_view, name='my_view'),
    path('', views.show_all, name='show_all'),
    path('read/<int:id>/', views.show_one, name='show_one'),
    path('api/people/<int:pk>/', PeopleUpdateView.as_view(), name='person-update'),
    path('api/peopled/<int:pk>/', PeopleDeleteView.as_view(), name='person-delete'),
    path('api/people/', PeopleCreateView.as_view(), name='people-create'),
]
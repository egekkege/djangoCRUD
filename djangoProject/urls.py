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
# from testdb.views import PeopleUpdateView
# from testdb.views import PeopleDeleteView
# from testdb.views import PeopleCreateView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.PeopleList.as_view(), name='show_all'),
    path('peoplelist/<int:pk>/', views.PeopleList.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('testdb/', include('testdb.urls')),
    # path('read/<int:id>/', views.show_one, name='show_one'),
    # path('api/people/<int:pk>/', PeopleUpdateView.as_view(), name='person-update'),
    # path('api/peopled/<int:pk>/', PeopleDeleteView.as_view(), name='person-delete'),
    # path('api/people/', PeopleCreateView.as_view(), name='people-create'),
     path('peoplelist/', views.PeopleList.as_view()),
]

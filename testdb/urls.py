from django.urls import path, include
from testdb.api import SimpleApI
urlpatterns = [
    path('api/hello', SimpleApI.as_view() ),
]
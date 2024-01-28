from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.template import loader
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import PeopleSerializer
from .models import People
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
#from rest_framework.tokens import RefreshToken

# Views below help to CRUD operations

class PeopleList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all people, or create a new person.
    """
    def get(self, request, format=None):
        person = People.objects.all()
        serializer = PeopleSerializer(person, many=True)
        mydata = People.objects.all().values()
        template = loader.get_template('template.html')
        context = {
            'mymembers': mydata,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, format=None):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PeopleSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
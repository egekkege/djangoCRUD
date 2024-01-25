from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.template import loader
from rest_framework import generics
from .serializers import PeopleSerializer
from .models import People

# Views below help to CRUD operations


@require_http_methods(["GET"])
def show_all(request):
    mydata = People.objects.all().values()
    template = loader.get_template('template.html')
    context = {
      'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

@require_http_methods(["GET"])
def show_one(request, id):

    mydata = People.objects.filter(id=str(id)).values()
    template = loader.get_template('template.html')
    context = {
      'mymembers': mydata,
    }
    if(len(mydata)==0):
        raise Http404("")
    else:
        return HttpResponse(template.render(context, request))


class PeopleCreateView(generics.CreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleUpdateView(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleDeleteView(generics.DestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

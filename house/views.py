from django. shortcuts import render

from . models import Slider, Company, students, Teams, pricings
from . serializers import CompanySerializer
from . serializers import studentSerializer
from rest_framework  import  viewsets
from . serializers import  TeamsSerializer
from . serializers import pricingsSerializer

# Create your views here.

class pricingsViewSet(viewsets.ModelViewSet):
    queryset =pricings.objects.all()
    serializer_class = pricingsSerializer


class studentviews(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = studentSerializer


class Companyviews(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class Teamsviews(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

def index(request):
    sliders =Slider.objects.all()
    return render(request, 'index.html',{"sliders":sliders})

def starter(request):
    return render(request, 'starter-page.html')

def teams(request):
    teams = Teams.objects.all()
    return render(request, 'index.html', {'teams':teams})













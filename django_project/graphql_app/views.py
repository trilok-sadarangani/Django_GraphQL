from django.shortcuts import render
from django.http import HttpResponse # IMPORT HttpResponse FROM MODULE
from graphql_app.models import Mod, Webpage, AccessRecord
# Create your views here.
def index(request):
    #my_dict = {'render_variable': "Testing Templates"}
    #return render(request,'try_app/index.html', context = my_dict)
    return HttpResponse("Hello World!")

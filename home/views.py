from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

from home.models import Slot_status

def index(request):

	#Genereate counts of the Parking Slots
	slot_count = Slot_status.objects.all().count()

	#Generate counts of available Parking slots
	slot_available = Slot_status.objects.filter(status__exact='1').count()

	context = {
		'slot_count' : slot_count,
		'slot_available' : slot_available,
	}
	# Render the HTML template index.html with the data in the context
	return render(request, 'index.html', context=context)
    #This is like hello world
    #return HttpResponse("This is Index Page.")

def login(request):
    return HttpResponse("This is Login Page.")

def register(request):
    return HttpResponse("This is Register Page.")

def home(request):
    return HttpResponse("This is home page.")

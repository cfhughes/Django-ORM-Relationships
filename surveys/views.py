from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder for all surveys")

def new(request):
    return HttpResponse("placeholder for new survey")
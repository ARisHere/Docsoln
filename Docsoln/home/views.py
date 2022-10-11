from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    
    return render (request, 'index.html')
    # return HttpResponse("this is home page")

def appointment(request):
    
    return render (request, 'appointment.html')

def ambulance(request):
    
    return render (request, 'ambulance.html')

def login(request):
    
    return render (request, 'Login And Resistration.html')

def medicine(request):
    
    return render (request, 'medicine.html')
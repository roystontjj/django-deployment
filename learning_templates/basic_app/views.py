from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def projects(request):
    return render(request,'basic_app/projects.html')

def getup(request):
    return render(request,'basic_app/getup.html')

def fyp(request):
    return render(request,'basic_app/fyp.html')

def ebike(request):
    return render(request,'basic_app/ebike.html')

def crampless(request):
    return render(request,'basic_app/crampless.html')

def uipath(request):
    return render(request,'basic_app/uipath.html')

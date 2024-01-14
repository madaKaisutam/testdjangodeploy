from django.shortcuts import render

# Create your views here.
def home(request):
    dom = 'Hello World'
    context = {
        'dom' : dom,
    }
    return render(request, 'home.html', context)
from django.shortcuts import render

# Create your views here.
def home(request):
    templates = 'home.html'
    context = locals()
    return render(request, templates, context)

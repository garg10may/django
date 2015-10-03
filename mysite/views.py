

from django.shortcuts import render




def home(request):

    context = {}
    template = "home.html"
    return render(request, template, context)



def base(request):

    context = {}
    template = 'base.html'
    return render(request, template, context)
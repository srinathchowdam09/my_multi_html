from django.shortcuts import render


def sri(request):

    d={'name':'SRINATH'}

    return render(request,'sri.html',d)

# Create your views here.

from django.shortcuts import render



def nath(request):

    d={'age':22}

    return render(request,'nath.html',d)

# Create your views here.

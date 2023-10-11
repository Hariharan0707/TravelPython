from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
def demo(request):
    obj=place.objects.all()

    return render(request, "index.html",{'result':obj})


#def about(request):
 #   return render(request, 'about.html')


#def contact(request):
#    return HttpResponse("hello contact")


#def addition(request):
#    x = int(request.GET.get('num1'))
 #   y = int(request.GET.get('num2'))
 #   res=x+y
 #   return render(request,'result.html',{'result':res})
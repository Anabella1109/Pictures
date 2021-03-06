from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Category

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def pic_of_day(request):
    
    date = dt.date.today()
    pics = Image.objects.all()
    return render(request, 'pictures/home.html', {"date": date,"pics":pics})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html',{"message":message})
def location(request,loc):
    images=Image.get_location_images(loc=loc)
    return render(request, 'pictures/location.html',{"pics": images})

def share(request,id):
    image=Image.share(id=id)
    return redirect(pic_of_day)


    


# Create your views here.

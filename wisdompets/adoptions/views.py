from django.shortcuts import render
from django.http import HttpResponse, Http404
# This class builds the response object that views are expected to return
# We can use this instead of the render function since the render function relies on templates to find

from .models import Pet

# # creating home function to return a http response
# # using <p> tag to test the home view
# def home(request):
#     return HttpResponse('<p>Home view</p>')
#
# def pet_detail(request, pet_id):
#     return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,

    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })

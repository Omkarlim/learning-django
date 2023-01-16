from django.shortcuts import render
from django.http import Http404
from .models import Pet


def home(request):
    all_pets = Pet.objects.all()
    return render(request, 'home.html', {'all_pets': all_pets})


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
    

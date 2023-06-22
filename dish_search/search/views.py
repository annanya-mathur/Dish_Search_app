from django.shortcuts import render
from .models import Dish

def search_dish(request):
    query = request.GET.get('q')
    if query:
        results = Dish.objects.filter(name__icontains=query)
    else:
        results = []
    return render(request, 'search/search_results.html', {'results': results})


# Create your views here.

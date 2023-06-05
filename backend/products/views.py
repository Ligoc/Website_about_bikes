from django.shortcuts import render, get_object_or_404

from .models import Bikes, Specification
from .forms import SearchForm

def index(request):
    return render(request, "index.html")

def bike_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)

    bikes = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "bike_model"
        if search_in == "bike_model":
            bikes = Bikes.objects.filter(bike_model__icontains=search)
        elif search_in == "brand":
            bikes = Bikes.objects.filter(brand__icontains=search)
        else:
            bikes = Bikes.objects.filter(bike_type__icontains=search)

    return render(request, "products/search-results.html", {"form": form, "search_text": search_text, "bikes": bikes })

def bike_list(request):
    bikes = Bikes.objects.all()
    bikes_dict = []
    for bike in bikes:
        bikes_dict.append({'bike': bike})
    
    context = {
        "bike_list" : bikes_dict
    }
    return render(request, "products/bike_list.html", context)

def bike_spec(request, pk):
    spec = get_object_or_404(Specification, pk=pk)
    bike = get_object_or_404(Bikes, pk=pk)

    context = {
        "bike_spec" : spec,
        "bike" : bike
    }
    return render(request, "products/bike_spec.html", context)

def questionnaire(request):
    return render(request, "products/form.html")

def comparison(request):
    return render(request, "products/bike_comp.html")
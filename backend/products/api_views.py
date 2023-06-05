from rest_framework import generics, filters
from .models import Bikes, Specification
from .serializers import BikeSerializer, SpecificationSerializer
from .forms import SearchForm

from  rest_framework.decorators import api_view
from rest_framework.response import Response

class AllBikes(generics.ListAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

class SingleBike(generics.RetrieveAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

class BikeSearchAPIView(generics.ListAPIView):
    queryset = Bikes.objects.all()
    serializer_class = BikeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand', 'bike_type', 'bike_model']




# @api_view()
# def all_bikes(request):
#     bikes = Bikes.objects.all()
#     bike_serializer = BikeSerializer(bikes, many=True)y
#     return Response(bike_serializer.data)

# @api_view()
# def all_spec(request):
#     spec = Specification.objects.all()
#     spec_serializer = SpecificationSerializer(spec, many=True)
#     return Response(spec_serializer.data)
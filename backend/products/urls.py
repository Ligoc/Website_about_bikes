from  django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.index),
    path('bikes/', views.bike_list, name='bike_list'),
    path('bikes/<int:pk>/', views.bike_spec, name='bike_spec'),
    # path('bike-search/', views.bike_search, name='bike_search'),
    path('form/', views.questionnaire, name='questionnaire'),
    path('comparison/', views.comparison, name='comparison'),
    path('api/all_bikes', api_views.AllBikes.as_view(), name='all_bikes'),
    path('api/all_bikes/<int:pk>/', api_views.SingleBike.as_view(), name='single_bike'),
    path('api/bike-search/', api_views.BikeSearchAPIView.as_view(), name='bike_search'),
]

 
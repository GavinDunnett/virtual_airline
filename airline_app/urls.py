from django.urls import path, include
from . import views
"""
URL configuration for airline_app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("aircraft/feedback/", views.AircraftFeedbackView, name='aircraft_feedback'),
    path('aircraft/overview', views.aircraft, name='aircraft'),
    path("aircraft/search/", views.AircraftFilterView, name='aircraft_search'),
    path('airline/analytics',views.airline_analytics,name='airline_analytics'),
    path('airline/overview', views.airline, name='airline'),
    path('airports/overview', views.airports, name='airports'),
    path('fleet/overview/', views.fleet, name='fleet'),
    path('flights/overview', views.flights, name='flights'),
    path('flights/results', views.flights, name='flights_results'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('registration/register/', views.register, name='register'),
    path('verification/', include('verify_email.urls')),
]

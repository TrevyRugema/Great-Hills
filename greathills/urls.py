from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('About', views.about, name="about"),
    path('Events', views.events, name="event"),
    path('Contact', views.contact, name="contact"),
    path('Events_Details/<int:pk>/', views.events_details, name='events_details'),
    path('future_Events/<int:pk>/', views.future_events, name='future_details'),
]
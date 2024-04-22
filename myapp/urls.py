from django.urls import path
#from .views import Home, Sawatdee, Research, Contact, TrackingPage
from .views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('research', Research, name= 'research'), #path จริงคือ www.localhost/research
    path('contact', Contact, name='contact'),
    path('tracking' ,TrackingPage, name= 'tracking'),
    path('sawatdee', Sawatdee),
]

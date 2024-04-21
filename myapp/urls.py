from django.urls import path
#from .views import Home, Sawatdee, Research, Contact, Tracking
from .views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('research', Research, name= 'research'), #path จริงคือ www.localhost/research
    path('contact', Contact, name='contact'),
    path('tracking' ,Tracking, name= 'tracking'),
    path('sawatdee', Sawatdee),
]

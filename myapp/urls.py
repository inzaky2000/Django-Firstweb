from django.urls import path
#from .views import Home, Sawatdee, Research, Contact, TrackingPage
from .views import *

urlpatterns = [
    path('', Home, name= 'home'),
    path('research', Research, name= 'research'), #path จริงคือ www.localhost/research
    path('contact', Contact, name='contact'),
    path('tracking' ,TrackingPage, name= 'tracking'), # TrackingPage เป็นชื่อ function ใน views.py
    path('sawatdee', Sawatdee),
    path('ask',Ask,name='ask'),
    path('questions', Questions, name='questions'),
    path('answer/<int:askid>', Answer, name='answer'),
    path('blogs',Posts, name='post'),
]

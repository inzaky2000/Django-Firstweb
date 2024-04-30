from django.shortcuts import render
from django.http import HttpResponse
#from .models import Tracking
#from .models import myresearch
from .models import *

# Create your views here.
# นี่คือเครื่องหมายคอมเม้นท์ ใน ไพทอน
# M T V (Model Template Views)

def Home(request):
    return render(request,'myapp/home.html')

def Research(request):
    #tracks = ['ลุงวิศวกร - TA349TH','พีระพล อ. - TA359TH','somchai - TA379TH','somwang - TA452Th']

    RS_research = myresearch.objects.all()
    contaxt = {'myrs_research':RS_research} #myrs_research อาจจะใช้คำว่า rs_research เพื่อให้จำง่าย
    return render(request,'myapp/research.html',contaxt)


def Contact(request):
    return render(request,'myapp/contact.html')

def Sawatdee(request):
    return HttpResponse('<h1>สวัสดีครับคุณนาย 555</h1>')

def TrackingPage(request):
    #tracks = ['ลุงวิศวกร - TA349TH','พีระพล อ. - TA359TH','somchai - TA379TH','somwang - TA452Th']

    tracks = Tracking.objects.all()
    contaxt = {'mytracks':tracks} #mythracks อาจจะใช้คำว่า tracks เพื่อให้จำง่าย
    return render(request,'myapp/tracking.html',contaxt)

def Ask(request):

    if request.method == 'POST':
        data = request.POST.copy()
        #print('DATA:', data)
        name = data.get('name') #name=name โดย name เป็นตัวที่อยู่ในไฟล์ html
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')
        print(name,email,title,detail)

        new = AskQA()
        new.name = name
        new.email = email
        new.title = title
        new.detail = detail
        new.save()

    return render(request, 'myapp/ask.html')


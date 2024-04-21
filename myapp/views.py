from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# นี่คือเครื่องหมายคอมเม้นท์ ใน ไพทอน
# M T V (Model Template Views)

def Home(request):
    return render(request,'myapp/home.html')

def Research(request):
    return render(request,'myapp/research.html')

def Contact(request):
    return render(request,'myapp/contact.html')

def Sawatdee(request):
    return HttpResponse('<h1>สวัสดีครับคุณนาย 555</h1>')

def Tracking(request):
    tracks = ['ลุงวิศวกร - TA349TH','พีระพล อ. - TA359TH','somchai - TA379TH','somwang - TA452Th']
    contaxt = {'mytracks':tracks} #mythracks อาจจะใช้คำว่า tracks เพื่อให้จำง่าย
    return render(request,'myapp/tracking.html',contaxt)

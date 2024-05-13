from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from .models import Tracking
#from .models import myresearch
from .models import *
from django.contrib.auth.decorators import login_required #บังคับล็อกอิน
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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


def Blogs(request):
    return render(request,'myapp/blogs.html')

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

@login_required
def Questions(request):
    #tracks = ['ลุงวิศวกร - TA349TH','พีระพล อ. - TA359TH','somchai - TA379TH','somwang - TA452Th']

    questions = AskQA.objects.all()
    contaxt = {'questions':questions} #question เป็น key เพื่อนำไปอ้างอิงในไฟล์ questions.html ตัวหลังเป็น value
    return render(request,'myapp/questions.html',contaxt)


def Answer(request,askid):
    # localshost:8000/answer/askid

    record = AskQA.objects.get(id=askid)

    if request.method == 'POST':
        data = request.POST.copy()
        #print('DATA:', data)
        # askid = data.get('askid') #บรรทัดนี้ ไม่จำเป็นต้องใส่ก็ได้
        detail_answer = data.get('detail_answer')
        record.detail_answer = detail_answer
        record.save()
    context = {'record':record}

    return render(request, 'myapp/answer.html',context)

def Posts(request):
    posts = Post.objects.all() #Post คือ model ที่ชื่อว่า Post ใน file model.py

    context = {"posts": posts}

    return render(request, 'myapp/blogs.html', context)

#ทำฟังค์ชั่นรายละเอียดบทความ
def PostDetail(request, slug):
    try:
        single_post = get_object_or_404(Post, slug=slug) #Post ในที่นี้ หมายถึง Model Post
        print("รายละเอียดบทความ", single_post)
    except Post.DoesNotExist:
        return render(request, 'myapp/home.html')
    context = {"single_post": single_post,}

    return render(request, 'myapp/blog-detail.html',context)



def Register(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        #print('DATA:', data)
        name = data.get('name') #name=name โดย name เป็นตัวที่อยู่ในไฟล์ html
        email = data.get('email')
        password = data.get('password')

        check = User.objects.filter(username = email)

        # print('CHECK:' ,check)

        if len(check) == 0:
            newuser = User()
            newuser.username = email
            newuser.first_name = name
            newuser.set_password(password)
            newuser.save()
            context['success'] = 'success'
        else:
            context['usertaken'] = 'usertaken'

    return render(request, 'myapp/register.html')


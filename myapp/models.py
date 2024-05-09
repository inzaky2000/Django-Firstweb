from typing import Any
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Tracking (models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100,null=True,blank=True) #null เป็นtrue แปลว่า ในดาต้าเบส สามารถเป็นค่าว่างได้้ 
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {} - ({})'.format(self.name, self.tel, self.tracking)
    
class myresearch (models.Model):
    rs_nameth = models.CharField(max_length=100) # ชื่องานวิจัยภาษาไทย
    rs_fname_th = models.CharField(max_length=500) # ชื่อนักงานวิจัยภาษาไทย
    rs_lname_th = models.CharField(max_length=500) # นามสกุลนักงานวิจัยภาษาไทย
    rs_year = models.SmallIntegerField() # ปีงบประมาณ
    rs_budget = models.SmallIntegerField() #งบประมาณที่ได้รับ(เงินทุน)
    rs_abs_th = models.TextField(null=True,blank=True, verbose_name='บทคัดย่อ') #Longtext - บทคัดย่อภาษาไทย
    rs_file = models.CharField(max_length= 250) # ชื่อไฟล์งานวิจัย

    def __str__(self):
        return '{} - {} - ({}) - {}'.format(self.rs_nameth, self.rs_fname_th, self.rs_year, self.rs_budget)

class AskQA(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True, verbose_name='ชื่อผู้ติดต่อ')
    email = models.CharField(max_length=100,null=True,blank=True, verbose_name='อีเมล์')
    title = models.CharField(max_length=100,null=True,blank=True, verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True, verbose_name='รายละเอียด')
    detail_answer = models.TextField(null=True,blank=True, verbose_name='คำตอบ')    

    def __str__(self):
        return '{} - ({}) - {}'.format(self.name, self.title,self.detail_answer)

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="author-image/",null=True, blank=True, default="default.png")

    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    decription = models.CharField(max_length=280, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to="post-image/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_upload = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
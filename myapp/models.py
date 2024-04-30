from django.db import models

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
    rs_abs_th = models.TextField #Longtext - บทคัดย่อภาษาไทย
    rs_file = models.CharField(max_length= 250) # ชื่อไฟล์งานวิจัย

    def __str__(self):
        return '{} - {} - ({}) - {}'.format(self.rs_nameth, self.rs_fname_th, self.rs_year, self.rs_budget)

class AskQA(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True, verbose_name='ชื่อผู้ติดต่อ')
    email = models.CharField(max_length=100,null=True,blank=True, verbose_name='อีเมล์')
    title = models.CharField(max_length=100,null=True,blank=True, verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True, verbose_name='รายละเอียด')

    def __str__(self):
        return '{} - ({}) '.format(self.name, self.title)

from django.db import models

# Create your models here.
class Tracking (models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100,null=True,blank=True) #null เป็นtrue แปลว่า ในดาต้าเบส สามารถเป็นค่าว่างได้้ 
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return '{} - {} - ({})'.format(self.name, self.tel, self.tracking)
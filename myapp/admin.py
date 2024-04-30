from django.contrib import admin

# Register your models here.

#from .models import Tracking
#from .models import myresearch
#from .models import AskQA

from .models import *

admin.site.register(Tracking)
admin.site.register(myresearch)
admin.site.register(AskQA)

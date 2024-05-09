from django.contrib import admin

# Register your models here.

#from .models import Tracking
#from .models import myresearch
#from .models import AskQA

from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Author)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "title", "images"]
    list_editable = ["title"]


admin.site.register(Post, PostAdmin)

admin.site.register(Tracking)
admin.site.register(myresearch)
admin.site.register(AskQA)

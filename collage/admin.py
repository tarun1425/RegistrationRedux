from django.contrib import admin
from collage.models import Notice
# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject','msg','crDate')
    search_fields = ('subject','msg')
    list_filter = ['crDate']   
    
admin.site.register(Notice, NoticeAdmin)


from django.contrib import admin

# Register your models here.
from .models import Passage, Subject

class PassageAdmin(admin.ModelAdmin):
    list_display = ["id","passage_name","passage","words"]
admin.site.register(Passage, PassageAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_name","passage_read","time_per_word"]
admin.site.register(Subject, SubjectAdmin)
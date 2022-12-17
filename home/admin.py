from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Option)

class AdminOption(admin.StackedInline):
    model= Option

class AdminQuestion(admin.ModelAdmin):
    inlines= [AdminOption]


admin.site.register(Question, AdminQuestion)
admin.site.register(Category)
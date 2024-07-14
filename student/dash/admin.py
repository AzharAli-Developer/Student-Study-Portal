from django.contrib import admin
from .models import  *
# Register your models here.
@admin.register(Notes)
class notesAdmin(admin.ModelAdmin):
    list_display = ['id','title','discription']

@admin.register(Homework)
class workAdmin(admin.ModelAdmin):
    list_display = ['id','subject','title','discription','due','status']

@admin.register(Todo)
class todoAdmin(admin.ModelAdmin):
    list_display = ['id','title','status']
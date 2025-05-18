from django.contrib import admin
from .models import student

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'deaprtment', 'grade', 'mark')
    fields = ('name', 'email', 'deaprtment', 'grade', 'mark', 'image')  # <-- Include 'image'

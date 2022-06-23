from django.contrib import admin
from todoApp.models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'completed']

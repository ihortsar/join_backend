from django.contrib import admin
from task_board.models import  Category, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'priority', 'due_date', 'category','subtasks']
    search_fields = ['title', 'description']
    list_filter = ['priority', 'due_date', 'category']
 
admin.site.register(Task, TaskAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name', 'id']
 
admin.site.register(Category, CategoryAdmin)


  

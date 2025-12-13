from django.contrib import admin
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_task_count', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description')
        }),
        ('Сроки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_task_count(self, obj):
        return obj.tasks.count()
    get_task_count.short_description = 'Tasks amount'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'deadline', 'category', 'executor')
    list_filter = ('is_done', 'category', 'created_at')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'category', 'executor')
        }),
        ('Статус и сроки', {
            'fields': ('is_done', 'deadline', 'created_at')
        }),
    )
    readonly_fields = ('created_at',)

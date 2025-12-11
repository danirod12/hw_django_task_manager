from .models import Task, Category

def statistics(request):
    """Контекстный процессор для статистики"""
    return {
        'stats_total_tasks': Task.objects.count(),
        'stats_total_categories': Category.objects.count(),
    }

from django.contrib import admin

from task.models import Task, Date


class TaskInline(admin.TabularInline):
    extra = 1
    model = Task


class DateAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display_links = ('date',)
    list_display = ('date', 'task_count')

    # noinspection PyMethodMayBeStatic
    def task_count(self, obj: Date):
        return obj.tasks.count()


class TaskAdmin(admin.ModelAdmin):
    list_display_links = ['content']
    list_display = ('content', 'severity', 'time', 'date')


admin.site.register(Date, DateAdmin)
admin.site.register(Task, TaskAdmin)

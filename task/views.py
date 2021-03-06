from datetime import datetime

from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, ListView, CreateView, UpdateView

from task.models import Task, Date


class TaskListView(ListView):
    model = Date
    paginate_by = 5
    context_object_name = 'dates'
    template_name = 'task/list.html'
    queryset = Date.objects.all().prefetch_related('tasks')


class DateTaskListView(ListView):
    model = Task
    paginate_by = 10
    context_object_name = 'tasks'
    template_name = 'task/date.html'

    def get_queryset(self):
        try:
            self.date = Date.objects.get(date=self.kwargs['date'])
        except Date.DoesNotExist:
            self.date = {'date': self.kwargs['date']}

        if isinstance(self.date, Date):
            return self.date.tasks.all()
        else:
            return Task.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = self.date
        return context


class TaskDeleteView(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        messages.success(request, 'task deleted successfully')
        return redirect('task:index')


class DeleteCompletedTaskView(View):
    @staticmethod
    def post(request: HttpRequest) -> HttpResponseRedirect:

        redirect_to = request.POST.get('next', 'task:index')

        tasks = Task.objects.filter(completed=True)
        delete_count, _ = tasks.delete()

        if delete_count == 0:
            messages.warning(request, 'no completed tasks found')
        else:
            messages.success(request, f'{delete_count} tasks deleted successfully')

        return redirect(redirect_to)


class ToggleTaskView(View):
    @staticmethod
    def get(request: HttpRequest, pk: int) -> HttpResponseRedirect:

        redirect_to = request.GET.get('next', 'task:index')

        task = get_object_or_404(Task, pk=pk)
        task.toggle_completed()

        completed = 'completed' if task.completed else 'pending'
        messages.info(request, f'task #{pk} marked {completed}.')

        return redirect(redirect_to)


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    fields = ['content', 'severity']
    template_name = 'task/create.html'
    success_url = reverse_lazy('task:index')
    success_message = 'task created successfully.'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'create task'
        data['severity_choices'] = Task.SEVERITY_CHOICES
        return data


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/create.html'
    success_message = 'task updated successfully'
    fields = ['content', 'severity', 'completed']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = f'update task #{self.object.id}'
        data['severity_choices'] = Task.SEVERITY_CHOICES
        return data

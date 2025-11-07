
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from accounts.mixins import AdminRequiredMixin
from .forms import TaskForm
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        user = self.request.user
        is_admin = user.is_superuser or user.groups.filter(name='ADMINISTRADOR').exists()
        return Task.objects.all() if is_admin else Task.objects.filter(usuario_asignado=user)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'tarea'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        is_admin = user.is_superuser or user.groups.filter(name='ADMINISTRADOR').exists()
        if obj.usuario_asignado != user and not is_admin:
            raise Http404('No encontrado')
        return obj

class TaskCreateView(AdminRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        messages.success(self.request, 'Tarea creada y asignada correctamente.')
        return super().form_valid(form)

class TaskUpdateView(AdminRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:list')

    def form_valid(self, form):
        messages.success(self.request, 'Tarea actualizada.')
        return super().form_valid(form)

class TaskDeleteView(AdminRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_detail.html'
    success_url = reverse_lazy('tasks:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Tarea eliminada.')
        return super().delete(request, *args, **kwargs)

@login_required
def change_status(request, pk):
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)

    tarea = get_object_or_404(Task, pk=pk)
    user = request.user
    is_admin = user.is_superuser or user.groups.filter(name='ADMINISTRADOR').exists()

    if tarea.usuario_asignado != user and not is_admin:
        return JsonResponse({'ok': False, 'error': 'Sin permisos'}, status=403)

    estado = request.POST.get('estado')
    if estado not in dict(Task.ESTADO_CHOICES).keys():
        return JsonResponse({'ok': False, 'error': 'Estado inválido'}, status=400)

    tarea.estado = estado
    tarea.save()
    return JsonResponse({'ok': True, 'estado': tarea.get_estado_display()})

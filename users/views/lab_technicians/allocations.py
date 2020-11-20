from .index import LabTechnicianDashboardView
from equipment.models import Allocation
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

User = get_user_model()


class AllocationCreateView(CreateView):
    model = Allocation
    fields = ('equipment','allocating_to',)
    template_name  = 'dashboard/equipment/allocations/add.html'

    user_type = None
    def form_valid(self, form):
        allocation = form.save(commit=False)
        self.user_type = allocation.allocating_to
        allocation.allocated_by = self.request.user
        allocation.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        if self.user_type == 'Student':
            return reverse_lazy('users:allocate_to_student',kwargs = {'pk': self.object.pk})
        return reverse_lazy('users:allocate_to_lecturer',kwargs = {'pk': self.object.pk})


class AllocateToStudentView(LabTechnicianDashboardView, ListView):
    model = User
    template_name = 'dashboard/equipment/allocations/allocate-student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Student')
        context["allocation"] = Allocation.objects.get(id=self.kwargs['pk'])
        return context


class AllocateToLecturerView(LabTechnicianDashboardView, ListView):
    model = User
    template_name = 'dashboard/equipment/allocations/allocate-lecturer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Lecturer')
        context["allocation"] = Allocation.objects.get(id=self.kwargs['pk'])
        return context





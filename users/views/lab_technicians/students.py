from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, ListView

from equipment.models import Allocation

from .index import LabTechnicianView

User = get_user_model()


class StudentListView(LabTechnicianView, ListView):
    model = User
    template_name = 'users/students/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Student')
        return context


class StudentDetailView(LabTechnicianView, DetailView):
    model = User
    template_name = 'users/students/details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        student = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipment_allocations"] = Allocation.objects.filter(
            allocated_to=student)
        return context





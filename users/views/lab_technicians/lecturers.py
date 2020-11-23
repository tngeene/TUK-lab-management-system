from schools.models import Department
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView

from equipment.models import Allocation

from .index import LabTechnicianView

User = get_user_model()


class LecturerListView(LabTechnicianView, ListView):
    model = User
    template_name = 'users/lecturers/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        lab = user.lab
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Lecturer', department__school=lab.school)
        return context


class LecturerDetailView(LabTechnicianView, DetailView):
    model = User
    template_name = 'users/lecturers/details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        lecturer = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipment_allocations"] = Allocation.objects.filter(
            allocated_to=lecturer)
        return context

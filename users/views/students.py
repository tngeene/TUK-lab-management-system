from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from equipment.models import Allocation


# check that the user has the role of a student
class StudentorLecturerView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.user_type == 'Student' or user.user_type == 'Lecturer':
            return True
        return False

class StudentorLecturerDashboardView(StudentorLecturerView, TemplateView):
    template_name = 'students/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user
        allocation = Allocation.objects.filter(allocated_to=student)
        context["recent_allocations"] = allocation.order_by('-pk')[:10]
        context["returned_allocation_count"] = allocation.filter(is_returned=True).count()
        context["unreturned_allocation_count"] = allocation.filter(is_returned=False).count()
        context["damaged_equipment_count"] = allocation.filter(equipment__is_damaged=True).count()
        return context

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import BadgeForm
from .models import Badge


class BadgeListView(ListView):
    template_name = "templates.html"
    queryset = Badge.templates.all().order_by("name")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Badge items"
        context["subtitle"] = "templates"
        context["add_action"] = reverse_lazy("badges:create")
        context["wysiwyg"] = []
        return context


class BadgeCreateView(SuccessMessageMixin, CreateView):
    template_name = "todo_update.html"
    form_class = BadgeForm
    success_url = reverse_lazy("badges:list")
    success_message = "badge item has been updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create badge item"
        context["subtitle"] = "templates"
        return context


class BadgeUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "todo_update.html"
    form_class = BadgeForm
    success_url = reverse_lazy("badges:list")
    queryset = Badge.templates.all()
    success_message = "Badge item has been updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update badge item"
        context["subtitle"] = "templates"
        # context["wysiwyg"] = context["badge"].content_json
        return context


class BadgeDeleteView(DeleteView):
    queryset = Badge.objects.all()
    success_url = reverse_lazy("badges:list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.info(request, "badge item has been removed")
        return response
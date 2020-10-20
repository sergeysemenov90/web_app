from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from articles.views import SuccessMessageMixin
from goals.forms import GoalsModelForm
from goals.models import Goals


class GoalsListView(ListView):
    model = Goals
    template_name = 'goals/goals_main.html'
    context_object_name = 'goals_list'


class CreateGoalsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('authentication_url')
    model = Goals
    template_name = 'goals/goals_main.html'
    form_class = GoalsModelForm
    success_url = reverse_lazy('goals_url')
    success_msg = 'Цель создана!'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['goals'] = Goals.objects.filter(owner=self.request.user).order_by('-id')
        return super().get_context_data(**kwargs)


class DeleteGoalView(DeleteView):
    model = Goals
    success_url = reverse_lazy('goals_url')
    template_name = 'goals/goals_main.html'


    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if self.request.user != self.object.owner:
    #         return self.handle_no_permission()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)
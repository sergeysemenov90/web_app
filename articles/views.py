from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticleModelForm, UserRegistrationForm, UserAuthForm


class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles_list'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class SuccessMessageMixin:
    @property
    def success_msg(self):
        return None

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(SuccessMessageMixin, self).form_valid(form)


class CreateArticleView(SuccessMessageMixin, CreateView):
    model = Articles
    template_name = 'articles/articles_changes.html'
    form_class = ArticleModelForm
    success_url = reverse_lazy('articles_changes')
    success_msg = 'Статья создана!'

    def get_context_data(self, **kwargs):
        kwargs['articles'] = Articles.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)


class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Articles
    template_name = 'articles/articles_changes.html'
    form_class = ArticleModelForm
    success_url = reverse_lazy('articles_changes')
    success_msg = 'Статья обновлена!'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'articles/articles_changes.html'
    success_url = reverse_lazy('articles_changes')


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'articles/registration.html'
    success_url = reverse_lazy('articles_changes')
    success_msg = 'Пользователь зарегистрирован!'
    
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username = username, password = password)
        login(self.request, auth_user)
        return form_valid


class UserAuthView(LoginView):
    model = User
    form_class = UserAuthForm
    template_name = 'articles/authentication.html'
    success_url = reverse_lazy('articles_changes')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('articles_changes')

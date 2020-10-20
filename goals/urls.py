from django.urls import path
from goals import views

urlpatterns = [
    path('', views.CreateGoalsView.as_view(), name='goals_url'),
    path('delete/<pk>/', views.DeleteGoalView.as_view(), name='delete_goal_url'),

    ]
"""
URL configuration for join_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_board.views import AllUsers, CategoryView, LoginView, TaskView, UserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", TaskView.as_view()),
    path("login/", LoginView.as_view()),
    path("tasks/<int:pk>/", TaskView.as_view()),
    path("signup/", UserView.as_view()),
    path("all_users/", AllUsers.as_view()),
    path("categories/", CategoryView.as_view()),
]

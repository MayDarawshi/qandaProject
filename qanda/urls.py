"""qanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ast import main
from django.contrib import admin 
from django.urls import path,include
from main.views import *

urlpatterns = [
    path('signin/admin/', admin.site.urls),
    path('',include("main.urls")),
    path('about_us/',include("main.urls")),
    path('adminPage/',include("main.urls")),
    path('signin/',include("main.urls")),
    path('signup_teacher',include("main.urls")),
    path('signup_user/',include("main.urls")),
    path('login/',include("main.urls")),
    path('pull_teachers_info/',include("main.urls")),
    path('teachers_names/',include("main.urls")),
    path('all_questions/',include("main.urls")),
    path('subjects/',include("main.urls")),
    # path('teacher_profile/1',include("main.urls")),
    path('',include("django.contrib.auth.urls")),
    path('subjects/view_question/',include("main.urls")),
    path('add_question/',include("main.urls")),
    path('take_test/',include("main.urls")),
    path('question_details/<int:id>/',include("main.urls")),
    path('question/',include("main.urls")),
    path('take_testTemplate/',include("main.urls")),
    path('signin/login_admin/',include("main.urls")),
    path('signin/login_user/',include("main.urls")),
    path('notfound/',include("main.urls")),
    path('signin/teacher_login/',include("main.urls")),
    # path('take_test/exams_answers/',include("main.urls")),






    # path('teacher_profile/',include("main.urls")),





]

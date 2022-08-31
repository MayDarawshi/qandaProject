from tokenize import String
from urllib.parse import urlencode
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home,name="home"),
    path("about_us/",views.about_us,name="about_us"),
    path("adminPage/",views.adminPage,name="adminPage"),
    path('teacher_profile/<int:id>',views.teacher_profile,name="teacher_profile"),
    path("signin/",views.signin,name="signin"),
    path("signup_user/",views.signup_user,name="signup_user"),
    path("signup_user/",views.signup_user,name="signup_user"),
    # path("login/teacher_profile",views.login,name="login"),  
    path("pull_teachers_info/",views.pull_teachers_info,name="pull_teachers_info"),  
    path("teachers_names/",views.teachers_names,name="teachers_names"),  
    path("all_questions/",views.all_questions,name="all_questions"),  
    path("subjects/",views.subjects,name="subjects"),  
    path("take_test/",views.take_test,name="take_test"),  
    # path("question/<int:id>",views.question_details,name="question"),  
    path("add_question/",views.add_question,name="add_question"),  
    path("index/",views.index,name="index"), 
    path("question_details/<int:id>/",views.question_details,name="question_details"),
    path("question/<int:id>/",views.question,name="question"),
    # path("r^login/$",views.login_user,name="login_user"),
    path("signin/login_user/",views.login_user,name="login_user"),
    path("signin/login_user/user_profile/",views.login_user,name="login_user"),
    # path("exams_answers/",views.exams_answers,name="exams_answers"),

    path("login/",views.login_user,name="login_user"),
    path("notfound/",views.notfound,name="notfound"),
    path("take_testTemplate",views.take_test,name="take_testTemplate"),
    path("signin/login_admin/",views.login_admin,name="login_admin"),
    path("signin/teacher_login/",views.teacher_login,name="teacher_login"),
    path("signin/teacher_login/teacher_profile",views.teacher_login,name="teacher_login"),



    # path('question/question_details/<int:id>/',views.add_answer,name="add_answer"),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.db.models import Sum,Count
import random


def home(response):
    return render(response, 'home.html', {})


def about_us(response):
    return render(response, 'about_us.html', {})


def adminPage(response):
    return render(response, 'admin.html', {})



def signin(response):
    return render(response, 'signin.html', {})

def notfound(request):
    return render(request,'notfound.html',{})


def login_user(request):
    
    if request.method == "POST":
        id = request.POST.get('user_id')
        password = request.POST.get('password')       
        user = users.objects.filter(user_id=id).filter(password=password)
        print(user)
        answers = Answer.objects.filter(user_id=id)
        context = {}
        context ['user'] = user
        context ['answers'] = answers
        if not user :
            return render(request,'notfound.html',{})   
        else:
            return render(request,'user_profile.html',context)

    else:
        return render(request,'login.html',{})


def signup_user(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get('user_name')
            email= request.POST.get('email')
            password=request.POST.get('password')
            school=request.POST.get('school')
            grade=request.POST.get('grade')
            phone=request.POST.get('phone')
            user_id=request.POST.get('user_id')

            t = users(user_id=user_id,user_name=user_name,email=email,password=password,grade=grade,school=school,phone=phone)
            t.save()
            return redirect('/')
            
        except Exception as e:
            return render(request, 'signup_user.html', { 'error': 'Something is wrong with the form!' })
    return render(request, 'signup_user.html', {})


def pull_teachers_info(response):
    all_teachers = teachers.objects.all
    return render(response, 'pull_teachers_info.html', {"all": all_teachers})


def teachers_names(response):
    all_teachers = teachers.objects.all()
    return render(response, 'teachers_names.html', {"all": all_teachers})

# change the template with the new one
def logout(request):
    return render(request, 'teachers_names.html', {})


def all_questions(response):
    all_questions = questions.objects.all
    return render(response, 'all_questions.html', {"all": all_questions})


def subjects(response):    
    all_questions = questions.objects.all
    return render(response, 'subjects.html', {"all": all_questions})


def index(request):
    context = {}
    context['questions'] = questions.objects.all()
    return render(request, 'index.html', context)


def user_profile(request):
    # all_answers_for_user = Answer.objects.filter(user_id=user_id)
    # context = {}
    # context['all_answers_for_user'] = all_answers_for_user
    
    return render(request, 'user_profile.html', {})

            

def add_question(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            question = request.POST.get('question')
            difficulty= request.POST.get('difficulty')
            grade=request.POST.get('grade')
            type=request.POST.get('type')
            author_id=request.POST.get('author_id')
            q = questions(question=question,title=title ,difficulty=difficulty,grade=grade,type=type,author_id=author_id)

            q.save()
            # return redirect(view_question, q.qid, q.slug)
        except Exception as e:
            return render(request, 'add_question.html', { 'error': 'Something is wrong with the form!' })
    return render(request, 'add_question.html', {})


def teacher_profile(request):
    return render(request, 'teacher_profile.html', {})

def teacher_login(request):
    if request.method == "POST":
        id = request.POST.get('user_id')
        password = request.POST.get('password')       
        teacher = teachers.objects.filter(author_id=id).filter(password=password)
        question = questions.objects.filter(author_id=id)
        context = {}
        context ['teacher'] = teacher
        context ['questions'] = question
        if not teacher: 
            return render(request,'notfound.html',{})   
        else:
            return render(request,'teacher_profile.html',context)
    else:
        return render(request,'login.html',{})




# def view_question(request, id):
#     context = {}
#     question = questions.objects.get(id=id)

#     # assuming obj is a model instance
#     question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']
#     question_json['id'] = question.id
#     question_json['question'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
#     question_json['difficulty'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
#     question_json['type'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
#     question_json['grade'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
#     context['question'] = question_json
#     context['answers'] = []
#     answers = Answer.objects.filter(id=id)
#     for answer in answers:
#         answer.answer_text = bleach.clean(markdown2.markdown(answer.answer_text), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
#         context['answers'].append(answer)
#     return render(request, 'view_question.html', context)


def take_test(request):
    if request.method == 'POST':
        type1 = request.POST.get('type1')
        difficulty1 = request.POST.get('difficulty1')
        type2 = request.POST.get('type2')
        difficulty2 = request.POST.get('difficulty2')
        type3 = request.POST.get('type3')
        difficulty3 = request.POST.get('difficulty3')
        question1 = questions.objects.filter(type=type1).filter(diffi=difficulty1)
        question2 = questions.objects.filter(type=type2).filter(diffi=difficulty2)
        question3 = questions.objects.filter(type=type3).filter(diffi=difficulty3)
        context = {}
        print(question1)
        print(question2)
        print(question3)

        if not question1 or not question2 or not question3 :
            context['question1'] = questions.objects.filter(type=type1)
            context['question2'] = questions.objects.filter(type=type2)
            context['question3'] = questions.objects.filter(type=type3)
        else:        
            context['question1'] = question1
            context['question2'] = question2
            context['question3'] = question3
                    
        return render(request, 'take_testTemplate.html', context)
            
    
    else:
        return render(request, 'take_test.html', {})

 
def teacher_profile(request,id):
    all_questions_for_teacher = questions.objects.filter(author_id=id)
    return render(request, 'teacher_profile.html', {"all": all_questions_for_teacher})

    

# def login_user(response):
#     return render(response, 'login.html', {})

def question(request,id):
    questionsall = questions.objects.filter(id=id)
    context = {'questionsall':questions}
    return render(request, 'subjects/question.html', context)    

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username =="mayd" and password=="root" :
            return render(request,'admin.html', {} )

    else:
        return render(request,'login_admin.html', {} )



@transaction.atomic
def question_details(request,id):
    question=questions.objects.filter(id=id)
    if request.method == 'POST':
        question=questions.objects.filter(id=id)
        user_id = request.POST.get('user_id')
        answer_text = request.POST.get('answer_text')
        q_image = request.FILES['q_image']
        diff = request.POST.get('difficulty') 
        a = Answer(q_id = id  , answer_text=answer_text , q_image = q_image , user_id=user_id)
        d = difficulty_tbl(id=user_id,qid = id,diff=diff)
        with transaction.atomic():
            a.save()
            d.save() 
    else:
        question=questions.objects.filter(id=id)
        if(questions.objects.filter(id=id)):
            sum_diff = difficulty_tbl.objects.filter(qid=id).aggregate(Sum('diff'))
            count_diff = difficulty_tbl.objects.filter(qid=id).aggregate(Count('diff'))
            if (sum_diff['diff__sum'] == None or count_diff['diff__count'] == None) :
                avg = question.values('difficulty')
                avg = float(avg[0]['difficulty'])
                print(avg)

            else:
                avg = ((sum_diff['diff__sum'])/(count_diff['diff__count']))
            avg = ("{:.2f}".format(avg))
            avg = float (avg)/10 * 100
            avg = str (avg) +"%"
            context = {}
            context['question'] = questions.objects.filter(id=id).first
            context['avg_diff'] = avg
            return render(request,"question.html",context)     
    ques = questions.objects.all
    return render(request, 'subjects.html', {"all":ques}) 
        

   



    
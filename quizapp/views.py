# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Quiz, Result
from django.http import HttpResponse
# from .forms import QuizForm
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate , login , logout



def qpage(request):
    if len(request.get_full_path().split('/'))>2:
        userpk = int(request.get_full_path().split('/')[-1])
        userData = User.objects.get(pk=userpk)
        if request.method=="GET":
            questions=Quiz.objects.all()
            return render(request, 'question.html', {'questions': questions,'userData':userData})
        if 'POST' == request.method:
            questions = Quiz.objects.all()
            db_ans = list(Quiz.objects.all().values_list('answer', flat=True))
            score_count=0
            wrong_count=0
            unattempt=0

            for i in range(len(questions)):
                try:
                    if (request.POST[('q'+str(i+1))])== db_ans[i]:
                        score_count+=1
                    else:
                        wrong_count+=1
                except:
                    unattempt+=1
            print(unattempt)
            user_id=User.objects.get(pk=userpk)
            score_data={'score_count':score_count,'wrong_count':wrong_count,'user':user_id, 'unattempt':unattempt}
            score_results=Result(**score_data)
            score_results.save()
            return render(request, 'display.html', {'score':score_count, 'wrong':wrong_count,'userData':userData, 'unattempt':unattempt})



def index(request):
    return render(request, 'index.html')

def questions(request):
    return render(request, 'quiz.html')

def studselect(request):
    return render(request, 'studselect.html')

def register(request):
    if request.method=='POST':
        # fname=request.POST.get('fname')
        # lname=request.POST.get('lname')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        password=request.POST.get('password')


        data = {'email':email,'username':uname,'password':password} #'first_name':fname,'last_name':lname,
        userObj=User(**data)
        userObj.save()
        return redirect('/')
        # return render(request, 'studselect.html')
    else:
        return render(request, 'register.html')
    #     form=UserCreationForm()
    #     return render(request,'login.html', {'form':form})

def login(request):
    if request.method=='POST':
        # fname=request.POST.get('fname')
        # lname=request.POST.get('lname')
        # email=request.POST.get('email')
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=uname)
            # user = authenticate(username = uname , password = password)
            # print 'userrrrrrrrrrrrrrr',user
            if uname==user.username and password==user.password:
                return redirect('/questions/'+str(user.pk))
                # return redirect('/userselect/')
            else:
                print 'incorrect password'
                return HttpResponse("""<html><body bgcolor="#E8E8E8">
                <h1>Oops! Incorrect username or password</h1>
                <a href=""><h2> Click here to login</h2></a>
                </body></html>""")
        except :
            print 'exceptionnnnnnnnnn'
            return HttpResponse(request,'not allowed')


        # data = {'email':email,'username':uname,'password':password} #'first_name':fname,'last_name':lname,
        # userObj=User(**data)
        # userObj.save()
        # return redirect('/')
    else:
        return render(request, 'login.html')


def userselect(request):
    return render(request, 'userselect.html')

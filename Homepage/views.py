# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
# Create your views here.
from UserDatabase.models import student_details, guide_details, spons_details, guide_inbox, student_inbox, notify_me, \
    scholorship


def HomePage(request):
    logout(request)
    # if request.user.is_authenticated():
    #     if request.user.first_name== 'student':
    #         dog = student_details.objects.get(email=request.user.email)
    #         g = guide_details.objects.all()
    #         s = spons_details.objects.all()
    #         return render(request, 'ryg_1_1/student_profile.html',{'f': dog,'g':g,'s':s})
    # elif  request.user.first_name== 'guide':
    #     dog = guide_details.objects.get(email=request.user.email)
    #     students = student_details.objects.all()
    #     return render(request, 'ryg_1_1/guide_homepage.html', {'f': dog, 'students': students})
    # elif request.user.first_name== 'sponsor':
    #     dog = spons_details.objects.get(email=request.user.email)
    #     students = student_details.objects.all()
    #     return render(request, 'ryg_1_1/sponsor_homepage.html', {'f': dog, 'students': students})
    return render(request, 'Homepage.html')

def check_user_in_db(request):
    #if request.user.is_authenticated():
        #if request.user.first_name == 'student':
    if request.method == 'GET':
        return render(request, 'Homepage.html')
    try:
        #logout(request)
        user = User.objects.get(email__iexact=request.POST["uname"])
        if user.first_name == 'student':
            dog = student_details.objects.get(email=request.POST["uname"])
            if dog.password == request.POST["psw"]:
                login(request, user)
                request.session.set_expiry(800)
                g=guide_details.objects.all()
                s=spons_details.objects.all()
                data1=notify_me.objects.all()
                data2=scholorship.objects.all()
                k1=notify_me.objects.filter(goaltype=dog.goal).count()
                k2 = scholorship.objects.filter(goaltype=dog.goal).count()
                smessages=student_inbox.objects.get(student_mail=request.POST["uname"])
                return render(request, 'studentpages/student_profile.html', {'f': dog,'g':g,'s':s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
            return render(request, 'alert/invalid_login.html')
        elif user.first_name == 'guide':
            if user.is_active:
                print('active-->',user.is_active)
                dog = guide_details.objects.get(email=request.POST["uname"])
                if dog.password == request.POST["psw"]:
                    login(request, user)
                    request.session.set_expiry(800)
                    students=student_details.objects.all()
                    gmessages = guide_inbox.objects.get(guide_mail=request.POST["uname"])
                    return render(request, 'guidepages/guide_homepage.html', {'f': dog,'students':students,'gmessages':gmessages})
                return render(request, 'alert/invalid_login.html')
            else:
                return render(request, 'alert/is_activated.html')
        elif user.first_name == 'sponsor':
            dog = spons_details.objects.get(email=request.POST["uname"])
            if dog.password == request.POST["psw"]:
                login(request, user)
                request.session.set_expiry(800)
                students = student_details.objects.all()
                return render(request, 'sponsorpages/sponsor_homepage.html', {'f': dog,'students': students})
            return render(request, 'alert/invalid_login.html')
    except ObjectDoesNotExist:
        return render(request, 'alert/invalid_login.html')


def editSchool(request,id):
    if request.user.is_authenticated():
        print(request.POST["SchoolName"])
        print(request.POST["Duration"])
        print(request.POST["edulist"])
        print(request.POST["SchoolAchievements"])
        t = student_details.objects.get(id=id)
        t.school = request.POST["SchoolName"]
        t.school_duration = request.POST["Duration"]
        t.school_board = request.POST["edulist"]
        t.school_achievements = request.POST["SchoolAchievements"]
        t.save()
        g = guide_details.objects.all()
        s = spons_details.objects.all()
        data1 = notify_me.objects.all()
        data2 = scholorship.objects.all()
        k1 = notify_me.objects.filter(goaltype=t.goal).count()
        k2 = scholorship.objects.filter(goaltype=t.goal).count()
        smessages = student_inbox.objects.get(student_mail=t.email)
        return render(request,'studentpages/student_profile.html',{'f':t,'g':g,'s':s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
    return render(request,'alert/session_timeout.html')

def editCollage1(request,id):
    if request.user.is_authenticated():
        print(request.POST["Collage1Name"])
        print(request.POST["Duration"])
        print(request.POST["edulist"])
        print(request.POST["CollageAchievements"])
        t = student_details.objects.get(id=id)
        t.collage1 = request.POST["Collage1Name"]
        t.collage_duration1 = request.POST["Duration"]
        t.collage_course1 = request.POST["edulist"]
        t.collage_achievements1 = request.POST["CollageAchievements"]
        t.save()
        g = guide_details.objects.all()
        s = spons_details.objects.all()
        data1 = notify_me.objects.all()
        data2 = scholorship.objects.all()
        k1 = notify_me.objects.filter(goaltype=t.goal).count()
        k2 = scholorship.objects.filter(goaltype=t.goal).count()
        smessages = student_inbox.objects.get(student_mail=t.email)
        return render(request, 'studentpages/student_profile.html', {'f': t, 'g': g, 's': s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
    return render(request, 'alert/session_timeout.html')
def editCollage2(request,id):
    if request.user.is_authenticated():
        print(request.POST["Collage2Name"])
        print(request.POST["Duration"])
        print(request.POST["edulist"])
        print(request.POST["CollageAchievements"])
        t = student_details.objects.get(id=id)
        t.collage1 = request.POST["Collage2Name"]
        t.collage_duration1 = request.POST["Duration"]
        t.collage_course1 = request.POST["edulist"]
        t.collage_achievements1 = request.POST["CollageAchievements"]
        t.save()
        g = guide_details.objects.all()
        s = spons_details.objects.all()
        data1 = notify_me.objects.all()
        data2 = scholorship.objects.all()
        k1 = notify_me.objects.filter(goaltype=t.goal).count()
        k2 = scholorship.objects.filter(goaltype=t.goal).count()
        smessages = student_inbox.objects.get(student_mail=t.email)
        return render(request, 'studentpages/student_profile.html', {'f': t, 'g': g, 's': s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
def guideProfileView(request,id,id2):
    if request.user.is_authenticated():
        print(request.user.first_name)
        k=student_details.objects.get(id=id2)
        v=guide_details.objects.get(id=id)
        return render(request,'guidepages/guideprofileview.html',{'v':v,'k':k})
    return render(request, 'alert/session_timeout.html')
def sponsorProfileView(request,id,id2):
    print(request.user.first_name)
    if request.user.is_authenticated():
        k = student_details.objects.get(id=id2)
        v=spons_details.objects.get(id=id)
        return render(request,'sponsorpages/sponsorprofileview.html',{'v':v,'k':k})
    return render(request, 'alert/session_timeout.html')




def StudentProfileView(request,id,id2):
    if request.user.is_authenticated():
        v=student_details.objects.get(id=id)
        f=guide_details.objects.get(id=id2)
        return render(request,'studentpages/student_profile_view.html',{'v':v,'f':f})
    return render(request, 'alert/session_timeout.html')

def StudentProfileView2(request,id,id2):
    if request.user.is_authenticated():
        v=student_details.objects.get(id=id)
        f=spons_details.objects.get(id=id2)
        return render(request,'studentpages/student_profile_view2.html',{'v':v,'f':f})
    return render(request, 'alert/session_timeout.html')

def BackToGuide(request,id):
    if request.user.is_authenticated():
        f=guide_details.objects.get(id=id)
        students = student_details.objects.all()
        gmessages = guide_inbox.objects.get(guide_mail=f.email)
        return render(request,'guidepages/guide_homepage.html', {'f': f,'students':students,'gmessages':gmessages})
    return render(request, 'alert/session_timeout.html')
def BackToSponsor(request,id):
    if request.user.is_authenticated():
        f=spons_details.objects.get(id=id)
        students = student_details.objects.all()
        return render(request,'sponsorpages/sponsor_homepage.html', {'f': f,'students':students})
    return render(request, 'alert/session_timeout.html')

def BackToStudent(request,id):
    if request.user.is_authenticated():
        f=student_details.objects.get(id=id)
        g = guide_details.objects.all()
        s = spons_details.objects.all()
        data1 = notify_me.objects.all()
        data2 = scholorship.objects.all()
        k1 = notify_me.objects.filter(goaltype=f.goal).count()
        k2 = scholorship.objects.filter(goaltype=f.goal).count()
        smessages = student_inbox.objects.get(student_mail=f.email)
        return render(request, 'studentpages/student_profile.html', {'f': f, 'g': g, 's': s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
    return render(request, 'alert/session_timeout.html')

def messageSendToStudentFromGuide(request,id,data):
    if request.user.is_authenticated():
        print(request.POST["message"])
        a=student_inbox.objects.get(student_mail=data)
        b=guide_details.objects.get(id=id)
        a.sender_mail_1=b.email
        a.sender_message_1=request.POST["message"]
        a.save()
        students=student_details.objects.all()
        gmessages=guide_inbox.objects.all()
        return render(request, 'guidepages/guide_homepage.html', {'f': b, 'students': students, 'gmessages': gmessages})
    return render(request, 'alert/session_timeout.html')


def messageSendToGuideFromStudent(request,id,data):
    if request.user.is_authenticated():
        print(request.POST["message"])
        a=guide_inbox.objects.get(guide_mail=data)
        b=student_details.objects.get(id=id)
        a.sender_mail_1=b.email
        a.sender_message_1=request.POST["message"]
        a.save()
        g=guide_details.objects.all()
        s=spons_details.objects.all()
        data1 = notify_me.objects.all()
        data2 = scholorship.objects.all()
        k1 = notify_me.objects.filter(goaltype=b.goal).count()
        k2 = scholorship.objects.filter(goaltype=b.goal).count()
        smessages = student_inbox.objects.get(student_mail=b.email)
        return render(request, 'studentpages/student_profile.html', {'f': b, 'g': g, 's': s,'smessages':smessages,'data1':data1,'data2':data2,'k1':k1,'k2':k2})
    return render(request, 'alert/session_timeout.html')

def forgotpass(request):
    try:
        if(User.objects.get(email__iexact=request.POST["email"])):
            j=User.objects.get(email__iexact=request.POST["email"])
            if j.first_name == 'student':
                k=student_details.objects.get(email=request.POST["email"])
                email = EmailMessage('Reach your goal administration ' + k.password, to=[request.POST["email"]])
                email.send()
            elif j.first_name == 'guide':
                k=guide_details.objects.get(email=request.POST["email"])
                email = EmailMessage('Reach your goal administration ' + k.password, to=[request.POST["email"]])
                email.send()
            elif j.first_name == 'sponsor':
                k=spons_details.objects.get(email=request.POST["email"])
                email = EmailMessage('Reach your goal administration ' + k.password, to=[request.POST["email"]])
                email.send()
        return render(request, 'alert/password_sent.html')
    except:
        return render(request, 'alert/email_doesnot_exists.html')
def logout_user(request):
    logout(request)
    return render(request, 'Homepage.html')
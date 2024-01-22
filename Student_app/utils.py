
from main.models import *
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import *
from Student_app.models import Student as app_stu
from django.contrib import messages


import random,string

def user_is_exits(enroll):
    try:
        use = User.objects.get(username=enroll)
        return use
    except User.DoesNotExist:
        return False

def valid_username(enroll):
    if valid_enroll(enroll):
        if user_is_exits(enroll):
            return False
        else:
            return True
    else:
        return False


def valid_enroll(enroll):
    student = app_stu.objects.filter(stu_enroll=enroll)
    if len(student) > 0:
        return True
    else:
        return False

def login_not_required_restric(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return render(request, 'login.html', {
                'link_title': 'signout',
                'link_message': 'you are arlady login with a account please logout first to login again or go to home page',
                'link1_url': reverse('student signout'),
                'link1_name': 'signout',
                'link2_url': reverse('student home'),
                'link2_name': 'home'
            })
        else:
            return func(request)
    return wrapper


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

branchlist = {
	'00':None,
	'01':'AERONAUTICAL ENGINEERING'
	,'02':'AUTOMOBILE ENGINEERING'
	,'03':'BIO-MEDICAL ENGINEERING'
	,'04':'BIO-TECHNOLOGY'
	,'05':'CHEMICAL ENGINEERING'
	,'06':'CIVIL ENGINEERING'
	,'07':'COMPUTER ENGINEERING'
	,'08':'ELECTRICAL & ELECTRONICS ENGINEERING'
	,'09':'ELECTRICAL ENGINEERING'
	,'10':'ELECTRONICS ENGINEERING'
	,'11':'ELECTRONICS & COMMUNICATION ENGINEERING'
	,'12':'ELECTRONICS & TELECOMMUNICATION ENGINEERING'
	,'13':'ENVIRONMENTAL ENGINEERING'
	,'14':'FOOD PROCESSING TECHNOLOGY'
	,'15':'INDUSTRIAL ENGINEERING'
	,'16':'INFORMATION TECHNOLOGY'
	,'17':'INSTRUMENTATION & CONTROL ENGINEERING'
	,'18':'MARINE ENGINEERING'
	,'19':'MECHANICAL ENGINEERING'
	,'20':'MECHATRONICS ENGINEERING'
	,'21':'METALLURGY ENGINEERING'
	,'22':'MINING ENGINEERING'
	,'23':'PLASTIC TECHNOLOGY'
	,'24':'POWER ELECTRONICS'
	,'25':'PRODUCTION ENGINEERING'
	,'26':'RUBBER TECHNOLOGY'
	,'28':'TEXTILE PROCESSING'
	,'29':'TEXTILE TECHNOLOGY'
	,'31':'COMPUTER SCIENCE & ENGINEERING'
	,'32':'INFORMATION & COMMUNICATION TECHNOLOGY'
	,'34':'MANUFACTURING ENGINEERING'
	,'35':'ENVIRONMENTAL SCIENCE & TECHNOLOGY'
	,'36':'CHEMICAL TECHNOLOGY'
	,'37':'ENVIRONMENTAL SCIENCE AND ENGINEERING'
	,'39':'NANO TECHNOLOGY'
	,'40':'CIVIL & INFRASTRUCTURE ENGINEERING'
	,'41':'ROBOTICS AND AUTOMATION'
	,'42':'COMPUTER SCIENCE & ENGINEERING (ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING)'
	,'43':'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE'
	,'44':'CHEMICAL ENGINEERING (GREEN TECHNOLOGY & SUSTAINABILITY ENGINEERING)'
    ,'45':'COMPUTER SCIENCE & ENGINEERING (INTERNET OF THINGS AND CYBER SECURITY INCLUDING BLOCK CHAIN TECHNOLOGY)'}
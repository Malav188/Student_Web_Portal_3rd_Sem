from django.contrib import messages
from django.shortcuts import render
import requests ,csv
from django.core.files.base import ContentFile
from .models import *
from faculty.models import Faculty_Records
from django.http import HttpResponse,Http404
from django.conf import settings
from django.conf.urls.static import static
from Student_app.utils import branchlist
from main.models import Sub_Syllabus,GtuExam

def collect_exam():
    subjects = Sub_Syllabus.objects.all()
    for subject in subjects:
        term = 'S2024'
        if int(subject.sub_sem)%2 == 1:
            term = 'W2023'

        urqql = f"https://gtu.ac.in/uploads/{term}/DI/{4341601}.pdf"
        url = "https://gtu.ac.in/uploads/W2023/DI/4335803.pdf"
        response = requests.get(url)
        if response.status_code == 200:
            ob = GtuExam()
            ob.subject=subject
            ob.sub_code=subject.sub_code
            ob.sub_branch_code=subject.sub_branch_code
            ob.sub_sem=subject.sub_sem
            ob.sub_academic_term=subject.sub_academic_term
            ob.sub_pdf.save(f'{term}-{subject.sub_code}.pdf', ContentFile(response.content),save=False)
            ob.save()
        break

def h():
    for row in csv.reader(open(r'C:\Users\Mohit\Downloads\reference-ds-practicals\mydata.csv', "r")):
        try:
            response = requests.get(row[0])
            if response.status_code == 200:
                ob = Sub_Syllabus()
                ob.sub_name = row[4]
                ob.sub_code = row[1]
                ob.Assigned_Sub_Faculty = Faculty_Records.objects.get(email='nonedit@gmail.com')
                ob.session = Sub_Syllabus.Session.SUMMER
                ob.sub_branch_code = row[2]
                ob.sub_lacture_hours = int(row[7])
                ob.sub_tutorial_hours = int(row[8])
                ob.sub_practical_hours = int(row[9])
                ob.sub_category = row[5]
                ob.sub_theory_mid1 = 0 if int(row[12]) == 0 else (int(row[12]) * 2) // 3
                ob.sub_theory_mid2 = 0 if int(row[12]) == 0 else (int(row[12]) * 2) // 3
                ob.sub_theory_micro = 0 if int(row[12]) == 0 else (int(row[12])) // 3
                ob.sub_theory_PA = int(row[12])
                ob.sub_theory_ESE = int(row[11])
                ob.sub_prctical_PA = int(row[13])
                ob.sub_prctical_ESE = int(row[14])
                ob.sub_sem = int(row[6])
                ob.sub_credit = int(row[10])
                ob.sub_academic_term = '23-24'
                ob.sub_pdf.save(f'syllabus-{row[2]}-{row[1]}.pdf', ContentFile(response.content), save=False)
                ob.save()
        except Exception as e:
            pass
    return None
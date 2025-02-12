from django.contrib import messages
from django.shortcuts import render
import requests ,csv
from django.core.files.base import ContentFile
from .models import *
from faculty.models import Faculty_Records
from django.http import HttpResponse,Http404
from django.conf import settings
from django.conf.urls.static import static
from Student_app.models import *
from Student_app.utils import branchlist
from Student_app.utils import branchlist
# Create your views here.
def homehii(request):
    # for key,value in branchlist.items():
    #     if int(key)  > 27:
    #         queryset = Sub_Syllabus.objects.filter(sub_branch_code=key)
    #         for q in queryset:
    #             response = requests.get(f'https://s3-ap-southeast-1.amazonaws.com/gtusitecirculars/Syallbus/{q.sub_code}.pdf')
    #             if response.status_code == 200:
    #                 q.sub_pdf.save(q.sub_pdf.name[-23:], ContentFile(response.content), save=False)
    #                 q.save()
    #                 print("save sucessfully key = ",key,q.sub_pdf.name[-23:])
    # ob = 908
    for row in csv.reader(open(r'D:\study\5th sem  it\Internship II\New folder\data.csv', "r")):
        try:
            response = requests.get(row[0])
            if response.status_code == 200:
                ob = Sub_Syllabus()
                ob.sub_name = row[5]
                ob.sub_code = row[1]
                ob.Assigned_Sub_Faculty = Faculty_Records.objects.get(email='nonedit@gmail.com')
                ob.session = Sub_Syllabus.Session.SUMMER
                ob.sub_branch_code = row[2]
                ob.sub_lacture_hours = int(row[7])
                ob.sub_tutorial_hours = int(row[8])
                ob.sub_practical_hours = int(row[9])
                ob.sub_category = row[4]
                ob.sub_theory_mid1 = 0 if int(row[12]) == 0 else (int(row[12])*2)//3
                ob.sub_theory_mid2 = 0 if int(row[12]) == 0 else (int(row[12])*2)//3
                ob.sub_theory_micro = 0 if int(row[12]) == 0 else (int(row[12]))//3
                ob.sub_theory_PA = int(row[12])
                ob.sub_theory_ESE = int(row[11])
                ob.sub_prctical_PA = int(row[13])
                ob.sub_prctical_ESE = int(row[14])
                ob.sub_sem = int(row[6])
                ob.sub_credit = int(row[10])
                ob.sub_academic_term = '23-24'
                ob.sub_pdf.save(f'syllabus-{row[2]}-{row[1]}.pdf',ContentFile(response.content),save=False)
                ob.save()
                print("save sucessfully",ob.sub_pdf.name)
        except Exception as e:
            pass
    return render(request,'main/home.html')

def gtu_exam_fetch():
    queryset = Sub_Syllabus.objects.filter(sub_branch_code='16')
    try:
        for q in queryset:
            url = f'https://gtu.ac.in/uploads/S2024/DI/{q.sub_code}.pdf'
            split = url.split('/')
            mark = GtuExam(
            sub_code = q.sub_code,
            sub_branch_code = q.sub_branch_code,
            subject = q,
            sub_sem = q.sub_sem,
            sub_academic_term = split[-3],
            )
            if split[-3][0] == 'S':
                mark.sub_session = Sub_Syllabus.Session.SUMMER
            else:mark.sub_session = Sub_Syllabus.Session.WINTER
            dic = {'S':1,'W':0}
            if int(q.sub_sem)%2 == dic[split[-3][0]]:mark.type = GtuExam.Type.REMEDIAL
            filename = '-'.join(split[-3:])
            response = requests.get(url)
            if response.status_code == 200:
                pat = r"D:\study\5th sem  it\Internship II\Student_Web_Portal_3rd_Sem\media\home\pdfs\syllabus\exam_test.pdf"
                with open(pat, 'wb+') as f:
                    f.write(response.content)

                mark.sub_pdf.save(filename,open(pat,'rb'))
                mark.save()
    except Exception as e:
        print(e)



def home(request):
    # gtu_exam_fetch()
    return render(request,'main/home.html')

def syllabus(request):
    if request.method == 'GET':
        sem = request.GET.get('sem',None)
        branch = request.GET.get('branch',None)
        sub_code = request.GET.get('sub_code',None)
        queryset = Sub_Syllabus.objects.all()
        if sub_code:
            queryset = Sub_Syllabus.objects.filter(sub_code=sub_code)
        if branch and branch != '00' :
            queryset = queryset.filter(sub_branch_code=branch)
        if queryset.count() == 0:
            messages.error(request, "The syllabus is not present for this filters")
        if sem or branch or sub_code:
            return render(request, 'main/syllabus.html',
                      {'branches': branchlist, 'queryset': queryset, 'branchid':branch,'sem':str(sem),
                       'sub_code': sub_code})
        return render(request, 'main/syllabus.html', {'branches': branchlist, 'input': True})


    elif request.method == 'POST':
        sem = request.POST['sem']
        branch = request.POST['branch']
        sub_code = request.POST['sub_code']
        queryset = Sub_Syllabus.objects.all()
        if sem != '0' :
            queryset = queryset.filter(sub_sem = sem)
        if branch != '00' :
            queryset = queryset.filter(sub_branch_code=branch)
        if sub_code:
            queryset = Sub_Syllabus.objects.filter(sub_code=sub_code)
        if queryset.count() == 0 :
            messages.error(request,"The syllabus is not present for this filters")
        return render(request,'main/syllabus.html',{'branches':branchlist,'queryset':queryset, 'branchid':branch,'sem':str(sem),'sub_code':sub_code})

    return render(request,'main/syllabus.html',{'branches':branchlist,'input':True})

def exam(request):

    # return render(request,'home/index.html',
    return render(request,'main/exam.html')
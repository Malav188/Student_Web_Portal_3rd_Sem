from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Sub_Syllabus)
class Sub_SyllabusAdmin(admin.ModelAdmin):
    model = Sub_Syllabus
    list_display = ('sub_code','sub_name','sub_sem','sub_branch_code','sub_credit','sub_academic_term','Assigned_Sub_Faculty')
    list_filter = ('sub_branch_code','sub_sem')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'Assigned_Sub_Faculty':
            # Filter out records with roll number '1111'
            kwargs['queryset'] = Faculty_Records.objects.exclude(email='nonedit@gmail.com')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    #

    def has_change_permission(self, request, obj=None):
        if obj and '11111' in obj.sub_code:
            return True
        return super().has_change_permission(request,obj)

    def has_delete_permission(self, request, obj=None):
        if obj and '11111' in obj.sub_code:
            return True
        return super().has_delete_permission(request, obj)

@admin.register(GtuExam)
class GtuExamAdmin(admin.ModelAdmin):
    model = GtuExam
    fields = ['subject','sub_code', 'sub_sem','sub_branch_code', 'sub_academic_term', 'sub_session', 'sub_pdf']
    list_display = ('sub_code', 'sub_academic_term', 'sub_session')
    list_filter = ('sub_branch_code','sub_sem')
    def get_readonly_fields(self, request, obj=None):
        return ['sub_code','sub_sem']
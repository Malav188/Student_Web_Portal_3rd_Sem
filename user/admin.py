from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    readonly_fields = ('groups','password','is_superuser','last_login','user_permissions','username','email','is_staff','is_active','date_joined','role')
    def get_queryset(self, request):
        if not request.user.is_superuser:
            return Faculty.objects.filter(username=request.user.email)
        return super().get_queryset(request)
admin.site.register(Student)
admin.site.register(User)




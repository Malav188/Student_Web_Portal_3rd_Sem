from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if not request.user.is_superuser:
            return Faculty.objects.filter(username=request.user.email)
        return super().get_queryset(request)
admin.site.register(Student)
admin.site.register(User)




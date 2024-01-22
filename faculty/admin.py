from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Faculty_Records)
class Faculty_RecordsAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['user']+list(super().get_readonly_fields(request,obj))

    def has_change_permission(self, request, obj=None):
        if obj and 'nonedit@' in obj.email:
            return False
        return super().has_change_permission(request,obj)

    def has_delete_permission(self, request, obj=None):
        if obj and 'nonedit@' in obj.email:
            return False
        return super().has_delete_permission(request, obj)

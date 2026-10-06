from django.contrib import admin
from .models import FacultyInfo,Department,Teacher,Program

@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', "head_name")
    search_fields = ('title', "head_name")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', "position","degree","department")
    search_fields = ('full_name',)
    list_filter = ('department',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('code', "title","department","coordinator_name")
    search_fields = ('title', "code")
    list_filter = ('department',)
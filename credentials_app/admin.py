from django.contrib import admin
from .models import Department, Course, FormEntry, Material

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(FormEntry)
class FormEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'course', 'purpose')
    list_filter = ('department', 'course', 'purpose')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

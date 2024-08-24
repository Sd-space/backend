from django.contrib import admin
from .models import Course, CourseInstance

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_code', 'year', 'semester')
    search_fields = ('title', 'course_code')
    list_filter = ('year', 'semester')

@admin.register(CourseInstance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'year', 'semester')
    search_fields = ('course__title', 'year', 'semester')
    list_filter = ('year', 'semester')


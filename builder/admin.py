from django.contrib import admin
from .models import (Resume, WorkExperience, Education, Skill,
                     Project, Certification, Language, Award, VolunteerWork)


class WorkInline(admin.TabularInline):
    model = WorkExperience
    extra = 0

class EduInline(admin.TabularInline):
    model = Education
    extra = 0

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display  = ['title', 'user', 'template', 'full_name', 'updated_at']
    list_filter   = ['template', 'created_at']
    search_fields = ['title', 'full_name', 'user__username']
    inlines       = [WorkInline, EduInline, SkillInline]

@admin.register(WorkExperience)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category', 'resume']
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import (Resume, WorkExperience, Education, Skill,
                     Project, Certification, Language, Award, VolunteerWork)


class RegisterForm(UserCreationForm):
    email      = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email address'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name  = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))

    class Meta:
        model  = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email      = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Password'})


class ResumeMetaForm(forms.ModelForm):
    class Meta:
        model  = Resume
        fields = ['title','template','accent_color']
        widgets = {
            'title':        forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Software Engineer Resume'}),
            'template':     forms.Select(attrs={'class':'form-select'}),
            'accent_color': forms.Select(attrs={'class':'form-select'}),
        }


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model  = Resume
        fields = ['full_name','job_title','email','phone','location','website','linkedin','github','summary','photo']
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control','placeholder':'John Doe'}),
            'job_title': forms.TextInput(attrs={'class':'form-control','placeholder':'Software Engineer'}),
            'email':     forms.EmailInput(attrs={'class':'form-control','placeholder':'john@example.com'}),
            'phone':     forms.TextInput(attrs={'class':'form-control','placeholder':'+1 (555) 000-0000'}),
            'location':  forms.TextInput(attrs={'class':'form-control','placeholder':'New York, NY'}),
            'website':   forms.URLInput(attrs={'class':'form-control','placeholder':'https://yoursite.com'}),
            'linkedin':  forms.TextInput(attrs={'class':'form-control','placeholder':'linkedin.com/in/johndoe'}),
            'github':    forms.TextInput(attrs={'class':'form-control','placeholder':'github.com/johndoe'}),
            'summary':   forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Brief professional summary...'}),
            'photo':     forms.FileInput(attrs={'class':'form-control','accept':'image/*'}),
        }


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model  = WorkExperience
        fields = ['company','position','location','start_date','end_date','is_current','description']
        widgets = {
            'company':     forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'position':    forms.TextInput(attrs={'class':'form-control','placeholder':'Job Title'}),
            'location':    forms.TextInput(attrs={'class':'form-control','placeholder':'City, Country'}),
            'start_date':  forms.TextInput(attrs={'class':'form-control','placeholder':'Jan 2020'}),
            'end_date':    forms.TextInput(attrs={'class':'form-control','placeholder':'Dec 2022'}),
            'is_current':  forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'• Led a team of 5...\n• Reduced load time by 40%...'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model  = Education
        fields = ['institution','degree','field_of_study','location','start_date','end_date','is_current','gpa','description']
        widgets = {
            'institution':    forms.TextInput(attrs={'class':'form-control','placeholder':'University Name'}),
            'degree':         forms.TextInput(attrs={'class':'form-control','placeholder':'Bachelor of Science'}),
            'field_of_study': forms.TextInput(attrs={'class':'form-control','placeholder':'Computer Science'}),
            'location':       forms.TextInput(attrs={'class':'form-control','placeholder':'City, Country'}),
            'start_date':     forms.TextInput(attrs={'class':'form-control','placeholder':'Sep 2016'}),
            'end_date':       forms.TextInput(attrs={'class':'form-control','placeholder':'May 2020'}),
            'is_current':     forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'gpa':            forms.TextInput(attrs={'class':'form-control','placeholder':'3.8/4.0'}),
            'description':    forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Relevant coursework, honors...'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model  = Skill
        fields = ['name','level','category']
        widgets = {
            'name':     forms.TextInput(attrs={'class':'form-control','placeholder':'Python'}),
            'level':    forms.Select(attrs={'class':'form-select'}),
            'category': forms.TextInput(attrs={'class':'form-control','placeholder':'Programming Languages'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model  = Project
        fields = ['name','role','url','start_date','end_date','description','technologies']
        widgets = {
            'name':         forms.TextInput(attrs={'class':'form-control','placeholder':'Project Name'}),
            'role':         forms.TextInput(attrs={'class':'form-control','placeholder':'Lead Developer'}),
            'url':          forms.URLInput(attrs={'class':'form-control','placeholder':'https://github.com/...'}),
            'start_date':   forms.TextInput(attrs={'class':'form-control','placeholder':'Jan 2022'}),
            'end_date':     forms.TextInput(attrs={'class':'form-control','placeholder':'Present'}),
            'description':  forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Brief description...'}),
            'technologies': forms.TextInput(attrs={'class':'form-control','placeholder':'React, Node.js, PostgreSQL'}),
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model  = Certification
        fields = ['name','issuer','date','expiry_date','credential_id','url']
        widgets = {
            'name':          forms.TextInput(attrs={'class':'form-control','placeholder':'AWS Solutions Architect'}),
            'issuer':        forms.TextInput(attrs={'class':'form-control','placeholder':'Amazon Web Services'}),
            'date':          forms.TextInput(attrs={'class':'form-control','placeholder':'Jun 2023'}),
            'expiry_date':   forms.TextInput(attrs={'class':'form-control','placeholder':'Jun 2026'}),
            'credential_id': forms.TextInput(attrs={'class':'form-control','placeholder':'ABC123XYZ'}),
            'url':           forms.URLInput(attrs={'class':'form-control','placeholder':'https://...'}),
        }


class LanguageForm(forms.ModelForm):
    class Meta:
        model  = Language
        fields = ['name','proficiency']
        widgets = {
            'name':        forms.TextInput(attrs={'class':'form-control','placeholder':'English'}),
            'proficiency': forms.Select(attrs={'class':'form-select'}),
        }


class AwardForm(forms.ModelForm):
    class Meta:
        model  = Award
        fields = ['title','issuer','date','description']
        widgets = {
            'title':       forms.TextInput(attrs={'class':'form-control','placeholder':'Employee of the Year'}),
            'issuer':      forms.TextInput(attrs={'class':'form-control','placeholder':'Company / Organization'}),
            'date':        forms.TextInput(attrs={'class':'form-control','placeholder':'2023'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':2}),
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model  = VolunteerWork
        fields = ['organization','role','start_date','end_date','description']
        widgets = {
            'organization': forms.TextInput(attrs={'class':'form-control','placeholder':'Organization Name'}),
            'role':         forms.TextInput(attrs={'class':'form-control','placeholder':'Volunteer Role'}),
            'start_date':   forms.TextInput(attrs={'class':'form-control','placeholder':'Jan 2021'}),
            'end_date':     forms.TextInput(attrs={'class':'form-control','placeholder':'Present'}),
            'description':  forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
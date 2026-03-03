from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from .models import (Resume, WorkExperience, Education, Skill, Project,
                     Certification, Language, Award, VolunteerWork)
from .forms import (RegisterForm, LoginForm, ResumeMetaForm, PersonalInfoForm,
                    WorkExperienceForm, EducationForm, SkillForm, ProjectForm,
                    CertificationForm, LanguageForm, AwardForm, VolunteerForm)


# ── Auth ──────────────────────────────────────────────────────────────────────

def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    templates_info = [
        {'name':'Modern',    'icon':'🎨','desc':'Sidebar layout',    'bg':'linear-gradient(135deg,#667eea,#764ba2)'},
        {'name':'Classic',   'icon':'📋','desc':'Timeless Garamond', 'bg':'linear-gradient(135deg,#2c3e50,#34495e)'},
        {'name':'Minimal',   'icon':'◻️', 'desc':'Clean & simple',   'bg':'linear-gradient(135deg,#bdc3c7,#2c3e50)'},
        {'name':'Executive', 'icon':'👔','desc':'Leadership style',  'bg':'linear-gradient(135deg,#8B0000,#b22222)'},
        {'name':'Creative',  'icon':'✨','desc':'Bold & artistic',   'bg':'linear-gradient(135deg,#f093fb,#f5576c)'},
        {'name':'Tech',      'icon':'💻','desc':'Developer style',   'bg':'linear-gradient(135deg,#0d1117,#161b22)'},
    ]
    features = [
        {'icon':'⚡','title':'Live Preview',      'desc':'See your resume update as you type.'},
        {'icon':'📄','title':'Perfect PDF',       'desc':'Export pixel-perfect PDFs instantly.'},
        {'icon':'🔒','title':'Secure & Private',  'desc':'Your data is stored safely.'},
        {'icon':'🎨','title':'6 Pro Templates',   'desc':'Multiple professional designs.'},
        {'icon':'✏️','title':'Full Edit Control', 'desc':'Add/remove every section freely.'},
        {'icon':'📱','title':'ATS-Optimized',     'desc':'Designed to pass screening systems.'},
    ]
    steps = [
        {'icon':'📝','title':'Create Account',  'desc':'Sign up free in 30 seconds'},
        {'icon':'🎨','title':'Pick Template',   'desc':'Choose from 6 designs'},
        {'icon':'✍️','title':'Fill Your Info',  'desc':'Enter details section by section'},
        {'icon':'📥','title':'Download PDF',    'desc':'Export and start applying'},
    ]
    return render(request, 'builder/landing.html', {
        'templates': templates_info, 'features': features, 'steps': steps
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = LoginForm(request)
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('landing')


# ── Dashboard ─────────────────────────────────────────────────────────────────

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'builder/dashboard.html', {'resumes': resumes})


# ── Resume CRUD ───────────────────────────────────────────────────────────────

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeMetaForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_edit', pk=resume.pk)
    else:
        form = ResumeMetaForm()
    return render(request, 'builder/resume_create.html', {'form': form})


@login_required
def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    sidebar_sections = [
        {'id':'personal',      'icon':'👤','label':'Personal Info',    'count': 1 if resume.full_name else 0},
        {'id':'work',          'icon':'💼','label':'Work Experience',  'count': resume.work_experiences.count()},
        {'id':'education',     'icon':'🎓','label':'Education',        'count': resume.educations.count()},
        {'id':'skill',         'icon':'⚡','label':'Skills',           'count': resume.skills.count()},
        {'id':'project',       'icon':'🚀','label':'Projects',         'count': resume.projects.count()},
        {'id':'certification', 'icon':'🏆','label':'Certifications',   'count': resume.certifications.count()},
        {'id':'language',      'icon':'🌐','label':'Languages',        'count': resume.languages.count()},
        {'id':'award',         'icon':'🎖️','label':'Awards',           'count': resume.awards.count()},
        {'id':'volunteer',     'icon':'🤝','label':'Volunteer',        'count': resume.volunteer_works.count()},
        {'id':'style',         'icon':'🎨','label':'Style & Template', 'count': ''},
    ]
    context = {
        'resume':            resume,
        'sidebar_sections':  sidebar_sections,
        'personal_form':     PersonalInfoForm(instance=resume),
        'meta_form':         ResumeMetaForm(instance=resume),
        'work_experiences':  resume.work_experiences.all(),
        'educations':        resume.educations.all(),
        'skills':            resume.skills.all(),
        'projects':          resume.projects.all(),
        'certifications':    resume.certifications.all(),
        'languages':         resume.languages.all(),
        'awards':            resume.awards.all(),
        'volunteer_works':   resume.volunteer_works.all(),
        'work_form':         WorkExperienceForm(),
        'education_form':    EducationForm(),
        'skill_form':        SkillForm(),
        'project_form':      ProjectForm(),
        'certification_form':CertificationForm(),
        'language_form':     LanguageForm(),
        'award_form':        AwardForm(),
        'volunteer_form':    VolunteerForm(),
    }
    return render(request, 'builder/resume_edit.html', context)


@login_required
def resume_save_personal(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            messages.success(request, 'Personal info saved!')
    return redirect('resume_edit', pk=pk)


@login_required
def resume_save_meta(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResumeMetaForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
    return redirect('resume_edit', pk=pk)


@login_required
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted.')
    return redirect('dashboard')


# ── Section Item AJAX CRUD ────────────────────────────────────────────────────

SECTION_MAP = {
    'work':          (WorkExperience, WorkExperienceForm),
    'education':     (Education,      EducationForm),
    'skill':         (Skill,          SkillForm),
    'project':       (Project,        ProjectForm),
    'certification': (Certification,  CertificationForm),
    'language':      (Language,       LanguageForm),
    'award':         (Award,          AwardForm),
    'volunteer':     (VolunteerWork,  VolunteerForm),
}


@login_required
def section_add(request, pk, section):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if section not in SECTION_MAP:
        return JsonResponse({'status': 'error', 'message': 'Invalid section'}, status=400)
    Model, FormClass = SECTION_MAP[section]
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.resume = resume
            item.save()
            return JsonResponse({'status': 'success', 'id': item.pk})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=405)


@login_required
def section_update(request, pk, section, item_id):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if section not in SECTION_MAP:
        return JsonResponse({'status': 'error'}, status=400)
    Model, FormClass = SECTION_MAP[section]
    item = get_object_or_404(Model, pk=item_id, resume=resume)
    if request.method == 'POST':
        form = FormClass(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error'}, status=405)


@login_required
def section_delete(request, pk, section, item_id):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if section not in SECTION_MAP:
        return JsonResponse({'status': 'error'}, status=400)
    Model, _ = SECTION_MAP[section]
    item = get_object_or_404(Model, pk=item_id, resume=resume)
    if request.method == 'POST':
        item.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=405)


# ── Preview & PDF ─────────────────────────────────────────────────────────────

@login_required
def resume_preview(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    template_name = f'builder/cv_templates/{resume.template}.html'
    context = _build_cv_context(resume)
    return render(request, template_name, context)


@login_required
def resume_pdf(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    template_name = f'builder/cv_templates/{resume.template}.html'
    context = _build_cv_context(resume)
    context['print_mode'] = True

    try:
        from weasyprint import HTML
        from weasyprint.logs import logger
        from django.template.loader import render_to_string
        import logging
        
        # Log that we're trying to generate PDF
        print("Attempting to generate PDF with WeasyPrint")
        
        html_string = render_to_string(template_name, context, request=request)
        
        # Optional: Save HTML to file for debugging
        with open(f'/tmp/debug_{resume.pk}.html', 'w') as f:
            f.write(html_string)
        print(f"HTML saved to /tmp/debug_{resume.pk}.html")
        
        html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
        pdf_bytes = html.write_pdf()
        
        print(f"PDF generated successfully, size: {len(pdf_bytes)} bytes")
        
        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        fname = f"{resume.full_name or 'resume'}_{resume.template}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{fname}"'
        response['Content-Length'] = len(pdf_bytes)
        return response
        
    except ImportError as e:
        print(f"WeasyPrint import error: {e}")
        messages.error(request, 'PDF generation library not installed. Please use Print instead.')
        return render(request, template_name, context)
        
    except Exception as e:
        print(f"PDF generation error: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, f'Error generating PDF: {str(e)}')
        return render(request, template_name, context)
    
def _build_cv_context(resume):
    skills = resume.skills.all()
    # group skills by category
    cats = {}
    for sk in skills:
        cats.setdefault(sk.category or 'General', []).append(sk)
    
    # Process projects to convert technology strings to lists
    projects = resume.projects.all()
    for project in projects:
        if project.technologies:
            # Split the technologies string by comma and strip whitespace
            project.tech_list = [tech.strip() for tech in project.technologies.split(',') if tech.strip()]
        else:
            project.tech_list = []
    
    return {
        'resume':          resume,
        'work_experiences':resume.work_experiences.all(),
        'educations':      resume.educations.all(),
        'skills':          skills,
        'skill_categories':cats,
        'projects':        projects,  # Now each project has a tech_list attribute
        'certifications':  resume.certifications.all(),
        'languages':       resume.languages.all(),
        'awards':          resume.awards.all(),
        'volunteer_works': resume.volunteer_works.all(),
    }
from django.db import models
from django.contrib.auth.models import User


TEMPLATE_CHOICES = [
    ('modern',    'Modern'),
    ('classic',   'Classic'),
    ('minimal',   'Minimal'),
    ('executive', 'Executive'),
    ('creative',  'Creative'),
    ('tech',      'Tech'),
]

COLOR_CHOICES = [
    ('#2c3e50', 'Navy Blue'),
    ('#1a1a2e', 'Midnight'),
    ('#0f3460', 'Royal Blue'),
    ('#533483', 'Purple'),
    ('#2d6a4f', 'Forest Green'),
    ('#b5451b', 'Terracotta'),
    ('#c0392b', 'Crimson'),
    ('#1b1b2f', 'Dark'),
]


class Resume(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title        = models.CharField(max_length=200, default='My Resume')
    template     = models.CharField(max_length=50, choices=TEMPLATE_CHOICES, default='modern')
    accent_color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='#2c3e50')
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    # Personal info
    full_name  = models.CharField(max_length=200, blank=True)
    job_title  = models.CharField(max_length=200, blank=True)
    email      = models.EmailField(blank=True)
    phone      = models.CharField(max_length=30, blank=True)
    location   = models.CharField(max_length=200, blank=True)
    website    = models.URLField(blank=True)
    linkedin   = models.CharField(max_length=200, blank=True)
    github     = models.CharField(max_length=200, blank=True)
    summary    = models.TextField(blank=True)
    photo      = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.title} — {self.user.username}"


class WorkExperience(models.Model):
    resume     = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    company    = models.CharField(max_length=200)
    position   = models.CharField(max_length=200)
    location   = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=20)
    end_date   = models.CharField(max_length=20, blank=True)
    is_current = models.BooleanField(default=False)
    description= models.TextField(blank=True)
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    resume         = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    institution    = models.CharField(max_length=200)
    degree         = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    location       = models.CharField(max_length=200, blank=True)
    start_date     = models.CharField(max_length=20)
    end_date       = models.CharField(max_length=20, blank=True)
    is_current     = models.BooleanField(default=False)
    gpa            = models.CharField(max_length=20, blank=True)
    description    = models.TextField(blank=True)
    order          = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner',     'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced',     'Advanced'),
        ('expert',       'Expert'),
    ]
    resume   = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name     = models.CharField(max_length=100)
    level    = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='intermediate')
    category = models.CharField(max_length=100, blank=True)
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'category', 'name']


class Project(models.Model):
    resume       = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    name         = models.CharField(max_length=200)
    role         = models.CharField(max_length=200, blank=True)
    url          = models.URLField(blank=True)
    start_date   = models.CharField(max_length=20, blank=True)
    end_date     = models.CharField(max_length=20, blank=True)
    description  = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, blank=True)
    order        = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Certification(models.Model):
    resume        = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    name          = models.CharField(max_length=200)
    issuer        = models.CharField(max_length=200, blank=True)
    date          = models.CharField(max_length=20, blank=True)
    expiry_date   = models.CharField(max_length=20, blank=True)
    credential_id = models.CharField(max_length=200, blank=True)
    url           = models.URLField(blank=True)
    order         = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Language(models.Model):
    PROFICIENCY_CHOICES = [
        ('native',       'Native'),
        ('fluent',       'Fluent'),
        ('professional', 'Professional'),
        ('intermediate', 'Intermediate'),
        ('basic',        'Basic'),
    ]
    resume      = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    name        = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='professional')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Award(models.Model):
    resume      = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='awards')
    title       = models.CharField(max_length=200)
    issuer      = models.CharField(max_length=200, blank=True)
    date        = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class VolunteerWork(models.Model):
    resume       = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='volunteer_works')
    organization = models.CharField(max_length=200)
    role         = models.CharField(max_length=200, blank=True)
    start_date   = models.CharField(max_length=20, blank=True)
    end_date     = models.CharField(max_length=20, blank=True)
    description  = models.TextField(blank=True)
    order        = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
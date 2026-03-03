from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('',          views.landing,      name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/',    views.login_view,    name='login'),
    path('logout/',   views.logout_view,   name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Resume CRUD
    path('resume/create/',                views.resume_create,       name='resume_create'),
    path('resume/<int:pk>/edit/',         views.resume_edit,          name='resume_edit'),
    path('resume/<int:pk>/delete/',       views.resume_delete,        name='resume_delete'),
    path('resume/<int:pk>/save-personal/',views.resume_save_personal, name='resume_save_personal'),
    path('resume/<int:pk>/save-meta/',    views.resume_save_meta,     name='resume_save_meta'),

    # Preview & PDF
    path('resume/<int:pk>/preview/', views.resume_preview, name='resume_preview'),
    path('resume/<int:pk>/pdf/',     views.resume_pdf,     name='resume_pdf'),

    # Section AJAX CRUD
    path('resume/<int:pk>/section/<str:section>/add/',                  views.section_add,    name='section_add'),
    path('resume/<int:pk>/section/<str:section>/<int:item_id>/update/', views.section_update, name='section_update'),
    path('resume/<int:pk>/section/<str:section>/<int:item_id>/delete/', views.section_delete, name='section_delete'),
]
from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.report, name='report'),
    path('assistant/', views.assistant, name='assistant'),
    path('profile/', views.profile, name='profile'),
    path("logout/", views.logout, name="logout"),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

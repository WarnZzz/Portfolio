from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),  # Redirect to home view
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('education/', views.education, name='education'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact')
]
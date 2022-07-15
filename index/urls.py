from django.urls import path, include
from index import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contect', views.contect, name='contect'),
]

from django.urls import path
from . import views_khr


urlpatterns = [
    path('reword/', views_khr.reword, name='교환신청'), 
    path('reword_action', views_khr.reword_action, name='교환신청액션'),
    path('reword_action_action', views_khr.reword_action_action, name='교환신청제출'),
    
]
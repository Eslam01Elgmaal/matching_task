from django.urls import path
from .views_api import MatchSkillsAPIView
from . import views, views_ai

urlpatterns = [
    path('', views.index, name='index'), 
    path('match-skills/', views.match_skills, name='match_skills'),
    path('api/match-skills/', MatchSkillsAPIView.as_view(), name='match_skills_api'),
    path('match-skills-ai/', views_ai.match_skills_ai, name='match_skills_ai'),
]

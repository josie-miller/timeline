from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline_view, name='timeline'),
    path('<int:pk>/', views.milestone_detail_view, name='milestone_detail'),
]

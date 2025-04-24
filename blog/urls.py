from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('<int:post_pk>/comment/<int:comment_pk>/edit/', views.edit_comment, name='edit_comment'),

]
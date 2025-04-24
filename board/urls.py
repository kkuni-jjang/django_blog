from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('new/', views.board_new, name='board_new'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('<int:pk>/delete/', views.board_delete, name='board_delete'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]

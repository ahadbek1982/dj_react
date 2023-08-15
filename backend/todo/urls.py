from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name= 'index'),
    # path('api/',views.TodoView.as_view(), name= 'todolist' ),
    # path('api/<int:pk>/', views.TodoDetail.as_view(), name='tododetail'),
]
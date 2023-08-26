from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
    # re_path(r'^api/todos/$', views.todo_list),
    # re_path(r'^api/todos/([0-9])/$', views.todo_detail)


]

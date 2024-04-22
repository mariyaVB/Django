from django.urls import path, re_path
import todo_list.views as task

urlpatterns = [
    path('', task.task),
    path('completed_task/', task.completed_task),
    path('edit_task/<int:id_task>/', task.edit_task),
    path('delete_task/<int:id_task>/', task.delete_task),
    path('<slug:id_task>/', task.status),


]

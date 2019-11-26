from django.urls import path
from . import views
app_name = "myplanner"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('addtask/', views.add_task, name="add_task"),
    path('add_to_completed/', views.add_to_completed, name='add_to_completed'),
    path('login/', views.auth_view, name="auth"),
    path('logout/', views.logout_view, name="logout")

]
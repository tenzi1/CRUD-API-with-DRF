
from django.contrib import admin
from django.urls import path

from api import views
from class_api import views as class_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
    path('api_class/', class_views.StudentApiView.as_view()),

]

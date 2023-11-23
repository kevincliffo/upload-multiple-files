from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload_and_display_files, name='upload-and-display'),
]

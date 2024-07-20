from django.urls import path

# importing views of same path as urls ( . ):
from . import views

# app_name = 'my_app'

urlpatterns = [
    # path('') ==== actual path
    # index is a func i created in views-file
    path('', views.index, name='index'),  #name=func-name#optional
]

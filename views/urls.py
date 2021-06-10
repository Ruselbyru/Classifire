from django.urls import path
from .views import *
urlpatterns = [
    path('',home_page,name='home'),
    path('image/<str:key>/',viewimg,name='image'),
    path('update/<str:id>/',updateimg, name='update'),
    path('delete/<str:id>/',deleteimg, name='delete'),
    path('infer/<str:id>/',run_inference, name='infer'),
]
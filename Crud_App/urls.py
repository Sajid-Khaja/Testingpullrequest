from django.urls import path
from .import views

urlpatterns = [

       path('',views.Read,name='Read'),
       path('add/',views.Create,name='Create'),
       path('detail/<int:pk>/',views.changes,name='changes'),
       path('delete/<int:pk>/',views.Delete_data,name='delete')

]

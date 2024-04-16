from django.urls import path
from .views import Add_view, List_view, Detail_view, Update_view, Delete_view

urlpatterns = [
    path('add/', Add_view.as_view()),
    path('list/', List_view.as_view()),
    path('detail/<int:pk>/', Detail_view.as_view()),
    path('update/<int:pk>/', Update_view.as_view()),
    path('delete/<int:pk>/', Delete_view.as_view()),
]

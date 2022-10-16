from django.urls import path ,include
from community import views

app_name='community'

urlpatterns = [
    path('',views.post_view, name='post_view'),
]
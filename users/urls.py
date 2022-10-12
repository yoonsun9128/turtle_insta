from django.urls import path ,include
from users import views

# 장고가 알아보기 위해
app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]

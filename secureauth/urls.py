from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
#     path('hello/', HelloView.as_view(), name='hello'),
#     path('adminview/', AdminAPIView.as_view(), name='admin-view'),
#     path('parentview/', ParentAPIView.as_view(), name='parent-view'),
#     path('teacherview/', TeacherAPIView.as_view(), name='teacher-view'),

]

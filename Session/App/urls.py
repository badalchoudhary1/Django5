from django.urls import path
from .views import set_session, get_session, delete_session

urlpatterns = [
    path('set-session/', set_session, name='set_session'),
    path('get-session/', get_session, name='get_session'),
    path('delete-session/', delete_session, name='delete_session'),
]

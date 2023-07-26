from django.urls import path

from apps.views import Home, Register, Profile, listview, Delete

urlpatterns = [
    path('login', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('', listview, name='list'),
    path('delete/<int:pk>', Delete.as_view(), name='delete')
]

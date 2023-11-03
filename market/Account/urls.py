from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'Account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='Account/signin.html'), name='signin'),
    path('signout/', LogoutView.as_view(next_page='Account:signin'), name='signout'),

]

from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('verify_registration_mail/', verify_registration_mail, name='verify_registration_mail'),
    path('registration_password_setter/', registration_password_setter, name='registration_password_setter'),
    path('logout/', logout_page, name='logout'),
]

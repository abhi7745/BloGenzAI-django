# This Django app is build for automation using python, build by Abhijith KR

## Contents

### app
- accounts/views.py (index, signup, login, logout)
- accounts/models.py (User_Account)
- accounts/urls.py (login, signup, logout)

### static
- accounts/dashboard/assets/(css, js, etc..)

### templates
- accounts/(signup.html,login.html)
- admin/(dashboard.html, sidebar.html)
- /index.html
- /base.html

### Requirements
- django

### Authentication Views
#### Using the views
```bash
urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
]
```
#### This will include the following URL patterns
```bash
urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_page, name='logout'),
]
```
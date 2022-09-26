# This Django app is build for automation using python, build by Abhijith KR

contents :-

    project directory ->
            urls.py (index) 

    app ->  accounts/views.py(index, signup, verify_registration_mail, registration_password_setter, login, logout)
            accounts/models.py(User_Account)
            accounts/urls.py(signup, verify_registration_mail, registration_password_setter, login, logout)
    

    static -> accounts/dashboard/assets/(css, js, etc..)
    
    templates -> templates/accounts/(signup.html,login.html)
                 templates/admin/(dashboard.html, sidebar.html)
                 templates/email_templates/registration_or_forgot_psd_sender.html
                 templates/base.html
                 templates/index.html
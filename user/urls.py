from django.urls import path

from .views import dashboard, create_blog, list_blog, update_blog, delete_blog, Magic_writer


urlpatterns = [
    path('dashboard/', dashboard, name='user-dashboard'),
    path('create/blog', create_blog, name='create-blog'),
    path('create/blog/magic-writer', Magic_writer, name='magic-writer'),
    path('list/blog', list_blog, name='list-blog'),
    path('update/blog/<str:pk>', update_blog, name='update-blog'),
    path('delete/blog/<int:pk>', delete_blog, name='delete-blog'),
]

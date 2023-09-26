from django.shortcuts import render, redirect

from django.http import JsonResponse

from .models import Blog

import os

from PIL import Image # image_file_size checking purpose 

from django.contrib import messages

# Create your views here.


def dashboard(request):
    return render(request, 'user/dashboard.html')


def create_blog(request):
    if request.method == "POST":
        print("this is post form")
        
        blog_title = request.POST.get('blog_title', '')
        thumbnail_img = request.FILES.get('thumbnail_img', None)
        content = request.POST.get('content', '')


        print(blog_title)
        print(thumbnail_img)
        print(content, '\n')

        print(request.POST)
        print(request.FILES)

        # saving to database
        Blog.objects.create(title=blog_title, thumbnail_img=thumbnail_img, content=content, user=request.user)
        print('data saved successfully')

        return JsonResponse({'status': True},safe=False)


    return render(request, 'user/create_blog.html')



def list_blog(request):

    if Blog.objects.all().exists():
        print('blog_exist')
        blog_data = Blog.objects.all().order_by('-id')

        context = {'blog_data' : blog_data}
        return render(request, 'user/list_blog.html', context)
    else:
        print('no_blog_exist')
        return redirect('create-blog')
    


def update_blog(request, pk):
    if Blog.objects.filter(id=pk, user = request.user.id).exists():
        blog_data = Blog.objects.get(id=pk, user=request.user.id)

        if request.method == "POST":
            print("this is post form")
        
            blog_title = request.POST.get('blog_title', '')
            thumbnail_img = request.FILES.get('thumbnail_img', None)
            content = request.POST.get('content', '')


            print(blog_title)
            print(thumbnail_img,type(thumbnail_img))
            # print(content, '\n')

            # print(request.POST)
            # print(request.FILES)

            # # re-saving to database
            blog_data.title=blog_title

            # splitting the "filename" of image from database_image ".name" attribute - start ******
            file_name = blog_data.thumbnail_img.name.split("/")[-1]
            print(file_name, 'filename', type(file_name))
            print(thumbnail_img, 'filename', type(str(thumbnail_img)))
            # splitting the "filename" of image from database_image ".name" attribute - end ******
        
            # open 2 image files(database_image, form_image) and calculate the file_size in bytes - start ####
            # Open the database_image
            with Image.open(blog_data.thumbnail_img.path) as database_image:
                database_image_bytes = len(database_image.tobytes())

            # Open the form_image
            with Image.open(thumbnail_img) as form_image:
                form_image_bytes = len(form_image.tobytes())
            
            print(f"File Size (bytes) of database_image is: {database_image_bytes} ######################### {type(database_image_bytes)}")
            print(f"File Size (bytes) of form_image is: {form_image_bytes} ######################### {type(form_image_bytes)}")
            # open 2 image files(database_image, form_image) and calculate the file_size in bytes - end ####

            # if the "database-filename" and "form-submitted-image" are not equal, or "database_image_bytes" and "form_image_bytes" are not equal
            # then remove the old-database-image from media folder and re-assign with new image
            if (file_name != str(thumbnail_img)) or (database_image_bytes != form_image_bytes):
                print('New image detected, removing/re-assign - process started')
                # image field
                if len(request.FILES) != 0:
                    if blog_data.thumbnail_img and os.path.exists(blog_data.thumbnail_img.path):
                        os.remove(blog_data.thumbnail_img.path) # removing the "old-image" from media folder
                        print('old image removed')

                    blog_data.thumbnail_img=thumbnail_img # re-assign with new image
                    print('NEW image assigned')
            else:
                print('image are same - no update for image')


            blog_data.content=content
            blog_data.save()
            print('data updated successfully')

            return JsonResponse({'status': True},safe=False)
    
        context = {'blog_data' : blog_data}
        return render(request, 'user/update_blog.html', context)
    
    else:
        return redirect('list-blog')


def delete_blog(request, pk):
    blog_data = Blog.objects.filter(id=pk, user=request.user.id).first()
    if blog_data:
        if request.method == 'POST':
            if blog_data.thumbnail_img and os.path.exists(blog_data.thumbnail_img.path):
                os.remove(blog_data.thumbnail_img.path) # removing the "old-image" from media folder
                print('old image removed from media folder')

            messages.success(request, blog_data.title , extra_tags='delete_msg')
            blog_data.delete()
            print('blog deleted successfully')
        return redirect('list-blog')
    else:
        messages.error(request, 'Something went wrong' , extra_tags='wrong_id')
        return redirect('list-blog')


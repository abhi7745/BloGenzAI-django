from django.shortcuts import render
from user.models import Blog

# Create your views here.

# home page
def index(request):
    blog_data=Blog.objects.all().order_by('-id')
    context = {'blog_data' : blog_data}
    return render(request,'home/index.html', context)
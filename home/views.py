from django.shortcuts import render
from user.models import Blog
from accounts.models import User

# pagination purpose
from django.core.paginator import Paginator

# Create your views here.

# home page
def index(request):
    total_users = User.objects.all().count()
    blog_data=Blog.objects.all().order_by('-id')[:10]

    context = {'blog_data' : blog_data, 'latest_three_blog': blog_data[:3], 'total_blog_count': blog_data.count(),
               'total_users':total_users}
    return render(request,'home/index.html', context)


def blogs(request):
    blog_data = Blog.objects.all().order_by('-id')
    # pagination purpose
    paginator = Paginator(blog_data, 2)
    page_number = request.GET.get('page')
    blog_page = paginator.get_page(page_number)

    context = {'blog_data':blog_page, 'latest_three_blog': blog_data[:3]}
    return render(request, 'home/blog.html', context)
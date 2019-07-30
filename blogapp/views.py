from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def write(request):
    return render(request, 'write.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blogapp/'+str(blog.id))

def delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('home')

def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = Create(request.POST, instance = blog)
        if form.is_vaild():
            blog = form.save(commit = False)
            blog.pub_date_date=timezone.now()
            blog.save()
            return redirect('detail')
    else:
        form = Create(instance = blog)
        return render(request, 'detail.html', {'form':form})
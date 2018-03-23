from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Request
from .forms import PostForm, JoinForm, StatusForm
from django.shortcuts import redirect

def introduce_voithru(request):
    return render(request, 'blog/introduce_voithru.html')


def introduce_service(request):
    return render(request, 'blog/introduce_service.html')


def post_list(request):
    candidates = Request.objects.all()
    posts = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
            form = StatusForm(request.POST)
            if form.is_valid():
                post_test = Request.objects.get(id=request.POST['post.id'])
                post_test.status = request.POST.get('status', False)  # form.save(commit=False)
                post_test.author = request.user
                post_test.save()
                return redirect('post_list')
    else:
        form = StatusForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'form': form, 'candidates': candidates})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
            '''
            기본 코드는 return redirect('post_detail', pk=post.pk)
            3/14일 테스트용으로 post_list로 redirect 설정
            '''
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Request, pk=pk)
    post.save()

    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            join_post = form.save(commit=False)
            join_post.j_user = post
            join_post.j_username = request.user
            post.view_cnt += 1
            post.save()
            join_post.save()
            return redirect('post_list')

    else:
        form = JoinForm()

    return render(request, 'blog/post_detail.html', {'post':post, 'form':form})

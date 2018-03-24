from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Request, Helpdesk
from .forms import PostForm, JoinForm, StatusForm, HelpdeskPostForm
from django.shortcuts import redirect

def published_post_list(request):
    candidates = Request.objects.all()
    posts = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
            form = StatusForm(request.POST)
            if form.is_valid():
                post_test = Request.objects.get(id=request.POST['post.id'])
                post_test.status = request.POST.get('status', False)  # form.save(commit=False)
                post_test.author = request.user
                post_test.save()
                return redirect('published_post_list')
    else:
        form = StatusForm()
    return render(request, 'blog/published_post_list.html', {'posts': posts, 'form': form, 'candidates': candidates})


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


#helpdesk 관련 사안들
#helpdesk list
def help_list(request):
    candidates = Helpdesk.objects.all()
    posts = Helpdesk.objects.filter(h_created_date__lte=timezone.now()).order_by('h_created_date')
    return render(request, 'blog/help_list.html', {'candidates':candidates, 'posts':posts})

#helpdesk 클릭시
def help_detail(request, pk):
    post = get_object_or_404(Helpdesk, pk=pk)
    post.save()

    if request.method == "POST":
        form = HelpdeskPostForm(request.POST)
        if form.is_valid():
            help_post = form.save(commit=False)
            help_post.h_user = post
            help_post.save()
            return redirect('help_list')
    else:
        form = HelpdeskPostForm()

    return render(request, 'blog/help_detail.html', {'post':post, 'form':form})

# #helpdesk 수정
# def help_edit(request, pk):
#     post = get_object_or_404(Helpdesk, pk=pk)
#     if request.method == "POST":
#         form = HelpdeskPostForm(request.POST,)


#helpdesk 글쓰기 확정 버튼 누르기
def help_new(request):
    if request.method == "POST":
        form = HelpdeskPostForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.h_user = request.user
            board.h_created_date = timezone.now()
            board.save()
            return redirect('help_list')
    else:
        form = HelpdeskPostForm()
    return render(request, 'blog/help_new.html', {'form':form})

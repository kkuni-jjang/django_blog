from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, Comment
from .forms import  CommentForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def board_list(request):
    posts = Post.objects.all().order_by('-created_at')

    # 검색어 필터
    q = request.GET.get('q', '')
    if q:
        posts = posts.filter(title__icontains=q)

    # 카테고리 필터 (카테고리 필드 있다면)
    category = request.GET.get('category', '')
    if category:
       posts = posts.filter(category=category)

    return render(request, 'board/board_list.html', {'posts': posts})

def board_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('board_detail', pk=post.pk)
    else:
        form = CommentForm()

    comments = post.comments.all().order_by('-created_at')
    return render(request, 'board/board_detail.html', {
        'post': post, 'form': form, 'comments': comments
    })

@login_required
def board_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            board_post = form.save(commit=False)
            board_post.author = request.user
            board_post.save()
            return redirect('board_detail', pk=board_post.pk)
    else:
        form = PostForm()
    return render(request, 'board/board_form.html', {'form': form})


def board_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('board_detail', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board_detail', pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'board/board_form.html', {'form': form})


# 게시글 삭제
def board_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('board_list')


# 댓글 수정
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('board_detail', pk=comment.post.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('board_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'board/comment_form.html', {'form': form})

# 댓글 삭제
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    if request.user == comment.author:
        comment.delete()
    return redirect('board_detail', pk=post_pk)
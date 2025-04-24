from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-created_at')[:3]
    return render(request, "blog/home.html",{'posts':posts})

# 게시글 / 댓글
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    comments = post.comments.all().order_by('-created_at')
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments})

# 어바웃미
def about(request):
    return render(request, 'blog/about.html')

def blog_list(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/blog_list.html', {'posts': posts, 'query': query})

@login_required
def edit_comment(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, post__pk=post_pk)

    if request.user != comment.author:
        return redirect('post_detail', pk=post_pk)  # 본인만 수정 가능

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post_pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {
        'form': form,
        'post': comment.post,
        'comment': comment,
    })
from django import forms
from .models import Post, Comment

# 게시글 작성/수정용 폼
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# 댓글 작성/수정용 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }
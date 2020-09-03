from django import forms
from comment.models import PostComment

class CommentForm(forms.ModelForm):
    class Meta():
        fields = ['text']
        model = PostComment
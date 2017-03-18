from django import forms

from .models import Post
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

from __future__ import unicode_literals


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('lockerId', 'lockerName', 'prime', 'standard')


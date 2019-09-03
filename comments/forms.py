from __future__ import unicode_literals
from django import forms

class CommentForm(forms.Form):
	comment = forms.CharField(max_length=10000)
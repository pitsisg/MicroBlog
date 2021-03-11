from django import forms
from .models import Post
from taggit.forms import *
from bootstrap_datepicker_plus import DatePickerInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
            'tags',
            'post_date',
            'draft',
        ]
        widgets = {
        	'title': forms.TextInput(attrs={'class': 'form-control'}),
        	'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'idval', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        	'tags': TagWidget(attrs={'data-role':'tagsinput','placeholder':'Add Tags','class':'form-control'}),
            'post_date': forms.DateInput(),
            'draft' : forms.CheckboxInput(),  
        }

        

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'tags',
            'post_date',
            'draft',
        ]
        widgets = {
        	'title': forms.TextInput(attrs={'class': 'form-control'}),
        	'body': forms.Textarea(attrs={'class': 'form-control'}),
        	'tags': TagWidget(attrs={'data-role':'tagsinput','placeholder':'Add Tags','class':'form-control'}),
            'post_date': forms.DateInput(),
            'draft' : forms.CheckboxInput(), 
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
            'tags',
            'post_date',
            'draft',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'idval', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'data-role':'tagsinput','placeholder':'Add Tags','class':'form-control'}),
            'post_date': forms.DateInput(),
            'draft' : forms.CheckboxInput(),  
        }
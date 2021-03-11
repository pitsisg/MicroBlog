from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import date
from django.core.exceptions import ValidationError

def present_future(value):
    today = date.today()
    if value < today:
        raise ValidationError('Post_Date cannot be in the past.')

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	body = RichTextField(blank=True,null=True)
	tags = TaggableManager()
	post_date=models.DateField(default=date.today(), help_text="If you don't like to publish immediately please enter future post date ", validators=[present_future])
	draft = models.BooleanField(default=False)
	## change to drafts 

	def __str__(self):
		return self.title +  ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')


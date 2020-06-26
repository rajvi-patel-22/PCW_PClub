from django import forms 
from .models import *
  
class UserBlogForm(models.ModelForm): 
    class Meta: 
        model = UserBlog 
        fields = ['user_name', 'user_emailId', 'Enrollment_No', 'BlogTitle', 'BlogDesc', 'image','uploaded_at'] 
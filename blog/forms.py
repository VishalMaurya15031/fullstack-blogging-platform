from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    
    class Meta:
        model = Post
        fields = ['title', 'category', 'excerpt', 'banner_url', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter blog title...'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Short introduction / summary'}),
            'banner_url': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://images.unsplash.com/... or image link'}),
            'content': forms.Textarea(attrs={'class': 'form-input editor-textarea', 'rows': 12, 'placeholder': 'Write your story in HTML or Markdown...'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'}),
            'body': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Join the discussion...'}),
        }

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

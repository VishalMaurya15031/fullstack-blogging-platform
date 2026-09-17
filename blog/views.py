import markdown
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm, UserRegisterForm

def post_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    posts = Post.objects.filter(status='published').select_related('author', 'category')
    
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=selected_category)
        
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        )

    categories = Category.objects.all()
    featured_post = posts.order_by('-views_count', '-created_at').first()
    recent_posts = posts.exclude(id=featured_post.id) if featured_post else posts

    context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'featured_post': featured_post,
        'categories': categories,
        'query': query,
        'selected_category': selected_category,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Increment view count
    post.views_count += 1
    post.save(update_fields=['views_count'])
    
    # Convert markdown to HTML if markdown syntax present
    post_html = markdown.markdown(
        post.content,
        extensions=['extra', 'codehilite', 'toc', 'nl2br']
    )

    comments = post.comments.filter(approved=True)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            if request.user.is_authenticated:
                new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been posted successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email
            }
        comment_form = CommentForm(initial=initial_data)

    related_posts = Post.objects.filter(status='published', category=post.category).exclude(id=post.id)[:3]

    context = {
        'post': post,
        'post_html': post_html,
        'comments': comments,
        'comment_form': comment_form,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    categories = Category.objects.all()
    
    context = {
        'category': category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/category_posts.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post published successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create New Story'})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Story', 'is_edit': True})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def register_user(request):
    if request.user.is_authenticated:
        return redirect('post_list')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, f'Welcome to BlogPulse, {user.username}!')
            return redirect('post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('post_list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'post_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('post_list')

@login_required
def user_profile(request):
    user_posts = Post.objects.filter(author=request.user)
    context = {
        'user_posts': user_posts,
        'published_count': user_posts.filter(status='published').count(),
        'draft_count': user_posts.filter(status='draft').count(),
        'total_views': sum(p.views_count for p in user_posts),
    }
    return render(request, 'blog/user_profile.html', context)

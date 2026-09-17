import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Post, Comment

def run_seed():
    print("Seeding database...")
    
    # 1. Create Superuser / Main Author
    admin_user, created = User.objects.get_or_create(username='admin')
    if created:
        admin_user.set_password('admin123')
        admin_user.email = 'admin@blogpulse.dev'
        admin_user.first_name = 'Alex'
        admin_user.last_name = 'Rivera'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print("Created admin user (Username: admin, Password: admin123)")

    author2, created = User.objects.get_or_create(username='sarah_dev')
    if created:
        author2.set_password('pass123')
        author2.first_name = 'Sarah'
        author2.last_name = 'Chen'
        author2.save()

    # 2. Create Categories
    categories_data = [
        {'name': 'Artificial Intelligence', 'badge_color': 'cyan', 'description': 'Deep learning, LLMs, and AI innovation.'},
        {'name': 'Web Development', 'badge_color': 'indigo', 'description': 'Python, Django, JavaScript, and CSS.'},
        {'name': 'UI & UX Design', 'badge_color': 'rose', 'description': 'Modern aesthetics, glassmorphism, and UX systems.'},
        {'name': 'Software Architecture', 'badge_color': 'purple', 'description': 'Scalable backends and API architecture.'},
        {'name': 'Tutorials', 'badge_color': 'emerald', 'description': 'Step-by-step programming guides.'},
    ]

    cat_map = {}
    for cat in categories_data:
        obj, _ = Category.objects.get_or_create(
            name=cat['name'],
            defaults={'badge_color': cat['badge_color'], 'description': cat['description']}
        )
        cat_map[cat['name']] = obj

    # 3. Create Sample Blog Posts
    posts_data = [
        {
            'title': 'Building Production-Grade Web Applications with Python & Django',
            'category': cat_map['Web Development'],
            'author': admin_user,
            'banner_url': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop',
            'views_count': 1420,
            'excerpt': 'Why Django remains the undisputed standard for modern full-stack web applications in 2026. Explore ORM performance, security, and scalable architecture.',
            'content': """
# The Power of Django in 2026

When building robust, secure, and scalable web applications, developers often debate between micro-frameworks and full-featured batteries-included frameworks. **Django** continues to stand tall as one of the most reliable and efficient web frameworks in the Python ecosystem.

---

## Key Advantages of Django

1. **Batteries-Included Philosophy**: Built-in authentication, ORM, CSRF protection, and administrative portal out of the box.
2. **Object-Relational Mapping (ORM)**: Seamless database abstraction with zero SQL boilerplate needed for common operations.
3. **Security by Default**: Protection against XSS, SQL injection, and clickjacking attacks out of the box.

```python
# Quick Django View Example
from django.shortcuts import render
from .models import Post

def home_view(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})
```

> "Django makes it easier to build better web apps more quickly and with less code."

### Conclusion

Whether you are building a SaaS product, a blogging system, or an enterprise portal, Django's maturity and rich ecosystem make it an unbeatable choice.
"""
        },
        {
            'title': 'The Next Wave of AI Agents: Autonomous Coding & Pair Programming',
            'category': cat_map['Artificial Intelligence'],
            'author': author2,
            'banner_url': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop',
            'views_count': 2380,
            'excerpt': 'How agentic LLMs are reshaping software engineering from writing basic scripts to designing full-stack architectures autonomously.',
            'content': """
# The Evolution of Autonomous Agentic AI

The software development paradigm is undergoing a massive shift. We have moved from syntax completion tools to **fully agentic assistants** capable of running commands, debugging stack traces, and designing UI components.

---

## What Makes an Agent "Agentic"?

Unlike standard chat bots, agentic AI tools possess:
- **Environment Interaction**: Ability to execute shell tools, read files, and inspect build output.
- **Self-Correction**: Reading runtime exception logs and iteratively resolving underlying root causes.
- **Multi-Step Reasoning**: Creating structured implementation plans before modifying codebases.

### Future Outlook

Developers who master pair-programming with AI tools are experiencing **3x to 5x productivity leaps**, focusing more on system design and user experience rather than repetitive syntax wiring.
"""
        },
        {
            'title': 'Designing Stunning Glassmorphism UIs with Modern Vanilla CSS',
            'category': cat_map['UI & UX Design'],
            'author': admin_user,
            'banner_url': 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?q=80&w=1200&auto=format&fit=crop',
            'views_count': 890,
            'excerpt': 'Learn how backdrop-filter, curated color palettes, and CSS custom properties create breathtaking visual interfaces without bloated libraries.',
            'content': """
# Master Modern Glassmorphism Styling

Glassmorphism creates a sense of depth, hierarchy, and premium polish in modern web designs. The secret lies in pairing translucent backdrop blurs with subtle glowing borders.

---

## Core CSS Snippet

```css
.glass-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}
```

### Tips for Best Visual Impact
- Use subtle radial background gradients behind translucent panels.
- Ensure high contrast typography so text remains crisp and readable.
- Add smooth hover micro-animations (`transform: translateY(-4px)`) for dynamic responsiveness.
"""
        },
        {
            'title': 'Mastering REST API Design & Django REST Framework',
            'category': cat_map['Software Architecture'],
            'author': author2,
            'banner_url': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1200&auto=format&fit=crop',
            'views_count': 640,
            'excerpt': 'A comprehensive guide to designing clean, versioned, and scalable HTTP endpoints with JSON serialization and JWT authentication.',
            'content': """
# Designing Clean RESTful APIs

Building APIs that frontends love consuming requires adhering to intuitive endpoint naming, proper HTTP verbs, and consistent error schemas.

---

## Best Practices

1. **Use Nouns for Endpoints**: `/api/v1/posts/` instead of `/api/v1/get_all_posts/`.
2. **Proper HTTP Status Codes**: `201 Created` for new resources, `400 Bad Request` for validation failures.
3. **Pagination**: Always paginate long lists to protect server memory.
"""
        },
    ]

    for p in posts_data:
        post_obj, created_p = Post.objects.get_or_create(
            title=p['title'],
            defaults={
                'category': p['category'],
                'author': p['author'],
                'banner_url': p['banner_url'],
                'views_count': p['views_count'],
                'excerpt': p['excerpt'],
                'content': p['content'],
                'status': 'published'
            }
        )

        if created_p:
            # Add sample comments
            Comment.objects.create(
                post=post_obj,
                name='Michael Scott',
                email='michael@dundermifflin.com',
                body='Fantastic article! Found the code examples extremely helpful.',
                approved=True
            )
            Comment.objects.create(
                post=post_obj,
                name='Elena Rostova',
                email='elena@techcorp.io',
                body='Great breakdown of full-stack Python development. Looking forward to more posts!',
                approved=True
            )
            print(f"Created post: {post_obj.title}")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    run_seed()

"""
WSGI config for blog_project project.

Exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

application = get_wsgi_application()
app = application

# Run auto-migration and seed data on serverless startup if needed
try:
    from django.core.management import call_command
    call_command('migrate', '--noinput')
    from seed_data import run_seed
    run_seed()
except Exception as e:
    print(f"Startup task info: {e}")

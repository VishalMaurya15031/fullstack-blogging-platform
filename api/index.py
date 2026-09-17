import os
import sys

# Add project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

# Run auto-migration and seed data on serverless startup if needed
try:
    from django.core.management import call_command
    call_command('migrate', '--noinput')
    from seed_data import run_seed
    run_seed()
except Exception as e:
    print(f"Startup task info: {e}")

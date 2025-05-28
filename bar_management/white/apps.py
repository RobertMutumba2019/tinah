from django.apps import AppConfig


class WhiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'white'

def ready(self):
    import white.signals  # Import# replace with your app name


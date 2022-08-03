from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts.profiles'

    def ready(self):
        from accounts.profiles import signals

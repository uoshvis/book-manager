from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_manager.apps.accounts'   # <- rename it like this, to respect the namespace

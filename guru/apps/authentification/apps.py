# auth/apps.py

from django.apps import AppConfig


class AuthentificationConfig(AppConfig):
    name = 'guru.apps.authentification'
    verbose_name = 'authentification helper app'
    label = 'authentification'
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bare_bones.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import bare_bones.users.signals  # noqa F401
        except ImportError:
            pass

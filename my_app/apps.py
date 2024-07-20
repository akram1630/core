from django.apps import AppConfig


# it will be created automatically when we create new app
class MyAppConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'my_app'

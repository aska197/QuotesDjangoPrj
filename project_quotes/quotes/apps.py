from django.apps import AppConfig
import data.add_created_add as add_created_add
import data.add_quotes_to_mongo as add_quotes_to_mongo


class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'

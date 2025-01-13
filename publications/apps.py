from django.apps import AppConfig


class PublicationsConfig(AppConfig):
    name = 'publications'
    default_auto_field = 'django.db.models.BigAutoField'
    

    def ready(self):
        try:
            from watson import search as watson_search
            from .models.publication import Publication
            watson_search.register(Publication)
        except:
            pass
from django.apps import AppConfig


class PublicationsConfig(AppConfig):
    name = 'publications'

    def ready(self):
        try:
            from watson import search as watson_search
            from .models.publication import Publication
            from .models.list import List
            watson_search.register(Publication)
            watson_search.register(List)
        except:
            pass
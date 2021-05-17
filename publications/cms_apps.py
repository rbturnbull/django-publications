from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .cms_menus import PublicationsMenu

@apphook_pool.register
class PublicationsApphook(CMSApp):
    app_name = "publications"
    name = "Publications Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["publications.urls"]

    def get_menus(self, page=None, language=None, **kwargs):
        return [PublicationsMenu]

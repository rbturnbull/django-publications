from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import Publication

class PublicationsMenu(CMSAttachMenu):
    name = _("Publications Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = [
            NavigationNode(
                title="Publications By Year",
                url=reverse("publications:publication_list"),
                id=-1,  # unique id for this node within the menu
                visible=True,
            ),
            NavigationNode(
                title="Add Publication",
                url=reverse("publications:publication_add"),
                id=0,  # unique id for this node within the menu
                visible=True,
            ),
        ]
        for obj in Publication.objects.all():
            node = NavigationNode(
                title=str(obj),
                url=obj.get_absolute_url(),
                id=obj.pk,  # unique id for this node within the menu
                visible=False,
            )
            update_node = NavigationNode(
                title=f"Update {obj}",
                url=obj.get_absolute_update_url(),
                id=-obj.pk,  # unique id for this node within the menu
                visible=False,
            )
            nodes.append(node)
            nodes.append(update_node)
            
        return nodes

menu_pool.register_menu(PublicationsMenu)

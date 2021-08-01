__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.urls import path

try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from publications import views

app_name = 'publications'
urlpatterns = [
    path('references/add/', views.ReferenceCreateView.as_view(), name='reference_add'),
    path('references/<int:pk>/', views.ReferenceDetailView.as_view(), name='reference_detail'),
    path('references/<int:pk>/update/', views.ReferenceUpdateView.as_view(), name='reference_update'),

    path('add/', views.PublicationCreateView.as_view(), name='publication_add'),
    path('authors/<str:name>/', views.author, name='author'),

    path('<str:citekey>/update/', views.PublicationUpdateView.as_view(), name='publication_update'),
    path('<str:citekey>/bibtex/', views.PublicationBibtexView.as_view(), name='publication_bibtex'),
    path('<str:citekey>/ris/', views.PublicationRISView.as_view(), name='publication_ris'),
    path('<str:citekey>/', views.PublicationDetailView.as_view(), name='publication_detail'),
    path("", views.year, name='publication_list'),

    url(r'^year/(?P<year>\d+)/$', views.year, name='year'),
    url(r'^tag/(?P<keyword>.+)/$', views.keyword, name='keyword'),
    url(r'^list/(?P<list>.+)/$', views.list, name='list'),
    url(r'^unapi/$', views.unapi, name='unapi'),
]

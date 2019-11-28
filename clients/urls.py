from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.ClientsListView.as_view(), name='clients'),
    url(r'^add_clients/$', views.NewClientView.as_view(), name='add_clients'),
    url(r'^edit_client/(?P<pk>.*)/$', views.ClientUpdateView.as_view(), name='edit_client'),
]

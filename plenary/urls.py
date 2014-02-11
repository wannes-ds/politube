from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from plenary.models import Plenary

urlpatterns = patterns('',
  url(r'^$', ListView.as_view(model=Plenary,
      template_name='pleniere/index.html',
      context_object_name='plenieres'), name='pleniere-list'),
  url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Plenary,
      template_name='pleniere/pleniere.html'),
      name='pleniere'),
)
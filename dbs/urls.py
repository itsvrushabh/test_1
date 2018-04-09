from django.urls import path
from django.views.generic.base import TemplateView
from dbs import views
urlpatterns = [
    path(r'',TemplateView.as_view(template_name='dbs/show.html'),name='demo1'),
    path(r'data/',views.showDB,name='data'),
]
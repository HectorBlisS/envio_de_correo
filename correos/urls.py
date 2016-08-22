from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',
		views.SuscriptorList.as_view(),
		name="list"),
	
	url(r'^(?P<pk>\d+)/$',
		views.SuscriptorDetail.as_view(),
		name="detail"),
	
	url(r'^nuevo/$',
		views.SuscriptorCreation.as_view(),
		name="new"),
	
	url(r'^editar/(?P<pk>\d+)/$',
		views.SuscriptorUpdate.as_view(),
		name="edit"),
	
	url(r'^borrar/(?P<pk>\d+)/$',
		views.SuscriptorDelete.as_view(),
		name="delete"),
	
	url(r'^spam/$', 
		views.Spam.as_view(), 
		name="spam"),
]
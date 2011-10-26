from django.contrib import admin
admin.autodiscover()

# from django.conf.urls.defaults import patterns, include, url
from django_consultants.views import *
from django.conf.urls.defaults import *


urlpatterns = patterns('',

	url(
		regex = r'^admin/',
		view = include(admin.site.urls),
		name = 'admin',
	),	
	
	url(
		regex = r'^$',
		view = main_page,
		name = 'main',
	),	
	
	# Login / logout.	
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),

	# Web portal.
	(r'^portal/', include('portal.urls')),


	# Serve static content.
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',	{'document_root': 'static',}),
)

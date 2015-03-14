from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from eshoper.views import *

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'eshoper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$', 'eshoper.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loginform/$',login),
    url(r'^contact-us form/$',contact_us),
    #mobiles url
    url(r'^loginform/$',login),
    url(r'^mobiles/contact-us form/$',contact_us),
    url(r'^mobiles/$',mobiles_data),
    url(r'^mobile/$',mobiles_data),
    url(r'^loginform/$',login),
    url(r'^mobiles/(.*)/$', details),
    url(r'^mobile/brand/(.*)/$', category_brand),
    url(r'^mobile/price/(.*)/$',category_price),
    url(r'^mobile/(.*)/(.*)/$',category_price_brand),
    url(r'^mobileSearch/$',mobileSearch),
    url(r'^searchError/$',searchError),

)

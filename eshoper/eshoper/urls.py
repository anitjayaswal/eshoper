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
    
    url(r'^contact-us form/$',contact_us),
    #mobiles url
    
    
    url(r'^mobiles/(.*)$',mobiles_data),
    #url(r'^mobiles/$',pagination),
    url(r'^mobiles/$',mobiles_data),
    url(r'^loginform/$',login),
    url(r'^logout/$',logout),

    url(r'^productdetails/(.*)/$', details),
    url(r'^mobile/brand/(.*)/$', category_brand),
    url(r'^product/mobiles/(.*)$', category_brand1),
    url(r'^mobile/price/(.*)/$',category_price),
    url(r'^mobile/(.*)/(.*)/$',category_price_brand),
    url(r'^mobileSearch/$',mobileSearch),
    url(r'^autocompleteModel/$', 'eshoper.views.autocompleteModel',name='autocompleteModel'),
    url(r'^autocompleteModel_brand/$', 'eshoper.views.autocompleteModel_Brand',name='autocompleteModel_Brand'),
    url(r'^searchError/$',searchError),

    url(r'^user_registration/$',user_registration),
    url(r'^user_varification/$',user_varification),

    
 


)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Shop.urls')),
    path('account/', include('App_Login.urls')),
    path('shop/', include('App_Order.urls')),
    path('payment/', include('App_Payment.urls')),
    path('userlog/', include('App_UserLog.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
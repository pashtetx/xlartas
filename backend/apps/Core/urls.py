from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views.auth.auth_views import signup, verify_email
from .views.auth.soc_auth_views import telegram_auth
from .views.common_views import health_test, theme_list, current_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health_test/', health_test),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/themes/', theme_list, name='theme_list'),
    path('api/current_user/', current_user, name='current_user'),

    path('api/signup/', signup, name='signup'),
    path('api/verify_email/', verify_email, name='verify_email'),

    path('accounts/', include('allauth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('apps.shop.desktop_software_urls')),

    path('accounts/telegram/login/callback/', telegram_auth, name='telegram_signup'),

    path('api/', include(('apps.shop.urls', 'apps.shop'), namespace='shop')),
    path('', include('apps.freekassa.urls')),
    # path('referral/', include(('apps.referral.urls', 'apps.referral'), namespace='referral')),
    # path('private-msg/', include(('apps.private_msg.urls', 'apps.private_msg'), namespace='private-msg')),
    # path('host/', include(('apps.filehost.urls', 'apps.filehost'), namespace='host')),
    # path('rp/', include(('apps.resource_pack.urls', 'apps.resource_pack'), namespace='rp')),
    # path('harmony/', include('apps.harmony.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEV:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

urlpatterns.append(re_path(r'^.*$', TemplateView.as_view(template_name='index.html')))
urlpatterns.append(path('', TemplateView.as_view(template_name='index.html'), name='main'))

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from webapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategView)
router.register('products', views.ProductView)
router.register('messages', views.MessageView)
router.register('comments', views.CommentView)
router.register(r'userproducts/(?P<author_id>[0-9]+)', views.UserProductView, base_name='userproducts')
router.register('trades', views.TradeView)
router.register(r'producttrades/(?P<product_id>[0-9]+)', views.ProductTradeView, base_name='producttrades')

urlpatterns = [
    path('', include('webapp.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/register/', include('rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

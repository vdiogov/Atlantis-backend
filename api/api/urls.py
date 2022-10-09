from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from controler import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'queue', views.QueueViewSet)
router.register(r'queuespecial', views.QueueSpecialViewSet)

queue_delete = views.QueueBulkDelete.as_view({
    'delete': 'destroy'
})
queuespecial_delete = views.QueueSpecialBulkDelete.as_view({
    'delete': 'destroy'
})


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('queueDELETE/', queue_delete, name='queue_delete'),
    path('queuespecialDELETE/', queuespecial_delete, name='queuespecial_delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from huscy.subjects import views


router = DefaultRouter()
router.register('subjects', views.SubjectViewSet, basename='subject')

subject_router = NestedSimpleRouter(router, 'subjects', lookup='subject')
subject_router.register('guardians', views.GuardianViewSet, basename='guardian')

urlpatterns = router.urls
urlpatterns += subject_router.urls

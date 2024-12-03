from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import MedicalNoteViewSet, AppointmentViewSet

router = DefaultRouter()
router.register("medical-note", MedicalNoteViewSet)
router.register("appointment", AppointmentViewSet)


urlpatterns = router.urls

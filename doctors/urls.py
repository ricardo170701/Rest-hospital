from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ListDoctorsView,
    DetailsDoctorView,
    ListDepartmentView,
    DetailsDepartmentView,
    ListDoctorAvailabilityView,
    DetailsDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailsMedicalNoteView,
)
from .viewsets import (
    DoctorViewSet,
    DepartmentViewSet,
    DoctorAvailabilityViewSet,
    MedicalNoteViewSet,
)

router = DefaultRouter()
router.register("doctors", DoctorViewSet)
router.register("department", DepartmentViewSet)
router.register("doctor-availability", DoctorAvailabilityViewSet)
router.register("medical-note", MedicalNoteViewSet)


urlpatterns = router.urls

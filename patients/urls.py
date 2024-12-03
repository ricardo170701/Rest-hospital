from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ListPatientsView,
    DetailsPatientsView,
    ListInsuranceView,
    DetailsInsuranceView,
    ListMedicalRecordView,
    DetailsMedicalRecordView,
)
from .viewsets import PatientViewSet, MedicalRecordViewSet, InsuranceViewSet

router = DefaultRouter()
router.register("patient", PatientViewSet)
router.register("medical-record", MedicalRecordViewSet)
router.register("insurance", InsuranceViewSet)

urlpatterns = router.urls

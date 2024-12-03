from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# GET /api/patients => listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificar
# DELETE /api/patients/<pk> => Borrar


class ListPatientsView(ListCreateAPIView):
    """
    Obtiene la lista de todos los pacientes
    """

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailsPatientsView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "pk"


class ListInsuranceView(ListCreateAPIView):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailsInsuranceView(RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    lookup_field = "pk"


class ListMedicalRecordView(ListCreateAPIView):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailsMedicalRecordView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    lookup_field = "pk"

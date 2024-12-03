from rest_framework import viewsets
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord
from rest_framework.decorators import action
from rest_framework.response import Response


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(["GET"], detail=True, url_path="get-history")
    def get_history(self, request, pk):
        patient = self.get_object()  # Obtener el paciente por su pk
        medical_record = MedicalRecord.objects.filter(
            patient=patient
        )  # Filtrar el historial clínico por paciente
        serializer = MedicalRecordSerializer(medical_record, many=True)
        return Response(
            serializer.data
        )  # Retornar el historial clínico en formato JSON


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
